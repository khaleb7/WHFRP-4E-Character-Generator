#!/usr/local/bin/python
# coding=utf-8
import random

from faker import Factory
fake = Factory.create('de_DE')



def charattr():
        roller = random.randint(1,10) + random.randint(1,10) + 20
        return roller
def dhundred():
        roller = random.randint(1,100)
        return roller

def makeachar():
        cattributes=[charattr(), charattr(), charattr(), charattr(), charattr(), charattr(), charattr(), charattr(), charattr(), charattr(),
         0, 0, 0, 0]
        crace = race(dhundred())  # Lack of time to flesh this one out...
        ccareer=racialcareers(crace)
        ccareerpkg = career_package(ccareer[0])
        cname = fake.first_name(), fake.last_name()
        cracialset = racialset(crace)



        cwounds= ((cattributes[2]/10)+(2*(cattributes[3]/10)) + (cattributes[7]/10))
        print "----------------------------------------------------------------------------------------------"
        print "\nName:" , cname[0].encode('utf-8'), cname[1].encode('utf-8'), "Race: " ,   crace#race(dhundred()) in final, only human for now
        print "Class:" , ccareer[1] , "Career:" , ccareer[0], "/" , ccareerpkg[4]
        print "\nWS:", cattributes[0],"/", (cattributes[0]/10), "BS:", cattributes[1],"/", (cattributes[1]/10), "S:", cattributes[2],"/", (cattributes[2]/10), "T:", cattributes[3], "/", (cattributes[3]/10),"I:", cattributes[4],"/", (cattributes[4]/10), "Ag:", cattributes[5],"/", (cattributes[5]/10), "Dex:", cattributes[6], "/", (cattributes[06]/10),"Int:", cattributes[7], "WP:", "/", cattributes[7], "/", (cattributes[7]/10), "Fel:", cattributes[9] , "/", (cattributes[9]/10),
        print "\n Movement:4 Wounds:", cwounds,"Fate:4 Resilience 1 Extra Points: 3"
        #WS BS S T I Ag Dex Int WP Fel
        ctalents=racialtalents(dhundred)
        print "\nTalents:"
        print ', '.join(cracialset[1])
        print "\nTrappings:"
        print ccareer[2],ccareerpkg[3]
        print "\nRacial Skills-Pick 3 racial skills to get 5 advances, and 3 skills to gain 3 advances (each):"

        print ', '.join(cracialset[0])
        print "\nClass Skills-Allocate 40 Advances to your 8 Class Skills, no more than 10 each to start:"

        print ccareerpkg[1]
        print "\nClass Talent:Pick ONE"
        print ccareerpkg[2]
        print "\nClass Attributes-Spend 5 Advances across any of the following:"
        print ccareerpkg[0] , "\n"





def race(numeric):
        if 1 <= numeric <= 90:
                crace="Human (Reiklander)"
        if 91 <= numeric <= 94:
                crace="Dwarf"
        if 95 <= numeric <= 98:
                crace="Halfling"
        if 99 == numeric:
                crace="High Elf"
        if 100 == numeric:
                crace="Wood Elf"

        return crace

def racialset(crace):
        if crace == "Human (Reiklander)":
                skills=["Animal Care", "Charm", "Command", "Cool", "Evaluate", "Haggle", "Gossip", "Language (Bretonnian)", "Language (Wastelander)", "Lore (Reikland)", "Melee (Basic)", "Ranged (Bow)"]
                talents=["Doomed", "Savvy OR Suave", randomtalents(), randomtalents(), randomtalents()]
        if crace == "Dwarf":
                skills=["Consume Alcohol, Cool, Endurance, Entertain (Storytelling), Evaluate, Intimidate, Language (Khazalid), Lore (Dwarfs), Lore (Geology), Lore (Metallurgy), Melee (Basic), Trade (any one)"]
                talents=["WS +10 |Toughness +10 |Agility -10 |Dexterity +10 |Willpower +20 |Fellowship -10","Magic Resistance", "Night Vision", "Read/Write or Relentless", "Resolute or Strong-minded", "Sturdy"]
        if crace == "Halfling":
                skills=["Charm, Consume Alcohol, Dodge, Gamble, Haggle, Intuition, Language (Mootish), Lore (Reikland), Perception, Sleight of Hand, Stealth, Trade (Cook)"]
                talents=["WS -10 | BS +10 |Strength -10 |Dexterity +10 |Willpower +10 |Wounds -SB |Fellowship +10","Acute Sense (Taste), Night Vision, Resistance (Chaos), Small", randomtalents(), randomtalents()]
        if crace == "High Elf":
                skills=["Cool, Entertain (Sing), Evaluate, Language (Eltharin), Leadership, Melee (Basic), Navigation, Perception, Play (any one), Ranged (Bow), Sail, Swim"]
                talents=["WS +10 |BS +10 |Initiative +20 |Agility +10 |Dexterity +10 |Intelligence +10 |Willpower +20","Acute Sense (Sight)", "Coolheaded or Savvy", "Night Vision", "Second Sight or Sixth Sense", "Read/Write"]
        if crace == "Wood Elf":
                skills=["Athletics, Climb, Endurance, Entertain (Sing), Intimidate, Language (Eltharin), Melee (Basic), Outdoor Survival, Perception, Ranged (Bow), Stealth (Rural), Track"]
                talents=["WS +10 |BS +10 |Initiative +20 |Agility +10 |Dexterity +10 |Intelligence +10 |Willpower +20","Acute Sense (Sight)", "Hardy or Second Sight", "Night Vision", "Read/Write or Very Resilient", "Rover"]
        return skills,talents

def racialtalents(crace):
        #Returns a list of Talents
        talents = ["Doomed", "Savvy OR Suave", randomtalents(), randomtalents(), randomtalents()]
        return talents
