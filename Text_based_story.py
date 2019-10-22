import time

def name(name):
    name = input('What is your name? ')
    time.sleep(0.5)
    print('Hello {}, you have woken up in the Arndale surrounded by zombies and you need to escape!'.format(name))
    return name


def id_card(): 
    print("There's an access card on the zombie infront of you, you can: ")
    time.sleep(0.5)
    id_card_list =['1. Take it', '2. Leave it']
    time.sleep(0.5)
    for option in id_card_list:
        print(option)
    id_card2 = input('What would you like to do? ')
    if id_card2 == '1':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('You bend down to pick up the access card.')
        time.sleep(0.5)
        print('As you reach for the access card the zombie wakes up and grabs your arm.')
        time.sleep(0.5)
        print("It pulls you in and you can't escape.")
        time.sleep(0.5)
        print('The zombie kills you!')
        exit()
    elif id_card2 == '2':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('You continue past the zombie without the access card.')
    else:
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('Use the number option, please try again.')
        id_card()

def fire_extinguisher():
    print("As you walk down the corridor, you notice a door.")
    time.sleep(0.5)
    print("You try to open it but it requires an access card, there's a fire extinguisher next to the door.")
    time.sleep(0.5)
    fire_extinguisher_list =['1. Pick it up', '2. Leave it and continue down the corridor']
    for i in fire_extinguisher_list:
        print(i)
    fire_extinguisher2 = input('What would you like to do with the fire extinguisher? ')
    if fire_extinguisher2 == '1':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('You pick up the fire_extinguisher.')
        smash_list=['1. Go back to the zombie and smash it with the extinguisher', '2. Continue down the corridor']
        time.sleep(0.5)
        for x in smash_list:
            print(x)
        smash = input('What would you like to do? ')
        if smash == '1':
            time.sleep(0.5)
            print(' ')
            time.sleep(0.5)
            print('You killed the zombie and get the access card, but the fire extinguisher burst and is now unusable.')
            return True
        elif smash == '2':
            time.sleep(0.5)
            print(' ')
            time.sleep(0.5)
            print("You place the fire extinguisher back on the floor as it's too heavy to carry.")
            print('You contine you without the access card.')
            return False
        else:
            time.sleep(0.5)
            print(' ')
            time.sleep(0.5)
            print('Use the number option, please try again.')
            fire_extinguisher()
    elif fire_extinguisher2 == '2':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('You left the extinguiser behind and continue.')
        return False
    else:
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('Use the number option, please try again.')
        fire_extinguisher()

def no_access_card():
    print('As you continue past the locked door you hear a phone start ringing, you search nearby for the phone and find it next to a dead body. Do you:')
    time.sleep(0.5)
    zombie_phone =['1. Pick the phone up and answer it.', '2. Run away from the noise because it might attract zombies.']
    time.sleep(0.5)
    for j in zombie_phone:
        print(j)
    answer = input('What would you like to do? ')
    if answer == '1':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('You answer the phone, its an automated message saying "If you are hearing this message, you have an hour to leave the mall before we blow it up to exterminate the zombies.".')
    elif answer == '2':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print("You run away from the noise but as you run down the corridor a zombie grabs you, you can't escape its grip. The zombie eats you.")
        exit()
    else:
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('Use the number option, please try again.')
        no_access_card()
        
def access_room_phone():
    print("You use the access card on the door, there's a click and the door opens.")
    time.sleep(0.5)
    print("As you step in to the room, the phone begins to ring. Do you:")
    time.sleep(0.5)
    phone_list=['1. Answer phone', '2. Ignore phone']
    time.sleep(0.5)
    for x in phone_list:
        print(x)
    phone2 = input('What would you like to do?')
    if phone2 == '1':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('You answer the phone, its an automated message saying "If you are hearing this message, you have an hour to leave the mall before we blow it up to exterminate the zombies.".')
    elif phone2 == '2':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('You walk around the mall aimlessly for an hour, then you get blown up with the rest of the zombies.')
        exit() #try loop
    else:
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('Use the number option, please try again.')
        access_room_phone()

