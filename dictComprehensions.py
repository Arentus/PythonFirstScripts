country_to_capital = {
    'UK'     : 'London',
    'Brazil' : 'Brasilia',
    'Morocco': 'Rabat',
    'Sweden' : 'Stockholm'
}

capital_to_country = {capital: country for country, capital in country_to_capital.items()}

from pprint import pprint as pp
print(country_to_capital.items())
pp(capital_to_country)