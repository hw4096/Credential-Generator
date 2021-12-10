import time 
import random



print("This is a username generator. I will ask you a few questions, then generate a username based upon your answers. Good Luck!")
firstname = input("\nFirst question. What is your first name?\n\n")
petname1 = input("\nSecond question. Give me one of your pet's names.\n\n")
favnumberstr = str(input("\nThird question. What is your favorite number?\n\n"))
favmonth = input("\nFourth question. What is your favorite month? \n\n")
favhr = input("\nFifth and last question. What is your favorite hour of the day? (1-12)\n\n")
favmonth_3 = favmonth[0:3]
firstname_3 = firstname[0:4]
favoptions = [firstname, petname1, favnumberstr,favmonth,favhr]
random.shuffle(favoptions)
username1 = favoptions[0] + favoptions[3] + favoptions[1]
username2 = favoptions[3] + favoptions[4] + favoptions[0]
username3 = favoptions[1] + favoptions[2] + favoptions[4]
print("\nThank you. Mixing results.....\n")
time.sleep(3)
print("\nWhich username do you like the most?")
favusername = input("\n" + username1 + "," + username2 + ", or " + username3 + "?\n\n")
print("\n" + favusername + " it is then!" + "\n")
time.sleep(1)
print("_____________________________________________________________________________\n")
print("Next, we can create you a password to go along with the username!\n")
time.sleep(0.5)
xlist = ["!", "@", "#"]
random.shuffle(xlist)
password1 = favoptions[4] + favoptions[3] + favoptions[2] + xlist[0]
password2 = favoptions[1] + xlist[1] + favoptions[3]
password3 = xlist[2] + favoptions[2] + favoptions[0]
time.sleep(1)
print("Which password do you like the most?")
favpassword = input("\n" + password1 + "," + password2 + ", or " + password3 + "?\n\n")
print("\nCreating results....\n")
time.sleep(2)
print("Username: " + favusername + "\n" + "Password: " + favpassword)
