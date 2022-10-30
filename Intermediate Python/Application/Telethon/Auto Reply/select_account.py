from function_list import *

print ("\n")
print ("===== SERVICE =====")
print ("1. View Post" + "\n" + "2. Airdrop Bot")
print ("\n")
select = int(input("Choose Number : "))

if select == 1 :
    packet1()

elif select == 2 :
    packet2()

else :
    print ("Error Input ..") 