import string

my_string = (input("Input Target : "))
mylist = my_string.split("/")

peer = (mylist[3])
msg_id = int(mylist[4])

print ("\n" + "Original String : " +my_string)
print ("Target : " +peer)
print ("Messages ID : " +str(msg_id) +"\n")

