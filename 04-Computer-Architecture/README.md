# Computer Architecture

## Introduction to Computer Architecture

#### 01.Creating an Adder Circuit

At the most basic level, the computer you are typing on right now is a complex combination of the gates you have already learned how to construct. But how do we go from having a NAND gate, for example, to having an entire processor that runs Mac OS?

One step we can take towards this goal is to create an ALU, or an Arithmetic Logic Unit. An ALU can perform a bunch of bitwise operations like adding, subtracting, and shifting.

For this project, we are going to focus on creating one part of the ALU, the adder.


## Introduction to Computer Architecture

#### 02.Ultra Super Calculation Computer

You are a software engineer and the new Ultra Super Calculation Computer (USCC) has just arrived in your office to be put online for use by users at USCC Headquarters. Every day the USCC will receive tons of data in the form of binary numbers and it is expected to perform specific calculations on this data but no one has told you how to do it!

Lucky for you, the engineers over at USCC headquarters have just sent you a copy of the Instruction Set Architecture that they are using. Finally, we can figure out what all those 1‘s and 0‘s have meant!

Your job today is to write the code for the CPU that will support the functions required by the ISA. Based on the design specification in the code editor window, you know you are asked to perform five functions:

- Add
- Subtract
- Multiply
- Divide
- Display a history of calculations

These five functions will also require several other support functions to be written as well so that we can access different parts of our computer hardware. We must also be able to:
- Read and split up our incoming data
- Store a binary number to a register
- Access what is stored in the register
- Allocate some registers for a ‘history’ of our calculations
- Store/Load from the history when needed
