#!/usr/bin/env python
import sys
evidence = []
  
def det_start(player_name):
# This function is used as a template for all subsequent ones, unless stated otherwise.
# The start_op list functions as the options the user has for progressing within the story, and return different results depending on which one is called.
  start_op = ["1","2","3"]
  user_choice = ""
  print "You awake to the sound of shrill ringing from your bedside table. Still disoriented, you lift your head up to examine your surroundings. The harsh glare of sunlight peaking through your curtains illuminates the small room."
  # The following print options are descriptors for each of the numbers in start_op.
  print "1. Look around room"
  print "2. Go outside"
  print "3. Answer phone"
  # Here, user_choice is defined as an input the player can use to decide which option, or number, they would like to pick based on which print statement piqued their interest.
  # It is converted to a string so it can be equivilated to each object in the start_op list.
  user_choice = raw_input("Enter Option Number:")
  while True:
  # The while loop is used to prevent errors if an option is inputted that does not match any within the list. If it does, the next function is loaded. If not, the loop continues.
    if user_choice in start_op:
        print "You have selected option " + user_choice
  # If the input entered by the player matches the first option in the list, a description of the event taking place in the story as a result of that option is printed, and the next function is called, which contains the same functionality with differing print statements that continue the story.
        if user_choice == start_op[0]:
            print "Your attention is immediately drawn to the bedside table, from which you can see your phone ringing and your alarm, set at 9:15 a.m. Overslept again. No doubt the phone call is from work."
            lookroom(player_name, evidence)
            break
  # The same thing happens if it matches the second option...
        elif user_choice == start_op[1]:
            print "The blinding sunlight causes you to emit a vampire-like hiss as a wave of pain engulfs your head. Not the best cure for a hangover. Adjusting to the glare, you see your beat-up car, parked stationary across from the busy intersection."
            go_out(player_name, evidence)
            break
  # ...and the third.
        elif user_choice == start_op[2]:
            print "Reluctantly, you pick up the phone. Mentally preparing an excuse to mumble out, you're snapped awake by a baritone yelling.\n", player_name, "! Where the hell are you? We've got a 187 on our hands, we need you at the station NOW!"
            go_station(player_name, evidence)
            break
    else:
        print "Please Try Again!"
        user_choice = raw_input("Enter Option Number:")
        continue
            
def lookroom(player_name, evidence):
    start_op = ["1","2"]
    user_choice = ""
    print "1. Answer phone"
    print "2. Turn phone off"
    user_choice = raw_input("Enter Option Number:")
    while True:
        if user_choice in start_op:
            print "You have selected option " + user_choice
            if user_choice == start_op[0]:
                print "Reluctantly, you pick up the phone. Mentally preparing an excuse to mumble out, you're snapped awake by a baritone yelling.\n", player_name, "! Where the hell are you? We've got a 187 on our hands, we need you at the station NOW!"
                go_station(player_name, evidence)
                break
            elif user_choice == start_op[1]:
                print "You fumble for your phone, eventually finding the power button and pressing in until the screeching fades into blissful silence. Immediately, you fade into unconsciousness."
                break
        else:
            print "Please Try Again!"
            user_choice = raw_input("Enter Option Number:")
            continue
        
def go_out(player_name, evidence):
    start_op = ["1","2"]
    user_choice = ""
    print "1. Get in car"
    print "2. Look around"
    user_choice = raw_input("Enter Option Number:")
    while True:
        if user_choice in start_op:
            print "You have selected option " + user_choice
            if user_choice == start_op[0]:
                print "Turning the key in the ignition, you hear the car sputter to life, engine check lights and all. Better head to the station and see what this is all about."
                go_station(player_name, evidence)
                break
            elif user_choice == start_op[1]:
                print "A surprising sunny day. A beam illuminates down on what would usually be a dark, blurred screen to reveal a text on your cracked phone from your partner. Seems like this is urgent."
                go_station(player_name, evidence)
                break
        else:
            print "Please Try Again!"
            user_choice = raw_input("Enter Option Number:")
            continue
        
def go_station(player_name, evidence):
    start_op = ["1","2"]
    user_choice = ""
    print "Finally arriving at the station, you push through the chaos of crowded hallways, ringing phones and second-hand smoke and escape into your office to find the chief sitting in your chair waiting for you. 'About damn time...' he grumbles. 'Dead cop reported last night, he was from a precinct across town. Got the autopsy and suspect list here, I'm trusting you to handle the rest so don't screw this up.' Great. No pressure."
    print "1. Look at autopsy"
    print "2. Look at suspect list"
    user_choice = raw_input("Enter Option Number:")
    while True:
        if user_choice in start_op:
            print "You have selected option " + user_choice
            if user_choice == start_op[0]:
                print "A single photo reveals a uniformed corpse outside what appears to be a pawn shop, with a blade hanging from his ribs. The handle seems to have some kind of pattern imprinted onto it, although the quality of the photo makes it hard to tell."
                evidence.append("autopsy")
                print "Autopsy Added To Evidence"
                go_station2(player_name, evidence)
                break
            elif user_choice == start_op[1]:
                print "'Quite a lineup we got here.' You jump at the sudden voice and spin around to see your partner hovering over the desk beside you. 'No kidding...' you murmur. Flicking through the portfolio, you see 3 faces: a grizzled looking biker, a gothic young woman and a chipper looking old lady."
                suspect_list(player_name, evidence)
                break
        else:
            print "Please Try Again!"
            user_choice = str(input("Enter Option Number:"))
            continue
        
