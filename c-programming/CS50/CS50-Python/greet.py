# bal = 0
# print(bal)
# while True:
#     n = str(input("Greeting: "))
#     n.lower()
#     if n == "hello":
#         print("$",bal)
#     if n == "hey":
#         bal += 20
#         print("$",bal)
#     else:
#         for i in range(0,5):
#             if n[0] == "h" and n[1] != "e":
#                 print("$",bal)


n = str(input("Greeting: "))
n.lower()
# if n == "hello":
#     print("$0")
# if n == "hey":
#     print("$20")
# else:
for i in range(0,5):
    if n[0] == "h" and n[1] == "e" and n[2] == "l" and n[3] == "l" and n[4] == "o":
        print("$0")
        break
    if n[0] == "h" and n[1] == "e" and n[2] == "y":
        print("$20")
        break
    else:
        print("$100")
    break






