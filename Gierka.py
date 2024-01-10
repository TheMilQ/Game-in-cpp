import random
import sys

print('''
*******************************************************************************
___|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_
|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|____
___|_____|_____|_____|_____|___██████████____|_____|_____|_____|_____|_____|_
|_____|_____|_____|_____|____██████████████|_____|_____|_____|_____|_____|____
___|_____|_____|_____|_____██████████████████|_____|_____|_____|_____|_____|_
|_____|_____|_____|_____|__██████████████████___|_____|_____|_____|_____|____
___|_____|_____|_____|_____██████████████████|_____|_____|_____|_____|_____|_
|_____|_____|_____|_____|__██████████████████___|_____|_____|_____|_____|____
___|_____|_____|_____|_____██████████████████|_____|_____|_____|_____|_____|_
/______/______/______/______/______/______/______/______/______/______/_____ /
___/______/______/______/______/______/______/______/______/______/_____ /____
/______/______/______/______/______/______/______/______/______/______/_____ /
___/______/______/______/______/______/______/______/______/______/_____ /____
*******************************************************************************
''')
print("Welcome to Treasure Dungeon.")
print("Your mission is to find the treasure.")

class player:
    nick=input('What is your nickname?\n')
    weapon=input('What is your weapon?\n')
p1=player
def sceleton():
    choice=input("""You are being chased by sceleton.
Do you want to:
(press 1) Fight back or (press 2) Run?\n""")
    if choice=="1":
      potential_ending1=random.randint(1,5)
      if potential_ending1==1:
        print('''You were not capable of beating the sceleton u are dead.
                                       :::!~!!!!!:.
                                  .xUHWH!! !!?M88WHX:.
                                 .X*#M@$!!  !X!M$$$$$$WWx:.
                                 :!!!!!!?H! :!$!$$$$$$$$$$8X:
                                !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
                               :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
                               ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
                                 !:~~~ .:!M"T#$$$$WX??#MRRMMM!
                                  ~?WuxiW*`   `"#$$$$8!!!!??!!!
                                :X- M$$$$       `"T#$T~!8$WUXU~
                              :%`  ~#$$$m:        ~!~ ?$$$$$$
                            :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
                  .....   -~~:<` !    ~?T#$$@@W@*?$$      /`
                  W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
                  #"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
                  :::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
                  .~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
                  Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
                  $R@i.~~ !     :   ~$$$$$B$$en:``
                  ?MXT@Wx.~    :     ~"##*$$$$M~''' )
        input("You lost:(.")
        sys.exit(19999999999999999999999999)
      else:
        print(f"""Fortunately you managed to beat him with your {p1.weapon}!
        Good Job {p1.nick}!!!""")
    else:
      potential_ending1=random.randint(1,5)
      if potential_ending1==1:
        print(f'''You were not capable of running away from the sceleton u are dead {p1.nick}.
                                       :::!~!!!!!:.
                                  .xUHWH!! !!?M88WHX:.
                                 .X*#M@$!!  !X!M$$$$$$WWx:.
                                 :!!!!!!?H! :!$!$$$$$$$$$$8X:
                                !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
                               :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
                               ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
                                 !:~~~ .:!M"T#$$$$WX??#MRRMMM!
                                  ~?WuxiW*`   `"#$$$$8!!!!??!!!
                                :X- M$$$$       `"T#$T~!8$WUXU~
                              :%`  ~#$$$m:        ~!~ ?$$$$$$
                            :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
                  .....   -~~:<` !    ~?T#$$@@W@*?$$      /`
                  W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
                  #"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
                  :::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
                  .~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
                  Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
                  $R@i.~~ !     :   ~$$$$$B$$en:``
                  ?MXT@Wx.~    :     ~"##*$$$$M~''' )
        input("You lost:(.")
        sys.exit(19999999999999999999999999)
      else:
        print(f"""Fortunately you managed to run away from him!
        Good Job {p1.nick}!!!""")