def go_station2(player_name, evidence):
    start_op = ["1","2"]
    user_choice = ""
    while len(evidence) < 7:
        print "1. Look at evidence"
        print "2. Look at suspect list"
        user_choice = raw_input("Enter Option Number:")
        while True:
            if "autopsy" not in evidence:
                evidence.append("autopsy")
            if user_choice in start_op:
                print "You have selected option " + user_choice
                if user_choice == start_op[0]:
                    look_evidence(player_name, evidence)
                    break
                elif user_choice == start_op[1]:
                    suspect_list(player_name, evidence)
                    break
            else:
                print "Please Try Again!"
                user_choice = raw_input("Enter Option Number:")
                continue
    epilogue(player_name, evidence)
            
def look_evidence(player_name, evidence):
# For each piece of evidence the user has gathered, it's corresponding number is appended to the start_op list, and the ability to view a description of the item is given to the user.
    start_op = []
    user_choice = ""
    if "autopsy" in evidence:
        print "1. Autopsy"
        start_op.append("1")
    if "switchblade" in evidence:
        print "2. Switchblade"
        start_op.append("2")
    if "cctv" in evidence:
        print "3. CCTV Footage"
        start_op.append("3")
    if "cloak" in evidence:
        print "4. Cloak"
        start_op.append("4")
    if "bikeralibi" in evidence:
        print "5. Biker's Alibi"
        start_op.append("5")
    if "gothalibi" in evidence:
        print "6. Store Owner's Alibi"
        start_op.append("6")
    if "granalibi" in evidence:
        print "7. Old Lady's Alibi"
        start_op.append("7")
    print "8. Return To Station"
    start_op.append("8")
    user_choice = raw_input("Enter Option Number:")
    while True:
        if user_choice in start_op:
            print "You have selected option " + user_choice
            if user_choice == "1":
                print "A single photo reveals a uniformed corpse outside what appears to be a pawn shop, with a blade hanging from his ribs. The handle seems to have some kind of pattern imprinted onto it, although the quality of the photo makes it hard to tell."
                look_evidence(player_name, evidence)
            elif user_choice == "2" and "switchblade" in evidence:
                print "A distinctive snake pattern covers the handle, reddened from dried blood. It seems it was sold in the very same shop it was used outside."
                look_evidence(player_name, evidence)
            elif user_choice == "3" and "cctv" in evidence:
                print "The camera's quality is less than ideal, causing the footage to be blurry and pixelated. The victim can be seen standing outside the shop, as a motorbike pulls up and a cloaked figure steps off, stopping only to stab the man before taking off."
                look_evidence(player_name, evidence)
            elif user_choice == "4" and "cloak" in evidence:
                print "A black cloak with a strange crest imprinted onto the back. You suspect it matches the one worn by the murderer, although the poor footage in the recording makes it hard to tell."
                look_evidence(player_name, evidence)
            elif user_choice == "5" and "bikeralibi" in evidence:
                print "He claims to have entered the shop that morning to buy parts for his bike, and a blade that matches the murder weapon to a tee."
                if "cctv" in evidence:
                    print "He also noted that the bike used in the murder is not one carried by him or his gang."
                look_evidence(player_name, evidence)
            elif user_choice == "6" and "gothalibi" in evidence:
                print "She claims to not have witnessed the murder immediately as she was in the back room of the shop, nor did she check immediately as screaming and loud noises are apparenly a common occurence in that part of town."
                if "switchblade" in evidence:
                    print "She also mentioned that the blade used in the murder was purchased in that store alongside an identical one, although she was unsure of who it was sold to."
                look_evidence(player_name, evidence)
            elif user_choice == "7" and "granalibi" in evidence:
                print "She claimed to be at home at the time of the murder, noting that the shop owner was covering for her."
                if "switchblade" in evidence:
                    print "She seemed adamant that the murder weapon was sold to a member of the biker gang that frequent the shop."
                look_evidence(player_name, evidence)
            elif user_choice == "8":
                go_station2(player_name, evidence)
                break
        else:
            print "Please Try Again!"
            user_choice = raw_input("Enter Option Number:")
            continue
            
def suspect_list(player_name, evidence):
    start_op = ["1","2","3","4"]
    user_choice = ""
    print "'Where to first, boss?' your partner leers sarcastically."
    print "1. Go to crime scene"
    print "2. Go to divebar"
    print "3. Go to suburbs"
    print "4. Look at evidence"
    user_choice = raw_input("Enter Option Number:")
    while True:
        if user_choice in start_op:
            print "You have selected option " + user_choice
            if user_choice == start_op[0]:
                crimescene(player_name, evidence)
                break
            elif user_choice == start_op[1]:
                divebar(player_name, evidence)
                break
            elif user_choice == start_op[2]:
                suburbs(player_name, evidence)
                break
            elif user_choice == start_op[3]:
                look_evidence(player_name, evidence)
        else:
            print "Please Try Again!"
            user_choice = raw_input("Enter Option Number:")
            continue
          
