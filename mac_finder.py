"""
##### 0) Header #####
# Text Adventure Game
A chance to make your own Text Adventure Game.
This is an INDIVIDUAL project. Do not consult with others or share code.
Refer to the instructions on Canvas for more information.
# When You Are Done
When you pass all tests, remember to clean and document your code.
Be sure to unit test and document your functions.
"""
##### 1) Author Info #####
# Change these three fields
__author__ = "cameron.cutler@dmail.dixie.edu"
__title__ = "Mac Finder"
__description__ = "Find the unidentified Mac and bring it to the CEO of Apple."
# Leave these two fields unchanged
__version__ = 1
__date__ = "Spring 2019"
##### 2) Record Definitions #####
# Add a new record and modify the existing ones to fit your game.
'''
Records:
    World:
        status (str): Whether or not the game is "playing", "won",
                    "quit", or "lost". Initially "playing".
        map (dict[str: Location]): The lookup dictionary matching 
                                location names to their
                                information.
        player (Player): The player character's information.     
    Player:
        location (str): The name of the player's current location.
        inventory (list[str]): The player's collection of items.
                            Initially empty.
    Location:
        about (str): A sentence that describes what this location 
                    looks like.
        neighbors (list[str]): A list of the names of other places 
                            that you can reach from this 
                            location.
        stuff (list[str]): A collection of things available at 
                        this location.
'''
##### 3) Core Game Functions #####
# Implement the following to create your game.
def render_introduction() -> str:
    '''
    Create the message to be displayed at the start of your game.    
    Returns:
        str: The introductory text of your game to be displayed.
    '''
    return "Someone broke into Apple Campus and stole an unreleased Mac from one of Apple's secret labs.\n" + "They hid it somewhere on Apple Campus that has easy access points so they can easily move it off location.\n" + "Apple officials have asked you to find and recover that Mac and bring it to the CEO's office so that he can send it to the right people."
def create_world() -> dict[str, any]:
    '''
    Creates a new version of the world in its initial state.   
    Returns:
        World: The initial state of the world
    '''
    return {"status": "playing", "player": {"location": "Lobby", "inventory": []}, "map": [{"location": "Lobby", "about": "You are in the main lobby of Apple Campus with seats all around.  If you go east to the outside, you will leave the game.", "neighbors": ["Cafeteria", "Computer Hardware Lab", "Outside", "CEO's Office"], "stuff": ["SEATS"]}, {"location": "CEO's Office","about": "You are in the Apple CEO's office", "neighbors": ["", "", "Lobby", ""], "stuff": ["A DESK"]}, {"location": "Cafeteria", "about": "You are in the cafeteria of Apple Campus filled with food and tables.", "neighbors": ["Kitchen", "Lobby", "Food Storage and Loading Dock", "Computer Software and Coding Lab"], "stuff": ["FOOD", "TABLES"]}, {"location": "Computer Software and Coding Lab", "about": "You are in a coding lab used to develop computer software filled with macs used to develop computer software.", "neighbors": ["", "", "Cafeteria", ""], "stuff": ["MACS USED FOR CODING"]}, {"location": "Kitchen", "about": "You are in the kitchen used for the nearby cafeteria filled with food and food preparation equipment.", "neighbors": ["", "Cafeteria", "", ""], "stuff": ["FOOD PREPARATION EQUIPMENT", "FOOD"]}, {"location": "Food Storage and Loading Dock", "about": "You are in the food storage and loading dock area filled with food boxes and what looks to be an unidentified computer inside of a box.", "neighbors": ["", "", "", "Cafeteria"], "stuff": ["FOOD BOXES", "COMPUTER"]}, {"location": "Computer Hardware Lab", "about": "You are in a computer hardware lab filled with incomplete macs and mac parts used to build macs.", "neighbors": ["Lobby", "", "Hardware Storage", ""], "stuff": ["VARIOUS MACS", "VARIOUS MAC PARTS"]}, {"location": "Hardware Storage", "about": "You are in a hardware storage room filled with various macs, both complete and incomplete, and miscellaneous mac parts.", "neighbors": ["", "", "", "Computer Hardware Lab"], "stuff": ["VARIOUS MACS", "VARIOUS MAC PARTS"]}, {"location": "Outside", "about": "You are outside Apple Campus.", "neighbors": ["", "", "", "Lobby"], "stuff": []}]}
def render(world: dict[str, any]) -> str:
    '''
    Consumes a world and produces a string that will describe the current state
    of the world. Does not print.    
    Args:
        world (World): The current world to describe.    
    Returns:
        str: A textual description of the world.
    '''
    loc = world["player"]["location"]
    for xdict in world["map"]:
        if xdict["location"] == loc:
            about = "===================================== \n" + xdict["about"] + "\n"
            for item in xdict["stuff"]:
                if item not in world["player"]["inventory"]:
                    about += '\n' + "There is " + item + " here. \n"
            about += "====================================="
            return about
    return "error"
