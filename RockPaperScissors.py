# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 19:32:32 2023

@author: Aly Mak
"""
import random

stop = False
player_times_won = 0
computer_times_won = 0
tied_games = 0 
games_played = 0

while stop == False:
    def randomRPS():
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        return computer_choice
    
    def checkWon(computer, player):
        # 0 means computer won
        # 1 means player on 
        # 2 means tie
        if(computer == "rock" and player == "scissors"):
            return 0
        elif(computer == "rock" and player == "paper"):
            return 1
        elif(computer == "rock" and player == "rock"):
            return 2
        elif(computer == "paper" and player == "scissors"):
            return 1
        elif(computer == "paper" and player == "rock"):
            return 0
        elif(computer == "paper" and player == "paper"):
            return 2
        elif(computer == "scissors" and player == "rock"):
            return 1
        elif(computer == "scissors" and player == "paper"):
            return 0
        elif(computer == "scissors" and player == "scissors"):
            return 2
        else:
            return 3
        
    player_choice = None
    player_choices = ["rock", "paper", "scissors"]
    while player_choice not in player_choices:
        player_choice = input("Please select rock, paper, or scissors: ").lower()
        if player_choice not in player_choices:
            print("Please input a valid choice.")
    
    computer_choice = randomRPS()
    winner = checkWon(computer_choice, player_choice)
    
    
    if(winner == 0):
        computer_times_won += 1
        games_played += 1
        print("You selected %s" % player_choice)
        print("Computer selected %s" % computer_choice)
        print("Therefore, computer won! Better luck next time :D")
    elif(winner == 1):
        player_times_won += 1
        games_played += 1
        print("You selected %s" % player_choice)
        print("Computer selected %s" % computer_choice)
        print("Therefore, you won! Congratzzz :D")
    elif(winner == 2):
        tied_games += 1
        games_played += 1
        print("You selected %s" % player_choice)
        print("Computer selected %s" % computer_choice)
        print("Therefore, it's a tie! No one wins and no one loses!")
    else:
        print("Unexpected error occured")
    print("\n")
    print("Game has been played %i times. Computer has won %i times. Player has won %i times. Game has tied %i times" % (games_played,computer_times_won, player_times_won, tied_games))
    valid_keep_playing = False
    while valid_keep_playing == False:
        play_again = input("Do you want to play again (Y/N): ").upper()
        if(play_again == "Y" or play_again == "N"):
            valid_keep_playing = True
        print("\n")
    if(play_again == "N"):
        print("Thanks for playing. Game Exited.")
        stop = True
    
