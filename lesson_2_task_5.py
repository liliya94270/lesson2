def month_to_season(month):
    seasons = {
        (12, 1, 2): "зима",
        (3, 4, 5): "весна",
        (6, 7, 8): "лето",
        (9, 10, 11): "осень",
    }
    for key, value in seasons.items():
        if month in key:
            return value
    return "некорректный номер месяца"

print(f"Месяц {month} относится к сезону: {month_to_season(int(input('Введите номер месяца (1-12): ')))}")
