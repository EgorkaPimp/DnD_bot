from RaceInformation import JsonClassRace

race = {'Дварф': "Горный дварф",
        'Эльф': "Высший эльф",
        'Гном': "Лесной гном",
        'Человек': None,
        'Тифлинг': None,
        'Полуэльф': None,
        'Полуорк': None,
        'Полурослик': "Легконогий полурослик"}

for i in race:
    print(f'__________________________{i}_______________')
    json_loader = JsonClassRace()
    x = json_loader.racial_bonuses(i)
    print(x)
    y = json_loader.racial_trait(i)
    print(y)
    q = json_loader.racial_speed(i)
    print(q)
    w = json_loader.racial_size(i)
    print(w)
    e = json_loader.racial_language(i)
    print(e)
    r = json_loader.racial_description(i)
    print(r)
    o = json_loader.racial_age(i)
    print(o)
    u = json_loader.racial_subrace(i)
    print(u)
    z = json_loader.subracial_bonuses(race[i])
    print(z)
    t = json_loader.subracial_trait(race[i])
    print(t)