def gameover2(player_name, evidence):
# This second game over function doubles as a save point. After a certain point in the game is reached, choosing to try again will return the user to the station with all of their evidence gathered to that point, rather than the start of the game.
    start_op = ["y","n"]
    print "Game Over. Try Again? \n (Y/N)"
    user_choice = raw_input("Enter Option:").lower().strip()
    if user_choice in start_op:
        if user_choice == start_op[0]:
            suspect_list(player_name, evidence)
        elif user_choice == start_op[1]:
            print "Thanks for playing!"
            sys.exit()
    else:
        gameover2(player_name, evidence)

def crimescene(player_name, evidence):
    start_op = ["1","2","3"]
    user_choice = ""
    print "Arriving at the murder scene, you feel a chill run down your spine. Chalk outlines where the body once lay, and the entire area is covered in tape save for the shop entrance."
    print "1. Meet suspect"
    print "2. Look around"
    print "3. Return to station"
    user_choice = raw_input("Enter Option Number:")
    while True:
        if user_choice in start_op:
            print "You have selected option " + user_choice
            if user_choice == start_op[0]:
                print "Entering the shop, you find yourself taken aback at how strange the place is. Occult-like imagery lines the walls, and locked cabinets contain weapons of all kinds. This is a pawn shop?"
                meet_goth(player_name, evidence)
                break
            elif user_choice == start_op[1]:
                print "Veering off of the footpath to take a closer look at the chalk outline, you notice blood dried into the pavement. What you don't notice is the car flying down the road towards you at 90 miles an hour. Should have looked both ways."
                gameover2(player_name, evidence)
                break
            elif user_choice == start_op[2]:
                go_station2(player_name, evidence)
                break
        else:
            print "Please Try Again!"
            user_choice = raw_input("Enter Option Number:")
            continue
            
def meet_goth(player_name, evidence):
    start_op = ["1","2","3"]
    user_choice = ""
    print "The suspect isn't hard to make. She glares at you in disgust from behind the shop counter. 'Umm...can I help you?' You clear your throat. 'I'm detective " + player_name + ", me and my partner are here on account of the murder that took place outside your shop last night.' There's a brief pause as she seems to examine you. 'Riiight. What do you wanna know?'"
    print "1. Where were you?"
    print "2. What were you doing?"
    print "3. What did you see?"
    if "switchblade" in evidence:
# If the user has certain items of evidence gathered, specific dialogue options can be accessed relating to that item when questioning a suspect.
        start_op.append("4")
        print "4. Show murder weapon"
    user_choice = raw_input("Enter Option Number:")
    while True:
        if user_choice in start_op:
            print "You have selected option " + user_choice
            if user_choice == start_op[0]:
                print "She motions behind her. 'In the back room.'"
                meet_goth2(player_name, evidence)
                break
            elif user_choice == start_op[1]:
                print "'Taking stock. Heard a scream from outside. Thought nothing of it initially - we get a lot of stupid kids playing pranks around here. Only when I had finished, I came out and saw the guy outside.' She shakes her head. 'Poor bastard.'"
                meet_goth2(player_name, evidence)
                break
            elif user_choice == start_op[2]:
                print "'At the time? Nothing. Only after I saw what happened, I checked the CCTV footage. Some cloaked figure pulled up on a motorcycle, stuck the guy and made off.' Your partner's eyes flash, and a smirk marks your face as you know you're making progress. 'We're gonna need that footage.' She rolls her eyes. 'Fine, if it'll get you out of my shop.'"
                evidence.append("cctv")
                print "CCTV Footage added to Evidence"
                meet_goth2(player_name, evidence)
                break
                meet_goth2(player_name, evidence)
            elif user_choice == start_op[3]:
                print "You pull the switchblade from out of your jacket. 'We found this - ' you begin, twisting it around to reveal the design, ' - was used to stab the victim.' Her eyes widen. 'I sold that!' she exclaims. 'Well, I definitely had that exact knife in my shop anyway.' You immediately change your tone, attempting to sound stern. 'This is important. Do you remember who you sold it to?' 'Well, I sold a couple of them. One was to this biker guy.' 'And the other? Do you remember?' A brief pause. '...No.' she murmurs. 'I'm sorry.' Your partner chuckles. 'Told you, you should leave the bad cop routine to me.'"
                meet_goth2(player_name, evidence)
                break
        else:
            print "Please Try Again!"
            user_choice = raw_input("Enter Option Number:")
            continue
           
