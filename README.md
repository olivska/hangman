# Hangman
Hangman is a guessing game for a single player, user vs computer.

## Table of contents
* [Description](#description)
* [Dependencies](#dependencies)
* [Setup and Execution](#setup-and-execution)

## Description
Computer randomly picks the word from a list and asks the user to provide a letter to guess, it keeps asking for a new 
letter as long as the word remains hidden and user has at least one life left. If the letter occurs in the chosen word, 
the display will show its placement. Otherwise, the user loses a life. Every time one is lost the program prints an image 
of a hangman that represents progress of the game. Once user loses all of 6 lives the game is over.

This project was created for learning purposes.
	
## Dependencies
Project is created with:
* Windows 10
* Python 3.10
* PyCharm 2022.1
## Setup and Execution
Clone this repo to your PyCharm and run main.py to start the program.