def racialcareers(crace):
        #Return your class/career/tier
        entropy=dhundred()



        if crace == "Human (Reiklander)":
                if 1 <= entropy <= 14:
                        if 1 <= entropy <= 1:
                                career = "Apothecary"
                        if 2 <= entropy <= 2:
                                career = "Engineer"
                        if 3 <= entropy <= 3:
                                career = "Lawyer"
                        if 4 <= entropy <= 5:
                                career = "Nun"
                        if 6 <= entropy <= 6:
                                career = "Physician"
                        if 7 <= entropy <= 11:
                                career = "Priest"
                        if 12 <= entropy <= 13:
                                career = "Scholar"
                        if 14 <= entropy <= 14:
                                career = "Wizard"
                        base_class = "Academics"
                        base_trappings = "Clothing, Dagger, Pouch, Sling Bag containing Writing Kit and 1d10 sheets of Parchment"
                if 15 <= entropy <= 27:
                        if 15 <= entropy <= 15:
                                career = "Agitator"
                        if 16 <= entropy <= 17:
                                career = "Artisan"
                        if 18 <= entropy <= 19:
                                career = "Beggar"
                        if 20 <= entropy <= 20:
                                career = "Investigator"
                        if 21 <= entropy <= 21:
                                career = "Merchant"
                        if 22 <= entropy <= 23:
                                career = "Rat Catcher"
                        if 24 <= entropy <= 26:
                                career = "Townsman"
                        if 27 <= entropy <= 27:
                                career = "Watchman"

                        base_class = "Burghers"
                        base_trappings = "Cloak, Clothing, Dagger, Hat, Pouch, Sling Bag containing Lunch"
                if 28 <= entropy <= 37:
                        if 28 <= entropy <= 28:
                                career = "Advisor"
                        if 29 <= entropy <= 29:
                                career = "Artist"
                        if 30 <= entropy <= 30:
                                career = "Duellist"
                        if 31 <= entropy <= 31:
                                career = "Envoy"
                        if 32 <= entropy <= 32:
                                career = "Noble"
                        if 33 <= entropy <= 35:
                                career = "Servant"
                        if 36 <= entropy <= 36:
                                career = "Spy"
                        if 37 <= entropy <= 37:
                                career = "Warden"
                        base_class = "Courtiers"
                        base_trappings = "Courtly Garb, Dagger, Pouch containing Tweezers, Ear Pick and a Comb"
                if 38 <= entropy <= 50:
                        if 38 <= entropy <= 38:
                                career = "Bailiff"
                        if 39 <= entropy <= 39:
                                career = "Hedge Witch"
                        if 40 <= entropy <= 40:
                                career = "Herbalist"
                        if 41 <= entropy <= 42:
                                career = "Hunter"
                        if 43 <= entropy <= 43:
                                career = "Miner"
                        if 44 <= entropy <= 44:
                                career = "Mystic"
                        if 45 <= entropy <= 45:
                                career = "Scout"
                        if 46 <= entropy <= 50:
                                career = "Villager"
                        base_class = "Peasants"
                        base_trappings = "Cloak, Clothing, Dagger, Pouch, Sling Bag containing Rations (1 day)"
                if 51 <= entropy <= 60:
                        if 51 <= entropy <= 51:
                                career = "Bounty Hunter"
                        if 52 <= entropy <= 52:
                                career = "Coachman"
                        if 53 <= entropy <= 54:
                                career = "Entertainer"
                        if 55 <= entropy <= 56:
                                career = "Flagellant"
                        if 57 <= entropy <= 57:
                                career = "Messenger"
                        if 58 <= entropy <= 58:
                                career = "Pedlar"
                        if 59 <= entropy <= 59:
                                career = "Road Warden"
                        if 60 <= entropy <= 60:
                                career = "Witch Hunter"
                        base_class = "Rangers"
                        base_trappings = "Cloak, Clothing, Dagger, Pouch, Backpack containing Tinderbox, Blanket, Rations (1 day)"
                if 61 <= entropy <= 74:
                        if 61 <= entropy <= 62:
                                career = "Boatman"
                        if 63 <= entropy <= 63:
                                career = "Huffer"
                        if 64 <= entropy <= 65:
                                career = "Riverwarden"
                        if 66 <= entropy <= 68:
                                career = "Riverwoman"
                        if 69 <= entropy <= 70:
                                career = "Seaman"
                        if 71 <= entropy <= 71:
                                career = "Smuggler"
                        if 72 <= entropy <= 73:
                                career = "Stevedore"
                        if 74 <= entropy <= 74:
                                career = "Wrecker"
                        base_class = "Riverfolk"
                        base_trappings = "Cloak, Clothing, Dagger, Pouch, Sling Bag containing a Flask of Spirits"
                if 75 <= entropy <= 88:
                        if 75 <= entropy <= 76:
                                career = "Bawd"
                        if 77 <= entropy <= 77:
                                career = "Charlatan"
                        if 78 <= entropy <= 78:
                                career = "Fence"
                        if 79 <= entropy <= 79:
                                career = "Grave Robber"
                        if 80 <= entropy <= 83:
                                career = "Outlaw"
                        if 84 <= entropy <= 84:
                                career = "Racketeer"
                        if 85 <= entropy <= 87:
                                career = "Thief"
                        if 88 <= entropy <= 88:
                                career = "Witch"
                        base_class = "Rogues"
                        base_trappings = "Clothing, Dagger, Pouch, Sling Bag containing 2 Candles, 1d10 Matches, a Hood or Mask"
                if 89 <= entropy <= 100:
                        if 89 <= entropy <= 90:
                                career = "Cavalryman"
                        if 91 <= entropy <= 92:
                                career = "Guard"
                        if 93 <= entropy <= 93:
                                career = "Knight"
                        if 94 <= entropy <= 94:
                                career = "Pit Fighter"
                        if 95 <= entropy <= 95:
                                career = "Protagonist"
                        if 96 <= entropy <= 99:
                                career = "Soldier"
                        if 0 <= entropy <= 0:
                                career = "Slayer"
                        if 100 <= entropy <= 100:
                                career = "Warrior Priest"
                        base_class = "Warriors"
                        base_trappings = "Clothing, Hand Weapon, Dagger, Pouch"
        if crace == "High Elf":

                if 1 <= entropy <= 16:
                        if  1 <= entropy <= 2:
                                career="Apothecary"
                        if 0 <= entropy <= 0:
                                career = "Engineer"
                        if 3 <= entropy <= 6:
                                career = "Lawyer"
                        if 0 <=  entropy <= 0:
                                career = "Nun"
                        if 7 <= entropy <= 8:
                                career = "Physician"
                        if 0 <= entropy <= 0:
                                career = "Priest"
                        if 9 <= entropy <= 12:
                                career = "Scholar"
                        if 13 <= entropy <= 16:
                                career = "Wizard"
                        base_class = "Academics"
                        base_trappings = "Clothing, Dagger, Pouch, Sling Bag containing Writing Kit and 1d10 sheets of Parchment"
                if 17 <= entropy <= 29:
                        if  0 <= entropy <= 0:
                                career="Agitator"
                        if 17 <= entropy <= 19:
                                career = "Artisan"
                        if 0 <= entropy <= 0:
                                career = "Beggar"
                        if 20 <=  entropy <= 21:
                                career = "Investigator"
                        if 22 <= entropy <= 26:
                                career = "Merchant"
                        if 0 <= entropy <= 0:
                                career = "Rat Catcher"
                        if 27 <= entropy <= 28:
                                career = "Townsman"
                        if 29 <= entropy <= 29:
                                career = "Watchman"

                        base_class = "Burghers"
                        base_trappings = "Cloak, Clothing, Dagger, Hat, Pouch, Sling Bag containing Lunch"
                if 30 <= entropy <= 45:
                        if 30 <= entropy <= 31:
                                career = "Advisor"
                        if 32 <= entropy <= 32:
                                career = "Artist"
                        if 33 <= entropy <= 34:
                                career = "Duellist"
                        if 35 <= entropy <= 37:
                                career = "Envoy"
                        if 38 <= entropy <= 40:
                                career = "Noble"
                        if 0 <= entropy <= 0:
                                career = "Servant"
                        if 41 <= entropy <= 43:
                                career = "Spy"
                        if 44 <= entropy <= 45:
                                career = "Warden"
                        base_class = "Courtiers"
                        base_trappings = "Courtly Garb, Dagger, Pouch containing Tweezers, Ear Pick and a Comb"
                if 46 <= entropy <= 56:
                        if 0 <= entropy <= 0:
                                career = "Bailiff"
                        if 0 <= entropy <= 0:
                                career = "Hedge Witch"
                        if 46 <= entropy <= 47:
                                career = "Herbalist"
                        if 48 <= entropy <= 50:
                                career = "Hunter"
                        if 0 <= entropy <= 0:
                                career = "Miner"
                        if 0 <= entropy <= 0:
                                career = "Mystic"
                        if 51 <= entropy <= 56:
                                career = "Scout"
                        if 0 <= entropy <= 0:
                                career = "Villager"
                        base_class = "Peasants"
                        base_trappings = "Cloak, Clothing, Dagger, Pouch, Sling Bag containing Rations (1 day)"
                if 57 <= entropy <= 63:
                        if 57 <= entropy <= 59:
                                career = "Bounty Hunter"
                        if 0 <= entropy <= 0:
                                career = "Coachman"
                        if 60 <= entropy <= 62:
                                career = "Entertainer"
                        if 0 <= entropy <= 0:
                                career = "Flagellant"
                        if 63 <= entropy <= 63:
                                career = "Messenger"
                        if 0 <= entropy <= 0:
                                career = "Pedlar"
                        if 0 <= entropy <= 0:
                                career = "Road Warden"
                        if 0 <= entropy <= 0:
                                career = "Witch Hunter"
                        base_class = "Rangers"
                        base_trappings = "Cloak, Clothing, Dagger, Pouch, Backpack containing Tinderbox, Blanket, Rations (1 day)"
                if 64 <= entropy <= 80:
                        if 64 <= entropy <= 64:
                                career = "Boatman"
                        if 0 <= entropy <= 0:
                                career = "Huffer"
                        if 0 <= entropy <= 0:
                                career = "Riverwarden"
                        if 0 <= entropy <= 0:
                                career = "Riverwoman"
                        if 65 <= entropy <= 79:
                                career = "Seaman"
                        if 80 <= entropy <= 80:
                                career = "Smuggler"
                        if 0 <= entropy <= 0:
                                career = "Stevedore"
                        if 0 <= entropy <= 0:
                                career = "Wrecker"
                        base_class = "Riverfolk"
                        base_trappings = "Cloak, Clothing, Dagger, Pouch, Sling Bag containing a Flask of Spirits"
                if 81 <= entropy <= 88:
                        if 81 <= entropy <= 82:
                                career = "Bawd"
                        if 83 <= entropy <= 85:
                                career = "Charlatan"
                        if 0 <= entropy <= 0:
                                career = "Fence"
                        if 0 <= entropy <= 0:
                                career = "Grave Robber"
                        if 86 <= entropy <= 88:
                                career = "Outlaw"
                        if 0 <= entropy <= 0:
                                career = "Racketeer"
                        if 0 <= entropy <= 0:
                                career = "Thief"
                        if 0 <= entropy <= 0:
                                career = "Witch"
                        base_class = "Rogues"
                        base_trappings = "Clothing, Dagger, Pouch, Sling Bag containing 2 Candles, 1d10 Matches, a Hood or Mask"
                if 89 <= entropy <= 100:
                        if 89 <= entropy <= 92:
                                career = "Cavalryman"
                        if 93 <= entropy <= 94:
                                career = "Guard"
                        if 95 <= entropy <= 95:
                                career = "Knight"
                        if 96 <= entropy <= 97:
                                career = "Pit Fighter"
                        if 98 <= entropy <= 98:
                                career = "Protagonist"
                        if 99 <= entropy <= 100:
                                career = "Soldier"
                        if 0 <= entropy <= 0:
                                career = "Slayer"
                        if 0 <= entropy <= 0:
                                career = "Warrior Priest"
                        base_class = "Warriors"
                        base_trappings = "Clothing, Hand Weapon, Dagger, Pouch"
        if crace == "Wood Elf":

                if 1 <= entropy <= 5:
                        if 0 <= entropy <= 0:
                                career = "Apothecary"
                        if 0 <= entropy <= 0:
                                career = "Engineer"
                        if 0 <= entropy <= 0:
                                career = "Lawyer"
                        if 0 <= entropy <= 0:
                                career = "Nun"
                        if 0 <= entropy <= 0:
                                career = "Physician"
                        if 0 <= entropy <= 0:
                                career = "Priest"
                        if 1 <= entropy <= 1:
                                career = "Scholar"
                        if 2 <= entropy <= 5:
                                career = "Wizard"
                        base_class = "Academics"
                        base_trappings = "Clothing, Dagger, Pouch, Sling Bag containing Writing Kit and 1d10 sheets of Parchment"
                if 6 <= entropy <= 10:
                        if 0 <= entropy <= 0:
                                career = "Agitator"
                        if 6 <= entropy <= 10:
                                career = "Artisan"
                        if 0 <= entropy <= 0:
                                career = "Beggar"
                        if 0 <= entropy <= 0:
                                career = "Investigator"
                        if 0 <= entropy <= 0:
                                career = "Merchant"
                        if 0 <= entropy <= 0:
                                career = "Rat Catcher"
                        if 0 <= entropy <= 0:
                                career = "Townsman"
                        if 0 <= entropy <= 0:
                                career = "Watchman"

                        base_class = "Burghers"
                        base_trappings = "Cloak, Clothing, Dagger, Hat, Pouch, Sling Bag containing Lunch"
                if 11 <= entropy <= 35:
                        if 11 <= entropy <= 14:
                                career = "Advisor"
                        if 15 <= entropy <= 18:
                                career = "Artist"
                        if 0 <= entropy <= 0:
                                career = "Duellist"
                        if 19 <= entropy <= 25:
                                career = "Envoy"
                        if 26 <= entropy <= 31:
                                career = "Noble"
                        if 0 <= entropy <= 0:
                                career = "Servant"
                        if 32 <= entropy <= 35:
                                career = "Spy"
                        if 0 <= entropy <= 0:
                                career = "Warden"
                        base_class = "Courtiers"
                        base_trappings = "Courtly Garb, Dagger, Pouch containing Tweezers, Ear Pick and a Comb"
                if 36 <= entropy <= 68:
                        if 0 <= entropy <= 0:
                                career = "Bailiff"
                        if 0 <= entropy <= 0:
                                career = "Hedge Witch"
                        if 36 <= entropy <= 42:
                                career = "Herbalist"
                        if 43 <= entropy <= 52:
                                career = "Hunter"
                        if 0 <= entropy <= 0:
                                career = "Miner"
                        if 53 <= entropy <= 57:
                                career = "Mystic"
                        if 58 <= entropy <= 68:
                                career = "Scout"
                        if 0 <= entropy <= 0:
                                career = "Villager"
                        base_class = "Peasants"
                        base_trappings = "Cloak, Clothing, Dagger, Pouch, Sling Bag containing Rations (1 day)"
                if 69 <= entropy <= 78:
                        if 69 <= entropy <= 70:
                                career = "Bounty Hunter"
                        if 0 <= entropy <= 0:
                                career = "Coachman"
                        if 71 <= entropy <= 75:
                                career = "Entertainer"
                        if 0 <= entropy <= 0:
                                career = "Flagellant"
                        if 76 <= entropy <= 78:
                                career = "Messenger"
                        if 0 <= entropy <= 0:
                                career = "Pedlar"
                        if 0 <= entropy <= 0:
                                career = "Road Warden"
                        if 0 <= entropy <= 0:
                                career = "Witch Hunter"
                        base_class = "Rangers"
                        base_trappings = "Cloak, Clothing, Dagger, Pouch, Backpack containing Tinderbox, Blanket, Rations (1 day)"
                if 79 <= entropy <= 79:
                        if 0 <= entropy <= 0:
                                career = "Boatman"
                        if 0 <= entropy <= 0:
                                career = "Huffer"
                        if 0 <= entropy <= 0:
                                career = "Riverwarden"
                        if 0 <= entropy <= 0:
                                career = "Riverwoman"
                        if 0 <= entropy <= 0:
                                career = "Seaman"
                        if 0 <= entropy <= 0:
                                career = "Smuggler"
                        if 0 <= entropy <= 0:
                                career = "Stevedore"
                        if 79 <= entropy <= 79:
                                career = "Wrecker"
                        base_class = "Riverfolk"
                        base_trappings = "Cloak, Clothing, Dagger, Pouch, Sling Bag containing a Flask of Spirits"
                if 80 <= entropy <= 85:
                        if 0 <= entropy <= 0:
                                career = "Bawd"
                        if 0 <= entropy <= 0:
                                career = "Charlatan"
                        if 0 <= entropy <= 0:
                                career = "Fence"
                        if 0 <= entropy <= 0:
                                career = "Grave Robber"
                        if 80 <= entropy <= 85:
                                career = "Outlaw"
                        if 0 <= entropy <= 0:
                                career = "Racketeer"
                        if 0 <= entropy <= 0:
                                career = "Thief"
                        if 0 <= entropy <= 0:
                                career = "Witch"
                        base_class = "Rogues"
                        base_trappings = "Clothing, Dagger, Pouch, Sling Bag containing 2 Candles, 1d10 Matches, a Hood or Mask"
                if 86 <= entropy <= 100:
                        if 86 <= entropy <= 90:
                                career = "Cavalryman"
                        if 91 <= entropy <= 92:
                                career = "Guard"
                        if 93 <= entropy <= 94:
                                career = "Knight"
                        if 95 <= entropy <= 96:
                                career = "Pit Fighter"
                        if 0 <= entropy <= 0:
                                career = "Protagonist"
                        if 97 <= entropy <= 100:
                                career = "Soldier"
                        if 0 <= entropy <= 0:
                                career = "Slayer"
                        if 0 <= entropy <= 0:
                                career = "Warrior Priest"
                        base_class = "Warriors"
                        base_trappings = "Clothing, Hand Weapon, Dagger, Pouch"

        if crace == "Halfling":

                if 1 <= entropy <= 8:
                        if  1 <= entropy <= 1:
                                career="Apothecary"
                        if 2 <= entropy <= 2:
                                career = "Engineer"
                        if 3 <= entropy <= 4:
                                career = "Lawyer"
                        if 0 <=  entropy <= 0:
                                career = "Nun"
                        if 5 <= entropy <= 6:
                                career = "Physician"
                        if 0 <= entropy <= 0:
                                career = "Priest"
                        if 7 <= entropy <= 8:
                                career = "Scholar"
                        if 0 <= entropy <= 0:
                                career = "Wizard"
                        base_class = "Academics"
                        base_trappings = "Clothing, Dagger, Pouch, Sling Bag containing Writing Kit and 1d10 sheets of Parchment"
                if 9 <= entropy <= 33:
                        if  9 <= entropy <= 10:
                                career="Agitator"
                        if 11 <= entropy <= 15:
                                career = "Artisan"
                        if 16 <= entropy <= 19:
                                career = "Beggar"
                        if 20 <=  entropy <= 21:
                                career = "Investigator"
                        if 22 <= entropy <= 25:
                                career = "Merchant"
                        if 26 <= entropy <= 28:
                                career = "Rat Catcher"
                        if 29 <= entropy <= 31:
                                career = "Townsman"
                        if 32 <= entropy <= 33:
                                career = "Watchman"

                        base_class = "Burghers"
                        base_trappings = "Cloak, Clothing, Dagger, Hat, Pouch, Sling Bag containing Lunch"
                if 34 <= entropy <= 46:
                        if 34 <= entropy <= 34:
                                career = "Advisor"
                        if 35 <= entropy <= 36:
                                career = "Artist"
                        if 0 <= entropy <= 0:
                                career = "Duellist"
                        if 37 <= entropy <= 37:
                                career = "Envoy"
                        if 0 <= entropy <= 0:
                                career = "Noble"
                        if 38 <= entropy <= 43:
                                career = "Servant"
                        if 44 <= entropy <= 44:
                                career = "Spy"
                        if 45 <= entropy <= 46:
                                career = "Warden"
                        base_class = "Courtiers"
                        base_trappings = "Courtly Garb, Dagger, Pouch containing Tweezers, Ear Pick and a Comb"
                if 47 <= entropy <= 57:
                        if 47 <= entropy <= 47:
                                career = "Bailiff"
                        if 0 <= entropy <= 0:
                                career = "Hedge Witch"
                        if 48 <= entropy <= 50:
                                career = "Herbalist"
                        if 51 <= entropy <= 52:
                                career = "Hunter"
                        if 53 <= entropy <= 53:
                                career = "Miner"
                        if 0 <= entropy <= 0:
                                career = "Mystic"
                        if 54 <= entropy <= 54:
                                career = "Scout"
                        if 55 <= entropy <= 57:
                                career = "Villager"
                        base_class = "Peasants"
                        base_trappings = "Cloak, Clothing, Dagger, Pouch, Sling Bag containing Rations (1 day)"
                if 58 <= entropy <= 68:
                        if 58 <= entropy <= 58:
                                career = "Bounty Hunter"
                        if 59 <= entropy <= 60:
                                career = "Coachman"
                        if 61 <= entropy <= 63:
                                career = "Entertainer"
                        if 0 <= entropy <= 0:
                                career = "Flagellant"
                        if 64 <= entropy <= 65:
                                career = "Messenger"
                        if 66 <= entropy <= 67:
                                career = "Pedlar"
                        if 68 <= entropy <= 68:
                                career = "Road Warden"
                        if 0 <= entropy <= 0:
                                career = "Witch Hunter"
                        base_class = "Rangers"
                        base_trappings = "Cloak, Clothing, Dagger, Pouch, Backpack containing Tinderbox, Blanket, Rations (1 day)"
                if 69 <= entropy <= 82:
                        if 69 <= entropy <= 69:
                                career = "Boatman"
                        if 70 <= entropy <= 70:
                                career = "Huffer"
                        if 71 <= entropy <= 71:
                                career = "Riverwarden"
                        if 72 <= entropy <= 74:
                                career = "Riverwoman"
                        if 75 <= entropy <= 75:
                                career = "Seaman"
                        if 76 <= entropy <= 79:
                                career = "Smuggler"
                        if 80 <= entropy <= 82:
                                career = "Stevedore"
                        if 0 <= entropy <= 0:
                                career = "Wrecker"
                        base_class = "Riverfolk"
                        base_trappings = "Cloak, Clothing, Dagger, Pouch, Sling Bag containing a Flask of Spirits"
                if 83 <= entropy <= 94:
                        if 83 <= entropy <= 85:
                                career = "Bawd"
                        if 86 <= entropy <= 86:
                                career = "Charlatan"
                        if 87 <= entropy <= 87:
                                career = "Fence"
                        if 88 <= entropy <= 88:
                                career = "Grave Robber"
                        if 89 <= entropy <= 89:
                                career = "Outlaw"
                        if 90 <= entropy <= 90:
                                career = "Racketeer"
                        if 91 <= entropy <= 94:
                                career = "Thief"
                        if 0 <= entropy <= 0:
                                career = "Witch"
                        base_class = "Rogues"
                        base_trappings = "Clothing, Dagger, Pouch, Sling Bag containing 2 Candles, 1d10 Matches, a Hood or Mask"
                if 95 <= entropy <= 100:
                        if 0 <= entropy <= 0:
                                career = "Cavalryman"
                        if 95 <= entropy <= 96:
                                career = "Guard"
                        if 0 <= entropy <= 0:
                                career = "Knight"
                        if 97 <= entropy <= 97:
                                career = "Pit Fighter"
                        if 0 <= entropy <= 0:
                                career = "Protagonist"
                        if 98 <= entropy <= 100:
                                career = "Soldier"
                        if 0 <= entropy <= 0:
                                career = "Slayer"
                        if 0 <= entropy <= 0:
                                career = "Warrior Priest"
                        base_class = "Warriors"
                        base_trappings = "Clothing, Hand Weapon, Dagger, Pouch"

        if crace == "Dwarf":

                if 1 <= entropy <= 10:
                        if  1 <= entropy <= 1:
                                career="Apothecary"
                        if 2 <= entropy <= 4:
                                career = "Engineer"
                        if 5 <= entropy <= 6:
                                career = "Lawyer"
                        if 0 <=  entropy <= 0:
                                career = "Nun"
                        if 7 <= entropy <= 7:
                                career = "Physician"
                        if 0 <= entropy <= 0:
                                career = "Priest"
                        if 8 <= entropy <= 9:
                                career = "Scholar"
                        if 0 <= entropy <= 0:
                                career = "Wizard"
                        base_class = "Academics"
                        base_trappings = "Clothing, Dagger, Pouch, Sling Bag containing Writing Kit and 1d10 sheets of Parchment"
                if 10 <= entropy <= 34:
                        if  10 <= entropy <= 11:
                                career="Agitator"
                        if 12 <= entropy <= 17:
                                career = "Artisan"
                        if 18 <= entropy <= 18:
                                career = "Beggar"
                        if 19 <=  entropy <= 20:
                                career = "Investigator"
                        if 21 <= entropy <= 24:
                                career = "Merchant"
                        if 25 <= entropy <= 25:
                                career = "Rat Catcher"
                        if 26 <= entropy <= 31:
                                career = "Townsman"
                        if 32 <= entropy <= 34:
                                career = "Watchman"

                        base_class = "Burghers"
                        base_trappings = "Cloak, Clothing, Dagger, Hat, Pouch, Sling Bag containing Lunch"
                if 35 <= entropy <= 45:
                        if 35 <= entropy <= 36:
                                career = "Advisor"
                        if 37 <= entropy <= 37:
                                career = "Artist"
                        if 38 <= entropy <= 38:
                                career = "Duellist"
                        if 39 <= entropy <= 40:
                                career = "Envoy"
                        if 41 <= entropy <= 41:
                                career = "Noble"
                        if 42 <= entropy <= 42:
                                career = "Servant"
                        if 43 <= entropy <= 43:
                                career = "Spy"
                        if 44 <= entropy <= 45:
                                career = "Warden"
                        base_class = "Courtiers"
                        base_trappings = "Courtly Garb, Dagger, Pouch containing Tweezers, Ear Pick and a Comb"
                if 46 <= entropy <= 56:
                        if 46 <= entropy <= 47:
                                career = "Bailiff"
                        if 0 <= entropy <= 0:
                                career = "Hedge Witch"
                        if 0 <= entropy <= 0:
                                career = "Herbalist"
                        if 48 <= entropy <= 49:
                                career = "Hunter"
                        if 50 <= entropy <= 54:
                                career = "Miner"
                        if 0 <= entropy <= 0:
                                career = "Mystic"
                        if 55 <= entropy <= 55:
                                career = "Scout"
                        if 56 <= entropy <= 56:
                                career = "Villager"
                        base_class = "Peasants"
                        base_trappings = "Cloak, Clothing, Dagger, Pouch, Sling Bag containing Rations (1 day)"
                if 57 <= entropy <= 67:
                        if 57 <= entropy <= 60:
                                career = "Bounty Hunter"
                        if 61 <= entropy <= 61:
                                career = "Coachman"
                        if 62 <= entropy <= 63:
                                career = "Entertainer"
                        if 0 <= entropy <= 0:
                                career = "Flagellant"
                        if 64 <= entropy <= 65:
                                career = "Messenger"
                        if 66 <= entropy <= 67:
                                career = "Pedlar"
                        if 0 <= entropy <= 0:
                                career = "Road Warden"
                        if 0 <= entropy <= 0:
                                career = "Witch Hunter"
                        base_class = "Rangers"
                        base_trappings = "Cloak, Clothing, Dagger, Pouch, Backpack containing Tinderbox, Blanket, Rations (1 day)"
                if 68 <= entropy <= 78:
                        if 68 <= entropy <= 69:
                                career = "Boatman"
                        if 70 <= entropy <= 70:
                                career = "Huffer"
                        if 0 <= entropy <= 0:
                                career = "Riverwarden"
                        if 71 <= entropy <= 72:
                                career = "Riverwoman"
                        if 73 <= entropy <= 73:
                                career = "Seaman"
                        if 74 <= entropy <= 75:
                                career = "Smuggler"
                        if 76 <= entropy <= 77:
                                career = "Stevedore"
                        if 78 <= entropy <= 78:
                                career = "Wrecker"
                        base_class = "Riverfolk"
                        base_trappings = "Cloak, Clothing, Dagger, Pouch, Sling Bag containing a Flask of Spirits"
                if 79 <= entropy <= 84:
                        if 0 <= entropy <= 0:
                                career = "Bawd"
                        if 0 <= entropy <= 0:
                                career = "Charlatan"
                        if 79 <= entropy <= 79:
                                career = "Fence"
                        if 0 <= entropy <= 0:
                                career = "Grave Robber"
                        if 80 <= entropy <= 82:
                                career = "Outlaw"
                        if 83 <= entropy <= 83:
                                career = "Racketeer"
                        if 84 <= entropy <= 84:
                                career = "Thief"
                        if 0 <= entropy <= 0:
                                career = "Witch"
                        base_class = "Rogues"
                        base_trappings = "Clothing, Dagger, Pouch, Sling Bag containing 2 Candles, 1d10 Matches, a Hood or Mask"
                if 85 <= entropy <= 100:
                        if 0 <= entropy <= 0:
                                career = "Cavalryman"
                        if 85 <= entropy <= 87:
                                career = "Guard"
                        if 0 <= entropy <= 0:
                                career = "Knight"
                        if 88 <= entropy <= 90:
                                career = "Pit Fighter"
                        if 91 <= entropy <= 93:
                                career = "Protagonist"
                        if 94 <= entropy <= 96:
                                career = "Soldier"
                        if 97 <= entropy <= 100:
                                career = "Slayer"
                        if 0 <= entropy <= 0:
                                career = "Warrior Priest"
                        base_class = "Warriors"
                        base_trappings = "Clothing, Hand Weapon, Dagger, Pouch"
        #print "DEBUG:", entropy
        career_package= career, base_class, base_trappings
        return career_package