def meet_goth2(player_name, evidence):
# Two functions for questioning a suspect were created so that the introduction paragraph in the first one was not printed each time a question was asked.
    start_op = ["1","2","3","4"]
    user_choice = ""
    print "'Anything else?'"
    print "1. Where were you?"
    print "2. What were you doing?"
    print "3. What did you see?"
    print "4. Return to station"
    if "switchblade" in evidence:
        start_op.append("5")
        print "5. Show murder weapon"
    user_choice = raw_input("Enter Option Number:")
    while True:
        if user_choice in start_op:
            print "You have selected option " + user_choice
            if user_choice == start_op[0]:
                print "She motions behind her. 'In the back room.'"
                meet_goth2(player_name, evidence)
                break
            elif user_choice == start_op[1]:
                print "'Taking stock. Heard a scream from outside. Thought nothing of it initially - we get a lot of stupid kids playing pranks around here. Only when I had finished, I came out and saw the guy outside.' She shakes her head. 'Poor bastard.'"
                meet_goth2(player_name, evidence)
                break
            elif user_choice == start_op[2]:
                if "cctv" in evidence:
                    print "'Didn't I already tell you?'"
                    meet_goth2(player_name, evidence)
                    break
                else:
                    print "'At the time? Nothing. Only after I saw what happened, I checked the CCTV footage. Some cloaked figure pulled up on a motorcycle, stuck the guy and made off.' Your partner's eyes flash, and a smirk marks your face as you know you're making progress. 'We're gonna need that footage.' She rolls her eyes. 'Fine, if it'll get you out of my shop.'"
                    evidence.append("cctv")
                    print "CCTV Footage added to Evidence"
                    meet_goth2(player_name, evidence)
                    break
            elif user_choice == start_op[3]:
                print "You tip your hat. 'Thank you for your time.' She seems unimpressed. 'Yeah, whatever.'"
                evidence.append("gothalibi")
                print "Store Owner's Alibi added to Evidence"
                go_station2(player_name, evidence)
                break
            elif user_choice == start_op[4]:
                print "You pull the switchblade from out of your jacket. 'We found this - ' you begin, twisting it around to reveal the design, ' - was used to stab the victim.' Her eyes widen. 'I sold that!' she exclaims. 'Well, I definitely had that exact knife in my shop anyway.' You immediately change your tone, attempting to sound stern. 'This is important. Do you remember who you sold it to?' 'Well, I sold a couple of them. One was to this biker guy.' 'And the other? Do you remember?' A brief pause. '...No.' she murmurs. 'I'm sorry.' Your partner chuckles. 'Told you, you should leave the bad cop routine to me.'"
                meet_goth2(player_name, evidence)
                break
        else:
            print "Please Try Again!"
            user_choice = raw_input("Enter Option Number:")
            continue
            
def divebar(player_name, evidence):
    start_op = ["1","2","3"]
    user_choice = ""
    print "'Keep your head down and stay frosty in here.' Your partner ushers you towards the entrance. 'We really don't need everyone knowing we're cops.' Despite your best efforts, it seems this is still the case."
    print "1. Meet suspect"
    print "2. Look around"
    print "3. Return to Station"
    user_choice = raw_input("Enter Option Number:")
    while True:
        if user_choice in start_op:
            print "You have selected option " + user_choice
            if user_choice == start_op[0]:
                print "Through the cigarette smoke, you see more and more faces look up and scowl at you. Eventually, you notice one of them is your man. 'Excuse me, sir?' you manage to choke out. 'Detective " + player_name + ". We're here to ask some questions about a murder that took place outside a pawn shop on Baker Street last night.' He speaks one word, poised with anger and deliberacy. '...What?'"
                meetbiker(player_name, evidence)
                break
            elif user_choice == start_op[1]:
                print "You mumble some excuse about getting drinks to your partner and decide to scope the place out. Nosing around, you hear a strange noise coming from an alley outside. Thinking to further investigate, you step outside. Bad idea. You turn around to see two burly bikers towering over you. 'Grab the barbecue Joe,' one of them snarls. 'I'm about to cook me a pig.'"
                gameover2(player_name, evidence)
                break
            elif user_choice == start_op[2]:
                go_station2(player_name, evidence)
                break
        else:
            print "Please Try Again!"
            user_choice = raw_input("Enter Option Number:")
            continue
           
def meetbiker(player_name, evidence):
    start_op = ["1","2","3"]
    user_choice = ""
    print "1. Where were you?"
    print "2. When were you there?"
    print "3. Did you know the victim?"
    if "cctv" in evidence:
        start_op.append("4")
        print "4. Show CCTV Footage"
    user_choice = raw_input("Enter Option Number:")
    while True:
        if user_choice in start_op:
            print "You have selected option " + user_choice
            if user_choice == start_op[0]:
                print "'Up your ass, picking daisies.' Your partner speaks up 'This'll be a lot easier if you co-operate.' He grunts. 'Fine. I was at that shop.' 'What for?' you enquire. 'Had to pick up a couple things. Muffler for my bike.' 'And?' There's a pause, and he sighs. 'This.' He pulls a familiar looking switchblade out of his pocket. 'We'll need that, I'm afraid.' you say. His expression becomes incredulous. 'What? No! Get bent!' You try to sound reassuring as you reply 'Look, it matches the one in our file, but that doesn't mean anything yet. If we get our man, we'll give it back, no questions asked.' 'Fine.'"
                evidence.append("switchblade")
                print "Switchblade added to Evidence"
                meetbiker2(player_name, evidence)
                break
            elif user_choice == start_op[1]:
                print "'That morning.' 'Were you only there once?' you press. 'No, a few times. Not many other places you can find parts for an '89 Harley chopper. Never caused trouble though.'"
                meetbiker2(player_name, evidence)
                break
            elif user_choice == start_op[2]:
                print "'You think I associate with cops?' he growls. 'No I didnt know him!' 'Well... did you know anyone in the area?' you continue cautiously. 'I knew the shopkeepers. Not personally, just from talking to them when I was buying stuff.'"
                meetbiker2(player_name, evidence)
                break
            elif user_choice == start_op[3]:
                print "Pulling your phone from your pocket, you scroll to the copy of the shop's footage that you had saved. 'Have a look at this.' you say as you motion to the screen. After the footage finishes, the man laughs. Not the reaction you were expecting. 'This is why you're bothering me, huh? Well I can tell you right now, that there's an '87 Triumph, and ain't none of our boys ride one of them.' Shocked, you only manage to murmur out '...I see.' That certainly throws a spanner in the works."
                meetbiker2(player_name, evidence)
                break
        else:
            print "Please Try Again!"
            user_choice = raw_input("Enter Option Number:")
            continue
            
