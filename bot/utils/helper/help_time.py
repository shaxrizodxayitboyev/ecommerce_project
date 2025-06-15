from datetime import datetime


def time_formatter(date_time: str, pattern: str = '%Y-yil %d-%B  %H:%M') -> str:
    return datetime.fromisoformat(date_time).strftime(pattern)


def format_price(value) -> str:
    try:
        return f"{float(value):,.0f} so‘m"
    except (ValueError, TypeError):
        return "Noma’lum"