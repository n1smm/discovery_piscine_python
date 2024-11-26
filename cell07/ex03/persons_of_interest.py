#!/usr/bin/env python3

women_scientists = {
        "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
        "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
        "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
        "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

def select_date(data):
    return (data["date_of_birth"])

def get_dates(women_scientists):
    new_scientists = dict(sorted(women_scientists.items(), key=lambda item: select_date(item[1])))
    return new_scientists

def famous_births(women_scientists):
    new_order = get_dates(women_scientists)
    for data in new_order.values():
        full_name = data.get("name")
        date = data.get("date_of_birth")
        print(full_name, "is a great scientist born in", date + ".")

famous_births(women_scientists)
