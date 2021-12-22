last_semester_gradebook = [['politics', 80], ['latin', 96], ['dance', 97], ['architecture', 65]]

# 1. Create a list with your classes and another list with your scores

subjects = ['physics', 'calculus', 'poetry', 'history'] 
grades = [98, 97, 85, 88]

# 2. Manually create a two-dimensional list to combine subjects and grades

gradebook = [['physics', 98],
             ['calculus', 97],
             ['poetry', 85],
             ['history', 88]]
print(gradebook)

# 3. Add more classes

gradebook.append(['computer science', 100])
gradebook.append(['visual arts', 93])

print(gradebook)

# 4. Modify the visual arts' grade
gradebook[-1][-1] = 98

# 5. Delete the grade value of the poetry class

gradebook[2].remove(85)

# 6. Add a 'Pass' value to the poetry class

gradebook[2].append('Pass')

# Create a new variable full_gradebook that combines both last_semester_gradebook and gradebook

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
