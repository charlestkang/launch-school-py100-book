# EXERCISE 11
# Consider the data in the following table:

# Name	Country
# Alice	USA
# Francois	Canada
# Inti	Peru
# Monika	Germany
# Sanya	Uganda
# Yoshitaka	Japan

# You need to write some Python code to determine the country name associated with one of the listed
# names. Your code should include the data structure(s) you need and at least one test case to ensure
# the code works.

name_country_dict = {
    "Alice": "USA",
    "Francois": "Canada",
    "Inti": "Peru",
    "Monika": "Germany",
    "Sanya": "Uganda",
    "Yoshitaka": "Japan",
}

supplied_name = input("Whose associated country do you want to check?:\n").capitalize()
try:
    print(f"{supplied_name} is associated with {name_country_dict[supplied_name]}.")
except KeyError:
    print(f"{supplied_name} is not in this directory.")