def lake():
    choice=input('''\
                             \  O
                      \_______\/ )_________/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    You are now standing in front of underground lake.
    Do you want to:
    (press 1) Swim across (press 2) Ask stranger if he would transport you on his boat.\n''')
    if choice=="1":
      potential_ending1=random.randint(1,5)
      if potential_ending1==1:
        print(f'''Unfortunately you drowned yourself because
your leg got caught on a tree root. You are dead {p1.nick}.
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⣄⠙⠿⠿⠋⣠⣾⠟⢉⠀⠈⠙⢿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡈⠛⠛⢁⣼⣿⣿⣿⠀⢿⣷⣴⠆⢸⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⠋⣉⡉⢻⣷⡄⢉⣀⡤⠀⠙⢿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠿⣿⣿⠀⠻⠟⢸⣿⠀⣾⣿⣄⠀⠀⢸⣿⣿⣿⡇
        ⣿⣿⣿⣿⣿⣿⣿⣿⡏⢠⣶⠀⠀⠈⢿⣷⣶⣶⣿⠟⢀⡉⠻⠿⠛⢁⣾⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣇⠘⢿⣿⠟⠀⠈⠉⠙⠻⣿⡀⠻⠟⢀⣶⣾⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⠀⢀⡀⠀⠀⢀⠀⠘⣿⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⡇
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠐⠿⠏⠀⠀⠻⠟⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣀⣤⣤⣀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠚⠉⠉⠉⠙⠃⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠉⠁⠀⠀⠀⠀⠀⠀⠉⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿''')
        input("You lost:(.")
        sys.exit(19999999999999999999999999)
      else:
        print(f'''You managed to swim across the entire lake! Good Job {p1.nick}!!!''')

    else:
      potential_ending1=random.randint(1,5)
      if potential_ending1==1:
        print(f'''It turned out that this stranger was a grim reaper who consumed your soul. You are dead {p1.nick}.
                                       :::!~!!!!!:.
                                  .xUHWH!! !!?M88WHX:.
                                 .X*#M@$!!  !X!M$$$$$$WWx:.
                                 :!!!!!!?H! :!$!$$$$$$$$$$8X:
                                !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
                               :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
                               ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
                                 !:~~~ .:!M"T#$$$$WX??#MRRMMM!
                                  ~?WuxiW*`   `"#$$$$8!!!!??!!!
                                :X- M$$$$       `"T#$T~!8$WUXU~
                              :%`  ~#$$$m:        ~!~ ?$$$$$$
                            :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
                  .....   -~~:<` !    ~?T#$$@@W@*?$$      /`
                  W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
                  #"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
                  :::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
                  .~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
                  Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
                  $R@i.~~ !     :   ~$$$$$B$$en:``
                  ?MXT@Wx.~    :     ~"##*$$$$M~''' )
        input("You lost:(.")
        sys.exit(19999999999999999999999999)
      else:
        print('The stranger transported you across the lake.')

def rat():
    choice=input('''You see small rat in the corner of the room.
    Do you want to:
    (press 1) Take him with you (press 2) Kill and eat him?\n''')
    if choice=="1":
      potential_ending1=random.randint(1,5)
      if potential_ending1==1:
        print(f"""When u were not watching the rat attacked you and he bit your carotid artery and you bled out. You are dead {p1.nick}.
                                            ____-----__
                                        .--'           `\
                                      .'                 `.
                                    .'                     \
                      _______     .'                        `.
             ____,---'   ~~~<.---'                            \
           _C~           `--'                                  \
  __--x_x-'  .~      `---'                                      `
 | /         \'                                                  |
  \|                                                             |
   \   \  ,                                             __       `,
    `~~ ~~ --__                                       .'  \       |
      `` \_                                          '     |      |
           `-._                                     /       `    /
               `-.___/--.              /           /         |  /
                         `~~--__       \          /          | <
                        __>     `,     >         |          /   \
                    .--'         /   ,'`---.___ .'           /   `.
                  .'    ___.---'/   /           |           /      `.___
                .'   .~~    .--'   /             \_      __/ \          `.
                |'/\|      /,   __,'               `----'     `.__        `,
                \'         `/._/                   //.<          `---..'   |
                            `'                     VV V        __..--'    .'
                                                             .'         .'
                                                           .'   .------'
                                                          |  .'
                                                   ______.'   |
                                                 .'         .'
                                   __====_`-----'  .-------'
                                          `-------' """)
        input("You lost:(.")
        sys.exit(19999999999999999999999999)
      else:
        print('Rat named "Grato" happily join you! Now u have a comrade!')
    else:
      potential_ending1=random.randint(1,5)
      if potential_ending1>1:
        print(f"""The rat was very sick and eating him poisoned you. You are dead {p1.nick}.
              NO!                          MNO!
     MNO!!                          MNNOO!
   MMNO!                           MNNOO!!
 MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!!
 !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO!
       ! MMMMMMMMMMMMMPPPPOOOOIII! !
        MMMMMMMMMMMMPPPPPOOOOOOII!!
        MMMMMOOOOOOPPPPPPPPOOOOMII!
        MMMMM..    OPPMMP    .,OMI!
        MMMM::   o.,OPMP,.o   ::I!!
          NNM:::.,,OOPM!P,.::::!!
         MMNNNNNOOOOPMO!!IIPPO!!O!
         MMMMMNNNNOO:!!:!!IPPPPOO!
          MMMMMNNOOMMNNIIIPPPOO!!
             MMMONNMMNNNIIIOO!
           MN MOMMMNNNIIIIIO! OO
          MNO! IiiiiiiiiiiiI OOOO
     NNN.MNO!   O!!!!!!!!!O   OONO NO!
    MNNNNNO!    OOOOOOOOOOO    MMNNON!
      MNNNNO!    PPPPPPPPP    MMNON!
         OO!                   ON!""")

        input("You lost:(.")
        sys.exit(19999999999999999999999999)
      else:
        print('You ate him and u are feeling completly fine but that was not cool dude!')

