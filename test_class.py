from ClassesInformation import JsonClassClass

data_class = ["Бард", "Варвар"]

json_l = JsonClassClass()
for i in data_class:
    print(f'\n________________________________{i}___________________')
    e = json_l.classes_description(i)
    print(e)
    r = json_l.classes_ability_score(i)
    print(r)
    t = json_l.classes_background(i)
    print(t)
    y = json_l.classes_hits_dise(i)
    print(y)
    o = json_l.classes_armor(i)
    print(o)
    p = json_l.classes_weapons(i)
    print(p)
    a = json_l.classes_instruments(i)
    print(a)
    s = json_l.classes_saving_throws(i)
    print(s)
    d = json_l.classes_skills(i)
    print(d)
    f = json_l.classes_equipment(i)
    print(f)
