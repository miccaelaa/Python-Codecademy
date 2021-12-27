# Logic gate's functions

# NAND gate
def NAND_gate(a, b):
  if a == 1 and b == 1:
      return 0
  return 1

# NOT gate
def NOT_gate(a):
  if NAND_gate(a, a): 
    return 1
  else:
    return 0

# AND gate
def AND_gate(a, b):
  return NOT_gate(NAND_gate(a, b))

# OR gate
def OR_gate(a, b):
  return NAND_gate(NAND_gate(a, a), NAND_gate(b,b))

# XOR gate
def XOR_gate(a, b):
  return AND_gate(NAND_gate(a, b), OR_gate(a, b))

#---------------------------------------------------
# Adder Circuit
# Half Adder
def half_adder(a, b):
  s = XOR_gate(a, b)
  c = AND_gate(a, b)
  return s, c

# TEST HALF ADDER 
print(half_adder(0,0))
print(half_adder(0,1))
print(half_adder(1,0))
print(half_adder(1,1))

# Full Adder
def full_adder(a, b, c):
  s1 = XOR_gate(a,b) 
  s2 = XOR_gate(s1, c)
  c1 = AND_gate(a, b)
  c2 = AND_gate(s1, c)
  c_out = OR_gate(c1, c2)
  return s2, c_out

# TEST FULL ADDER
print(full_adder(0,0,0))
print(full_adder(1,1,1))
print(full_adder(0,1,1))
print(full_adder(1,1,0))

# ALU
def ALU(a, b, c, opcode):
  if opcode == 0:
    return half_adder(a, b)
  else:
    return full_adder(a, b, c)

  
# TEST ALU 
print(ALU(0, 0, 1, 0))
print(ALU(0,0,1,1))
print(ALU(1, 1, 1, 0))
print(ALU(1, 1, 1, 1))