def scavange():
    print("You leave the room and realise you're hungry.")
    time.sleep(0.5)
    print("So, you head to Mcdonalds in the food court and find a half eaten Big Mac on the table and a lighter, you take the lighter as you may need it later. Do you:")
    time.sleep(0.5)
    food_list=['1. Eat the Big Mac', '2. Leave the Big Mac']
    time.sleep(0.5)
    for food in food_list:
        print(food)
    foods = input('What would you like to do? ')
    if foods == '1':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('You get poisoned off the half eaten Big Mac and collapse, then a zombie comes and eats you.')
        exit() # Try loop
    elif foods == '2':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('You leave the Big Mac on the table and stay hungry.')
    else:
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('Use the number option, please try again.')
        scavange()

def scavange2():
    print("As you walk down the corridor, realise you're hungry.")
    time.sleep(0.5)
    print("So, you head to Mcdonalds in the food court and find a half eaten Big Mac on the table and a lighter, you take the lighter as you may need it later. Do you:")
    time.sleep(0.5)
    food_list2=['1. Eat the Big Mac', '2. Leave the Big Mac']
    time.sleep(0.5)
    for food2 in food_list2:
        print(food2)
    foods2 = input('What would you like to do? ')
    if foods2 == '1':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('You get poisoned off the half eaten Big Mac and collapse, then a zombie comes and eats you.')
        exit() # Try loop
    elif foods2 == '2':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('You leave the Big Mac on the table and stay hungry.')
    else:
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('Use the number option, please try again.')
        scavange2()

def make_burger():
    print("You decide to go to the kitchen to make yourself a burger, as you walk in there's a zombie at the grill with an apron on.")
    time.sleep(0.5)
    print("It turns towards you. You have multiple items in the vacinity you can use. Do you:")
    time.sleep(0.5)
    weapon_list=['1. Mop', '2. Scissors', '3. Gas Canister', '4. Knife']
    time.sleep(0.5)
    for wep in weapon_list:
        print(wep)
    weapons = input('Which weapon will you use? ')
    if weapons == '1':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('You pick up the mop and smack the zombie on the head with it, it takes muliple hits.')
        time.sleep(0.5)
        print('The zombie then falls onto the grill and burns.')
    elif weapons == '2':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('You pick up the scissors and stab the zombie repeatdly till it falls on to the grill and burns.')
    elif weapons == '4':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('You pick up the knife and stab the zombie repeatdly till it falls on to the grill and burns.')
    elif weapons == '3':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('You pick the the gas canister up, you hold it over your head ready to throw it.')
        time.sleep(0.5)
        print('Suddenly your arms go weak and the gas canister falls on you.')
        time.sleep(0.5)
        print('As it hits the ground it explodes.')
        time.sleep(0.5)
        print('You die.')
        exit() #try loop
    else:
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('Use the number option, please try again.')
        make_burger()

def zombie_grill():
    print('As the zombie falls onto the grill, it screams alerting the others nearby.')
    time.sleep(0.5)
    print('A herd of zombies begins to scurry towards you.')
    time.sleep(0.5)
    print('You decide to make a weapon using what you have around you.')
    time.sleep(0.5)
    print('Which combinations will you use:')
    time.sleep(0.5)
    weaponcombo=['1. Mop with knife on the end', '2. Flaming mop', '3. Scissorhands']
    time.sleep(0.5)
    for combo in weaponcombo:
        print(combo)
    weaponcombos = input('Choose your weapon: ')
    if weaponcombos == '1':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('You tie the knife to the end of the mop.')
        return True
    elif weaponcombos == '2':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print("You use the gas canister to light the end of mop.")
        time.sleep(0.5)
        print("FIREMOP!")
        time.sleep(0.5)
        print("The firemop acts as a becon to the nearby zombies and they swarm you.")
        time.sleep(0.5)
        print("You don't survive.")
        exit()
    elif weaponcombos == '3':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('You tie the scissors and knife to your hands.')
        return False
    else:
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('Use the number option, please try again.')
        zombie_grill()

