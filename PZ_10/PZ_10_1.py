# Туристические агенства предлагают следущие туры. Вояж - Мексика, Канада, Израиль, Италия, США. РейнаТур - Англия,
# Япония, Канада, ЮАР. Радуга - США, Испания, Швеция, Австралия. Определить в каких турагенствах можно
# приобрести туры в Канаду, а в каких в США.
agents = {
    'Вояж': {'Мексика', 'Канада', 'Израиль', 'Италия', 'США'},  # Все турагенства
    'РейнаТур': {'Англия', 'Япония', 'Канада', 'ЮАР'},
    'Радуга': {'США', 'Испания', 'Швеция', 'Австралия'},
}

Kanada_tours = ", ".join({  # Список в турагенств для тура в Канаду
    x for x in agents.keys()
    if "Канада" in agents[x]
})
USA_tours = ", ".join({  # Список в турагенств для тура в США
    x for x in agents.keys()
    if "США" in agents[x]
})
print(f'Турагенства в которых можно приобрести туры в Канаду: {Kanada_tours}')
print(f'Турагенства в которых можно приобрести туры в США: {USA_tours}')
