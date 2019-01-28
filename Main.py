

i = int(0)

genres = ["", "Puzzle", "Action", "Role-playing", "Sandbox", "Survival",  "Adventure", "MOBA", "Battle-royale", "First-Person-Shooter", "Third-Person-Shooter",  "Platformer", "Tactical", "Turn-based-strategy", "Simulation", "Massive Multi-player Online", "Strategy", "Sport", "Stealth"]
mode = ["Single-player", "Multi-player", "Single-player and Multi-player"]

games = [
                # game name, genre 1, genre 2, genre 3, playing-mode

    ["Portal 2", genres[1], genres[0], genres[0], mode[2]],                                            # 1
    ["The Witcher 3: Wild Hunt", genres[2], genres[3], genres[0], mode[0]],                            # 2
    ["Minecraft", genres[4], genres[5], genres[0], mode[2]],                                           # 3
    ["Grand Theft Auto V", genres[2], genres[6], genres[0], mode[2]],                                  # 4
    ["The Elder Scrolls V: Skyrim", genres[2], genres[3], genres[0], mode[0]],                         # 5

    ["Dota 2", genres[7], genres[0], genres[0], mode[1]],                                              # 6
    ["League of Legends", genres[7], genres[0], genres[0], mode[1]],                                   # 7
    ["Fortnite Battle Royale", genres[8], genres[0], genres[0], mode[1]],                              # 8 The worst!
    ["Overwatch", genres[9], genres[0], genres[0], mode[1]],                                           # 9
    ["Divinity: Original Sin 2 - Definitive Edition", genres[3], genres[0], genres[0], mode[2]],       # 10

    ["Mass Effect 2", genres[2], genres[3], genres[10], mode[0]],                                      # 11
    ["Spelunky", genres[11], genres[0], genres[0], mode[2]],                                           # 12
    ["Celeste", genres[11], genres[0], genres[0], mode[0]],                                            # 13
    ["XCOM 2", genres[12], genres[3], genres[13], mode[2]],                                            # 14

    ["Fallout: New Vegas", genres[2], genres[3], genres[0], mode[0]],                                  # 15
    ["Sid Meier's Civilization V", genres[13], genres[16], genres[0], mode[2]],                        # 16
    ["Stardew Valley", genres[14], genres[3], genres[0], mode[2]],                                     # 17
    ["World of Warcraft", genres[15], genres[3], genres[0], mode[1]],                                  # 18
    ["FTL: Faster Than Light", genres[16], genres[0], genres[0], mode[0]],                             # 19

    ["Undertale", genres[3], genres[0], genres[0], mode[0]],                                           # 20
    ["Rocket League", genres[17], genres[0], genres[0], mode[2]],                                      # 21
    ["Metal Gear Solid V: The Phantom Pain", genres[2], genres[6], genres[18], mode[2]],               # 22
    ["Counter-Strike: Global Offensive", genres[9], genres[0], genres[0], mode[1]],                    # 23
    ["The Witness", genres[1], genres[0], genres[0], mode[0]]                                          # 24
]

while True:
    print("How do you want to sort the games?")
    print("[1]  -  By genre")
    print("[2]  -  By mode")
    print("[3]  -  View all")
    print("[4]  -  Quit")
    choice = input()


    if choice == 1:
        print("What game genre do you want to play?")
        i = 0
        list = games
        while i < len(list):
            if i < 10:
                print("["+str(i+1)+"]  -  " + list[i][0])
            if 10 < i < 100:
                print("["+str(i+1)+"] -  " + list[i][0])
            if i >len(list):
                break
            i = i + 1

        print
        choice = input()

    elif choice == 2:
        print("What game mode do you want to play?")
        i = 0
        list = mode
        while i < len(list):
            if i < 10:
                print("[" + str(i + 1) + "]  -  " + list[i][0])
            if 10 < i < 100:
                print("[" + str(i + 1) + "] -  " + list[i][0])
            if i > len(list):
                break
            i = i + 1

        print
        choice = input()
    elif choice == 3:
        print("")
    elif choice == 4:
        print("Exiting")
        break
    else:
        print("error")