def investigate_noise():
    print('You hear a cry from across the mall, do you:')
    time.sleep(0.5)
    investigation=['1. Investigate the noise', '2. Ignore the noise and hope it goes away']
    time.sleep(1)
    for j in investiagtion:
        print(j)
    investigations = input('What do you choose to do? ')
    if investigations == '1':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('You check where the noise is coming from, you see theres a little girl running away from the zombies.')
    elif investigations == '2':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print("You pretend there was no noise and eventually it stops.")
        time.sleep(0.5)
        print("Since, you're a horrible person that left someone to die, a pit of shame forms below you and zombies fall into it with you. You die.")
        time.sleep(0.5)
        exit()
    else:
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('Use the number option, please try again.')
        investigate_noise()

def choice1_investigate_noise(): #knife mop option
    print('You hear a cry from across the mall, do you:')
    time.sleep(0.5)
    investigation2=['1. Investigate the noise', '2. Ignore the noise and hope it goes away']
    time.sleep(0.5)
    for j2 in investigation2:
        time.sleep(0.5)
        print(j2)
    invest2 = input('What do you choose to do? ')
    if invest2 == '1':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('You pick up your knifemop and run to where the noise is coming from, as you are running there you spot a note on the floor.')
        time.sleep(0.5)
        print('You pick the note up and it has the numbers "1234". You put the note back on the floor and you continue running to where the noise is coming from.')
        time.sleep(0.5)
        print('You see theres a little girl running away from the zombies.')
    elif invest2 == '2':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print("You pretend there was no noise and eventually it stops.")
        time.sleep(0.5)
        print("Since, you're a horrible person that left someone to die, a pit of shame forms below you and zombies fall into it with you. You die.")
        exit()
    else:
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('Use the number option, please try again.')
        choice1_investigate_noise()


def choice3_investigate_noise(): #scissor hands option
    print('You hear a cry from across the mall, do you:')
    time.sleep(0.5)
    investi4=['1. Investigate the noise', '2. Ignore the noise and hope it goes away']
    time.sleep(0.5)
    for j4 in investi4:
        print(j4)
    invest4 = input('What do you choose to do? ')
    if invest4 == '1':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('You run towards the noise waving your scissor hands around like a maniac.')
        time.sleep(0.5)
        print('You see a note on the floor but you cant pick it up becaues you have scissorhands.')
        time.sleep(0.5)
        print('After a few seconds of struggling you manage to open the note and it has the numbers "1234" on it.')
        time.sleep(0.5)
        print('Then you put the note back down and continue to run to the noise.')
        time.sleep(0.5)
        print('When you arrive you see theres a little girl running away from the zombies.')
    elif invest4 == '2':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print("You pretend there was no noise and eventually it stops. Since, you're a horrible person that left someone to die, a pit of shame forms below you and zombies fall into it with you. You die.")
        exit()
    else:
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('Use the number option, please try again.')
        choice3_investigate_noise()

def follow_or_not():
    print('You defend the girl using your chosen weapon, she thanks you. Then, she asks if you will follow her. Do you:')
    time.sleep(0.5)
    options=['1.Follow the girl.', '2.Leave the girl and continue alone.']
    time.sleep(0.5)
    for p in options:
        print(p)
    follow = input('What do you choose to do? ')
    if follow == '1':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('The girl leads you to an air duct nearby that goes to the roof, she says "Come with me up the roof so we can signal a helicopter."')
    elif follow == '2':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('You dont follow the girl and try to find a different way out, you decide to try smash on of the windows.')
        time.sleep(0.5)
        print('You run at the window, not realising the glass is stronger than it looks, when you make contact you knock yourself out.')
        time.sleep(0.5)
        print('Then you get blown up with the rest of the zombies.')
        exit()
    else:
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('Use the number option, please try again.')
        follow_or_not()

