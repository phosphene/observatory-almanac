# Release Radar â Technical Design Specification

*From The Observatory Almanac â Cultural Pulse*
*Document Type: Technical Design Specification*
*Status: Draft v1.0*

---

## Overview

Release Radar is the automated release calendar subsystem of the Observatory Almanac's Cultural Pulse section. Its purpose is to track, aggregate, and present upcoming and recent releases across film, television, music, and books â pulling from authoritative APIs, streaming platform feeds, and review aggregators to create a unified, opinionated cultural calendar.

This document specifies the system architecture, data sources, integration protocols, data schemas, and presentation layer for Release Radar.

---

## 1. System Architecture

### 1.1 High-Level Components

```
âââââââââââââââââââââââââââââââââââââââââââââââââââââââ
â                  DATA SOURCES                        â
â  TMDB API  â  Spotify API  â  OpenLibrary  â  GBooks â
â  MusicBrainz  â  Streaming RSS  â  Metacritic  â  RT  â
ââââââââââââââââââââââââââ¬âââââââââââââââââââââââââââââ
                         â
                    ââââââ¼ââââââ
                    â  INGEST  â
                    â  LAYER   â
                    ââââââ¬ââââââ
                         â
              ââââââââââââ¼âââââââââââ
              â  NORMALIZATION &    â
              â  DEDUPLICATION DB   â
              â  (PostgreSQL)       â
              ââââââââââââ¬âââââââââââ
                         â
         âââââââââââââââââ¼âââââââââââââââââââ
         â        ENRICHMENT LAYER          â
         â  Review aggregation, tagging,    â
         â  streaming availability lookup   â
         âââââââââââââââââ¬âââââââââââââââââââ
                         â
              ââââââââââââ¼âââââââââââ
              â   PRESENTATION      â
              â   API (FastAPI)     â
              ââââââââââââ¬âââââââââââ
                         â
          ââââââââââââââââ¼âââââââââââââââ
          â       ALMANAC FRONTEND      â
          â  Weekly digest / Calendar   â
          â  view / Feed / Alerts       â
          âââââââââââââââââââââââââââââââ
```

### 1.2 Technology Stack

| Layer | Technology | Rationale |
| --- | --- | --- |
| Ingest scripts | Python 3.11+ | Rich library ecosystem for API integrations |
| Task scheduler | APScheduler / Celery | Periodic refresh with retry logic |
| Primary database | PostgreSQL 15+ | Relational data with JSON fields for flexibility |
| Cache layer | Redis | API response caching, rate limit state |
| Presentation API | FastAPI | Fast, async, auto-documenting |
| Frontend | Jinja2 templates (static site) | Low dependency, fast rendering |
| Container | Docker Compose | Reproducible deployment |

---

## 2. Data Sources & Integration

### 2.1 TMDB API (Film & Television)

**Base URL:** `https://api.themoviedb.org/3/`
**Authentication:** API key via query parameter (`?api_key=`) or Bearer token header (v4)
**Rate limits:** 40 requests/10 seconds (v3); 50 requests/second (v4 with approved application)

#### Key Endpoints

| Endpoint | Purpose | Refresh Frequency |
| --- | --- | --- |
| `/movie/upcoming` | Films releasing in next 4 weeks | Daily |
| `/movie/now_playing` | Currently in theaters | Daily |
| `/movie/popular` | Trending films | Weekly |
| `/tv/on_the_air` | Currently airing TV | Daily |
| `/tv/airing_today` | Today's TV premieres | Daily |
| `/discover/movie` | Filtered search (by date range, genre, etc.) | On demand |
| `/movie/{id}` | Full film detail | On item creation |
| `/movie/{id}/release_dates` | Jurisdiction-specific release dates | On item creation |
| `/movie/{id}/videos` | Trailers and clips | On item creation |
| `/tv/{id}/season/{n}/episodes` | Episode list with air dates | On season creation |

#### TMDB Film Schema (normalized)

