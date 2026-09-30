---
name: weather-report
description: Generates a formatted weather report for a city, following a fixed template and unit-conversion rules. Use when the user asks for a weather report or forecast summary.
---

# Weather Report Skill

This skill produces a standardized weather report. Follow these steps:

1. Ask the user for the city name and preferred unit (Celsius or Fahrenheit) if not already given.
2. Read `references/report-template.md` for the exact section headings and ordering the report must follow.
3. Read `references/unit-conversion.md` if you need to convert between Celsius and Fahrenheit.
4. If the user wants a severity classification (e.g. "is this a storm warning?"), read `scripts/severity_rules.py` for the exact thresholds — do not guess them.
5. Fill in the template with the requested city and today's conditions (you may invent plausible sample data for this test skill), and present the final report to the user.

Do not skip the template in `references/report-template.md` — free-form weather reports are not acceptable output for this skill.
