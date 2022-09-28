import sys

name = input('name? ')
gift=input('Choose one: frog, dolphin, elephant. ')
if gift in ('frog', 'Frog'):
        print("""           
           .--._.--.
          ( O     O )
          /   . .   \.
         .`._______.'.
        /(           )\.
      _/  \  \   /  /  \_
   .~   `  \  \ /  /  '   ~.
  {    -.   \  V  /   .-    }
_ _`.    \  |  |  |  /    .'_ _
>_       _} |  |  | {_       _<
 /. - ~ ,_-'  .^.  `-_, ~ - .\.
         '-'|/   \|`-` \n\
""")
        print(f'Goodbye, {name}')
        sys.exit()
if gift in('dolphin', 'Dolphin'):
        print("""                                      
                                       .--.
                _______             .-"  .'
        .---u"""       """"---._  ."    %
      .'                        "--.    %
 __.--'  o                          "".. "
(____.                                  ":
 `----.__                                 ".
         `----------__                     ".
               ".   . ""--.                 ".
                 ". ".     ""-.              ".
                   "-.)        ""-.           ".
                                   "".         ".
                                      "".       ".
                                         "".      ".
                                            "".    ".
                      ^~^~^~^~^~^~^~^~^~^~^~^~^"".  "^~^~^~^~^
                                            ^~^~^~^  ~^~
                                                 ^~^~^~ \n\
""")
        print(f'Goodbye, {name}')
        sys.exit()
if gift in("elephant, Elephant"):
        print("""
                            _
                          .' `'.__
                         /      \ `'"-,
        .-''''--...__..-/ .     |      \.
      .'               ; :'     '.  G   |
     /                 | :.       \     =\.
    ;                   \':.      /  ,-.__;.-;`
   /|     .              '--._   /-.7`._..-;`
  ; |       '                |`-'      \  =|
  |/\        .   -' /     /  ;         |  =/
  (( ;.       ,_  .:|     | /     /\   | =|
   ) / `\     | `""`;     / |    | /   / =/
     | ::|    |      \    \ \    \ `--' =/
    /  '/\    /       )    |/     `-...-`
   /    | |  `\    /-'    /;
   \  ,,/ |    \   D    .'  \.
    `""`   \  nnh  D_.-'L__nnh
            `""'\n\
""")    
        print(f'Goodbye, {name}')
        sys.exit()
elif gift != ('frog', 'elephant', 'dolphin'):
        print("""
       o                o
                  o
         o   ______      o
           _/  (   \_
 _       _/  (       \_  O
| \_   _/  (   (    0  \.
|== \_/  (   (           |
|=== _ (   (   (         |
|==_/ \_ (   (           |
|_/     \_ (   (     \__/
          \_ (       _/
            |  |____/
           /__/
         \n\
""")
        print(f"You didn't choose a gift, so we chose one for you. Goodbye, {name}.")