def woman():
    choice=input( f"""
                                              _..
                                          .qd$$$$bp.
                                        .q$$$$$$$$$$m.
                                       .$$$$$$$$$$$$$$
                                     .q$$$$$$$$$$$$$$$$
                                    .$$$$$$$$$$$$P\$$$$;
                                  .q$$$$$$$$$P^"_.`;$$$$
                                 q$$$$$$$P;\   ,  /$$$$P
                               .$$$P^::Y$/`  _  .:.$$$/
                              .P.:..    \ `._.-:.. \$P
                              $':.  __.. :   :..    :'
                             /:_..::.   `. .:.    .'|
                           _::..          T:..   /  :
                        .::..             J:..  :  :
                     .::..          7:..   F:.. :  ;
                 _.::..             |:..   J:.. `./
            _..:::..               /J:..    F:.  :
          .::::..                .T  \:..   J:.  /
         /:::...               .' `.  \:..   F_o'
        .:::...              .'     \  \:..  J ;
        ::::...           .-'`.    _.`._\:..  \'
        ':::...         .'  `._7.-'_.-  `\:.   \
            `-:/"-7.--''            _::.-'P::..    \
 _....------''''''            _..--".-'   \::..     `.
(::..              _...----'''  _.-'       `---:..    `-.
 \::..      _.-''''   `''''---''                `::...___)
  `\:._.-'''                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    You see a beutiful woman that calls your name.
    -{p1.nick}! Come to me!
    Do you want to:
    (press 1) Come to her or (press 2) Run?\n""")
    if choice=="1":
      potential_ending1=random.randint(1,5)
      if potential_ending1>1:
        print(f"""She was bloodthirsty vampire and she sucked all your blood. You are dead {p1.nick}.

                   .d:....:h.
                .:!!!!!!!!!!!!:.
           .::!!!!!!!!!!!!!!!!!!!!::.
    ..::!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!::..
..``.. . eeee .... ... '~' ... .... eeee . ..'..
 `!h:. $ $$$$ $$$$ $$$$b d$$$$ $$$$ $$$$ $ .:h!'
  `!!!!. `$$$ '$$' '$$$' `$$$` '$$' $$$'.!!!!!'
    `!!!!.`$$ .   .  ......   .   . $$'.!!!!'
     `!!!! $$ !!!!!!!!!!!!!!!!!!!!! $$ !!!!'
       `!!h ` !!!!!!!!!!!!!!!!!!!!! ' d!!'
         `!h !!!!!!!!!!!!!!!!!!!!!!! d!'
          ``!!!!!!!!!!!!!!!!!!!!!!!!''
             ``!!!!!!!!!!!!!!!!!!''
                 ```!!!!!!!!'``` """)
        input("You lost:(.")
        sys.exit(19999999999999999999999999)
      else:
        print(f"""The woman gave you a kiss and show you which path should you take. Nice rizz {p1.nick}!!!""")

    else:
      potential_ending1=random.randint(1,5)
      if potential_ending1==1:
        print(f"""You were not capable of running away from her because she was a vampire. You are dead {p1.nick}.
                    .d:....:h.
                .:!!!!!!!!!!!!:.
           .::!!!!!!!!!!!!!!!!!!!!::.
    ..::!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!::..
..``.. . eeee .... ... '~' ... .... eeee . ..'..
 `!h:. $ $$$$ $$$$ $$$$b d$$$$ $$$$ $$$$ $ .:h!'
  `!!!!. `$$$ '$$' '$$$' `$$$` '$$' $$$'.!!!!!'
    `!!!!.`$$ .   .  ......   .   . $$'.!!!!'
     `!!!! $$ !!!!!!!!!!!!!!!!!!!!! $$ !!!!'
       `!!h ` !!!!!!!!!!!!!!!!!!!!! ' d!!'
         `!h !!!!!!!!!!!!!!!!!!!!!!! d!'
          ``!!!!!!!!!!!!!!!!!!!!!!!!''
             ``!!!!!!!!!!!!!!!!!!''
                 ```!!!!!!!!'``` """ )
        input("You lost:(.")
        sys.exit(19999999999999999999999999)
      else:
        print(f"""Fortunately you managed to run away from her!
        Good Job {p1.nick}!!!""")