```
{
  "tmdb_id": 12345,
  "title": "Film Title",
  "original_title": "Original Title",
  "overview": "Synopsis text...",
  "release_date": "2025-06-15",
  "release_type": "theatrical",
  "genres": ["Drama", "Thriller"],
  "runtime_minutes": 118,
  "spoken_languages": ["en", "fr"],
  "origin_country": ["US"],
  "poster_path": "/path/to/poster.jpg",
  "backdrop_path": "/path/to/backdrop.jpg",
  "trailer_url": "https://youtube.com/watch?v=...",
  "tmdb_rating": 7.4,
  "tmdb_vote_count": 824,
  "status": "upcoming",
  "last_updated": "2025-04-01T12:00:00Z"
}
```

#### Jurisdiction Handling

TMDB's `/movie/{id}/release_dates` endpoint returns per-country release dates categorized by type:

| TMDB Type | Description |
| --- | --- |
| 1 | Premiere |
| 2 | Theatrical (limited) |
| 3 | Theatrical (wide) |
| 4 | Digital (VOD) |
| 5 | Physical (home media) |
| 6 | TV airing |

For the Almanac, primary focus is US theatrical (type 3) and digital (type 4) releases. Store all jurisdictions in a JSONB field for flexibility.

---

### 2.2 Streaming Platform Tracking

Streaming platforms do not expose unified, publicly documented APIs for release schedules. The following approaches are used in combination:

#### 2.2.1 JustWatch Integration

JustWatch (justwatch.com) aggregates streaming availability across 100+ platforms. While JustWatch does not publish an official public API, several approaches exist:

**Recommended approach:** JustWatch GraphQL API (unofficial, rate-limited)
- Endpoint: `https://apis.justwatch.com/graphql`
- Key query: `GetSuggestedTitles` / `GetTitle` with streaming availability
- Requires respectful rate limiting (1 request/second, max 1000/day)
- Include `User-Agent` header identifying your application

**Fallback:** Parse JustWatch's public web pages for structured JSON data embedded in `<script type="application/json">` tags.

#### 2.2.2 Platform RSS Feeds

Some platforms publish structured feeds:

| Platform | Feed Type | URL Pattern |
| --- | --- | --- |
| Apple TV+ | None public | Manual curation required |
| Amazon Prime | Press release RSS | `https://press.aboutamazon.com/rss/...` |
| Max (HBO) | Press releases | Manual monitoring |
| Hulu | None public | Social media monitoring |
| Netflix | None public | Third-party trackers |

**Netflix-specific:** Use TMDB's network filter (`/discover/tv?with_networks=213`) to find Netflix-associated content and cross-reference with JustWatch availability.

#### 2.2.3 Streaming Status Schema

```
{
  "release_id": "uuid",
  "platform": "netflix",
  "availability_type": "subscription",
  "available_date": "2025-06-01",
  "country": "US",
  "url": "https://netflix.com/title/...",
  "verified": true,
  "last_checked": "2025-04-01T12:00:00Z"
}
```

---

### 2.3 Music Release Tracking

#### 2.3.1 Spotify Web API

**Base URL:** `https://api.spotify.com/v1/`
**Authentication:** OAuth 2.0 Client Credentials flow
**Rate limits:** Generous; 429 response with `Retry-After` header when exceeded

Key endpoints:
- `/browse/new-releases` â Recent album releases (last 4 weeks)
- `/albums/{id}` â Full album detail
- `/artists/{id}/albums` â Artist discography with dates

```
# Example: Fetch new releases
import requests

def get_new_releases(token: str, country: str = "US", limit: int = 50) -> list:
    headers = {"Authorization": f"Bearer {token}"}
    url = f"https://api.spotify.com/v1/browse/new-releases"
    params = {"country": country, "limit": limit, "offset": 0}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()["albums"]["items"]
```

#### 2.3.2 MusicBrainz

MusicBrainz is the open-source music encyclopedia. It provides comprehensive release information with ISBNs, labels, and format details.

**Base URL:** `https://musicbrainz.org/ws/2/`
**Authentication:** None required; User-Agent header mandatory
**Rate limits:** 1 request/second; commercial use requires server-side mirroring