def meetbiker2(player_name, evidence):
    start_op = ["1","2","3","4"]
    user_choice = ""
    print "'You done?'"
    print "1. Where were you?"
    print "2. When were you there?"
    print "3. Did you know the victim?"
    print "4. Return to Station"
    if "cctv" in evidence:
        start_op.append("5")
        print "5. Show CCTV Footage"
    user_choice = raw_input("Enter Option Number:")
    while True:
        if user_choice in start_op:
            print "You have selected option " + user_choice
            if user_choice == start_op[0]:
                if "switchblade" in evidence:
                    print "You deaf or something?"
                    meetbiker2(player_name, evidence)
                else:
                    print "'Up your ass, picking daisies.' Your partner speaks up 'This'll be a lot easier if you co-operate.' He grunts. 'Fine. I was at that shop.' 'What for?' you enquire. 'Had to pick up a couple things. Muffler for my bike.' 'And?' There's a pause, and he sighs. 'This.' He pulls a familiar looking switchblade out of his pocket. 'We'll need that, I'm afraid.' you say. His expression becomes incredulous. 'What? No! Get bent!' You try to sound reassuring as you reply 'Look, it matches the one in our file, but that doesn't mean anything yet. If we get our man, we'll give it back, no questions asked.' 'Fine.'"
                    evidence.append("switchblade")
                    print "Switchblade added to Evidence"
                    meetbiker2(player_name, evidence)
                    break
            elif user_choice == start_op[1]:
                print "'That morning.' 'Were you only there once?' you press. 'No, a few times. Not many other places you can find parts for an '89 Harley chopper. Never caused trouble though.'"
                meetbiker2(player_name, evidence)
                break
            elif user_choice == start_op[2]:
                print "'You think I associate with cops?' he growls. 'No I didnt know him!' 'Well... did you know anyone in the area?' you continue cautiously. 'I knew the shopkeepers. Not personally, just from talking to them when I was buying stuff.'"
                meetbiker2(player_name, evidence)
                break
            elif user_choice == start_op[3]:
                print "'Thanks for your co-operation.' You get out of your seat and turn to leave. 'Don't come back here again.' is the last thing you hear as you leave the bar."
                evidence.append("bikeralibi")
                print "Biker's Alibi added to Evidence"
                go_station2(player_name, evidence)
                break
            elif user_choice == start_op[4]:
                print "Pulling your phone from your pocket, you scroll to the copy of the shop's footage that you had saved. 'Have a look at this.' you say as you motion to the screen. After the footage finishes, the man laughs. Not the reaction you were expecting. 'This is why you're bothering me, huh? Well I can tell you right now, that there's an '87 Triumph, and ain't none of our boys ride one of them.' Shocked, you only manage to murmur out '...I see.' That certainly throws a spanner in the works."
                meetbiker2(player_name, evidence)
                break
        else:
            print "Please Try Again!"
            user_choice = raw_input("Enter Option Number:")
            continue
            
def suburbs(player_name, evidence):
    start_op = ["1","2","3"]
    user_choice = ""
    print "'Do we really have to do this?' your partner groans. 'We have to consider all possibilities. Trust me, I speak from experience.' He rolls his eyes. 'Whatever you say, oh wise one.'"
    print "1. Meet suspect"
    print "2. Look around"
    print "3. Return to station"
    user_choice = raw_input("Enter Option Number:")
    while True:
        if user_choice in start_op:
            print "You have selected option " + user_choice
            if user_choice == start_op[0]:
                print "'Alright. Looks like this is the house.' You knock on the door and hear a shrill 'Coming!' in response. The door opens to reveal a smiling old lady. 'Hello! How can I help you two gentlemen?' Suddenly finded yourself flustered for some reason, you begin 'Um... hello miss, I'm detective " + player_name + ", we're here on account of a murder that took place outside a pawn shop on Baker Street last night, we were told you work there?' Her smile dampens. 'Oh yes... terrible thing. Come in, I'm happy to answer any questions you boys have.'"
                meetgran(player_name, evidence)
                break
            elif user_choice == start_op[1]:
                if "cloak" in evidence:
                    print "'Enough already!' your partner moans. 'Let's get this over with!'"
                else:
                    print "'Oh come on, what could you possibly hope to find here?' your partner snorts in derision. But you insist. Noticing a strange fabric coming out of the bin beside the house, you come closer and see it's a familiar looking cloak. 'So now we're stealing private property too?' he pipes up. 'Oh, shut up will ya!' you snap back."
                    evidence.append("cloak")
                    print "Cloak added to Evidence"
                suburbs(player_name, evidence)
                break
                user_choice = raw_input("Enter Option Number:")
            elif user_choice == start_op[2]:
                go_station2(player_name, evidence)
                break
        else:
            print "Please Try Again!"
            user_choice = raw_input("Enter Option Number:")
            continue