def bartender():
    choice=input('''
                                        _______________________________________
                                   |,--------------_----------------------.|
                                   ||______ __,---'_ |         ||--.   || ||
                                   ||__,--'| _,---' ||         ||   )  || ||
           ______________________  ||__,-: ||       ||         ||--' * || ||
     __,--'                __,--'| ||;-. : ||      __:         || .    || ||
 ,-_'__________________,--'__,-: | ||/ '>: ||    ,%%%%%.       ||   )) || ||
 |'.      .   ______ ,'| -',--.: | ||):' : ||   |%%" o \       ||   (  ||*||
 ||.'.    .  /,----,',|| :<' \/: | || )) : ||   \%|o 7 |       ||__|"|_||_||
 || ||    . //   ,',' || : `;( : | ||'/  : ||    \%`..'(____   ||""|_|"||"||
 || ||    .||    ||   || : (( `: __  :: ,mMMm.    %%,  " )  `. ||__"""_||_||
 || ||    .||:   ||   || :  \` ,%%%%%. |MMMMMm     / `--' _)  \`----------||
 || ||    .||:   ||   || :  ;; %%%%%%%.-"MMMM/    |  | _)   |\ \      =o.,||
 || ||    .||:   ||   || : __,  \%_%%_|   `",      \ \_,_ _,\| |        |o||
 || ||    .||:   ||   || ''      /     `-._/        `._\_)______________|_||
 || ||    .||:   ||   ||        ;          `-.  ____:|_________________)_(||
 || ||    .||::  ||   ||       /  ,           \  ------------___ ----------'
 || ||    .||::  ||   ||      |  <;     `.     \ ___________ ) ( ___________
 || ||    .||::  ||   ||    _ `._/;         /  |            (___)      __,--|
 || (|    .||::: ||)  ||_-'______ ;._       |  ; __________________,--'     |
 || ||    .||::: ||   ||`.______, |._`--...-|,' ______,'|`.______,'|        |
 || ||    .||::: ||   || |      | |  `--...-|: |      | | |      | |        |
 || ||    .||::::||   || | :    | ;         || |:     |o|o|:     | |        |
 || ||    ._\\:::||   || |  ::  | |     :   || |::    | | |:::   | |        |
 || ||_,-'   \\__||   || |___::_| :         || |______| | |__::__| |   __,--'
 |'.||________`-_||  ,'|,_______`_|         ||,_______`_|,'______`_|--'
  `. |           ||,','           |  .      :
____`|  ________ |_,'___________  ;      :  |  ______________________________
.*,--.*,--.*,--.*,--.*,--.*,--.* ;__;    :   \ ,--.*,--.*,--.*,--.*,--.*,--.*
'`--'' `--' `--' `--' `--' `--' `  |`'---..__; `--' `--' `--' `--' `--' `--'
,--.*,--.*,--.*,--.*,--.*,--.*,--. '--'  '--' --.*,--.*,--.*,--.*,--.*,--.*,-

    You are now standing in front of weird shop.
    The peddler propose you some potion.
    Do you want to:
    (press 1) Drink it (press 2) Propose that u will drink it after he drinks it first.\n''')
    if choice=="1":
      potential_ending1=random.randint(1,5)
      if potential_ending1==1:
        print(f'''Unfortunately the potion was poison. You are dead {p1.nick}.

      _________
     `._______,'
      (_______)
      <       >
       )     (
      /`  - .\
     /        \
    / _       _\
   :,'   `-.'  `:
   |            |
   :            ;
    \          /
     `.______.' ''')
        input("You lost:(.")
        sys.exit(19999999999999999999999999)
      else:
        print(f'''The poison gave you additional vital forces! You are now super strong and super fast and u are able to see in dark {p1.nick}!!!''')

    else:
      potential_ending1=random.randint(1,5)
      if potential_ending1==1:
        print(f'''The peddler did not died from it because he was already dead but you did. You are dead {p1.nick}.
      _________
     `._______,'
      (_______)
      <       >
       )     (
      /`  - .\
     /        \
    / _       _\
   :,'   `-.'  `:
   |            |
   :            ;
    \          /
     `.______.''' )
        input("You lost:(.")
        sys.exit(19999999999999999999999999)
      else:
        print('The peddler droped in front of you. You decided to dont drink it and went away')

