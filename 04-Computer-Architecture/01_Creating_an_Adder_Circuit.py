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


