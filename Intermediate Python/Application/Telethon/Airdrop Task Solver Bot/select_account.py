from function_list import *

print ("\n")
print ("===== SERVICE =====")
print ("1. GoSpace Airdrop" + "\n" + "2. Astra Protocol")
print ("\n")
select = int(input("Choose Number : "))

print ("\n")
print ("Press CTRL + C to abort ...")

if select == 1 :
    packet1()

elif select == 2 :
    packet2()

else :
    print ("Error Input ..") 