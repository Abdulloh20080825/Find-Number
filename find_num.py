import random

def find_num(num = 10):
        random_num = random.randint(1, num)
        print(f"I came up with a number from 1 and {num} can you find the number ?")
        attempts = 0
        while True:
                attempts += 1 
                random_enter = int(input(">>>"))
                if random_enter<random_num:
                        print("Error: the number I came up with is greater than the number you entered. Try again")
                elif random_enter > random_num:
                        print("Error: the number I came up with is less than the number you entered. Try again")
                else:
                        print(f"Congratulation you find it with {attempts} attepts")
                        break
        return attempts


def find_num_pc(num = 10):
        input(f"Think of a number from 1 to {num}, I'll try to find it (enter)")
        min_num = 1
        max_num = num
        attepts = 0
        while True:
                attepts += 1
                if min_num != max_num:
                        random_pc = random.randint(min_num,max_num)
                else:
                        random_pc = min_num
                answer = input(f"You thouth a {random_pc}\n\nPress (y) if i find correct.\nMy number greant (+).\nMy number less (-)\n\n").lower()
                
                if answer == '-':
                        max_num = random_pc - 1
                elif answer == '+':
                        min_num = random_pc + 1
                else:
                        break
        print(f"I find it with {attepts} attepts")
        
        return attepts  

def play(x = 10):
        _game_ = True
        while _game_:
                user_att = find_num(x)
                pc_att = find_num_pc(x)
                if user_att > pc_att:
                        print("I won")
                elif user_att < pc_att:
                        print("You won")    
                else:
                        print("...")
                _game_ = int(input("Will you still play? No(0) Yes(1)"))