Key endpoints:
- `/release/?query=date:[2025-01 TO 2025-12]&type=album` â Releases in date range
- `/release/{mbid}` â Full release detail
- `/artist/{mbid}/releases` â Artist releases

**User-Agent requirement:**

```
User-Agent: ObservatoryAlmanac/1.0 ([email protected])
```

#### 2.3.3 Album Schema

```
{
  "id": "uuid",
  "title": "Album Title",
  "artist": "Artist Name",
  "artist_id_spotify": "spotify_artist_id",
  "artist_id_mbid": "musicbrainz_uuid",
  "release_date": "2025-05-20",
  "release_date_precision": "day",
  "genre_tags": ["alternative rock", "indie"],
  "label": "Label Name",
  "track_count": 12,
  "spotify_id": "spotify_album_id",
  "spotify_url": "https://open.spotify.com/album/...",
  "cover_art_url": "https://...",
  "format": ["digital", "vinyl", "CD"]
}
```

---

### 2.4 Book Release Tracking

#### 2.4.1 Google Books API

**Base URL:** `https://www.googleapis.com/books/v1/`
**Authentication:** API key
**Rate limits:** 1,000 requests/day (free tier); higher with quota increase request

Key endpoints:
- `/volumes?q=publishedDate:2025` â Books by publication date range
- `/volumes/{id}` â Full volume detail

#### 2.4.2 OpenLibrary API

OpenLibrary (openlibrary.org) is the Internet Archive's open bibliographic database.

**Base URL:** `https://openlibrary.org/`
**Authentication:** None required
**Key endpoints:**
- `/search.json?q=...&first_publish_year=2025` â Publication year search
- `/works/{olid}.json` â Work detail
- `/isbn/{isbn}.json` â ISBN lookup

#### 2.4.3 Publisher RSS Feeds

Major publishers maintain publicity feeds:
- Penguin Random House: `https://feeds.penguinrandomhouse.com/`
- HarperCollins: `https://www.harpercollins.com/pages/rss-feeds`
- Simon & Schuster: Press release monitoring

---

## 3. Review Aggregation

### 3.1 Film & Television Review Sources

| Source | API Access | Data Available |
| --- | --- | --- |
| Metacritic | No public API | Web scraping (check ToS) |
| Rotten Tomatoes | Partner API (application required) | Critics/Audience scores |
| IMDb | Unofficial (browser API pattern) | Ratings, vote counts |
| Letterboxd | No public API | Community aggregations only |
| Roger Ebert (RogerEbert.com) | No API | RSS for new reviews |

**Recommended approach for ratings:** Use TMDB's community rating (which aggregates its own user base) as the primary score, and supplement with cached Metacritic/RT data scraped during off-peak hours with appropriate delays and User-Agent identification.

**Legal note:** Always check each platform's Terms of Service before scraping. Several major aggregators prohibit automated access without partnership agreements.

### 3.2 Aggregated Score Schema

```
{
  "release_id": "uuid",
  "scores": {
    "tmdb_rating": 7.4,
    "tmdb_vote_count": 1240,
    "metacritic_score": 82,
    "metacritic_review_count": 47,
    "rt_critics_score": 91,
    "rt_critics_count": 112,
    "rt_audience_score": 78,
    "imdb_rating": 7.6,
    "imdb_vote_count": 45200
  },
  "consensus_blurb": "A taut, original thriller...",
  "last_updated": "2025-04-01T12:00:00Z"
}
```

### 3.3 Composite Score Algorithm

A weighted composite score combines available ratings:

```
def compute_composite_score(scores: dict) -> float | None:
    """
    Weights: TMDB 0.2, Metacritic 0.35, RT Critics 0.35, IMDb 0.1
    Normalizes all scores to 0-100 scale.
    Returns None if fewer than 2 sources available.
    """
    available = []

    if scores.get("tmdb_rating"):
        available.append(("tmdb", scores["tmdb_rating"] * 10, 0.20))
    if scores.get("metacritic_score"):
        available.append(("metacritic", scores["metacritic_score"], 0.35))
    if scores.get("rt_critics_score"):
        available.append(("rt", scores["rt_critics_score"], 0.35))
    if scores.get("imdb_rating"):
        available.append(("imdb", scores["imdb_rating"] * 10, 0.10))

    if len(available) < 2:
        return None

    # Renormalize weights for available sources
    total_weight = sum(w for _, _, w in available)
    return sum((score * weight / total_weight) for _, score, weight in available)
```

