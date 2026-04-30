@author_Flow @okr_I004
Feature: Brittani Content Task Board
    As a Content Editor (Brittani)
    I want a task board generated from actual repo state
    In order to know exactly what is broken, missing, or incomplete

    Rule: Broken author profile links are surfaced as tasks

        Scenario: Author profile references an article not yet in the repo
            Given an area "science" exists
            And an author profile "authors/missing-article-author.md" exists
            And the author profile contains a link to a missing article
            When I run the task generator
            Then the exit code should be 0
            And the file "meta/brittani-tasks.md" should exist
            And the file "meta/brittani-tasks.md" should contain "🔴 Broken Links"
            And the file "meta/brittani-tasks.md" should contain "missing-article-author"

        Scenario: All author profile links resolve — no broken links reported
            Given an area "science" exists
            And an author profile "authors/clean-author.md" exists
            And a document "areas/science/present-article.md" with:
                """
                ---
                title: Present Article
                area: science
                type: article
                author: Clean Author
                author_slug: clean-author
                source: The Observatory
                source_url: https://observatory.wiki/Present
                license: CC BY-NC-SA 4.0
                published: 2026-01-01
                updated: 2026-01-01
                summary: An article that exists.
                tags: [test]
                ---
                Body.
                """
            When I run the task generator
            Then the exit code should be 0
            And the file "meta/brittani-tasks.md" should contain "No broken links found"

    Rule: Empty areas are surfaced as tasks

        Scenario: An area with no articles appears in the task board
            Given an area "cooking" exists
            When I run the task generator
            Then the exit code should be 0
            And the file "meta/brittani-tasks.md" should contain "🟡 Empty Areas"
            And the file "meta/brittani-tasks.md" should contain "cooking"

        Scenario: An area with at least one article is not flagged as empty
            Given an area "environment" exists
            And an author profile "authors/env-author.md" exists
            And a document "areas/environment/climate-basics.md" with:
                """
                ---
                title: Climate Basics
                area: environment
                type: article
                author: Env Author
                author_slug: env-author
                source: The Observatory
                source_url: https://observatory.wiki/Climate
                license: CC BY-NC-SA 4.0
                published: 2026-01-01
                updated: 2026-01-01
                summary: Climate basics.
                tags: [climate]
                ---
                Body.
                """
            When I run the task generator
            Then the exit code should be 0
            And the file "meta/brittani-tasks.md" should not contain "**Environment**"

    Rule: Validation failures are surfaced as tasks

        Scenario: Invalid content file appears in the validation section
            Given an area "science" exists
            And a document "areas/science/invalid.md" with:
                """
                ---
                title: Invalid Article
                area: science
                type: article
                license: CC BY-NC-SA 4.0
                published: 2026-01-01
                updated: 2026-01-01
                summary: Missing required fields.
                tags: [broken]
                ---
                """
            When I run the task generator
            Then the exit code should be 0
            And the file "meta/brittani-tasks.md" should contain "🟠 Validation Failures"
            And the file "meta/brittani-tasks.md" should contain "invalid.md"
