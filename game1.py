class Stone:

    def __init__(self,items):
        self.items=items


    def display(self):
        while(True):
            print("1-to play 5 chances")
            print("2-to play 10 chances")
            print("3-to play 20 chances")
            print("and press q for quite")
            choice2=input("entr your choice")
            if(choice2 not in ["1","2","3","q"]):
                print("enter a valid option")
            if(choice2=="1"):
                no=5
                harsh.choice3(no)
            elif(choice2=="2"):
                no=10
                harsh.choice3(no)
            elif (choice2 == "3"):
                no = 20
                harsh.choice3(no)
            elif(choice2=="q"):
                exit()


    def choice3(self,no):
        j=0
        your = 0
        computer = 0
        while(j<no):
            print("select any option")
            print("s for stone")
            print("p for paper")
            print("c for sizer")
            user=input("select any one")
            if(user not in ["s","p","c"]):
                print("selct a valid option")
            else:
                import random
                bot = random.choice(["s", "c", "p"])


                if (user == "s" and bot == "c"):
                    your = your + 1
                    print(
                        f"You win\n you choose {self.items.get(user)} an computer chose {self.items.get(bot)}.\nyour score is {your} nad computer's score is {computer}.")

                elif (user == "p" and bot == "s"):
                    your = your + 1
                    print(
                        f"You win \nyou choose {self.items.get(user)} and computer chose {self.items.get(bot)}.\nyour score is {your} nad computer's score is {computer}.")

                elif (user == "c" and bot == "s"):
                    your = your + 1
                    print(
                        f"You win \n you choose {self.items.get(user)} and computer chose {self.items.get(bot)}.\nyour score is {your} nad computer's score is {computer}.")

                elif (user == bot):

                    your=your+1
                    computer=computer+1
                    print(f"you both select same action\n computer allso select {self.items.get(bot)}\n your score {your} computer score {computer} ")

                else:
                    computer = computer + 1
                    print(
                        f"computer win\nYou choose {self.items.get(user)} and computer chose {self.items.get(bot)}.\nyour score is {your} nad computer's score is {computer}.")
                j=j+1
        if(computer<your):
            print(".....congratulations.....\nyou win.....!!!!")
        elif(computer>your):
            print("you lose>>>\nbetter luck next time")
        else:
            print("<<<<<<<<<match is draw>>>>>>>>")


harsh=Stone({"s":"stone","c":"sicer","p":"paper"})
harsh.display()
