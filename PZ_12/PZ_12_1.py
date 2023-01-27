# 1.Даны средние значения температур за каждый месяц в году. Найти минимальное
# и максимальное значения температур за год. Вывести значения температур по временам
# года.
average = [-9.3, -7.7, -2.2, 5.8, 13.1, 16.6, 18.2, 16.4, 11.0, 5.1, -1.2, -6.1]  # Средние значения температур
print(f"Средние знчения температур за год: {average}")
min_temperature = min(average)  # Минимальные теспературы за год
max_temperature = max(average)  # Максимальные теспературы за год
print(f"Минимальное значение температур: {min_temperature}\n"
      f"Максимальное значение температур за год: {max_temperature}")
seasons = ["Зима", "Лето", "Весна", "Осень"]  # Сезоны
seasons_with_temperature = {
    seasons[0]: round((sum([average[0], average[1], average[11]])/3), 2),
    seasons[2]: round((sum([average[2], average[3], average[4]])/3), 2),
    seasons[1]: round((sum([average[5], average[6], average[7]])/3), 2),
    seasons[3]: round((sum([average[8], average[9], average[10]])/3), 2),
}
for x in seasons_with_temperature:  # Поэтмапный вывод сезонов года и температур
    print(f'{x}: {seasons_with_temperature.get(x)}')