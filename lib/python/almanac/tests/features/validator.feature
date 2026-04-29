@author_Flow @okr_I004
Feature: Content Validation
    As an Almanac Architect
    I want to validate content against the schema
    In order to ensure structural integrity and referential correctness

    Scenario: Validate a healthy article
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

    Scenario: Detect missing required fields
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
