letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# dictionary that has letters as the keys and points as the value
letter_to_points = {k:v for k, v in zip(letters, points)}

# Add blank tiles to the dictionary
letter_to_points[' '] = 0

# Create a function that will take in a word and return how many points that word is worth.
def score_word(word):
  point_total = 0
  for letter in word.upper():
    point_total += letter_to_points.get(letter, 0)
  return point_total

brownie_points = score_word('brownie')
print(brownie_points)

# Create a dictionary that maps players to a list of the words they have played. 
player_to_words = {
  'player1': ['BLUE', 'TENNIS', 'EXIT'],
  'word:Nerd': ['EARTH', 'EYES', 'MACHINE'],
  'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'],
  'Prof Reader': ['ZAP', 'COMA', 'PERIOD']
}

# Function that would take in a player and a word, and add that word to the list of words they’ve played
def play_word(player, word):
  player_to_words[player].append(word.upper())

play_word('Lexi Con', 'hello')

# Create a dictionary that contains the mapping of players to how many points they’ve scored.
player_to_points = {}

def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0 
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points

update_point_totals()
print(player_to_points)
