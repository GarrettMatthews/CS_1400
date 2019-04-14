# Garrett Matthews, CS 1400, Project 6
# Problem: Create a program that receives bowling scores as an input, store the data, run some computations, and organize and display it in several organized tables as well as
# print some summaries of the data.
# Help with sorting the tables was found at https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/

# This project was a little more on the challenging side- specifically on working with dictionaries to edit their contents, and reorder those contents. Figuring out how to
# write tables to a text file was also challenging. I couldn't get it to work by simply putting writeline in front of the formated text. I found though that this could be avoided
# by assigning the formated text to a variable, and then writing that variable to a line.
# By completing this assignment I learned a lot about interacting with dictionaries, and displaying and using these dictionaries for text and informative purposes. 

# Just preparing some variables needed to complete the initial steps
answer = 'yes'
blank = ""
bowlers = {}
bowl = {}

# Making the initial dictionary
while answer == 'yes':
    user_input = input("Please enter the bowlers name and their score, seperated by a comma. When there are no more players, please enter a blank line.")
    
    if user_input == blank:
        print("All bowlers entered")
        break
    else:
        key, value = user_input.split(",")
        key = key.strip()
        value = value.strip()
        try:
            value = int(value)
        except ValueError:
            print("Thats not a valid number, sorry")
        bowl[key] = value
        
# Making the dictionary that gives an astericks for any player with a perfect score
for akey in (bowl.keys()):
    if '*' in akey:
        break
    if bowl[akey] == 300:
        bowlers['*{0:}'.format(akey)] = bowl[akey]
    else:
        bowlers[akey] = bowl[akey]
# Making a dictionary for sorting alphabetically by player names
bowl_alpha = bowl.copy()
# Making a dictionary for sorting numerically by player scores
bowl_numb = bowl.copy()

# Making the lists that will congratulate and express sympathies for best and worst scores respectively
names = sorted(bowl_numb, key=bowl_numb.__getitem__)
scores = sorted(bowl_numb.values())
# Finding the average score for the game
average = sum(scores) // len(scores)
# First line for each table
first = ("Bowler",'\t','\t',"Score \n")
# Writing the text file with all the tables and parts
file = open('game_results.txt','w')
file.write("Entered Order \n")
file.writelines(first)
for akey, avalue in zip(bowlers.keys(),bowlers.values()):
    line = (akey,'\t','\t', str(avalue), '\n')
    file.writelines(line)

file.write("\n")
file.write("\n")

file.write("Numerical Order \n")
file.writelines(first)
for key, value in sorted(bowl_numb.items(), key=lambda item: item[1], reverse = True):
    line = (key, "\t", "\t", str(value), "\n")
    file.writelines(line)

file.write("\n")
file.write("\n")

file.write("Alphabetical Order \n")
file.writelines(first)
for key in sorted(bowl_alpha.keys()):
    line = (key, "\t", "\t", str(bowl_alpha[key]), "\n")
    file.writelines(line)

file.write("\n")
file.write("\n")


congrats = ("Congratulations {0:}!".format(names[-1])," You had the high score of {0:}!".format(scores[-1]),"\n")
file.writelines(congrats)

file.write("\n")
file.write("\n")

sympathies = ("Sorry {0:},".format(names[0])," you had the lowest score of {0:}.".format(scores[0]),"\n")
file.writelines(sympathies)

file.write("\n")
file.write("\n")

mean = ("The average score for the team is {0:}".format(str(average)))
file.writelines(mean)

file.close()

