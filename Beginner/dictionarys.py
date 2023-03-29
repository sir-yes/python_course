travel_log_dict = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": ["Berlin", "Stuttgart"],
}

print(travel_log_dict["France"])






travel_log_list = [
    {
    "country": "France",
    "visits": 12,
    "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    {
    "country": "Germany",
    "visits": 5,
    "cities_visited": ["Berlin", "Stuttgart"],
    },
]

def add_new_country(country_visited,number_of_visits,cities_visited):
    travel_log_list.append(
        {
        "country": country_visited,
        "visits": number_of_visits,
        "cities_visited": cities_visited
    }
    )

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
#print(add_new_country)
print(travel_log_list)