def priest():
    choice=input("""


                  .^.
                .'| |`.
               /__| |__\
              /___ + ___\
              |   | |   |
              | __|_|__ |               .---.
              |/'_'''_'\|             .' .-. `.
             /(( ^ | ^ ))\           / ,',-.) |
            (())  _|_  ((()         / / | '' .'
           ((((`-' - `-'))))       / /   `--'
          ((()))\((())))(()))     / /
        .'.`)('\()))(((/.`)' `.  / /
      .'. . . .|))())((|. . . .`/ /
     /. . . . .| \)))( | . . . / x
    /. . . . . | |())) |. . . / /.\
   /. . . . . .| || || | . . / /. .\
   |___________| |\ || |____/ /_____\
   |_____________|| ||_____/ /_______)
    !!!!!!!!!!!!!!| |!!!!!/ /!!!!!!!!!
    |         |:I / \ I::/ //      -'``---.'|__
    |`.    -._|:I | | I:/ /:I\      -'   /     `-.
     \      _.'\I | / I/ /::I `.        /,-------'
      \    '    \ \ | / /:::I   `-._    \    |
      |\        _\| |/ /::::I    /  `-.  \  /
      \ \      /  `,/_/_::::I  .'|     `-.\/
      /`.\     |.       |:::I    |
      |   `.   |I`-.___/::::I    /
      |   I:`. |I/ /| I:::::I  .'\
      \   I:::`\/ / | I:::::I    |
      |   I::I:/ /| \ I::I::I    |
      |   I:=I/ / | | I:=I=:I    \
      \   I::/ /I \ | I::I::I    /
      /`. I:/ /:I | | I:::::I    |
      \   I/ /III | \ IIIIIII .-'\
      |   / /     / |            |
      |.'/ /   .-'| \          `.)
      | / /       | |            |
     / / /        | |`-.         \
     |/ /        _/ |          `-.|
    // /__________| |_____________\
    / /SSSSSSSSSSS| |SSSSSSSSSSSSS|
   / /____________/  \____________|
  / /   .'     :       `.   _     \
 / / -._     .----.       '  `--.  `.
/ /          ____     ___._.'"--.__  `.
`'  `--.__.-|   |`---'   \__    \__`--'
hjw         \ ^ /           `-.___/
             \_/
    You went into the temple. The priest greets you but sudenly he wants to kill you as a sacrifice
    Do you want to:
    (press 1) Kill him and escape (press 2) Run?\n""")
    if choice=="1":
      potential_ending1=random.randint(1,5)
      if potential_ending1==1:
        print(f"""Priest used his powers to defeat you. You are dead {p1.nick}.
               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#                |
   ::::::`:::::;'         `#                .
   ::::::`:::::;'         `#
   ::::::`:::::;'         `#                0
""")
        input("You lost:(.")
        sys.exit(19999999999999999999999999)
      else:
        print('''You menaged to beat him with your {p1.weapon} and escaped safely! Fortunately!''')
    else:
      potential_ending1=random.randint(1,5)
      if potential_ending1==1:
        print(f"""He managed to catch up with you. You are dead {p1.nick}.
               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#                |
   ::::::`:::::;'         `#                .
   ::::::`:::::;'         `#
   ::::::`:::::;'         `#                0""")

        input("You lost:(.")
        sys.exit(19999999999999999999999999)
      else:
        print('You escaped!')


chamber=[sceleton,lake,rat,woman,bartender,priest]

path=input("""You came across 2 paths.
Which path you want to choose?
First (press 1) is wet and slipery
Second (press 2) looks pretty normal.\n""")
for random_variable in range(3):
    if path=="1":
        random_chamber=random.randint(1,3)
        if random_chamber==1:
            chamber[0]()
        elif random_chamber==2:
            chamber[1]()
        else:
            chamber[2]()
    else:
        random_chamber=random.randint(1,3)
        if random_chamber==1:
            chamber[3]()
        elif random_chamber==2:
            chamber[4]()
        else:
            chamber[5]()
for random_variable in range(3):
    if path=="2":
        random_chamber=random.randint(1,3)
        if random_chamber==1:
            chamber[0]()
        elif random_chamber==2:
            chamber[1]()
        else:
            chamber[2]()
    else:
        random_chamber=random.randint(1,3)
        if random_chamber==1:
            chamber[3]()
        elif random_chamber==2:
            chamber[4]()
        else:
            chamber[5]()

print(f'''CONGRATULATIONS {p1.nick}!!!
You managed to find the treasure.
|                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /''')