def endingpt1():
    print('What do you do with the air duct?')
    time.sleep(0.5)
    ending_options=['1.Enter the air duct.', '2.Walk away from the air duct']
    time.sleep(0.5)
    for q in ending_options:
        print(q)
    air_duct = input('What do you choose to do? ')
    if air_duct == '1':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('You and the girl shimmy your way up the air duct, you reach a locked door.')
    elif air_duct == '2':
        print(' ')
        time.sleep(0.5)
        print('You wander away from the airduct, you see a hoard of zombies running towards you. You try to fight them off but you become overwhelmed. You die.')
        time.sleep(0.5)
        exit()
    else:
        print(' ')
        print('Use the number option, please try again.')
        endingpt1()

def ending_passcode():
    print("As you reach the top of the air duct, there's a keypad asking for a password.")
    time.sleep(0.5)
    print("There was a piece of paper earlier in your adventure with the password on it.")
    count = 0
    while count < 3:
        password = input('Please enter the correct password: ')
        if password == '1234':
            time.sleep(0.5)
            print('Correct password!')
            time.sleep(0.5)
            print('You climb through the air duct and are now on the roof.')
            return True
        else:
            time.sleep(0.5)
            print('Incorrect password, access denied.')
            count += 1
            

def bossfight():
    print("As you climb out of the air duct, you see a massive zombie blocking your way.")
    time.sleep(0.5)
    print("The only way to pass is to kill the zombie.")
    time.sleep(0.5)
    print("There's a millitary case to the right of you with many weapons inside it.")
    time.sleep(0.5)
    print("How shall you kill the massive zombie.")
    time.sleep(0.5)
    bossfight_weapons=['1. Bazooka', '2. Minigun', '3. Two miniguns', '4. The injection']
    for weps in bossfight_weapons:
        print(weps)
    count = 0
    while count < 3:
        winning_weapon = input('Choose your weapon: ')
        if winning_weapon == '1':
            time.sleep(0.5)
            print('You aim the bazooka at the massive zombie and fire a missile at it.')
            time.sleep(0.5)
            print("This staggers him but doesn't kill him, you're going to need another weapon.")
            count += 1
        elif winning_weapon == '2':
            time.sleep(0.5)
            print('You empty all 500 rounds into the massive zombie and looks weakened.')
            time.sleep(0.5)
            print('You are going to need a bit more to push it over the edge.')
            count += 1
        elif winning_weapon == '4':
            time.sleep(0.5)
            print('You put the needle into your arm and inject yourself.')
            time.sleep(0.5)
            print('You start to experience aggonising pain, you start to grow.')
            time.sleep(0.5)
            print('With your increased size you charge at the zombie and pummel it.')
            count += 1
        else:
            time.sleep(0.5)
            print('You try to pick up two miniguns but you struggle to aim them.')
            time.sleep(0.5)
            print("I don't know what you were thinking, you're not rambo.")
            time.sleep(0.5)
            print('The massive zombie kills you.')
            exit()
    if count > 1:
        endingpt2()
    
            