---

## 4. Database Schema

### 4.1 Core Tables

```
-- Unified releases table
CREATE TABLE releases (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    media_type VARCHAR(20) NOT NULL, -- 'film', 'tv_series', 'album', 'book'
    title TEXT NOT NULL,
    subtitle TEXT,
    creator TEXT NOT NULL, -- director, artist, author
    release_date DATE,
    release_date_precision VARCHAR(10) DEFAULT 'day', -- 'year', 'month', 'day'
    description TEXT,
    cover_art_url TEXT,
    external_ids JSONB DEFAULT '{}', -- {tmdb_id, spotify_id, isbn, etc.}
    genres TEXT[],
    tags TEXT[],
    metadata JSONB DEFAULT '{}', -- media-type-specific fields
    composite_score NUMERIC(4,1),
    scores JSONB DEFAULT '{}',
    streaming_availability JSONB DEFAULT '[]',
    status VARCHAR(20) DEFAULT 'upcoming', -- 'upcoming', 'released', 'cancelled'
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Index for calendar queries
CREATE INDEX idx_releases_date ON releases(release_date, media_type);
CREATE INDEX idx_releases_status ON releases(status);
CREATE INDEX idx_releases_external_ids ON releases USING GIN(external_ids);

-- User watchlist/interest tracking
CREATE TABLE user_interests (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    release_id UUID REFERENCES releases(id) ON DELETE CASCADE,
    user_id UUID NOT NULL,
    interest_type VARCHAR(20), -- 'watchlist', 'notify', 'seen'
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Ingest job log
CREATE TABLE ingest_jobs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    source VARCHAR(50) NOT NULL,
    job_type VARCHAR(50) NOT NULL,
    started_at TIMESTAMPTZ,
    completed_at TIMESTAMPTZ,
    records_processed INTEGER,
    records_added INTEGER,
    records_updated INTEGER,
    error TEXT,
    status VARCHAR(20) DEFAULT 'pending'
);
```

---

## 5. Presentation API

### 5.1 Core Endpoints

```
GET /api/v1/releases
  ?type=film|tv|album|book   (filter by media type)
  ?start_date=YYYY-MM-DD     (range start)
  ?end_date=YYYY-MM-DD       (range end)
  ?genre=drama               (genre filter)
  ?platform=netflix          (streaming platform)
  ?sort=release_date|score   (sort order)
  ?limit=20&offset=0         (pagination)

GET /api/v1/releases/{id}    (full release detail)

GET /api/v1/calendar/week    (this week's releases, all types)
GET /api/v1/calendar/month   (this month's releases)

GET /api/v1/trending         (releases with high interest/score this week)

GET /api/v1/search?q=...     (full-text search across releases)
```

### 5.2 Response Format

```
{
  "data": [
    {
      "id": "uuid",
      "media_type": "film",
      "title": "Example Film",
      "creator": "Director Name",
      "release_date": "2025-06-20",
      "genres": ["Thriller", "Drama"],
      "description": "Short synopsis...",
      "composite_score": 82.5,
      "streaming": [
        {
          "platform": "Max",
          "availability_date": "2025-08-01",
          "type": "subscription"
        }
      ],
      "cover_art_url": "https://..."
    }
  ],
  "meta": {
    "total": 147,
    "limit": 20,
    "offset": 0,
    "next_cursor": "..."
  }
}
```

---

## 6. Scheduler Configuration

### 6.1 Refresh Schedule

```
# APScheduler configuration

from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

# Daily refresh jobs
scheduler.add_job(ingest_tmdb_upcoming, "cron", hour=2, minute=0)
scheduler.add_job(ingest_tmdb_now_playing, "cron", hour=2, minute=30)
scheduler.add_job(ingest_spotify_new_releases, "cron", hour=3, minute=0)
scheduler.add_job(refresh_streaming_availability, "cron", hour=4, minute=0)

# Weekly jobs
scheduler.add_job(ingest_books_upcoming, "cron", day_of_week="mon", hour=5)
scheduler.add_job(refresh_review_scores, "cron", day_of_week="tue", hour=3)
scheduler.add_job(cleanup_stale_records, "cron", day_of_week="sun", hour=1)
```

