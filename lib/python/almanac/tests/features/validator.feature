@author_Flow @okr_I004
Feature: Content Validation
    As an Almanac Architect
    I want to validate content against the schema
    In order to ensure structural integrity and referential correctness

    Rule: Every article must declare all required fields

        Scenario: Healthy article passes validation
            Given an area "science" exists
            And a document "areas/science/consciousness.md" with:
                """
                ---
                title: Why Consciousness is Hard
                area: science
                type: article
                author: Leslie Alan Horvitz
                author_slug: leslie-alan-horvitz
                source: The Observatory
                source_url: https://observatory.wiki/Consciousness
                license: CC BY-NC-SA 4.0
                published: 2026-04-29
                updated: 2026-04-29
                summary: A brief overview of the hard problem of consciousness.
                tags: [consciousness, philosophy]
                ---
                # Why Consciousness is Hard
                Body text.
                """
            And an author profile "authors/leslie-alan-horvitz.md" exists
            When I run the validator
            Then the exit code should be 0
            And the stderr should contain "Validated 2 files — 0 violation(s) found"

        Scenario: Missing required fields are reported
            Given an area "science" exists
            And a document "areas/science/broken.md" with:
                """
                ---
                title: Broken Article
                area: science
                type: article
                # missing author, author_slug, source_url
                license: CC BY-NC-SA 4.0
                published: 2026-04-29
                updated: 2026-04-29
                summary: This article is missing fields.
                tags: [broken]
                ---
                """
            When I run the validator
            Then the exit code should be 1
            And the stdout should contain "field: author"
            And the stdout should contain "field: author_slug"

    Rule: The area slug must be a canonical value from AREAS.md

        Scenario: Article with a recognised area slug passes
            Given an area "environment" exists
            And a document "areas/environment/valid-area.md" with:
                """
                ---
                title: Climate Change Basics
                area: environment
                type: article
                author: Reynard Loki
                author_slug: reynard-loki
                source: The Observatory
                source_url: https://observatory.wiki/Climate_Basics
                license: CC BY-NC-SA 4.0
                published: 2026-04-01
                updated: 2026-04-01
                summary: An overview of climate change science.
                tags: [climate, environment]
                ---
                Body.
                """
            And an author profile "authors/reynard-loki.md" exists
            When I run the validator
            Then the exit code should be 0

        Scenario: Article with an unrecognised area slug is rejected
            Given an area "environment" exists
            And a document "areas/environment/wrong-area.md" with:
                """
                ---
                title: Article In Wrong Area
                area: made-up-area
                type: article
                author: Reynard Loki
                author_slug: reynard-loki
                source: The Observatory
                source_url: https://observatory.wiki/Wrong_Area
                license: CC BY-NC-SA 4.0
                published: 2026-04-01
                updated: 2026-04-01
                summary: This article declares a non-canonical area.
                tags: [test]
                ---
                Body.
                """
            When I run the validator
            Then the exit code should be 1
            And the stdout should contain "area"

    Rule: Auto-generated area index.md nav pages are excluded from content validation

        Scenario: An index.md nav page alongside articles does not trigger violations
            Given an area "science" exists
            And a document "areas/science/bees.md" with:
                """
                ---
                title: Bees Are Sentient
                area: science
                type: article
                author: Stephen Buchmann
                author_slug: stephen-buchmann
                source: The Observatory
                source_url: https://observatory.wiki/Bees
                license: CC BY-NC-SA 4.0
                published: 2026-01-15
                updated: 2026-01-15
                summary: Bees have subjective experiences.
                tags: [bees, sentience]
                ---
                Body.
                """
            And an author profile "authors/stephen-buchmann.md" exists
            And a document "areas/science/index.md" with:
                """
                ---
                title: Science
                area: science
                hide:
                  - toc
                ---
                # Science
                *1 document*
                """
            When I run the validator
            Then the exit code should be 0
            And the stderr should contain "Validated 2 files — 0 violation(s) found"

        Scenario: An index.md nav page alone in an area does not trigger violations
            Given an area "cooking" exists
            And a document "areas/cooking/index.md" with:
                """
                ---
                title: Cooking
                area: cooking
                hide:
                  - toc
                ---
                # Cooking
                *0 documents*
                """
            When I run the validator
            Then the exit code should be 0
            And the stderr should contain "Validated 0 files — 0 violation(s) found"

        Scenario: A non-index content file with nav-style frontmatter is still validated
            Given an area "science" exists
            And a document "areas/science/nav-lookalike.md" with:
                """
                ---
                title: Science
                area: science
                hide:
                  - toc
                ---
                # Science
                """
            When I run the validator
            Then the exit code should be 1
            And the stdout should not contain "index.md"