def meetgran(player_name, evidence):
    start_op = ["1","2","3"]
    user_choice = ""
    print "1. Where were you?"
    print "2. Did you know the victim?"
    print "3. What do you know?"
    if "switchblade" in evidence:
        start_op.append("4")
        print "4. Show murder weapon"
    user_choice = raw_input("Enter Option Number:")
    while True:
        if user_choice in start_op:
            print "You have selected option " + user_choice
            if user_choice == start_op[0]:
                print "'Oh, I was right here at home. Sally was covering the shop that night.' 'Sally?' you enquire. 'Yes, Sally. The girl who runs the shop. Poor girl was awfully broken up about it.' You find that hard to believe."
                meetgran2(player_name, evidence)
                break
            if user_choice == start_op[1]:
                print "'No, I didn't know the young man. Poor thing.' Her voice hardens and she stares intently into the distance. 'Too much senseless violence happening these days...'"
                meetgran2(player_name, evidence)
                break
            if user_choice == start_op[2]:
                print "'Only what Sally told me. An officer was stabbed outside the shop, wasn't he?' You nod and she continues. 'Doesn't surprise me at all, to be honest. There's rackets of all sorts happening in that town. If you ask me, it's that darn biker gang you ought to be questioning. Always coming into our shop and causing trouble.'"
                meetgran2(player_name, evidence)
                break
            if user_choice == start_op[3]:
                print "'We found the murder weapon was purchased in your shop.' you begin, as you pull it from your pocket. Her cheeks begin to turn red, as she stammers 'Oh...I-I see.' You continue 'Do you know who it was sold to?' 'No, I-I'm sure... it must have been one of those biker boys.' She starts to regain her composure. 'Yes, it definitely was. They come in there buying guns and knifes of all kinds for God knows what. No wonder there's so much crime happening in this town!'"
                meetgran2(player_name, evidence)
                break
        else:
            print "Please Try Again!"
            user_choice = raw_input("Enter Option Number:")
            continue
            
def meetgran2(player_name, evidence):
    start_op = ["1","2","3","4"]
    user_choice = ""
    print "'Is that all?'"
    print "1. Where were you?"
    print "2. Did you know the victim?"
    print "3. What do you know?"
    print "4. Return to station"
    if "switchblade" in evidence:
        start_op.append("5")
        print "5. Show murder weapon"
    user_choice = raw_input("Enter Option Number:")
    while True:
        if user_choice in start_op:
            print "You have selected option " + user_choice
            if user_choice == start_op[0]:
                print "'Oh, I was right here at home. Sally was covering the shop that night.' 'Sally?' you enquire. 'Yes, Sally. The girl who runs the shop. Poor girl was awfully broken up about it.' You find that hard to believe."
                meetgran2(player_name, evidence)
                break
            if user_choice == start_op[1]:
                print "'No, I didn't know the young man. Poor thing.' Her voice hardens and she stares intently into the distance. 'Too much senseless violence happening these days...'"
                meetgran2(player_name, evidence)
                break
            if user_choice == start_op[2]:
                print "'Only what Sally told me. An officer was stabbed outside the shop, wasn't he?' You nod and she continues. 'Doesn't surprise me at all, to be honest. There's rackets of all sorts happening in that town. If you ask me, it's that darn biker gang you ought to be questioning. Always coming into our shop and causing trouble.'"
                meetgran2(player_name, evidence)
                break
            if user_choice == start_op[3]:
                print "'Can I get you two a cup of tea?' she offers, but you decline. 'No thank you, we better get back now. Thanks for your time, ma'am.' you respond as you shake her hand. 'Anytime. Let me know if there's anything else I can help with.'"
                evidence.append("granalibi")
                print "Old Lady's Alibi added to Evidence"
                go_station2(player_name, evidence)
                break
            if user_choice == start_op[4]:
                print "'We found the murder weapon was purchased in your shop.' you begin, as you pull the switchblade from your pocket. 'Looked exactly like this.' Her cheeks begin to turn red, as she stammers 'Oh...I-I see.' You continue 'Do you know who it was sold to?' 'No, I-I'm sure... it must have been one of those biker boys.' She starts to regain her composure. 'Yes, it definitely was. They come in there buying guns and knifes of all kinds for God knows what. No wonder there's so much crime happening in this town!'"
                meetgran2(player_name, evidence)
                break
        else:
            print "Please Try Again!"
            user_choice = raw_input("Enter Option Number:")
            continue
            