def endingpt2():
    print('After your tough fight with the huge zombie you take a minute to think.')
    time.sleep(0.5)
    print('You think about using the oil to spell out "help!" and then setting it on fire with the lighter you got before. Do you:')
    endingpt2_options=['1.Spell out "help!" with oil and then set it on fire.', '2.Go back down the airduct to try find another way out']
    time.sleep(0.5)
    for v in endingpt2_options:
        print(v)
    oil_fire = input('What do you choose to do? ')
    if oil_fire == '1':
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        print('You write "help!" with the oil and use the lighter to set it on fire.')
        time.sleep(0.5)
        print('A passing helicopter notices your message and lands on the roof.')
        time.sleep(0.5)
        print('You and the girl board the helicopter and fly away into the sunset, with the explosion behind you.')
        time.sleep(0.5)
        print(' __     ______  _    _    _____ _    _ _______      _________      ________  __          ________ _      _        _____   ____  _   _ ______ _ ')
        print(' \ \   / / __ \| |  | |  / ____| |  | |  __ \ \    / /_   _\ \    / /  ____| \ \        / /  ____| |    | |      |  __ \ / __ \| \ | |  ____| |')
        print('  \ \_/ / |  | | |  | | | (___ | |  | | |__) \ \  / /  | |  \ \  / /| |__     \ \  /\  / /| |__  | |    | |      | |  | | |  | |  \| | |__  | |')
        print('   \   /| |  | | |  | |  \___ \| |  | |  _  / \ \/ /   | |   \ \/ / |  __|     \ \/  \/ / |  __| | |    | |      | |  | | |  | | . ` |  __| | |')
        print('    | | | |__| | |__| |  ____) | |__| | | \ \  \  /   _| |_   \  /  | |____     \  /\  /  | |____| |____| |____  | |__| | |__| | |\  | |____|_|')
        print('    |_|  \____/ \____/  |_____/ \____/|_|  \_\  \/   |_____|   \/   |______|     \/  \/   |______|______|______| |_____/ \____/|_| \_|______(_)')
                                                                                                                                               
                                                                                                                                              
        exit()
    elif oil_fire == '2':
        print(' ')
        print('You try go back down the air duct to find your way out.')
        time.sleep(0.5)
        print('As you shimmy back down the duct your foot slips.')
        time.sleep(0.5)
        print('You fall and break your legs.')
        time.sleep(0.5)
        print('You are stuck inside the air duct and get blown up.')
        exit()
    else:
        print(' ')
        print('Use the number option, please try again.')
        endingpt2()

def filler():
    bossfight() == True
    return True
        

    


print('___________                                .__         __________              .__  .__  __          ')
time.sleep(0.5)
print('\__    ___/_________________  ___________  |__| ______ \______   \ ____ _____  |  | |__|/  |_ ___.__.')
time.sleep(0.5)
print('  |    |_/ __ \_  __ \_  __ \/  _ \_  __ \ |  |/  ___/  |       _// __ \\__  \ |  | |  \   __<   |  |')
time.sleep(0.5)
print('  |    |\  ___/|  | \/|  | \(  <_> )  | \/ |  |\___ \   |    |   \  ___/ / __ \|  |_|  ||  |  \___  |')
time.sleep(0.5)
print('  |____| \___  >__|   |__|   \____/|__|    |__/____  >  |____|_  /\___  >____  /____/__||__|  / ____|')
time.sleep(0.5)
print('             \/                                    \/          \/     \/     \/               \/     ')
time.sleep(0.5)
print('[¬º-°]¬')
time.sleep(0.5)
print(' ')
time.sleep(0.5)
print('For the questions, please use the corrosponding number. For example, "1.Play game" you would type "1".')
print(' ')
time.sleep(0.5)
name(name)
time.sleep(0.5)
print(' ')
time.sleep(0.5)
id_card()
time.sleep(0.5)
print(' ')
time.sleep(0.5)
if fire_extinguisher() == True:
    access_room_phone()
    print(' ')
    scavange()
else:
    no_access_card()
    print(' ')
    scavange2()
print(' ')
time.sleep(0.5)
make_burger()
time.sleep(0.5)
print(' ')
if zombie_grill() == True:
    print(' ')
    time.sleep(0.5)
    choice1_investigate_noise()
else:
    choice3_investigate_noise()
time.sleep(0.5)
print(' ')
follow_or_not()
time.sleep(0.5)
endingpt1()
time.sleep(0.5)
if ending_passcode() == True:
    time.sleep(0.5)
    print(' ')
    time.sleep(0.5)
    bossfight()
else:
    time.sleep(0.5)
    print('You try climb back down the air duct.')
    time.sleep(0.5)
    print('Your foot slips and you fall to the bottom, breaking your legs.')
    time.sleep(0.5)
    print('You are now stuck and get caught in the explosion.')
    time.sleep(0.5)
    print('You are dead.')
    time.sleep(0.5)
    print('Next time remember the number!')
    exit()
    if bossfight() == True:
        time.sleep(0.5)
        print(' ')
        time.sleep(0.5)
        endingpt2()

    
    
