from function_list import *

print ("\n")
print ("===== SELECT PACKET =====")
print ("1. Packet 1" + "\n" + "2. Packet 2")
print ("\n")
select = int(input("Choose Number : "))

if select == 1 :
    packet1()

elif select == 2 :
    packet2()

else :
    print ("Error Input ...") 