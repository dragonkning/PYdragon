# First program 
number = range(101)#create a list of 100 values
even_list = list()#create list for even values
odd_list = list()#create list for odd values
even = 0#number of even values
odd = 0#number of odd values

for i in number:#count the number of even and odd
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(even)
print(odd)

for i in number:#select odd values
    if i % 2 != 0:
        odd_list.append(i)
print(odd_list)

for i in number:#select even values
    if i % 2 == 0:
        even_list.append(i)
print(even_list)

#Thecond progman
dict_countries = {"Austria": "Vienna",
                  "Armenia": "Yerevan",
                  "Belarus": "Minsk",
                  "Bulgaria": "Sofia",
                  "Germany": "Berlin",
                  "France": "Paris",
                  "Ukraine": "Kiev",
                  "Sweden": "Stockholm"}#create a dictionary with countries and capitals
list_countries = ("Ukraine", "USA", "Hungary", "England", "Poland", "Romania")#create a list with countries

for i in list_countries:#check the availability of countries from the list in the dictionary
    if i in dict_countries:
        print(dict_countries [i])#we display the result in case of coincidence in the form of the capital of the country
