# Nesting
# diccionario dentro de un diccionario

capitals = {
    "France":"Paris",
    "Germany":"Berlin"
}

# Nesting a List in a Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting Dictionary in a Dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 12}
}

# Nesting Dictionary in a List

travel_log = [
    {
        "country": "France", "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12
    },
    {
        "country": "Germany", "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 12
    },
]


'''Dictionary in List Exercise, Prime Numbers'''

def add_new_country(country, total_visits, cities_visited):
    travel_log.append({"country":country, "cities_visited":cities_visited, "total_visits": total_visits})

add_new_country('Russia', 2, ['Moscow', 'Saint Petersburg'])

# Otra forma de hacerlo

# def add_new_country_2(country_visited, time_visited, cities_visited):
#     new_country = {}
#     new_country['country'] = country_visited
#     new_country['visits'] = time_visited
#     new_country['cities'] = cities_visited
#     travel_log.append(new_country)

#add_new_country_2('Russia', 2, ['Moscow', 'Saint Petersburg'])
