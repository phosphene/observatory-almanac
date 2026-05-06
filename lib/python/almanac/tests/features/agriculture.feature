@author_Flow @area_agriculture
Feature: Agriculture Area
    As a Content Editor
    I want to add content to the Agriculture area
    In order to publish articles on sustainable farming, gardening, and seasonal planting

    Rule: `agriculture` is a recognised canonical area slug

        Scenario: Agriculture area index page is a valid nav page
            Given an area "agriculture" exists
            And a document "areas/agriculture/index.md" with:
                """
                ---
                title: Agriculture
                area: agriculture
                hide:
                  - toc
                ---
                # Agriculture

                Sustainable farming, soil science, and food systems.

                ## Subareas

                - **Gardening** · home and community growing, soil health, plant care
                - **Seasonal Planting** · planting calendars, crop rotation, climate-adapted growing

                *0 documents*
                """
            When I run the validator
            Then the exit code should be 0
            And the stderr should contain "Validated 0 files — 0 violation(s) found"

    Rule: Articles filed under `agriculture` must satisfy the full schema

        Scenario: Valid agriculture article passes validation and appears in index
            Given an area "agriculture" exists
            And an author profile "authors/the-observatory.md" exists
            And a document "areas/agriculture/regenerative-farming.md" with:
                """
                ---
                title: Regenerative Farming and Soil Health
                area: agriculture
                type: article
                author: The Observatory
                author_slug: the-observatory
                source: The Observatory
                source_url: https://observatory.wiki/Regenerative_Farming
                license: CC BY-NC-SA 4.0
                published: 2026-01-01
                updated: 2026-01-01
                summary: How regenerative practices restore soil carbon and biodiversity.
                tags: [agriculture, soil, regenerative-farming]
                ---
                # Regenerative Farming and Soil Health
                Body content.
                """
            When I run the validator
            Then the exit code should be 0
            When I run the indexer
            Then the exit code should be 0
            And the file "areas/agriculture/index.md" should contain "Regenerative Farming"

        Scenario: Agriculture article missing required fields is rejected
            Given an area "agriculture" exists
            And a document "areas/agriculture/incomplete.md" with:
                """
                ---
                title: Incomplete Agriculture Article
                area: agriculture
                type: article
                license: CC BY-NC-SA 4.0
                published: 2026-05-01
                updated: 2026-05-01
                summary: Missing author and source_url.
                tags: [agriculture]
                ---
                Body.
                """
            When I run the validator
            Then the exit code should be 1
            And the stdout should contain "field: author"

    Rule: Almanac-native documents may be filed under `agriculture`

        Scenario: Almanac-native seasonal planting calendar validates cleanly
            Given an area "agriculture" exists
            And a document "areas/agriculture/seasonal-planting-calendar.md" with:
                """
                ---
                title: Seasonal Planting Calendar
                area: agriculture
                type: almanac
                source: Observatory Almanac
                license: MIT
                updated: 2026-05-06
                summary: Month-by-month planting guide for temperate and subtropical climates.
                tags: [seasonal-planting, gardening, calendar]
                ---
                # Seasonal Planting Calendar
                Body content.
                """
            When I run the validator
            Then the exit code should be 0
