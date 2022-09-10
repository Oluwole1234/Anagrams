import random

def userInput():
    user_action=input(f"\nwhich level would you like to play. Enter 1 for Level_1,Enter 2 for Level_2 and Enter 3 for Level_3{possible_levels}.\n:")
    print(user_action)
    formatUserAction = user_action.lower()
    print(f"\nYou choose {formatUserAction}.\n")
    return formatUserAction

def anagrams_1():
    Level_1=["meat","goat","fish"]
    anagrams_meat=['am','at','em','et','ma','me','ate','eat','eta','mat','mea','met','tae','tam','tea','tem','mate','meat','meta','tame','team']
    anagrams_goat=['at','go','ta','to','ago','gat','goa','got','oat','tag','tao','tog','toga']
    anagrams_fish=['fi','hi','if','is','si','his','ifs']
    random_word=random.choice(Level_1)
    print(f"\nYour word is {random_word}.\n")
    return random_word

def anagrams_2():
    Level_2=["above","blood","class","entry"]
    anagrams_above=['ab','ae','ba','be','bo','oe','Eva','abo','ave','avo','boa','oba','obe','ova','voe']
    anagrams_blood=['bo','do','lo','od','bod','boo','dol','lob','loo','old','bold','bolo','lobo','obol']
    anagrams_class=['AC','al','as','ca','la','ACS','Sal','als','ass','cal','lac','las','sac','sal','lacs','lass','sacs','sals']
    anagrams_entry=['en','er','et','ne','re','ye','yr','ern','net','ret','rye','ten','try','tye','yen','yet','rent','tern','trey','tyer','tyne','tyre']
    random_word=random.choice(Level_2)
    print(f"\nYour word is {random_word}.\n")
    return random_word

def anagrams_3():
    Level_3=["animal","beauty","client","design"]
    anagrams_animal=['am','an','in','la','ma','ail','aim','ain','lam','lin','man','mil','min','nam','nil','nim','mali','mila','alma','anal',
    'anil','lain','lama','lima','mail','main','mana','mina','nail','milan','liman','mania','almain','manila']
    anagrams_beauty=['at','be','by','bat','bay','bet','bey','but','buy','bye','eat','tab','tea','tye','uta','yea','yet','abet','abye','bate',
    'beat','beau','beta','bute','byte','eBay','tube','beaut','tubae']
    anagrams_client=['in','it','etc','ice','let','lie','lin','lit','net','nil','nit','tel','ten','tic','tie','til','tin','neil','nile','ceil',
    'celt','cent','cine','cite','lent','lice','line','lint','lite','nice','nite','tile','tine','clint','intel','cline','elint','inlet','telic',
    'lectin','lentic']
    anagrams_design=['in','is','den','die','dig','din','end','ged','gen','gid','gie','gin','sen','sin','dens','dies','digs','dine','ding','dins',
    'ends','geds','gens','gies','gins','nide','send','side','sign','sine','sing','sned','Denis','deign','dines','dinge','dings','nides','segni',
    'sengi','singe','snide','dinges','signed','singed','deigns']
    random_word=random.choice(Level_3)
    print(f"\nYour word is {random_word}.\n")

print("WELCOME TO THE ANAGRAM GAME")
possible_levels=1,2,3
userInput()
anagrams_1()