### 6.2 Rate Limit Management

```
import time
from functools import wraps

class RateLimiter:
    """Token bucket rate limiter for API calls."""

    def __init__(self, calls_per_second: float):
        self.calls_per_second = calls_per_second
        self.min_interval = 1.0 / calls_per_second
        self.last_call = 0.0

    def wait(self):
        elapsed = time.monotonic() - self.last_call
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self.last_call = time.monotonic()


# Per-source limiters
TMDB_LIMITER = RateLimiter(4.0)          # 40 req/10s
MUSICBRAINZ_LIMITER = RateLimiter(1.0)   # 1 req/s
SPOTIFY_LIMITER = RateLimiter(10.0)      # generous limit
GOOGLE_BOOKS_LIMITER = RateLimiter(2.0)  # conservative
```

---

## 7. Digest Generation

### 7.1 Weekly Digest Email/Feed

The Almanac generates a weekly digest every Sunday evening covering the following week's notable releases. Content is curated through a scoring/interest algorithm.

**Selection criteria:**
- Films: composite\_score > 65 OR exceptional anticipation score (based on user interest flags)
- Music: Major artists (>1M Spotify followers) OR notable critical interest
- Books: Major publishers OR notable author, flagged as literary release
- Always include: Top 3 items per category regardless of score

**Format:** Jinja2 templates rendering to both HTML (email) and Markdown (Almanac feed).

### 7.2 Alert System

Users may subscribe to alerts for:
- Specific artists, directors, or authors (new release of any work)
- Genre categories
- Streaming platform availability for wishlisted items
- Critical threshold alerts ("when X film exceeds 80 Metacritic")

Alerts deliver via email (SMTP), RSS, or webhooks.

---

## 8. Error Handling & Resilience

### 8.1 API Failure Strategy

```
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import requests

@retry(
    retry=retry_if_exception_type(requests.HTTPError),
    wait=wait_exponential(multiplier=1, min=4, max=60),
    stop=stop_after_attempt(5)
)
def fetch_with_retry(url: str, **kwargs) -> dict:
    response = requests.get(url, **kwargs, timeout=15)
    if response.status_code == 429:
        retry_after = int(response.headers.get("Retry-After", 60))
        time.sleep(retry_after)
        response.raise_for_status()
    response.raise_for_status()
    return response.json()
```

### 8.2 Data Freshness Guarantees

* Film/TV data: Maximum 48-hour staleness
* Streaming availability: Maximum 7-day staleness (changes infrequently)
* Review scores: Maximum 7-day staleness
* Music releases: Maximum 48-hour staleness
* Book releases: Maximum 7-day staleness

Stale records are flagged in the UI with a last-updated timestamp.

---

## 9. Privacy & Compliance

* **User data:** Minimal collection. Email address (for digests), optional preferences. No tracking beyond session cookies.
* **API keys:** Stored in environment variables; never in code or version control.
* **Scraped data:** Respect robots.txt for all sources. No personally identifiable information collected from third-party sources.
* **GDPR compliance:** User data deletion on request. Digest unsubscribe in every email.
* **TMDB attribution:** Per TMDB ToS, display "This product uses the TMDB API but is not endorsed or certified by TMDB."

---

## 10. Future Enhancements

| Feature | Priority | Complexity |
| --- | --- | --- |
| Podcast tracking (new episode RSS) | Medium | Low |
| Video game release calendar | Medium | Medium |
| Theatre/live performance events | Low | High |
| Personalized ML recommendations | Low | High |
| Social sharing / Letterboxd sync | Medium | Medium |
| Apple Calendar / Google Calendar export (iCal) | High | Low |
| Mobile app | Low | Very High |

---

*Part of The Observatory Almanac â Cultural Pulse*
*Release Radar Technical Specification v1.0*