def careerinformation(career):
        career=[0,1,2,3,4,5,6,7,8,9,10,11]
        return career
def randomtalents():
        numeric=dhundred()
        if 1 <= numeric <= 3:
                talent="Acute Sense (Any One)"
        if 4 <= numeric <= 6:
                talent="Ambidextrous"
        if 7 <= numeric <= 9:
                talent="Animal Affinity"
        if 10 <= numeric <= 12:
                talent="Artistic"
        if 13 <= numeric <= 15:
                talent = "Attractive"
        if 16 <= numeric <= 18:
                talent="Coolheaded"
        if 19 <= numeric <= 21:
                talent="Craftsman (any one)"
        if 22 <= numeric <= 24:
                talent="Flee!"
        if 25 <= numeric <= 28:
                talent="Hardy"
        if 29 <= numeric <= 31:
                talent="Lightning Reflexes"
        if 32 <= numeric <= 34:
                talent="Linguistics"
        if 35 <= numeric <= 38:
                talent="Luck"
        if 39 <= numeric <= 41:
                talent="Marksman"
        if 42 <= numeric <= 44:
                talent="Mimic"
        if 45 <= numeric <= 47:
                talent="Night Vision"
        if 48 <= numeric <= 50:
                talent="Nimble Fingered"
        if 51 <= numeric <= 52:
                talent="Noble Blood"
        if 53 <= numeric <= 55:
                talent="Orientation"
        if 56 <= numeric <= 58:
                talent="Perfect Pitch"
        if 59 <= numeric <= 62:
                talent="Pure Soul"
        if 63 <= numeric <= 65:
                talent="Quick Witted"
        if 66 <= numeric <= 68:
                talent="Resistance"
        if 69 <= numeric <= 71:
                talent="Savvy"
        if 72 <= numeric <= 74:
                talent="Sharp"
        if 75 <= numeric <= 78:
                talent="Luck"
        if 79 <= numeric <= 81:
                talent="Strong Legs"
        if 82 <= numeric <= 84:
                talent="Sturdy"
        if 85 <= numeric <= 87:
                talent="Suave"
        if 88 <= numeric <= 91:
                talent="Super Numerate"
        if 92 <= numeric <= 94:
                talent = "Very Resilient"
        if 95 <= numeric <= 97:
                talent = "Very Strong"
        if 98 <= numeric <= 100:
                talent = "Warrior Born"

        return talent

