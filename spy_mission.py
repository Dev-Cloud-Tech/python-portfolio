    print('''
    ███████╗██████╗ ██╗   ██╗    ███╗   ███╗██╗███████╗███████╗██╗ ██████╗ ███╗   ██╗
    ██╔════╝██╔══██╗╚██╗ ██╔╝    ████╗ ████║██║╚══███╔╝██╔════╝██║██╔═══██╗████╗  ██║
    █████╗  ██████╔╝ ╚████╔╝     ██╔████╔██║██║  ███╔╝ █████╗  ██║██║   ██║██╔██╗ ██║
    ██╔══╝  ██╔═══╝   ╚██╔╝      ██║╚██╔╝██║██║ ███╔╝  ██╔══╝  ██║██║   ██║██║╚██╗██║
    ███████╗██║        ██║       ██║ ╚═╝ ██║██║███████╗███████╗██║╚██████╔╝██║ ╚████║
    ╚══════╝╚═╝        ╚═╝       ╚═╝     ╚═╝╚═╝╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
    ''')
    print("Welcome, Agent.")
    print("Your mission is to infiltrate the enemy facility, retrieve the stolen data, and escape undetected.\n")

    choice1 = input("You approach the facility. Do you enter through the 'vent' or the 'main gate'?\n").lower()
    if choice1 == "vent":
        choice2 = input("You sneak through the ventilation and drop into a hallway. A security camera is sweeping the area.\n"
                        "Do you 'wait' for it to pass or 'run' past quickly?\n").lower()
        if choice2 == "wait":
            choice3 = input("You slipped by unnoticed. You find three rooms: 'red', 'blue', and 'green'. One contains the data.\n"
                            "Which room do you enter?\n").lower()
            if choice3 == "red":
                print("It's a trap room! You triggered a silent alarm. Game Over.")
            elif choice3 == "blue":
                print("The room is empty. Suddenly, guards storm in. Game Over.")
            elif choice3 == "green":
                print("Bingo! You found the server. Data downloaded. You Win! 🕶️💾")
            else:
                print("No such room. You hesitate too long. Game Over.")
        elif choice2 == "run":
            print("The camera caught you. Guards swarm in. Game Over.")
        else:
            print("Invalid choice. Game Over.")
    elif choice1 == "main gate":
        print("You’re spotted immediately and captured. Game Over.")
    else:
        print("Invalid entry point. Mission Failed.")

# Replay loop
while True:
    spy_mission()
    again = input("\nMission complete. Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Mission terminated. Stay sharp, Agent. 🕵️‍♂️")
        break
