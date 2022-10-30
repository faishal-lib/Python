def packet1():
    print ("Anda memilih Packet 1")

def packet2():
    print ("Anda memilih Packet 2")

select = int(input("Choose Number : "))

if select == 1 :
    packet1()

elif select == 2 :
    packet2()

else :
    print ("Error Input") 