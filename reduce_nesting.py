# age = 25                  Junior level code
# city = "New York"
# income = 50000
# education_level = "Bachelor"

# if age >= 18:
#     if city == "New York" or city == "Los Angeles":
#         if income >= 40000 and income <= 100000:
#             if education_level == "Bachelor" or education_level == "Master":
#                 print("Eligible for the program")
#             else:
#                 print("Not eligible due to education level")
#         else:
#             print("Not eligible due to income")
#     else:
#         print("Not eligible due to city")
# else:
#     print("Not eligible due to age")                   So much nesting can make you mess up your indentations easily especially in a language like python


# Senior level code

age = 25
city = "New York"
income = 50000
education_level = "Bachelor"

eligible_age = age >= 18
eligible_city = city == "New York" or city == "Los Angeles"
eligible_income = 40000 <= income <= 100000
eligible_education = education_level == "Bachelor" or education_level == "Master"

if not eligible_age:
    print("Not eligible due to age")
elif not eligible_city:
    print("Not eligible due to city")
elif not eligible_income:
    print("Not eligible due to income")
elif not eligible_education:
    print("Not eligible due to education level")
else:
    print("Eligible for the program")