def epilogue(player_name, evidence):
# Once the user has all items of evidence gathered, the epilogue of the game can be accessed. From here, the user can select who they think committed the murder.
    start_op = ["1","2","3","4"]
    user_choice = ""
    print "'Alright.' you declare to your partner. 'Time to put this to bed.' Your boss enters the office. 'We've got the three suspects in the interrogation room, along with the evidence. Come inside and make your call.' He steps outside, then turns around. 'And hurry it up, I wanna catch the game tonight.'"
    print "The interrogation room is as cold and musty as you remember it. You enter to find all the suspects staring up at you, with less than welcoming expressions on their faces. You clear your throat. 'Apologies for the wait. We just have one final round of questioning to carry out and then you're... well, two of you are free to go."
    print "1. Look at evidence"
    print "2. Pick Shop Owner"
    print "3. Pick Biker"
    print "4. Pick Old Lady"
    user_choice = raw_input("Enter Option Number:")
    while True:
        if user_choice in start_op:
            print "You have selected option " + user_choice
            if user_choice == start_op[0]:
                partnerevidence(player_name, evidence)
                break
            elif user_choice == start_op[1]:
                ending1(player_name, evidence)
                break
            elif user_choice == start_op[2]:
                ending2(player_name, evidence)
                break
            elif user_choice == start_op[3]:
                ending3(player_name, evidence)
                break
        else:
            print "Please Try Again!"
            user_choice = raw_input("Enter Option Number:")
            continue
            
def epilogue2(player_name, evidence):
    start_op = ["1","2","3","4"]
    user_choice = ""
    print "1. Look at evidence"
    print "2. Pick Shop Owner"
    print "3. Pick Biker"
    print "4. Pick Old Lady"
    user_choice = raw_input("Enter Option Number:")
    while True:
        if user_choice in start_op:
            print "You have selected option " + user_choice
            if user_choice == start_op[0]:
                partnerevidence(player_name, evidence)
                break
            elif user_choice == start_op[1]:
                ending1(player_name, evidence)
                break
            elif user_choice == start_op[2]:
                ending2(player_name, evidence)
                break
            elif user_choice == start_op[3]:
                ending3(player_name, evidence)
                break
        else:
            print "Please Try Again!"
            user_choice = raw_input("Enter Option Number:")
            continue
            
def partnerevidence(player_name, evidence):
    start_op = ["1","2","3","4","5","6","7","8"]
    user_choice = ""
    print "1. Autopsy"
    print "2. Switchblade"
    print "3. CCTV Footage"
    print "4. Cloak"
    print "5. Biker's Alibi"
    print "6. Store Owner's Alibi"
    print "7. Old Lady's Alibi"
    print "8. Return to Interrogation Room"
    user_choice = raw_input("Enter Option Number:")
    while True:
        if user_choice in start_op:
            print "You have selected option " + user_choice
            if user_choice == start_op[0]:
                print "'See the knife in the photo? Shop owner said there were multiple like it.' 'Yeah.' your partner continues, 'This isn't as clear cut as it once looked.'"
                partnerevidence(player_name, evidence)
                break
            elif user_choice == start_op[1]:
                print "'We got this from the biker, right? Looks exactly like the murder weapon.' 'Yeah, but it isn't. Some kid ran off with it after the autopsy was taken.' he replies. 'Seriously!?' you almost shout. 'This damn town...'"
                partnerevidence(player_name, evidence)
                break
            elif user_choice == start_op[2]:
                print "'That cloak did it's job well. Not a glimpse of the guy who did it.' 'Yeah, but that cloak's the next best thing.' he retorts. Good point."
                partnerevidence(player_name, evidence)
                break
            elif user_choice == start_op[3]:
                print "'If I didn't know any better, I'd swear this was the cloak used by the murderer.' your partner says with a smirk. This certainly clears things up."
                partnerevidence(player_name, evidence)
                break
            elif user_choice == start_op[4]:
                print "'He said the bike used by the killer wasn't used by him or his gang. Mentioned they rode Harleys. Think we can cross him off?' 'Not outright. He still had that knife, remember?' your partner counters. 'But it isn't THE murder weapon.' you follow up. 'Yeah, but his gang sure seems to like that kind of switchblade. And he was in the shop that day.'"
                partnerevidence(player_name, evidence)
                break
            elif user_choice == start_op[5]:
                print "'She was in the shop when it happened, but somehow missed it happening. What a concidence.' You sigh and rub your temple in frustration. 'A cop murdered outside a shop known to sell weapons, and to be frequented by bikers. At least we have a motive.' 'In fairness though, she was the one who put in the call. And was apparently inside the shop when it happened.' your partner reasons."
                partnerevidence(player_name, evidence)
                break
            elif user_choice == start_op[6]:
                print "'She claimed to be at home when it happened. Store owner's alibi back that up. I'd almost believe her, if not for this...' You pull out the cloak. 'It's certainly suspect. But it's not like there's only one of those in the world.' your partner reasons. 'Hell of a coincidence though.' you counter. 'And she seemed to have a weird vendetta against those bikers...' 'Yeah, so why would she kill a cop?' he asks, incredulous. Why indeed."
                partnerevidence(player_name, evidence)
                break
            elif user_choice == start_op[7]:
                epilogue2(player_name, evidence)
                break
        else:
            print "Please Try Again!"
            user_choice = raw_input("Enter Option Number:")
            continue
            
