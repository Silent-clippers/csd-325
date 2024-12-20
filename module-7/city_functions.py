# Keanu Foltz Module 7.2 CSD-325 12/1
#

def main():
    print(format_city_country("Madrid", "Spain", ))
    print(format_city_country("Honolulu", "USA", 1000000))
    print(format_city_country("Tokyo", "Japan", 5000000, "Japanese"))

def format_city_country(city, country, population = None, language = None):
    if population:
        return f"{city.capitalize()}, {country.capitalize()} - Population: {population} "

    elif language:
        return f"{city.capitalize()}, {country.capitalize()}, {language.capitalize()}"

    elif population and language:
        return f"{city.capitalize()}, {country.capitalize()}, - Population: {population}, {language.capitalize()}"

    else:
        return f"{city.capitalize()}, {country.capitalize()}"


if __name__ == '__main__':
    main()