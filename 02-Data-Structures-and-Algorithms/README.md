# Data Structures and Algorithms

## Stacks

#### 01.Towers of Hanoi

Towers of Hanoi is an ancient mathematical puzzle that starts off with three stacks and many disks.The objective of the game is to move the stack of disks from the leftmost stack to the rightmost stack.

The game follows three rules:

1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
3. No disk may be placed on top of a smaller disk.

In this project, we are going to use our knowledge of stacks to implement this game!

## Hash Maps

#### 02.Blossom

The language of the flowers has a long history and has often been a topic resigned to the domain of dusty books in a thrift bookseller or a library. With Blossom, we want to give people lightning fast access to all of the possible meanings of their favorite flowers.

In this project, we are going to implement a hash map to relate the names of flowers to their meanings. In order to avoid collisions when our hashing function collides the names of two flowers, we are going to use separate chaining. We will implement the Linked List data structure for each of these separate chains.

## Sorting Algorithms

#### 03.A Sorted Tale

You recently began employment at “A Sorted Tale”, an independent bookshop. Every morning, the owner decides to sort the books in a new way.

Some of his favorite methods include:

- By author name
- By title
- By number of characters in the title
- By the reverse of the author’s name
Throughout the day, patrons of the bookshop remove books from the shelf. Given the strange ordering of the store, they do not always get the books placed back in exactly the correct location.

The owner wants you to research methods of fixing the book ordering throughout the day and sorting the books in the morning. It is currently taking too long!

## Trees

#### 04.Choose Your Own Adventure: Wilderness Escape

Welcome to Wilderness Escape, an online Choose-Your-Own-Adventure. Our users get a unique story experience by picking the next chapter of their adventure. We use the tree data structure to keep track of the different paths a user may choose.

## Graphs and Graph Search

#### 05.SkyRoute: A Graph Search Program
Vancouver’s public metro system has asked you to help create a program to help commuters get from one landmark to another. You’ll be building out “SkyRoute,” a routing tool that uses breadth-first search, depth-first search, and Python dictionaries to accomplish this feat. For the purposes of this project, you can assume that it takes the same amount of time to get from each station to each of its connected neighboring stations.

First, tab through the files you have at your disposal:

- graph_search.py has the bfs() and dfs() functions implemented in Python
- vc_metro.py contains a graph of all stations in the Vancouver metro system
- vc_landmarks.py contains a dictionary of Vancouver landmarks mapped to their nearest metro station(s)
- landmark_choices.py contains a dictionary of letters of the alphabet mapped to landmarks to make it easier for users to make a selection

## Greedy Algorithms

#### 06.Traveling Salesperson

Traveling Salesperson is a widely studied graph theory problem that is solved by using a greedy algorithm. The premise is that you have a graph of cities with certain distances (or weights) between them. The objective is to find the shortest path that will allow you to visit each city once, leaving you at the city in which you began your journey.

## Dynamic Programming

#### 07.Longest Common Subsequence

Given two strings: "ABAZDC" and "BACBAD", how can we determine the longest common subsequence?

In other words, what series of letters from left to right do they share? The letters don’t need to be directly next to each other. In this example, the longest sequence is "ABAD" for a length of 4.

Longest Common Subsequence may seem like an obscure problem, but it has applications in genomics. “A”, “C”, “G”, and “T” represent the four nucleotide bases of a DNA strand. The longest common subsequence of among these letters would provide valuable information about two people’s genetics.

In this project, we are going to use our knowledge of graphs and greedy algorithms to solve the problem.
