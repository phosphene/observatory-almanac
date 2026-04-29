@author_Flow @okr_I004
Feature: Area Index Generation
    As an Almanac Architect
    I want to generate area index pages from content
    In order to keep navigation current after every article addition

    Scenario: Generate index for an area with one article
        Given an area "science" exists
        And a document "areas/science/bees-are-sentient.md" with:
            """
            ---
            title: Bees Are Sentient and May Be Self-Aware
            area: science
            type: article
            author: Stephen Buchmann
            author_slug: stephen-buchmann
            source: The Observatory
            source_url: https://observatory.wiki/Bees_Are_Sentient
            license: CC BY-NC-SA 4.0
            published: 2026-01-15
            updated: 2026-01-15
            summary: New research suggests bees have subjective experiences.
            tags: [bees, sentience, cognition]
            ---
            # Bees Are Sentient and May Be Self-Aware
            Body text.
            """
        When I run the indexer
        Then the exit code should be 0
        And the file "areas/science/index.md" should exist
        And the file "areas/science/index.md" should contain "Bees Are Sentient"

    Scenario: Index includes author attribution
        Given an area "animals" exists
        And a document "areas/animals/captive-elephants.md" with:
            """
            ---
            title: Captive Elephants — The Harsh Reality
            area: animals
            type: article
            author: Sy Montgomery
            author_slug: sy-montgomery
            source: The Observatory
            source_url: https://observatory.wiki/Captive_Elephants
            license: CC BY-NC-SA 4.0
            published: 2026-02-10
            updated: 2026-02-10
            summary: An examination of captive elephant welfare.
            tags: [elephants, welfare, captivity]
            ---
            # Captive Elephants
            Body text.
            """
        When I run the indexer
        Then the exit code should be 0
        And the file "areas/animals/index.md" should contain "Sy Montgomery"

    Scenario: Dry run does not write files
        Given an area "history" exists
        And a document "areas/history/ancient-debt.md" with:
            """
            ---
            title: Debt Forgiveness in the Bronze Age
            area: history
            type: article
            author: Michael Hudson
            author_slug: michael-hudson
            source: The Observatory
            source_url: https://observatory.wiki/Debt_Forgiveness
            license: CC BY-NC-SA 4.0
            published: 2026-03-01
            updated: 2026-03-01
            summary: How ancient economies handled debt jubilees.
            tags: [debt, bronze-age, economics]
            ---
            # Debt Forgiveness in the Bronze Age
            Body.
            """
        When I run the indexer with "--dry-run"
        Then the exit code should be 0
        And the file "areas/history/index.md" should not exist

    Scenario: Empty area produces a valid index page
        Given an area "cooking" exists
        When I run the indexer
        Then the exit code should be 0
        And the file "areas/cooking/index.md" should exist
