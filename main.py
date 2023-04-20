
import os
if __name__ == '__main__':
    print('Welcome to RoboSpecker 1.1 Created by Avi')
    while True:
            x=input("Enter what do you want to you speck:")
            if x =="q":
                os.system("say 'bye bye Friend'")
                break
            command = f"say {x}"
            os.system(command)