import os
import random
import time

class TicTacToe:
    def __init__(self):
        self.new_game = True
        self.turn = 'X'
        self.theBoard = {'1': ' ','2': ' ','3': ' ','4': ' ','5': ' ','6': ' ','7': ' ','8': ' ','9': ' '}
        self.players = []
        self.game_over = False

    def play_again(self):
        self.new_game = False
        self.theBoard = {'1': ' ','2': ' ','3': ' ','4': ' ','5': ' ','6': ' ','7': ' ','8': ' ','9': ' '}

    def help(self):
        print("""
            WELCOME TO TIC TAC TOE GAME THE COLOMNS AND ROWS ARE DISPLAY LIKE THIS
            TAKE A NUMBER FROM 1 - 9 FOR YOUR TURN POSITION
                    1 | 2 | 3
                    ---------
                    4 | 5 | 6
                    ---------
                    7 | 8 | 9
        """)

    def is_valid(self, input):
        """
            check input:
                if it's a number between 1 -9 only
                if the field is empty
        """
        try:
            if self.theBoard[input] != ' ':
                print('This field here is not empty.')
                return False
        except KeyError:
                print('Invalid Character!\nYou can only choose from 1 to 9')
                return False
        return True


    def start(self, redo=False, needhelp=True, playwithcomputer=False) -> None:
        if needhelp:
            self.help()
        self.printBoard()   
        while True:
            
            # take input
            # taking input neither computer or player
            if playwithcomputer and self.turn == 'O':
                sign = f'{random.randint(1, 9)}'
                print(f'Computer choosed {sign}')
                time.sleep(1)
            else:
                sign = input(f"It's your turn {self.turn}: ")
                
            if self.is_valid(input=sign) == False:
                continue
            else:
                os.system('cls||clear')
                    

            # CHANGING THE POSITION WITH THE TURN USER INPUTED
            self.theBoard[sign] = self.turn


            # PRINTING THE BOARD
            self.printBoard()

            # CHECKING THE WINNING MATCH OF ALL SIDES
            if self.check_rows() or self.check_columns() or self.check_sides():
                os.system('cls||clear')  
                self.printBoard()
                self.players.append(self.turn)

                print(f'*** {self.turn} Wins ***')
                print('\n\n')
                if redo:
                    self.play_again()
                    self.printBoard()
                    continue

                next = input('Do you want to start over?: ').upper()
                
                if next in ['Y', 'YES']:
                    self.play_again()
                    self.printBoard()
                    continue
                elif next in ['N', 'NO']:
                    break

            # CHANGING THE TURN
            self.turn = 'O' if self.turn == 'X' else 'X'
                
                
            # CHECKING IF ALL FEILDS ARE FILLED UP IF YES GAME OVER WHICH IS DRAW
            if ' ' not in self.theBoard.values():
                os.system('cls||clear')
                self.printBoard()
                print('** DROW')
                if redo:
                    self.play_again()
                    continue
                elif input('Do you want to start over?: ').upper() in ['Y', 'YES']:
                    self.play_again()
                    continue
                else:
                    break
        
        if self.players:
            if self.players.count('X') > self.players.count('O'):
                print(f'---   X is the Winner ------')
            elif self.players.count('X') < self.players.count('O'):
                print(f'--- O is the Winner ------')
            elif self.players.count('X') == self.players.count('O'):
                print('----- DRAW ------')

            else:
                print('---- NO WINNER  ---')
            
    def printBoard(self) -> None:
        """Display the rows and coloumns of the board"""
        print(self.theBoard['1'], ' | ', self.theBoard['2'], ' | ', self.theBoard['3'])
        print('---+-----+---')
        print(self.theBoard['4'], ' | ', self.theBoard['5'], ' | ', self.theBoard['6'])
        print('---+-----+---')
        print(self.theBoard['7'], ' | ', self.theBoard['8'], ' | ', self.theBoard['9'])


    def check_rows(self, turn=None) -> bool:
        """
            return True if any of the three row are matched
            1, 2, 3
            4, 5, 6
            7, 8, 9
        """
        if self.theBoard['1'] == self.theBoard['2'] == self.theBoard['3'] != ' ':
            return True
        elif self.theBoard['4'] == self.theBoard['5'] == self.theBoard['6'] != ' ':
            return True
        elif self.theBoard['7'] == self.theBoard['8'] == self.theBoard['9'] != ' ':
            return True
        return False

    def check_columns(self, turn=None) -> bool:
        """
            return True if any of the three colomns are matched
            1, 4, 7
            2, 5, 8
            3, 6, 9
        """
        if self.theBoard['1'] == self.theBoard['4'] == self.theBoard['7'] != ' ':
            return True
        elif self.theBoard['2'] == self.theBoard['5'] == self.theBoard['8'] != ' ':
            return True
        elif self.theBoard['3'] == self.theBoard['6'] == self.theBoard['9'] != ' ':
            return True
        return False

    def check_sides(self, turn=None) -> bool:
        """
            return True if any of the tow sides are matched
            1, 5, 9
            3, 5, 7
        """
        if self.theBoard['1'] == self.theBoard['5'] ==  self.theBoard['9'] != ' ':
            return True
        elif self.theBoard['3'] ==  self.theBoard['5'] == self.theBoard['7'] != ' ':
            return True

        return False