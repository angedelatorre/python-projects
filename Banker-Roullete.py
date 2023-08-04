import random

names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")

names_num = len(names) #len() function, to get the total number of list
random_name = random.randint(0, names_num - 1) #this will allow to generate random number 
choosen = names[random_name] #convert number to name 
print(f"{choosen} is going to buy the meal today!")

#choice method() // optional
choosen = random.choice(names)
print(choosen + "is going to buy the meal today!")