def get_options(world: dict[str, any]) -> list[str]:
    '''
    Consumes a world and produces a list of strings representing the options
    that are available to be chosen given this state.    
    Args:
        world (World): The current world to get options for.    
    Returns:
        list[str]: The list of commands that the user can choose from.
    '''
    loc = world["player"]["location"]
    options = []
    for xdict in world["map"]:
        if xdict["location"]  == loc:
            neighbors_pos=xdict["neighbors"]
    if neighbors_pos[0] != "":
        options.append("NORTH")
    if neighbors_pos[1] != "":
        options.append("SOUTH")
    if neighbors_pos[2] != "":
        options.append("EAST")
    if neighbors_pos[3] != "":
        options.append("WEST")
    for xdict in world["map"]:
        for item in xdict["stuff"]:
            if xdict["location"] == loc and item not in world["player"]["inventory"]:
                options.append("GET " + item)
    options.append("QUIT")
    return options
def update(world: dict[str, any], command: str) -> str:
    '''
    Consumes a world and a command and updates the world according to the
    command, also producing a message about the update that occurred. This
    function should modify the world given, not produce a new one.    
    Args:
        world (World): The current world to modify.    
    Returns:
        str: A message describing the change that occurred in the world.
    '''
    loc = world["player"]["location"]
    if command == "QUIT":
        world["status"] = "quitting"
        return "Sorry to see you go!"
    elif command == "NORTH":
        for xdict in world["map"]:
            if xdict["location"]  == loc:
                world["player"]["location"] = xdict["neighbors"][0]
    elif command == "SOUTH":
        for xdict in world["map"]:
            if xdict["location"]  == loc:
                world["player"]["location"] = xdict["neighbors"][1]
    elif command == "EAST":
        for xdict in world["map"]:
            if xdict["location"]  == loc:
                world["player"]["location"] = xdict["neighbors"][2]
    elif command == "WEST":
        for xdict in world["map"]:
            if xdict["location"] == loc:
                world["player"]["location"] = xdict["neighbors"][3]
    elif command == "GET FOOD":
        world["player"]["inventory"].append("FOOD")
    elif command == "GET A DESK":
        world["player"]["inventory"].append("A DESK")
    elif command == "GET TABLES":
        world["player"]["inventory"].append("TABLES")
    elif command == "GET MACS USED FOR CODING":
        world["player"]["inventory"].append("MACS USED FOR CODING")
    elif command == "GET FOOD PREPARATION EQUIPMENT":
        world["player"]["inventory"].append("FOOD PREPARATION EQUIPMENT")
    elif command == "GET VARIOUS MACS":
        world["player"]["inventory"].append("VARIOUS MACS")
    elif command == "GET VARIOUS MAC PARTS":
        world["player"]["inventory"].append("VARIOUS MAC PARTS")
    elif command == "GET COMPUTER":
        world["player"]["inventory"].append("COMPUTER")
    elif command == "GET FOOD BOXES":
        world["player"]["inventory"].append("FOOD BOXES")
    elif command == "GET SEATS":
        world["player"]["inventory"].append("SEATS")
    if world["player"]["location"] == "Outside":
        world["status"] = "loose"
    if world["player"]["location"] == "CEO's Office" and ("COMPUTER" in world ["player"]["inventory"]):
        world["status"] = "win"
    return ""
def render_ending(world: dict[str, any]) -> str:
    '''
    Create the message to be displayed at the end of your game.    
    Args:
        world (World): The final world state to use in describing the ending.    
    Returns:
        str: The ending text of your game to be displayed.
    '''
    if world["status"] == "win":
        return "The CEO thanks the finder and awards them with a new Mac."
    elif world["status"] == "loose":
        return "The supposed finder left to find other opportunities."
    else:
        return "The supposed finder gave up."
def choose(options: list[str]) -> str:
    '''
    Consumes a list of commands, prints them for the user, takes in user input
    for the command that the user wants (prompting repeatedly until a valid
    command is chosen), and then returns the command that was chosen.    
    Note:
        Use your answer to Programming Problem #42.3    
    Args:
        options (list[str]): The potential commands to select from.    
    Returns:
        str: The command that was selected by the user.
    '''
    print("Your current options are:")
    for i in range(len(options)):
        print("   " + options[i])
    while True:
        command=input("What do you want to do? ")
        command=command.upper()
        if command in options:
            break
        print("  That does not seem to be an option at this point")
    return command
###### 6) Main Function #####
# Do not modify this area
def main() -> None:
    '''
    Run your game using the Text Adventure console engine.
    Consumes and produces nothing, but prints and indirectly takes user input.
    '''
    print(render_introduction())
    world = create_world()
    while world['status'] == 'playing':
        print(render(world))
        options = get_options(world)
        command = choose(options)
        print(update(world, command))
    print(render_ending(world))
    input("Press any key to continue")
if __name__ == '__main__':
    main()