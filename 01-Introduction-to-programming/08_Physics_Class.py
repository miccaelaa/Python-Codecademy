# 1. Write a function that takes a temperature in Fahrenheit, and converts Celsius.

def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

# 2. Write a function that takes a temperature in Celsius and converts it Fahrenheit.

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32 
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# 3. Define a function that takes in mass and acceleration. It should return mass multiplied by acceleration. 

def get_force(mass, acceleration):
  return mass * acceleration

train_mass = 22680
train_acceleration = 10
train_force = get_force(train_mass, train_acceleration)

print(f'The GE train supplies {train_force} Newtons of force.')

# 4. Define a function that takes in mass. If should return mass multiplied by c (constant) squared.

def get_energy(mass):
  # c = constant
  c = 3*10**8
  return mass * c**2

bomb_mass = 1
bomb_energy = get_energy(bomb_mass)

print(f'A 1kg bomb supplies {bomb_energy} Joules.')

# 5. Define a funtion that takes in mass, acceleration and distance. 

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  work = force * distance
  return work

train_distance = 100
train_work = get_work(train_mass, train_acceleration, train_distance)

print(f'The GE train does {train_work} Joules of work over {train_distance} meters.')
