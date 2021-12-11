# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import telebot

bot = telebot.TeleBot("5017812708:AAEj8LjlGJrHKFTUusplyqxIkgOrPOyToqc")
def extract_arg(arg, num):
    s = arg.split(" ", 3)
    return s[num]
@bot.message_handler(commands=[ 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello. Have you missed me? Use /math")
@bot.message_handler(commands=['math'])
def math_general(message):
    bot.reply_to(message, "What type of math do you need? /sin, /cos, /+, /-, //, /*, /systemscount")
@bot.message_handler(commands=['systemscount'])
def math_system(message):
    MYNUMBER = int(extract_arg(message.text, 1))
    FirstSystem = int(extract_arg(message.text, 2))
    SecondSystem = int(extract_arg(message.text, 3))
    TenDigNumber = 0
    k = 0
    print(MYNUMBER)
    print(FirstSystem)
    print(SecondSystem)
    while MYNUMBER != 0:
        while (MYNUMBER/10 != MYNUMBER//10):
            TenDigNumber += FirstSystem**k
            MYNUMBER = MYNUMBER - 1
        MYNUMBER = MYNUMBER/10
        k = k+1
    print(MYNUMBER)
    print(TenDigNumber)
    k = 15
    while TenDigNumber != 0:
        while (TenDigNumber >= SecondSystem**k):
            TenDigNumber -= SecondSystem**k
            MYNUMBER = MYNUMBER + 1*(10**k)
        k = k - 1
    print(MYNUMBER)
    bot.reply_to(message, str(int(MYNUMBER)))
@bot.message_handler(commands=['+'])
def math_one(message):
    a = float(extract_arg(message.text, 1))
    b = float(extract_arg(message.text, 2))
    bot.reply_to(message, str(float(a + b)))
@bot.message_handler(commands=['-'])
def math_two(message):
    a = float(extract_arg(message.text, 1))
    b = float(extract_arg(message.text, 2))
    bot.reply_to(message, str(float(a - b)))
@bot.message_handler(commands=['*'])
def math_three(message):
    a = float(extract_arg(message.text, 1))
    b = float(extract_arg(message.text, 2))
    bot.reply_to(message, str(float(a * b)))
@bot.message_handler(commands=['/'])
def math_four(message):
    a = float(extract_arg(message.text, 1))
    b = float(extract_arg(message.text, 2))
    bot.reply_to(message, str(float(a / b)))
@bot.message_handler(commands=[ 'DandD'])
def DungeonsandDragons(message):
    bot.reply_to(message, "Oh, you want to throw dices? Use /dice")
@bot.message_handler(commands=[ 'dice'])
def DungeonsandDragons(message):
    DiceAlmount = int(extract_arg(message.text, 1))
    DiceWariable = int(extract_arg(message.text, 2))
    answer = 0
    while DiceAlmount > 0:
        answer += random.randint(1, DiceWariable)
        DiceAlmount = DiceAlmount-1
    bot.reply_to(message, str(answer))
@bot.message_handler(commands=['stand'])
def AllStands(message):
    mystand = str((extract_arg(message.text, 1)))
    if (mystand == "StarPlatinum"):
        bot.reply_to(message, str("Star Platinum is a prime example of a Stand that is really good at one role, being offensive. Star Platinum has access to Time Skip and Stand Leap; both are good for mobility or to close distance. With access to inhale, a move that pulls targets near the user, Star Platinum excels at close range combat. Star Finger can also blind and stun enemies which makes close range combat even easier. Rage Mode also increases the already good damage from Star Platinum.Within rage mode, Star Platinum can pause time for a maximum of 4 seconds. Only a handful of Stands can counter this. Stands that can pause time such as The World or Stands that can move within paused time regardless, such as Tusk (Act 4) with Infinite Rotation. Within stopped time, it is most efficient to just use LMBs to attack. If you have the Hamon or Boxing specs, you can use a Zoom Punch or Eye Gouge at the end of the Time Stop, which will stun the opponent and allow for an additional post-time stop combo. Due to the cost of Star Platinum's timestop and the nerf which made it last for only 4 seconds, the move is almost entirely useless against stands that can move within time stop, however if you wish to spend the extra skill points you can get off great damage from time stop."))
    elif (mystand == "WhiteSnake"):
        bot.reply_to(message, str("Whitesnake is the Stand of Enrico Pucci, the main antagonist of Jojo's Bizarre Adventure: Stone Ocean. Its primary ability is to extract or insert DISCs, primarily Stand and Memory DISCs. DISC insertion is currently not a feature in the game and probably never will be. It also has an ability to excrete an acid that slowly melts its opponents and puts them into a dream-like, hallucinatory state, known as Melt Your Heart.Whitesnake is the first of a trilogy of Stands that were used by Enrico Pucci. The other two are also in the game, C-Moon and Made in Heaven. Whitesnake's percentage is 1%, making it the rarest arrow Stand in game."))
    elif(mystand == "SPTW"):
        bot.reply_to(message, str("Star Platinum: The World is a mastered Stand that takes on the appearance of it's former evolution, Star Platinum from the Anime adaptation of JoJo's Bizarre Adventure: Diamond is Unbreakable. SP:TW's design is that of Star Platinum but with swapped brighter colors to fit the style of Part 4 (the gloves changed from black to white, while a big part of the skin is changed from purple to cyan). SP:TW also has a noticeable increase in size compared to the non-requiem version. This stand is still considered to be very viable, and is usually paired with Boxing and Hamon."))
    elif (mystand == 'CMoon'):
        bot.reply_to(message, str("C-Moon is an evolved Stand belonging to Enrico Pucci, the main villain of Part 6, requiring Whitesnake to achieve. With assistance from Enrico Pucci, this Stand can be achieved by giving him DIO's Diary and completing a quest for him which involves defeating multiple NPCs. (10 Vampires, 15 Zombie Henchmen, 20 Corrupt Police, 25 Alpha Thugs and 30 Thugs.) Doing so will give the player the Green Baby. It is recommended to have Worthiness V before fusing the Green Baby with Whitesnake, otherwise there is a possibility for the user to turn to stone and not obtain C-Moon, losing the Green Baby. This Stand has been renamed G-Moon in-game in order to avoid copyright issues."))
    elif (mystand == "MadeInHeaven"):
        bot.reply_to(message, str("Made in Heaven is the Stand of Enrico Pucci, the main antagonist of JoJo's Bizarre Adventure Part 6: Stone Ocean and the final evolution in Whitesnake's line; which concludes The Heaven's Plan.Made in Heaven is an extremely powerful stand if used correctly. Players can loop maxed Double Accel and Time Acceleration to make sure that their stand is never slow, meaning that you can generally get free combos, then run away easily. it is often criticized because of the low damage of its moves, but the amount of damage you do is irrelevant if you can hit your opponent, but your opponent can't hit you.sert DISCs, primarily Stand and Memory DISCs. DISC insertion is currently not a feature in the game and probably never will be. It also has an ability to excrete an acid that slowly melts its opponents and puts them into a dream-like, hallucinatory state, known as Melt Your Heart."))
    elif (mystand == "TheWorld"):
        bot.reply_to(message, str("The World is a close-range power type of Stand like Star Platinum. Its power far exceeds most Stands and is equal to the previously mentioned Star Platinum. The World is the Stand of the main antagonist of Stardust Crusaders, DIO. This Stand is capable of stopping time itself for a limit of 5 seconds (9 when Dio drinks Joseph's blood) This Stand is obtainable from an arrow with a 1.5% chance, making it one of the rarest Stands in-game. The World is now called “The Universe” in-game, in order to avoid copyright issues."))
    elif (mystand == 'TheWorldOwerHeaven'):
        bot.reply_to(message, str("Originally, this Stand was paired with Hamon thanks to The World: Over Heaven's passive ability. However, in an update after it's release, it is no longer able to get the damage buff from Hamon, making it near useless on it now. Spin took it's place thanks to it's low cost and stun, but when the stun on Heaven Ascended Knives and Steel Balls were nerfed, it was dropped too. In recent times, Boxing has become the main specialty, though whether or not others will pop up remains to be seen."))
    elif (mystand == "Aerosmith"):
        bot.reply_to(message, str("Aerosmith is a long-ranged Stand used by Narancia. This Stand can be obtained by using an arrow, with an 8% chance. This Stand is rare, in the sense that you can pilot it from long ranges.In the past, Aerosmith was considered to be one of the worst, if not THE worst, stands in the game. Vola barrage used to do a pitiful 0.2 damage on average [0.4 if charged with Hamon], making it perhaps the weakest move in the game. However, in a recent update, Aerosmith was given a massive damage boost, with the minimum 0.2 barrage upgraded to a minimum 1.3 barrage, as well as slight changes to the other 2 moves."))
    elif(mystand == "Anubis"):
        bot.reply_to(message, str("Anubis is a unique Stand that takes the form of a Scimitar and is based on the Egyptian God of Death, Anubis. It does not have a 'set' user, but rather possesses anyone who unsheathes it- though Anubis does not unsheathe for anyone, only those it deems worthy to wield its power. Anubis can be obtained from a Mysterious Arrow with a 2% chance."))
    elif (mystand == 'SilverChariot'):
        bot.reply_to(message, str("Silver Chariot is a close-ranged Stand based off The Chariot, a Tarot card. Silver Chariot is used by Jean Pierre Polnareff in Stardust Crusaders. The Stand also appears later on in the series in Golden Wind. At first glance, Silver Chariot appears to be similar to a medieval knight. Its pupils are blue and its irises are yellow. Silver Chariot has 2 rapiers (1 is used to attack and the other is for Last Shot)."))
    elif (mystand == "SilverChariotRequiem"):
        bot.reply_to(message, str("Chariot Requiem is a Requiem Stand obtained with the Requiem Arrow, much like King Crimson Requiem, Gold Experience Requiem, Killer Queen: Bites The Dust and Star Platinum: The World. The Stand was first formed when Polnareff's Silver Chariot pricked itself against a Requiem Arrow, turning into Chariot Requiem for a brief moment. Chariot Requiem was permanently formed when Diavolo killed Polnareff in Rome, Italy before the remaining members of Bucciarati's gang could reach him. Before Polnareff's physical death, he stabbed Silver Chariot with the arrow with the intent of never letting Diavolo obtain the arrow."))
    elif (mystand == "CrazyDiamond"):
        bot.reply_to(message, str("Crazy Diamond is a Stand from JoJo's Bizarre Adventure Part 4: Diamond is Unbreakable. It is wielded by the main protagonist, Josuke Higashikata. During this part, the Stand is seen repairing objects such as a motorcycle, a pipe, and broken debris like sidewalks and broken glass. In-game, Crazy Diamond has a 2.5% chance of obtainment. Crazy Diamond has been renamed Shining Sapphire in-game in order to avoid copyright issues."))
    elif (mystand == 'Cream'):
        bot.reply_to(message, str("Cream (changed to Void for copyright reasons) is the stand of Vanilla Ice from Part 3 of JoJo's Bizarre Adventure, also known as Stardust Crusaders. It is a humanoid stand with a cloak around its head covering most of its head region. Notable features include its glowing yellow eyes and pure white skin colour that at times appear malleable in the anime. It was a monster-type stand that had extra-dimensional properties, sending anything it hit when it ate itself into a ball to a dark dimension inside its mouth, effectively erasing it from this dimension. The only ones capable of escaping this dimension are Cream itself and its user. Cream is also one of the best Stands to win Steel Ball Run because of the limb erasure and high damage and health. It is also arguably the best Stand in the game to use with Vampirism thanks to the ability to avoid the sun entirely by entering the dark dimension, and the effective easy damage combos such as Vaporization Freezing and Void Surprise. There is a 4% chance to get Cream from a Mysterious Arrow."))
    elif (mystand == "D4C"):
        bot.reply_to(message, str("Dirty Deeds Done Dirt Cheap is great at zoning. Its pocket revolver can detonate smoke clouds from The World (Alternate Universe), allowing it to utilize the crowd control effect of the explosion. The gun itself, when upgraded, is also quicker than TWAU's Revolver. Aside from the gun, a D4C user also relies on Dimensional Victim Clone for damage at longer ranges and Dimensional Clones to overwhelm their opponent with M1s and M2s. This can be used in tandem with Clone Swap to punish opponents barraging or to give some (albeit unreliable) mobility."))
    elif (mystand == 'D4CLoveTrain'):
        bot.reply_to(message, str("Dirty Deeds Done Dirt Cheap: Love Train or D4C:LT for short is the evolved version of D4C. It is the Stand used by Funny Valentine, the main antagonist of JoJo's Bizarre Adventure Part 7. It is obtained through using the Heart of the Saint's Corpse- which is obtainable by completing the Steel Ball Run or from rolling it in the Arcade- on D4C. This version of D4C gains an extra Destructive Power node and receives higher base damage, along with an extremely fast barrage speed, making it one of the highest DPS Stands in the game. This Stand also has the highest base Destructive Power in the game."))
    elif (mystand == "GoldenExperience"):
        bot.reply_to(message, str("Gold Experience by itself, is a mediocre stand, but its saving grace is its life-giving powers, Gold Experience can create trees, make frogs, and shoot eagles, all of which can be used offensively. Its Seven Page Beatdown is also useful, although slow and most likely damage-dealing only instead of disorienting, unlike Star Platinum: The World's Ora Beatdown. It's recommended to try to get this Stand mainly for its Requiem counterpart, which is much stronger. Overall, Gold Experience is a decent stand, but its Requiem overshadows it."))
    elif(mystand == "GoldenExperienceRequiem"):
        bot.reply_to(message, str("Gold Experience Requiem was considered by many to be one of the best Stands in-game. Every move is offensive, even the healing is powerful, with its self-healing and others. Its only real weakness is its damage, which can be removed as a flaw with Awakening which can also stack with Hamon Punch from the Hamon skill tree. This has since changed due to scorpions from life beam (GER's main source for a lot of damage) having a lot more endlag, resulting in players not being able to immobilize opponents with barrage [or any one of a myriad of other moves] quick enough."))
    elif (mystand == 'HermitPurple'):
        bot.reply_to(message, str("Hermit Purple is a Stand that is displayed as purple vines with thorns surrounding both hands. In the anime and manga, Hermit Purple is owned by Joseph Joestar. It can be used to find the location of people or things, as well as working as a grappling hook for faster travelling. The ability to find things or people is most commonly used on electronics, but can also be used on pretty much everything."))
    elif (mystand == "KillerQueen"):
        bot.reply_to(message, str("Killer Queen is the Stand of Yoshikage Kira in Jojo's Bizarre Adventure. Its most notable feature is being able to transform anything into a bomb with a touch of its finger and detonating it by pressing its thumb on its index finger, similar to activating a detonator (note that Roblox characters don't have thumbs, so Killer Queen just moves its hand similar to detonating it in the anime/manga.) It has a 2.5% chance of being obtained from a Stand arrow. It is primarily a close-range Stand but uses some ranged attacks."))
    elif (mystand == "KillerQueenBiteTheDust"):
        bot.reply_to(message, str("Killer Queen: Bites the Dust, is a stand obtained with a Requiem Arrow used on Killer Queen. This stand belonged to Kira Yoshikage, the main antagonist of Part 4 of JoJo's Bizarre Adventure. He attained KQ: BTD after being stabbed by The Arrow the second time. The ability let him attain a 3rd bomb which re-winded time by an hour every time his identity was exposed."))
    elif (mystand == 'KingCrimzon'):
        bot.reply_to(message,str("King Crimson's main advantage is its damage output. It has access to Impale, which induces bleed. This bypasses Love Train (if the impale was used before Love Train was activated.) It also has Epitaph to teleport behind whoever hits the user [or guarantees a chop if you get the Chop Passive] - this can shut down piloting Stands. King Crimson can also use Time Skip to engage or disengage from combat. Its key ability, Time Erase, makes the user immune to damage and invisible."))
    elif (mystand == "KingCrimzonRequiem"):
        bot.reply_to(message,str("King Crimson Requiem is a hypothetical Stand based on King Crimson, if Diavolo got ahold of the Requiem Arrow instead of Giorno Giovanna. King Crimson Requiem has been renamed Scarlet King Requiem in-game in order to avoid copyright issues. This is currently the only stand that is purely unofficial as other Requiem stands such as Killer Queen: Bites the Dust or Star Platinum: The World is still based on events within the series, which King Crimson Requiem is not."))
    elif (mystand == 'MagicansRed'):
        bot.reply_to(message,str("Magician's Red appears as a humanoid figure with a bird-like head. It has a heavily muscular upper body and its feathered legs are sometimes covered in burning flames. Its arms have claws instead of nails and it wears dark bracelets on both of its wrists. Originally, the Stand was barefooted, but during Avdol's return, it wore Arabian shoes. This stand is typically paired with Hamon or Sword-Style due to the increased damage and defense from the former and the combo potential of the latter."))
    elif (mystand == "PurpleHaze"):
        bot.reply_to(message,str("Magician's Red appears as a humanoid figure with a bird-like head. It has a heavily muscular upper body and its feathered legs are sometimes covered in burning flames. Its arms have claws instead of nails and it wears dark bracelets on both of its wrists. Originally, the Stand was barefooted, but during Avdol's return, it wore Arabian shoes. This stand is typically paired with Hamon or Sword-Style due to the increased damage and defense from the former and the combo potential of the latter."))

    elif (mystand == 'ScaryMonsters'):
        bot.reply_to(message,str("While possessing a small movepool and average damage, Scary Monsters is widely thought of to be one of the best Stands in the game. Scary Monsters has two passive abilities, the first of which allows the user, in Stand form, to run slightly faster while the other one prevents the user from having their Stand Crashed. This is huge against Stands like King Crimson and C-Moon, who rely on Stand Crashing the opponent to get in damage. Pounce may be blockable, but its hyper armor and low endlag make it a phenomenal mobility option. The Stand Crashing side effect it inflicts comes in hand vs Pilot Stands as well (e.g. Hierophant Green stuck using Emerald Splash). Head Charge is a frame one true block break which, like Pounce, is uncancellable while dealing more damage and still Stand Crashes. Most players follow Pounce up with it if the opponent blocks the move."))
    elif (mystand == "SixPistols"):
        bot.reply_to(message,str("Sex Pistols is the Stand of Guido Mista, a core ally in Part 5: Golden Wind and a part of Bruno Bucciarati's gang. Six Pistols consists of a purple revolver, with 6 bullet slots in its cylinder. When equipped, the user's arm that holds Six Pistols has a purple/blue aura. Six Pistols in Golden Wind is shown to be 6 numbered bullet-like entities with numbers labeled on them (skipping no. 4.) In-game, Six Pistols is shown to be merely a gun with omnidirectional bullets, similar to The Emperor. However, in some of its moves (Multi Shot, Redirection Barrage) if you look closely you may see some of the Pistols appear and redirect bullets."))
    elif (mystand == 'Tusk'):
        bot.reply_to(message,str("Tusk Act 1 is considered to be one of the worst Stands in the game, due to how limited it is in terms of combat. Aside from its nail shots, the user cannot attack. Its heal is a self-heal only that heals for a minor amount, and its only mobility is Nail Glide. Despite this, it is possible to complete the main story, even without a Speciality. This is not recommended though, due to Tusk's limited attacks. However, Focused Nail Shot can be used to start combos due to being able to block break and stun. Tusk Act 2 adds a couple of abilities on top of Tusk Act 1, with the main one being an upgraded version of the Focused Nail Shot called Golden Rectangle Nail and Wormhole Nails. This allows the user to redirect any missed nail shots to a target, allowing the use of some mind games or less precise aiming. In addition to maintaining every previous ability, Act 3 adds Wormhole Uppercut. This gives Tusk the extra dynamic of being able to engage combat. The attack has some crowd control as the attack inflicts knock down, which allows the user to dash away to increase the distance between the user and the target, as Tusk is purely a long range stand. Wormhole Nails can also redirect any nail based attacks that did not hit someone. The attack gets cancelled if the user gets hit during the animation start up, which emphases the importance for a Tusk Act 3 user to keep their distance from whoever they are fighting. Tusk Act 4 has a couple of niches when compared to its previous incarnations. Infinite Rotation is a key ability of Tusk Act 4 as it allows the user to walk within time stop for two to four seconds. All the while, Infinite Rotation bypasses attacks that redirect, with the most notable example being Love Train. The only way other Stands can damage its redirect abilities is via status effects, such as bleed or poison. Tusk Act 4 is also the only version of Tusk that has any melee capabilities, due to its barrage and barrage finisher. Wormhole Uppercut can also be used to engage to a target as a Tusk Act 4 can use barrage or barrage finisher, which Tusk Act 3 does not have."))
    elif (mystand == "WhiteAlbum"):
        bot.reply_to(message,str("White Album is the Stand of Ghiaccio, a side antagonist from Part 5 of JoJo's Bizarre Adventure, who is a member of La Squadra Esecuzioni. White Album appears as a suit of armor the user wears, it does this by freezing the moisture around the user, forming an armor of ice. White Album has a very potent power called Cryokinesis that is able to freeze things in a matter of seconds and drop temperatures to -100°C with ease. It can use many mobile abilities with Cryokinesis highlighted in its Skills."))
    else:
        bot.reply_to(message,str("I cant remember this stand"))
@bot.message_handler(commands=['**'])
def math_five(message):
    a = float(extract_arg(message.text, 1))
    b = float(extract_arg(message.text, 2))
    bot.reply_to(message, str(float(a ** b)))
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "I think I don't understand you. Use /help")

bot.infinity_polling()




