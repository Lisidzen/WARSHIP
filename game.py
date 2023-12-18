import random

def rules():
    print("\n")
    print("YOU COMMAND AN AMERICAN SUBMARINE THAT BEEN SENT OUT")
    print("TO ATTACK JAPANESE SHIPS AT SEA DURING WORLD WAR TWO")
    print("THE ORDERS THAT CAN BE GIVEN ARE THE FOLLOWING:")
    print("PERISCOPE - TO SEARCH FOR JAPANESE SHIPS")
    print("TORPEDO - TO LAUNCH TORPEDOES AT JAPANESE SHIPS")
    print("DIVE - TO ESCAPE JAPANESE SHIPS THAT ARE ATTACKING\n")

def periscope(tesn):
    if tesn == 0:
        tes = random.randint(0, 99)
        if tes <= 75:
            tesn = 1  # Tanker
        else:
            tesn = 2  # Destroyer
        return tesn
    else:
        print("Target already set: ")
        return tesn

def tonnage(tonn):
    if tonn == 0:
        return random.randint(0, 9999)
    else:
        return tonn

def torpedo(torpedofire):
    itogchet = 0
    for i in range(1, torpedofire + 1):
        percentdetonation = 51
        random_num = random.randint(0, 99)
        if random_num < percentdetonation:
            itogchet += 1
    return itogchet

def generate_distance(distd):
    if distd == 0:
        distd = random.randint(0, 9999)
        return distd
    else:
        if distd >= 500:
            distd -= 500
            return distd
    return 0

def dive(typeship, distd):
    if typeship == 1:
        return 1
    else:
        if typeship == 2:
            b = distd // 1000
            depth = 12
            for i in range(1, b + 1):
                print(f"DEPTH: [{depth}] UNDER WATER")
                depth += 22
            print("\n")
            a = random.randint(0, 99) / 2
            c = int(a)
            depth += c
            if depth < 101:
                return 3
            else:
                return 2
    return 0


def main():
    tesn = 0
    typeship = 0
    tonn = 0
    result_ship_destroy = 0
    result_tonn = 0
    result_dive = 0
    distd = 0

    print("Before starting the game, please activate CAPS LOCK")
    print("DO YOU DESIRE THE RULES OF WARFISH?\n")
    rule_answer = input("Enter only [YES or NO]: ").upper()

    if rule_answer == 'NO':
        print("\n")
    else:
        if rule_answer == 'YES':
            rules()
        else:
            while rule_answer not in ['YES', 'NO']:
                rule_answer = input("Enter only [YES or NO]: ").upper()

    boat_name = input("PRINT THE NAME OF YOUR SUBMARINE : ")
    print("\n")

    torpedo_count = 26

    while torpedo_count != 0:
        orders = input("ORDERS, COMMANDER.[PERISCOPE/DIVE/TORPEDO]: ").upper()
        print("\n")
        if orders == 'PERISCOPE' or orders == 'P':
            typeship = periscope(tesn)
            tesn = typeship
            tonn = tonnage(tonn)
            if typeship == 1:
                print(f"CONTACT: JAPANESE TANKER")
                print(f"TONNAGE: [{tonn}]")
                print("\n")
            else:
                if typeship == 2:
                    distd = generate_distance(distd)
                    print(f"CONTACT: JAPANESE DESTROYER")
                    print(f"TONNAGE: [{tonn}]   DISTANCE: [{distd}] METER")
                    print("\tWARNING! WARNING! WARNING!")
                    print("More torpedoes are needed to guarantee destruction of the destroyer ship.")
                    print("OR CRASH DIVE!")
                    print("If the enemy ship is closer than 500 meters, we will not have time to hide in depth.")
                    print("\n")
                    if distd <= 500:
                        print(" Enemy destroyer dropped depth bombs and sank your boat. You are dead!\n")
                        break
        elif orders == 'TORPEDO' or orders == 'T':
            if typeship == 0:
                print("SIR, NO TARGET, NEED UP PERISCOPE.\n")
            else:
                if typeship == 1:
                    print(f"TARGET IS: JAPANESE TANKER")
                    print(f"TONNAGE: [{tonn}]")
                    print(f"{torpedo_count} Torpedos left")
                    torpedoes_to_fire = int(input("Number of torpedoes to fire? "))
                    print("\n")
                    torpedo_count -= torpedoes_to_fire
                    result_attack = torpedo(torpedoes_to_fire)
                    if result_attack >= 1:
                        print(f"Target Destroyed!!! {result_attack} of {torpedoes_to_fire} torpedoes hit the target.\n")
                        result_ship_destroy += 1
                        result_tonn += tonn
                        typeship = 0
                        tesn = 0
                        tonn = 0
                    else:
                        print("Better, attack again, sir!\n")
                else:
                    if typeship == 2:
                        print(f"{torpedo_count} Torpedos left")
                        print("TARGET IS: JAPANESE DESTROYER")
                        print(f"TONNAGE: [{tonn}]   DISTANCE: [{distd}] METER")
                        torpedoes_to_fire = int(input("Number of torpedoes to fire? "))
                        print("\n")
                        torpedo_count -= torpedoes_to_fire
                        result_attack = torpedo(torpedoes_to_fire)
                        if result_attack >= 1:
                            print(f"Target Destroyed!!! {result_attack} of {torpedoes_to_fire} torpedoes hit the target.\n")
                            result_ship_destroy += 1
                            result_tonn += tonn
                            typeship = 0
                            tesn = 0
                            tonn = 0
                            distd = 0
                        else:
                            print(f"{torpedoes_to_fire} torpedo miss, Sir!")
                            print("BETTER, crash dive, sir!\n")
                            distd = generate_distance(distd)
                            print(f"TARGET IS: JAPANESE DESTROYER")
                            print(f"TONNAGE: [{tonn}]   DISTANCE: [{distd}] METER")
                            if distd <= 500:
                                print(" Enemy destroyer dropped depth bombs and sank your boat. You are dead!\n")
                                break

        elif orders == 'DIVE' or orders == 'D':
            if typeship == 0:
                print("WE DON'T HAVE TO HIDE. NO ONE IN CONTACT\n")
            else:
                result_dive = dive(typeship, distd)
                if result_dive == 1:
                    print("WE'VE LOST CONTACT WITH THE TANKER\n")
                    tesn = 0
                    typeship = 0
                    tonn = 0
                elif result_dive == 2:
                    print("WE SUCCESSFULLY LEFT THE LINE OF FIRE\n")
                    tesn = 0
                    typeship = 0
                    tonn = 0
                    distd = 0
                elif result_dive == 3:
                    print("WE DID NOT HIDE.")
                    print("BOAT DESTROYED.\n")
                    tesn = 0
                    typeship = 0
                    tonn = 0
                    distd = 0
                    break
        else:
            print("ORDER NOT UNDERSTOOD, REPEAT:\n")

    print("Game END")
    print(f"Statistics: {boat_name} Sink the {result_ship_destroy} enemy ships")
    print(f"And all TONNAGE = {result_tonn} TONN")

if __name__ == "__main__":
    main()