def career_package(career):
        career_attributes = "UNSET"
        if career=="Apothecary":
                career_attributes="T,Dex,Int"
                career_skills="Consume Alcohol, Heal, Language (Classical), Lore (Chemistry), Lore (Medicine), Lore (Plants), Trade (Apothecary), Trade (Poisoner)"
                career_talents="Concoct, Craftsman (Apothecary), Etiquette (Scholar), Read/Write"
                career_trappings="Book (Blank), Healing Draft, Leather Jerkin, Pestle and Mortar"
                career_status="Apothecary’s Apprentice - Brass 3"
        if career == "Engineer":
                career_attributes = "BS,Dex,Int"
                career_skills = "Consume Alcohol, Cool, Endurance, Language (Classical), Lore (Engineer), Perception, Ranged (Blackpowder), Trade (Engineer)"
                career_talents = "Artist, Gunner, Read/Write, Tinker"
                career_trappings = "Book (Engineer), Hammer and Spikes"
                career_status="Student Engineer — Brass 4"
        if career == "Lawyer":
                career_attributes = "I,Dex,Int"
                career_skills = "Consume Alcohol, Endurance, Haggle, Language (Classical), Lore (Law), Lore (Theology), Perception, Research"
                career_talents = "Blather, Etiquette (Scholar), Read/Write, Speedreader"
                career_trappings = "Book (Law), Magnifying Glass"
                career_status = "Student Lawyer — Brass 4"
        if career == "Nun":
                career_attributes = "Dex,Int,Fel"
                career_skills = "Art (Calligraphy), Cool, Endurance, Entertain (Storyteller), Gossip, Heal, Lore (Theology), Pray"
                career_talents = "Bless (Any), Stone Soup, Panhandle, Read/Write"
                career_trappings = "Religious Symbol, Robes"
                career_status = "Novitiate — Brass 1"
        if career == "Physician":
                career_attributes = "Dex,Int,WP"
                career_skills = "Bribery, Cool, Drive, Endurance, Gossip, Heal, Perception, Sleight of Hand"
                career_talents = "Bookish, Field Dressing, Read/Write, Strike to Stun"
                career_trappings = "Bandages, Healing Draught"
                career_status = "Physician’s Apprentice — Brass 4"
        if career == "Priest":
                career_attributes = "T,Agi,WP"
                career_skills = "Athletics, Cool, Endurance, Intuition, Lore ( Theology), Perception, Pray, Research"
                career_talents = "Bless (Any), Holy Visions, Read/Write, Suave"
                career_trappings = "Religious Symbol, Robes"
                career_status = "Initiate — Brass 2"
        if career == "Scholar":
                career_attributes = "T,Int,WP"
                career_skills = "Consume Alcohol, Entertain (Storytelling), Gamble, Gossip, Haggle, Language (Classical), Lore (Any), Research"
                career_talents = "Carouser, Read/Write, Savvy, Super Numerate"
                career_trappings = "Alcohol, Book, Opinions, Writing Kit"
                career_status = "Student — Brass 3"
        if career == "Wizard":
                career_attributes = "WS,Int,WP"
                career_skills = "Channelling (Any Colour), Dodge, Intuition, Language (Magick), Lore (Magic), Melee (Basic), Melee (Polearm), Perception"
                career_talents = "Aethyric Attunement, Petty Magic (Any), Read/Write, Second Sight"
                career_trappings = "Grimoire, Staff"
                career_status = "Wizard’s Apprentice — Brass 3"
        if career == "Agitator":
                career_attributes = "BS,Int,Fel"
                career_skills = "Art (Writing), Bribery, Charm, Consume Alcohol, Gossip, Haggle, Lore (Politics), Trade (Printing)"
                career_talents = "Blather, Gregarious, Panhandle, Read/Write"
                career_trappings = "Writing Kit, Hammer and Nails, Pile of Leaflets"
                career_status = "Pamphleteer — Brass 1"
        if career == "Artisan":
                career_attributes = "S,T,Dex"
                career_skills = "Athletics, Cool, Consume Alcohol, Dodge, Endurance, Evaluate, Stealth (Urban), Trade (Any)"
                career_talents = "Artistic, Craftsman (any), Strong Back, Very Strong"
                career_trappings = "Chalk, Leather Jerkin, d10 rags"
                career_status = "Apprentice Artisan — Brass 2"
        if career == "Beggar":
                career_attributes = "T,Agi,Fel"
                career_skills = "Athletics, Charm, Consume Alcohol, Cool, Dodge, Endurance, Intuition, Stealth (Urban)"
                career_talents = "Panhandle, Resistance (Disease), Stone Soup, Very Resilient"
                career_trappings = "Poor Quality Blanket, Cup"
                career_status = "Pauper — Brass 0"
        if career == "Investigator":
                career_attributes = "I,Agi,Int"
                career_skills = "Charm, Climb, Cool, Gossip, Intuition, Perception, Stealth (Urban), Track"
                career_talents = "Alley Cat, Beneath Notice, Read/Write, Sharp"
                career_trappings = "Lantern, Lamp Oil, Journal, Quill and Ink"
                career_status = "Sleuth — Silver 1"
        if career == "Merchant":
                career_attributes = "WS,Agi,Fel"
                career_skills = "Animal Care, Bribery, Charm, Consume Alcohol, Drive, Gamble, Gossip, Haggle"
                career_talents = "Blather, Dealmaker, Read/Write, Suave"
                career_trappings = "Abacus, Mule and Cart, Canvas Tarpaulin, 3d10 Silver Shillings"
                career_status = "Trader — Silver 2"
        if career == "Rat Catcher":
                career_attributes = "WS,BS,WP"
                career_skills = "Athletics, Animal Training (Dog), Charm Animal, Consume Alcohol, Endurance, Melee (Basic), Ranged (Sling), Stealth (Underground or Urban)"
                career_talents = "Night Vision, Resistance (Disease), Strike Mighty Blow, Strike to Stun"
                career_trappings = "Sling with Ammunition, Sack, Small but Vicious Dog"
                career_status = "Rat Hunter — Brass 3"
        if career == "Townsman":
                career_attributes = "Agi,Int,Fel"
                career_skills = "Charm, Climb, Consume Alcohol, Drive, Dodge, Gamble, Gossip, Haggle"
                career_talents = "Alley Cat, Beneath Notice, Etiquette (Servants), Sturdy"
                career_trappings = "Lodgings, Sturdy Boots"
                career_status = "Clerk — Silver 1"
        if career == "Watchman":
                career_attributes = "WS,S,Fel"
                career_skills = "Athletics, Climb, Consume Alcohol, Dodge, Endurance, Gamble, Melee, Perception"
                career_talents = "Drilled, Hardy, Strike to Stun, Tenacious"
                career_trappings = "Hand Weapon, Leather Jack, Uniform"
                career_status = "Watchman — Silver 1"
        if career == "Advisor":
                career_attributes = "T,I,Agi"
                career_skills = "Bribery, Consume Alcohol, Endurance, Gossip, Haggle, Language (Classical), Lore (Politics), Perception"
                career_talents = "Beneath Notice, Etiquette (Any), Gregarious, Read/Write"
                career_trappings = "Writing Kit"
                career_status = "Aide — Silver 2"
        if career == "Artist":
                career_attributes = "S,I,Dex"
                career_skills = "Art (Any), Cool, Consume Alcohol, Evaluate, Endurance, Gossip, Perception, Stealth (Urban)"
                career_talents = "Artistic, Sharp, Strong Back, Tenacious"
                career_trappings = "Brush or Chisel or Quill Pen"
                career_status = "Apprentice Artist — Silver 1"
        if career == "Duellist":
                career_attributes = "WS,I,Agi"
                career_skills = "Athletics, Dodge, Endurance, Heal, Intuition, Language (Classical), Melee (Any), Perception"
                career_talents = "Beat Blade, Distract, Feint, Step Aside"
                career_trappings = "Basic Weapon or Rapier, Sling Bag containing Clothing and 1d10 Bandages"
                career_status = "Fencer — Silver 3"
        if career == "Envoy":
                career_attributes = "T,Agi,Fel"
                career_skills = "Athletics, Charm, Drive, Dodge, Endurance, Intuition, Ride (Horse), Row"
                career_talents = "Blather, Etiquette (Nobles), Read/Write, Suave"
                career_trappings = "Leather Jack, Livery, Scroll Case"
                career_status = "Herald — Silver 2"
        if career == "Noble":
                career_attributes = "WS,I,Dex"
                career_skills = "Bribery, Consume Alcohol, Gamble, Intimidate, Leadership, Lore (Heraldry), Melee (Fencing), Play (Any)"
                career_talents = "Etiquette (Nobles), Luck, Noble Blood, Read/Write"
                career_trappings = "Courtly Garb, Foil or Hand Mirror, Jewellery"
                career_status = "Scion — Gold 1"
        if career == "Servant":
                career_attributes = "S,T,Agi"
                career_skills = "Athletics, Climb, Drive, Dodge, Endurance, Intuition, Perception, Stealth (Any)"
                career_talents = "Beneath Notice, Strong Back, Strong-minded, Sturdy"
                career_trappings = "Floor Brush"
                career_status = "Menial — Silver 1"
        if career == "Spy":
                career_attributes = "Agi,WP,Fel"
                career_skills = "Bribery, Charm, Cool, Gamble, Gossip, Haggle, Perception, Stealth (Any)"
                career_talents = "Blather, Carouser, Gregarious, Shadow"
                career_trappings = "Charcoal stick, Sling Bag containing 2 different sets of clothing and Hooded Cloak"
                career_status = "Informer — Brass 3"
        if career == "Warden":
                career_attributes = "S,T,WP"
                career_skills = "Athletics, Charm Animal, Consume Alcohol, Cool, Endurance, Intuition, Perception, Trade (Any)"
                career_talents = "Menacing, Night Vision, Sharp, Strike to Stun"
                career_trappings = "Keys, Lantern, Lamp Oil, Livery"
                career_status = "Custodian — Silver 1"
        if career == "Bailiff":
                career_attributes = "WS,I,WP"
                career_skills = "Cool, Dodge, Endurance, Gossip, Haggle, Intimidate, Melee, Perception"
                career_talents = "Embezzle, Numismatics, Strong Back, Tenacious"
                career_trappings = "Hand weapon, small lock box"
                career_status = "Tax Collector — Silver 1"
        if career == "Hedge Witch":
                career_attributes = "T,I,Dex"
                career_skills = "Channelling, Endurance, Intuition, Lore (Folklore), Lore (Herbs), Outdoor Survival, Perception, Trade (Charms"
                career_talents = "Fast-Hands, Petty Magic, Rover, Strider (Woodlands)"
                career_trappings = "1d10 Lucky Charms, Quarterstaff , Backpack"
                career_status = "Hedge Apprentice — Brass 1"
        if career == "Herbalist":
                career_attributes = "T,I,Agi"
                career_skills = "Charm Animal, Climb, Endurance, Lore (Herbs), Outdoor Survival, Perception, Swim, Trade (Herbalist)"
                career_talents = "Acute Sense (Taste), Orientation, Rover, Strider (any)"
                career_trappings = "Boots, Cloak, Sling Bag containing Assortment of Herbs"
                career_status = "Herb Gatherer — Brass 2"
        if career == "Hunter":
                career_attributes = "S,T,Int"
                career_skills = "Charm Animal, Climb, Endurance, Lore (Beasts), Outdoor Survival, Perception, Ranged (Bow), Set Trap"
                career_talents = "Hardy, Rover, Strider (any), Trapper"
                career_trappings = "Selection of Animal Traps, Hand Weapon, Sturdy Boots and Cloak"
                career_status = "Trapper — Brass 2"
        if career == "Miner":
                career_attributes = "S,T,WP"
                career_skills = "Cool, Endurance, Intuition, Lore (Local), Melee (Two-handed), Outdoor Survival, Perception, Swim"
                career_talents = "Rover, Strider (Rocky), Sturdy, Tenacious"
                career_trappings = "Charcoal Stick, Crude Map, Pan, Spade"
                career_status = "Prospector — Brass 2"
        if career == "Mystic":
                career_attributes = "I,Dex,Fel"
                career_skills = "Charm, Entertain (Fortune Telling), Dodge, Gossip, Haggle, Intuition, Perception, Sleight of Hand"
                career_talents = "Attractive, Luck, Second Sight, Suave"
                career_trappings = "Deck of Cards or Dice, Cheap Jewellery"
                career_status = "Fortune Teller — Brass 1"
        if career == "Scout":
                career_attributes = "T,I,Ag"
                career_skills = "Charm Animal, Climb, Endurance, Gossip, Lore (Local), Melee (Basic), Outdoor Survival, Perception Talents: Orientation, Rover, Sharp, Strider (any)"
                career_talents = "Orientation, Rover, Sharp, Strider (any)"
                career_trappings = "Hand Weapon, Leather Jack, Sturdy Boots and Cloak, Rope"
                career_status = "Guide — Brass 3"
        if career == "Villager":
                career_attributes = "S,T,Agi"
                career_skills = "Animal Care, Athletics, Consume Alcohol, Endurance, Gossip, Melee (Fist), Lore (Local), Outdoor Survival"
                career_talents = "Rover, Strong Back, Strong-minded, Stone Soup"
                career_trappings = "None"
                career_status = "Peasant — Brass 2"
        if career == "Bounty Hunter":
                career_attributes = "WS,T,Agi"
                career_skills = "Bribery, Charm, Gossip, Haggle, Intuition, Melee (Basic), Outdoor Survival, Perception"
                career_talents = "Break and Enter, Shadow, Strike to Stun, Suave"
                career_trappings = "Hand Weapon, Leather Jerkin, Rope"
                career_status = "Thief-taker — Silver 1"
        if career == "Coachman":
                career_attributes = "BS,T,WP"
                career_skills = "Animal Care, Charm Animal, Climb, Drive, Endurance, Perception, Ranged (Entangling), Ride (Horse)"
                career_talents = "Animal A nity, Seasoned Traveller, Trick-Riding, Tenacious"
                career_trappings = "Warm Coat and Gloves, Whip"
                career_status = "Postilion — Silver 1"
        if career == "Entertainer":
                career_attributes = "Agi,Dex,Fel"
                career_skills = "Athletics, Charm, Entertain (Any), Gossip, Haggle, Perform (Any), Play (any), Sleight of Hand"
                career_talents = "Attractive, Mimic, Public-Speaking, Suave"
                career_trappings = "Bowl, Instrument"
                career_status = "Busker — Brass 3"
        if career == "Flagellant":
                career_attributes = "W,S,T"
                career_skills = "Dodge, Endurance, Heal, Intimidate, Intuition, Lore (Theology), Melee (Flail), Outdoor Survival"
                career_talents = "Berserk Charge, Frenzy, Read/Write, Stone Soup"
                career_trappings = "Flail, Tattered Robes"
                career_status = "Zealot — Brass 0"
        if career == "Messenger":
                career_attributes = "T,I,Agi"
                career_skills = "Athletics, Climb, Dodge, Endurance, Gossip, Navigation, Perception, Melee (Fist)"
                career_talents = "Flee!, Fleet Footed, Sprinter, Step Aside"
                career_trappings = "Scroll Case"
                career_status = "Runner — Brass 3"
        if career == "Pedlar":
                career_attributes = "T,Dex,WP"
                career_skills = "Charm, Endurance, Entertain (Storytelling), Gossip, Haggle, Intuition, Outdoor Survival, Stealth (Rural or Urban)"
                career_talents = "Fisherman, Flee!, Rover, Tinker"
                career_trappings = "Backpack, Bedroll, Goods worth 2d10 brass, Tent"
                career_status = "Vagabond — Brass 1"
        if career == "Road Warden":
                career_attributes = "BS,T,I"
                career_skills = "Bribery, Consume Alcohol, Gamble, Gossip, Haggle, Melee (Basic), Perception, Ranged (Crossbow)"
                career_talents = "Coolheaded, Embezzle, Marksman, Numismatics"
                career_trappings = "Crossbow with 10 Bolts, Leather Jack"
                career_status = "Toll Keeper — Brass 5"
        if career == "Witch Hunter":
                career_attributes = "T,I,WP"
                career_skills = "Charm, Consume Alcohol, Heal, Intimidate, Intuition, Lore (Torture), Melee (Basic), Perception"
                career_talents = "Coolheaded, Menacing, Read/Write, Resolute"
                career_trappings = "Hand Weapon, Instruments of Torture"
                career_status = "Interrogator — Silver 1"
        if career == "Boatman":
                career_attributes = "S,T,Agi"
                career_skills = "Consume Alcohol, Dodge, Endurance, Gossip, Melee (Basic), Row, Sail, Swim"
                career_talents = "Dirty Fighting, Fisherman, Strong Back, Strong Swimmer"
                career_trappings = "Hand Weapon (Boat Hook), Leather Jack,Pole"
                career_status = "Boat-hand — Silver 1"
        if career == "Huffer":
                career_attributes = "WS,T,I"
                career_skills = "Consume Alcohol, Gossip, Intuition, Lore (Local), Lore (Riverways), Perception, Row, Swim"
                career_talents = "Fisherman, Night Vision, Orientation, Waterman"
                career_trappings = "Hand Weapon (Boat Hook), Storm Lantern and Oil"
                career_status = "Riverguide — Brass 4"
        if career == "Riverwoman":
                career_attributes = "T,Agi,Dex"
                career_skills = "Athletics, Consume Alcohol, Dodge, Endurance, Gossip, Outdoor Survival, Row, Swim"
                career_talents = "Fisherman, Gregarious, Strider (Marshes), Strong Swimmer"
                career_trappings = "Bucket, Fishing Rod and Bait, Leather Leggings"
                career_status = "Greenfish — Brass 2"
        if career == "Riverwarden":
                career_attributes = "BS,S,Fel"
                career_skills = "Athletics, Dodge, Endurance, Melee (Basic), Perception, Row, Sail, Swim"
                career_talents = "Strong Swimmer, Strong Back, Very Strong, Waterman"
                career_trappings = "Hand Weapon (Sword), Leather Jack, Uniform"
                career_status = "River Recruit — Silver 1"
        if career == "Seaman":
                career_attributes = "Agi,Dex,Fel"
                career_skills = "Climb, Consume Alcohol, Gamble, Gossip, Row, Melee (Fist), Sail, Swim"
                career_talents = "Fisherman, Strider (Coastal), Strong Back, Strong Swimmer"
                career_trappings = "Bucket, Brush, Mop"
                career_status = "Landsman — Silver 1"
        if career == "Smuggler":
                career_attributes = "Agi,Dex,WP"
                career_skills = "Athletics, Bribery, Cool, Consume Alchohol, Row, Sail, Stealth (Rural or Urban),Swim"
                career_talents = "Criminal, Fisherman, Strider (Marshes), Strong Back"
                career_trappings = "Large Sack, Mask or Scarves, Tinderbox, Storm Lantern and Oil"
                career_status = "River Runner — Brass 2"
        if career == "Stevedore":
                career_attributes = "WS,T,I"
                career_skills = "Athletics, Climb, Consume Alcohol, Dodge, Endurance, Gossip, Melee (Basic), Swim"
                career_talents = "Dirty Fighting, Strong Back, Sturdy, Very Strong"
                career_trappings = "Hand Weapon (Boat Hook), Leather Gloves"
                career_status = "Dockhand — Brass 3"
        if career == "Wrecker":
                career_attributes = "WS,S,I"
                career_skills = " Climb, Consume Alcohol, Dodge, Endurance, Row, Melee (Basic), Outdoor Survival, Swim"
                career_talents = "Break and Enter, Criminal, Fisherman,Strong Back"
                career_trappings = "Crowbar, Large Sack, Leather Gloves"
                career_status = "Cargo Scavenger — Brass 2"
        if career == "Bawd":
                career_attributes = "Agi,Dex,Fel"
                career_skills = "Bribery, Charm, Consume Alcohol, Entertain (Any), Gamble, Gossip, Haggle, Intimidate  "
                career_talents = "Attractive, Alley Cat, Blather, Gregarious"
                career_trappings = "Flask of Spirits"
                career_status = "Hustler — Brass 1"
        if career == "Charlatan":
                career_attributes = "I,Agi,Fel"
                career_skills = "Bribery, Consume Alcohol, Charm, Entertain (Storytelling), Gamble, Gossip, Haggle, Sleight of Hand"
                career_talents = "Cardsharp, Diceman, Etiquette (Any), Luck"
                career_trappings = "Backpack, 2 Sets Clothing, Deck of Cards, Dice"
                career_status = "Swindler — Brass 3"
        if career == "Fence":
                career_attributes = "I,Agi,Fel"
                career_skills = "Charm, Dodge, Evaluate, Gamble, Gamble, Gossip, Haggle, Melee (Basic)"
                career_talents = "Alley Cat, Cardsharp, Dealmaker, Gregarious"
                career_trappings = "Hand Weapon, Stolen Goods worth 3d10 Shillings"
                career_status = "Broker — Silver 1"
        if career == "Grave Robber":
                career_attributes = "S,I,WP"
                career_skills = "Climb, Cool, Dodge, Endurance, Gossip, Intuition, Perception, Stealth (Any)"
                career_talents = "Alley Cat, Criminal, Flee!, Strong Back"
                career_trappings = "Crowbar, Handcart, Hooded Cloak, Tarpaulin"
                career_status = "Body Snatcher — Brass 2"
        if career == "Outlaw":
                career_attributes = "WS,S,T"
                career_skills = "Athletics, Consume Alcohol, Cool, Endurance, Gamble, Intimidate, Melee (Basic), Outdoor Survival"
                career_talents = "Combat Aware, Criminal, Rover, Flee!"
                career_trappings = "Bedroll, Hand Weapon, Leather Jerkin, Tinderbox"
                career_status = "Brigand — Brass 1"
        if career == "Racketeer":
                career_attributes = "WS,S,T"
                career_skills = "Consume Alcohol, Cool, Dodge, Endurance, Intimidate, Lore (Local), Melee (Fist), Stealth (Urban)"
                career_talents = "Criminal, Etiquette (Criminals), Menacing, Strike Mighty Blow"
                career_trappings = "Brass Knuckles, Leather Jack"
                career_status = "Thug — Brass 3"
        if career == "Thief":
                career_attributes = "I,Agi,WP"
                career_skills = "Athletics, Climb, Cool, Dodge, Endurance, Intuition, Perception, Stealth (Urban)"
                career_talents = "Alley Cat, Criminal, Etiquette (Criminals), Flee!, Strike to Stun"
                career_trappings = "Crowbar, Leather Jerkin, Sack"
                career_status = "Prowler — Brass 1"
        if career == "Witch":
                career_attributes = "WS,T,WP"
                career_skills = "Channelling, Cool, Endurance, Gossip, Intimidate, Language (Magick), Sleight of Hand, Stealth (Rural)"
                career_talents = "Criminal, Menacing, Petty Magic, Witch!"
                career_trappings = "Candles, Chalk, Doll, Pins"
                career_status = "Hexer — Brass 1"
        if career == "Cavalryman":
                career_attributes = "WS,S,Agi"
                career_skills = "Animal Care, Charm Animal, Endurance, Language (Battle), Melee (Basic), Outdoor Survival, Perception, Ride (Horse)"
                career_talents = "Combat Aware, Crack the Whip, Lightning Re exes, Roughrider"
                career_trappings = "Hand Weapon, Leather Jack, Riding Horse with Saddle and Tack"
                career_status = "Horseman — Silver 2"
        if career == "Guard":
                career_attributes = "WS,T,Agi"
                career_skills = "Consume Alcohol, Endurance, Entertain (Storytelling), Gamble, Gossip, Intuition, Melee (Basic), Perception"
                career_talents = "Diceman, Etiquette (Servants), Strike to Stun, Tenacious"
                career_trappings = "Hand Weapon, Leather Jerkin, Storm Lantern with Oil"
                career_status = "Sentry — Silver 1"
        if career == "Knight":
                career_attributes = "S,I,Agi"
                career_skills = "Athletics, Animal Care, Charm Animal, Heal, Lore (Heraldry), Melee (Cavalry), Ride (Horse), Trade (Farrier)"
                career_talents = "Etiquette (any), Roughrider, Sturdy, Warrior Born"
                career_trappings = "Demilance, Leather Jack, Mail Shirt, Riding Horse with Saddle and Tack, Shield, Trade Tools (Farrier)"
                career_status = "Squire — Silver 3"
        if career == "Pit Fighter":
                career_attributes = "WS,S,T"
                career_skills = "Athletics, Cool, Dodge, Endurance, Gamble, Intimidate, Melee (Any), Melee (Fist)"
                career_talents = "Dirty Fighter, In- ghter, Iron Jaw, Reversal"
                career_trappings = "Bandages, Brass Knuckles, Hand Weapon, Leather Jack"
                career_status = "Pugilist — Brass 4"
        if career == "Protagonist":
                career_attributes = "WS,T,Agi"
                career_skills = "Athletics, Dodge, Endurance, Entertain (Taunt), Gossip, Haggle, Intimidate, Melee (Any),"
                career_talents = "In- ghter, Dirty Fighting, Menacing, Warrior Born"
                career_trappings = "Brass Knuckles, Hood or Mask, Leather Jack"
                career_status = "Braggart — Brass 2"
        if career == "Slayer":
                career_attributes = "WS,S,WP"
                career_skills = "Consume Alcohol, Cool, Dodge, Endurance, Gamble, Heal, Lore (Trolls), Melee (Basic)"
                career_talents = "Duel Wielder, Fearless (Everything), Frenzy, Slayer"
                career_trappings = " Axe, Flask of Spirits, Shame, Tattoos"
                career_status = "Troll Slayer — Brass 2"
        if career == "Soldier":
                career_attributes = "WS,T,WP"
                career_skills = "Athletics, Climb, Cool, Dodge, Endurance, Language (Battle), Melee (Basic), Play (Drum or Fife)"
                career_talents = "Diceman, Marksman, Strong Back, Warrior Born"
                career_trappings = "Hand Weapon (Sword), Leather Armour (uniform)"
                career_status = "Recruit — Silver 1"
        if career == "Warrior Priest":
                career_attributes = "WS,WP,Fel"
                career_skills = "Cool, Dodge, Endurance, Heal, Leadership, Lore ( eology), Melee (Any), Pray"
                career_talents = "Bless (Any), Etiquette (Cultists), Read/Write, Strong-minded"
                career_trappings = "Book (Religion), Leather Jerkin, Religious Symbol, Robes, Weapon (Any)"
                career_status = "Novitiate — Brass 2"

        if career_attributes == "UNSET":
                print "ERROR:", career
                exit(1)


        careerpackage=career_attributes, career_skills, career_talents, career_trappings, career_status
        return careerpackage


makeachar()