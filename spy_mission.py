    print('''
    ███████╗██████╗ ██╗   ██╗    ███╗   ███╗██╗███████╗███████╗██╗ ██████╗ ███╗   ██╗
    ██╔════╝██╔══██╗╚██╗ ██╔╝    ████╗ ████║██║╚══███╔╝██╔════╝██║██╔═══██╗████╗  ██║
    █████╗  ██████╔╝ ╚████╔╝     ██╔████╔██║██║  ███╔╝ █████╗  ██║██║   ██║██╔██╗ ██║
    ██╔══╝  ██╔═══╝   ╚██╔╝      ██║╚██╔╝██║██║ ███╔╝  ██╔══╝  ██║██║   ██║██║╚██╗██║
    ███████╗██║        ██║       ██║ ╚═╝ ██║██║███████╗███████╗██║╚██████╔╝██║ ╚████║
    ╚══════╝╚═╝        ╚═╝       ╚═╝     ╚═╝╚═╝╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
    ''')
    print("Welcome, Agent.")
    print("Operation: BLACKOUT\nYour mission is to retrieve stolen intel from a high-security enemy base.\n")

    # Gadget choice
    gadget = input("Choose your gadget: 'EMP', 'cloak', or 'grapple':\n").lower()
    if gadget not in ["emp", "cloak", "grapple"]:
        print("You hesitated choosing a gadget. Mission failed.")
        return

    # Entry choice
    entry = input("You approach the facility. Do you enter through the 'vent' or the 'main gate'?\n").lower()
    if entry == "vent":
        print("You slide through the vents and drop down quietly into a dim corridor.")
        cam_choice = input("A security camera is sweeping the area. Do you 'wait' or 'run'?\n").lower()
        
        if cam_choice == "wait":
            if gadget == "cloak":
                print("You activate your cloak and walk right past the camera. Nice!")
            else:
                print("You wait for the camera to turn and slip by unnoticed.")
        elif cam_choice == "run":
            if gadget == "cloak":
                print("You sprint with your cloak activated. You’re invisible and fast—well done.")
            else:
                print("The camera spots you! Alarms blare. Guards incoming. Game Over.")
                return
        else:
            print("Invalid action. Mission failed.")
            return

        # Random guard encounter
        if random.choice([True, False]):
            print("\nA guard turns the corner suddenly!")
            if gadget == "emp":
                print("You use your EMP to disable his comms and knock him out. Clean.")
            elif gadget == "cloak":
                print("You freeze, cloaked. He walks past you. Close one.")
            elif gadget == "grapple":
                print("You zip up to a pipe overhead using your grappling hook. He never saw you.")
        else:
            print("\nNo guards in sight. Proceeding smoothly...")

        # Final choice
        door = input("\nYou find three rooms: 'red', 'green', 'black'. One holds the intel. Which do you choose?\n").lower()
        if door == "green":
            print("You find the terminal and download the intel...")
            print("But wait! Your handler's voice buzzes in your earpiece. \"Abort mission, Agent. The intel is fake!\"")
            twist = input("Do you 'abort' or 'download' anyway?\n").lower()
            if twist == "abort":
                print("You escape safely. Mission success—but the real data is still out there. 🕵️‍♂️")
            elif twist == "download":
                print("It was a trap! The data contained a tracking virus. They’re coming. Game Over.")
            else:
                print("You hesitated. Too long. They found you. Game Over.")
        elif door == "black":
            print("It’s a server room full of decoys. You triggered a silent alarm. Game Over.")
        elif door == "red":
            print("The door locks behind you and gas fills the room. Game Over.")
        else:
            print("Invalid door. Mission Failed.")

    elif entry == "main gate":
        print("Even with your gadget, you're spotted and surrounded. You’re no match for the front guards. Game Over.")
    else:
        print("Mission aborted due to indecision.")

# Replay loop
while True:
    spy_mission()
    again = input("\nPlay again, Agent? (yes/no): ").lower()
    if again != "yes":
        print("Mission control signing off. Stay sharp out there. 🔍")
        break
