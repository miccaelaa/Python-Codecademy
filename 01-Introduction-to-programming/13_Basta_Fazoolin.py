class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

    
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return self.address
  
  def available_menus(self, time):
    available = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time: 
        available.append(menu)
    return available


class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time 

  def __repr__(self):
    return f'{self.name} menu available from {self.start_time} to {self.end_time}'
  
  def calculate_bill(self, purchased_items):
    bill = 0
    for item in purchased_items:
      if item in self.items:
        bill += self.items[item]
    return bill

  
# Brunch Menu 
brunch_items = {
   'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 
   'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 
   'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch = Menu('Brunch', brunch_items, 11, 16)

# Early Bird Menu 
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 
  'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 
  'coffee': 1.50, 'espresso': 3.00
}
early_bird = Menu('Early Bird', early_bird_items, 15, 18)

# Dinner Menu 
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 
  'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 
  'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00
}
dinner = Menu('Dinner', dinner_items, 17, 23)

# Kids Menu 
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 
  'apple juice': 3.00
}
kids = Menu('Kids', kids_items, 11, 21)

# Arepa's Menu
arepa_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 
  'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepa_menu = Menu('Take a\' Arepa', arepa_items, 10, 20)


print(brunch)
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))


# Franchises
menus = [brunch, early_bird, dinner, kids]

flagship_store = Franchise('1232 West End Road', menus)

new_installment = Franchise('12 East Mulberry Street', menus)

arepas_place = Franchise('189 Fitzgerald Avenue',[arepa_menu])


# Business 
basta = Business('Basta Fazoolin\' with my Heart', [flagship_store, new_installment])

arepa = Business('Take a\' Arepa', [arepas_place])
