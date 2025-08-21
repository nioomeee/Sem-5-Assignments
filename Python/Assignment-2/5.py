# 5 Create a dictionary of city names and temperatures. 
# Remove all cities withtemperature < 15°C or > 40°C, and 
# display the cleaned dictionary.

city_temperatures = {
    "Mumbai" : 34,
    "Delhi" : 39,
    "Ahmedabad" : 33,
    "Jaipur" : 44,
    "Moscow" : 8,
    "Dubai" : 45
}

print(f"Original Temperatures: {city_temperatures}")

cleaned_temperatures = {
    city: temp for city, temp in city_temperatures.items()
    if 15 <= temp <= 40
}

print(f"Cleaned temperatures (<15 and >40) : {cleaned_temperatures}")