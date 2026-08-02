from langchain_core.tools import tool

@tool
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers and returns the result."""
    return a + b


@tool
def get_weather(city: str) -> str:
    """Returns today's weather for a given city.
    Input should be a city name like 'Karachi' or 'Lahore'.
    Only returns current weather, not forecasts."""
    return f"{city} mein aaj 34 degree hai"