@author_Flow @okr_I004
Feature: Brittani Content Workflow
    As a Content Editor (Brittani)
    I want to add articles, validate them, and regenerate indexes
    In order to publish new content to the Observatory Almanac confidently

    Background:
        Given an area "environment" exists
        And an author profile "authors/reynard-loki.md" exists

    Scenario: Add a valid article — full workflow passes
        Given a document "areas/environment/hydropower-false-solution.md" with:
            """
            ---
            title: 10 Reasons Why Hydropower Isn't a Climate Solution
            area: environment
            type: article
            author: Reynard Loki
            author_slug: reynard-loki
            source: The Observatory
            source_url: https://observatory.wiki/Hydropower
            license: CC BY-NC-SA 4.0
            published: 2026-02-20
            updated: 2026-02-20
            summary: Why hydropower dams cause more harm than good.
            tags: [hydropower, climate, environment]
            ---
            # 10 Reasons Why Hydropower Isn't a Climate Solution
            Body text.
            """
        When I run the validator
        Then the exit code should be 0
        When I run the indexer
        Then the exit code should be 0
        And the file "areas/environment/index.md" should contain "10 Reasons Why Hydropower"

    Scenario: Article with missing required fields fails validation before indexing
        Given a document "areas/environment/bad-article.md" with:
            """
            ---
            title: An Incomplete Article
            area: environment
            type: article
            license: CC BY-NC-SA 4.0
            published: 2026-04-01
            updated: 2026-04-01
            summary: Missing author and source fields.
            tags: [incomplete]
            ---
            # An Incomplete Article
            Body.
            """
        When I run the validator
        Then the exit code should be 1
        And the stdout should contain "field: author"

    Scenario: Article with invalid area is rejected
        Given a document "areas/environment/wrong-area.md" with:
            """
            ---
            title: Article In Wrong Area
            area: nonexistent-area
            type: article
            author: Reynard Loki
            author_slug: reynard-loki
            source: The Observatory
            source_url: https://observatory.wiki/Wrong_Area
            license: CC BY-NC-SA 4.0
            published: 2026-04-01
            updated: 2026-04-01
            summary: This article has an invalid area slug.
            tags: [test]
            ---
            # Article In Wrong Area
            Body.
            """
        When I run the validator
        Then the exit code should be 1
        And the stdout should contain "area"

    Scenario: Author slug in article must match an author profile
        Given a document "areas/environment/orphaned-author.md" with:
            """
            ---
            title: Article With Unknown Author
            area: environment
            type: article
            author: Unknown Person
            author_slug: unknown-person
            source: The Observatory
            source_url: https://observatory.wiki/Unknown
            license: CC BY-NC-SA 4.0
            published: 2026-04-01
            updated: 2026-04-01
            summary: Author slug has no matching profile.
            tags: [test]
            ---
            # Article With Unknown Author
            Body.
            """
        When I run the validator
        Then the exit code should be 1
        And the stdout should contain "unknown-person"

    Scenario: Multiple valid articles all pass and appear in index
        Given a document "areas/environment/plastic-oceans.md" with:
            """
            ---
            title: 600 Million Metric Tons of Plastic May Fill Oceans by 2036
            area: environment
            type: article
            author: Reynard Loki
            author_slug: reynard-loki
            source: The Observatory
            source_url: https://observatory.wiki/Plastic_Oceans
            license: CC BY-NC-SA 4.0
            published: 2026-03-10
            updated: 2026-03-10
            summary: Projection of ocean plastic pollution trajectories.
            tags: [plastic, oceans, pollution]
            ---
            # Plastic
            Body.
            """
        And a document "areas/environment/carbon-farming.md" with:
            """
            ---
            title: Carbon Farming — A Sustainable Agriculture Technique
            area: environment
            type: article
            author: Reynard Loki
            author_slug: reynard-loki
            source: The Observatory
            source_url: https://observatory.wiki/Carbon_Farming
            license: CC BY-NC-SA 4.0
            published: 2026-03-15
            updated: 2026-03-15
            summary: How carbon farming keeps soil healthy and captures CO2.
            tags: [carbon-farming, agriculture, soil]
            ---
            # Carbon Farming
            Body.
            """
        When I run the validator
        Then the exit code should be 0
        When I run the indexer
        Then the exit code should be 0
        And the file "areas/environment/index.md" should contain "600 Million Metric Tons"
        And the file "areas/environment/index.md" should contain "Carbon Farming"
