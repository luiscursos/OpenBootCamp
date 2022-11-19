def countries_input():
    countries = set()
    length_set = int(input("Enter the length of the list: "))
    for i in range(length_set):
        country_user = input("Enter a country: ")
        countries.add(country_user)
         
    return(sorted(countries))

print(countries_input()) 

