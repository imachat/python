
# Write a program in python that tells if the name you supplied is in a list or the name is not in a list
x = str(input("enter candidates name:"))
contestants  = ["buhari", "atiku", "donald duke", "fela durotoye", "ike keke"]
if x in contestants:
   print("a candidate for 2019 presidential election")
else:
    print("i dont know dat man")
