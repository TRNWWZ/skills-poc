"""Severity thresholds for the weather-report skill (test fixture, not executed)."""

def classify_severity(wind_speed_mph: float, precipitation_chance_pct: float) -> str:
    if wind_speed_mph >= 74:
        return "Hurricane-force warning"
    if wind_speed_mph >= 39 or precipitation_chance_pct >= 90:
        return "Storm warning"
    if wind_speed_mph >= 25 or precipitation_chance_pct >= 60:
        return "Advisory"
    return "None"
