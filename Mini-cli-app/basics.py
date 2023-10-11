from argparse import ArgumentParser, Namespace


argparser = ArgumentParser() 

argparser.usage = " To serve food to bots and humans! "
argparser.add_argument("isHuman", help= "Are you human (0 for No,  1 for Yes.)", type=int, choices = [0,1])
argparser.add_argument("-mt", "--menu_type", help= "Select a menu ", type=str, choices = ["color", "grey"])


a: Namespace = argparser.parse_args()


if a.isHuman==True:
    if a.menu_type:
        printstr = f" Hello Human!\n You will be served food according to the {a.menu_type} menu"
    else:
        printstr = f" Hello Human!"
    print(printstr)

else:
    if a.menu_type:
        printstr = f" Hello bot!\n You will be served food according to the {a.menu_type} menu"
    else:
        printstr = f" Hello bot!"
    print(printstr)