def ending1(player_name, evidence):
    print "Are You Sure? (Y/N)"
    user_choice = raw_input("Enter Option:").lower().strip()
    while True:
        if user_choice == "y":
            print "'Sally, isn't it?' You stare down at the girl, whose standoffish attitude seems to have all but faded. 'Y-yes?' 'You'll need to come with us.' you say with a pang of reluctance. 'W-what? You think it was me?' The anger in her voice returned. 'This is insane! I did NOT!' 'Yet you were in the shop when it happened. A shop notorious for being a gang hideout, filled with weapons. Weapons awfully similar to the one murder weapon that you don't remember selling. And you somehow missed it. How convenient for you, right? One less cop poking around.' You fire back, the anger in your voice rising to match. She seems to enter shock. 'B-but...I...' You sigh, and continue in a low voice. 'Look, I'm sorry kid, but rules are rules.' You motion for the guard outside to escort her out, and leave shortly after with your partner in tow. After you leave the station for the day, your partner breaks the silence. 'Thank God that's over. You wanna grab a drink to celebrate?' 'Ah, not tonight.' you respond. 'Head's still killing me. I'll catch you on the weekend.' 'Alright then.' He tips his hat. 'Till tomorrow, supercop.' You chuckle and head back to your apartment for what you hope will be a good nights rest."
            print "You have completed Ending 1. Thanks for playing!"
            sys.exit()
        elif user_choice == "n":
            epilogue2(player_name, evidence)
            break
        else:
            print "Please Try Again!"
            user_choice = raw_input("Enter Option:").lower().strip()
            continue
    
def ending2(player_name, evidence):
    print "Are You Sure? (Y/N)"
    user_choice = raw_input("Enter Option:").lower().strip()
    while True:
        if user_choice == "y":
            print "You stare down at the biker, and without needing to say anything he begins to roar at you in a blind rage. 'I knew it! I KNEW IT! YOU PIGS JUST COULDN'T HELP YOURSELVES!' The guard outside comes in, attempting to restrain him. 'WELL I DIDN'T! I WISH I DID! ONE LESS PIG IN THE WORLD!' 'Anything else?' your partner snorts, amused. He seems to calm down, staring you in the eyes. 'A few years in the can ain't nothing to me. I'll be seeing you when I'm out.' On cue, he's taken out of the room and into his new cell. 'He won't be seeing anyone for a long time.' your partner says, smiling. 'Come on, let's get out of here. You wanna grab a drink?' You return the smile 'Hell, why not.' You walk out of the station, relieved that it's finally over."
            print "You have completed Ending 2. Thanks for playing!"
            sys.exit()
        elif user_choice == "n":
            epilogue2(player_name, evidence)
            break
        else:
            print "Please Try Again!"
            user_choice = raw_input("Enter Option:").lower().strip()
            continue
    
def ending3(player_name, evidence):
    print "Are You Sure? (Y/N)"
    user_choice = raw_input("Enter Option:").lower().strip()
    while True:
        if user_choice == "y":
            print "You look down at the old lady. 'Is something wrong?' she inquires, smiling sweetly. You drop the cloak onto the table before her. 'Does this look familiar to you?' Her smile drops. 'Why, I...' 'This very cloak was worn by the murderer.' 'That's... that's impossible! It was him! He was at the shop that day!' she stammers, motioning to the biker. 'At first, we thought so too. But he was accounted for. He was only in the shop that morning. And the bike used in the murder isn't his - the footage taken by the shop proves that.' Her once friendly face contorts into a scowl. 'That proves nothing! What about the murder weapon? It's his!' 'It is awfully similar..,' you continue, '...but not the same. His was a separate one. And while we're on the subject...' You hunch over the table, matching her scowl. 'Where did that murder weapon come from? Your shop, right? Only it wasn't sold - there's no records on file, neither yourself nor Sally here have any recollection of who bought it. Could it be that it was taken from someone who had access to everything in the shop? That no one would suspect?' The silence in the air is palpable, and after a brief staring contest she drops the act. 'Alright.' she hisses in a tone of voice you didn't think possible. 'I did it. And I'd do it again. You cops aren't doing your jobs, so I had to.' You smile in satisfaction. Finally. 'So you got yourself a bike, threw on a cloak and stabbed a cop. All to set up our biker friend here.' 'I wouldn't have had to if you'd DO YOUR DAMN JOBS!' she roars. 'EVERY DAY THOSE SCUMBAGS COME AROUND AND CAUSE TROUBLE! AND YOU DON'T DO A DAMN THING!' She lowers her voice to a rasp. That man died so criminal scum would be put away. The kind you should really be arresting.' 'I've heard enough.' you say undeterred as you motion for the guards outside. 'Take her away, boys.'"
            print "Exhausted, you leave the station with your partner in tow. 'Holy hell!' he scoffs, laughing. 'You're good, I'll give you that! Never would have guessed it was her!' 'That's what she was counting on.' you retort. 'Welcome to the force, kid. Wanna grab a drink?' 'Damn right!' Climbing into your beat up sedan, you smile, satisfied with a good day's work."
            print "You have completed Ending 3. Thanks for playing!"
            sys.exit()
        elif user_choice == "n":
            epilogue2(player_name, evidence)
            break
        else:
            print "Please Try Again!"
            user_choice = raw_input("Enter Option:").lower().strip()
            continue