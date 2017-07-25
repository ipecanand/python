__author__ = 'inatiwari'

def dictcomp():
	country_to_capital = {'United Kingdom': 'London',
						'Brazil': 'Brazila',
						'Morocco': 'Rabit',
						'Sweedon': 'Stockholm'}
	capital_to_country = {capital: country for country,
						capital in country_to_capital.items()}
	print(capital_to_country)

if __name__ == '__main__':
	dictcomp()