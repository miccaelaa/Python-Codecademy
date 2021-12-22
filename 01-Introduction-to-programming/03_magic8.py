import random 

# 1. Declare a variable name and assign it to the name of the person who will be asking the Magic 8-Ball

name = 'Lucas'

# 2. Declare a variable question, and assign it to a “Yes” or “No” question you’d like to ask the Magic 8-Ball.

question = 'Will I win the lottery?'

# 3. We want to store the answer of the Magic 8-Ball in another variable, which we’ll call answer

answer = ''

# 4. Declare a variable called random_number.

random_number = random.randint(1, 9)

# 5. Utilize control flow using an if/elif/else statement to assign different answers for each randomly generated value.

if random_number == 1:
  answer = 'Yes - definitely'
elif random_number == 2:
  answer = 'It is decidedly so.'
elif random_number == 3:
  answer = 'Without a doubt.'
elif random_number == 4:
  answer = 'Reply hazy, try again.'
elif random_number == 5:
  answer = 'Ask again later.'
elif random_number == 6:
  answer = 'Better not tell you now.'
elif random_number == 7:
  answer = 'My sources say no.'
elif random_number == 8:
  answer = 'Outlook not so good.'
elif random_number == 9:
  answer = 'Very doubtful.'
else:
  answer = 'Error'

# 6. Write a print() statement to output the asker’s name and their question

print(name + ' asks: ' + question)

# 7. Add a second print() statement that will output the Magic 8-Ball’s answer.

print('Magic 8-Ball\'s answer: ' + answer)

# 8. What if the asker does not provide a name?

if name == '':
  print('Question: ' + question)
else:
  print(name + ' asks: ' + question)

# 9. What if the question string is empty? 

if question == '':
  print('The Magic 8-Ball cannot provide a fortune unless you ask it something.')
else:
  print(name + ' asks: ' + question)
  print('Magic 8-Ball\'s answer: ' + answer)


