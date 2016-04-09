import os, time, shutil
def main():
    print('Lets begin')     
    time.sleep(0.3)
    os.system('clear')
    pokemon_logo()
    time.sleep(0.2)
    flag = "false flag"
    while(flag != ""):
        print("       This is strictly for educational purposes.  Please don't sue us.")
        flag = input("                    Press Enter to Start")
    clear = os.system('clear')
    clear
    flag = "false flag"
    while(flag != ""):
        flag = input("New Game?")
        clear
    clear
    print("Hello there welcome to the world of POKEMON! My name is BEN! People call me the PYTHON PROF!")
    input("")
    clear
    nidorino_ascii()
    print("This world is inhabited by creatures called POKEMON! For some people, POKEMON are pets.  Others use them for fights.  Myself... I just study PYTHON as a profession")
    input("")
    os.system('clear')
    gender = input("Are you a boy or a girl? ").upper()
    os.system('clear')
    gender = check_gender(gender)
    name = input("First what is your name?")
    print("Right! So your name is "+name)
    os.system('clear')
    print("This is my grandson.")
    rival_name = input("Eh what is his name again?")

def check_gender(gender):
    if(gender=="BOY"):
        return "Boy"
    elif(gender=="GIRL"):
        return "Girl"
    while(gender != "BOY" or gender != "GIRL"):
        gender = input("Are you a Boy or a Girl? ")
        gender = gender.upper()
        if(gender=="BOY"):
            return "Boy"
        elif(gender=="GIRL"):
            return "Girl"
def ask():
    ask = input("Do you want to play Pokemon? (Yes/No) : ")
    ask=ask.upper()
    if(ask=="YES"):
        return True
    elif(ask=="NO"):
        return False
    while(ask!="YES" or ask!="NO"):
        ask = input("Do you want to play Pokemon? (Yes/No) : ")
        ask=ask.upper()
        if(ask=="YES" or ask=="Y"):
            return True
        elif(ask=="NO"):
            return False
        
def pokemon_logo():
    columns = shutil.get_terminal_size().columns	
    print(('                        .::.\n'+
"                             .;:**'            AMC\n"+
"                              `                  0\n"+
"  .:XHHHHk.              db.   .;;.     dH  MX   0\n"+
"oMMMMMMMMMMM       ~MM  dMMP :MMMMMR   MMM  MR      ~MRMN\n"+
"QMMMMMb  "+"MMX       MMMMMMP !MX' :M~   MMM MMM  .oo. XMMM 'MMM\n"+
"  `MMMM.  )M> :X!Hk. MMMM   XMM.o\"  .  MMMMMMM X?XMMM MMM>!MMP\n"+
"   'MMMb.dM! XM M'?M MMMMMX.`MMMMMMMM~ MM MMM XM `\" MX MMXXMM\n"+
"    ~MMMMM~ XMM. .XM XM`\"MMMb.~*?**~ .MMX M t MMbooMM XMMMMMP\n"+
"     ?MMM>  YMMMMMM! MM   `?MMRb.    `\"\"\"   !L\"MMMMM XM IMMM\n"+
"      MMMX   \"MMMM\"  MM       ~%:           !Mh.\"\"\" dMI IMMP\n"+
"      'MMM.                                             IMX\n"+
"       ~M!M                                             IMP\n").center(columns))

def nidorino_ascii():
	f = open('nidorino.txt', 'r')
	file_contents = f.read()
	print(file_contents)
	f.close()
def start():
    if(ask()==True):
        os.system('clear')
        time.sleep(0.5)
        for i in range(3):
            time.sleep(0.3)
            print('.', end="",flush=True)
        main()
start()
