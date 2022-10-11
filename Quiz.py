
#write a program Quiz

print("--------welcome To Quiz Program---------")
ans={"what is sum of value 10+5?":"A=12,B=15,C=20,D=1",
     "who is current pm":"A=gandhi,B=stalin,C=subash,D=modi",
     "vikram movie director is ?":"A=sankar,B=Nelson,"
                                  "C=lokesh,D=manirathinam",
    "what is full form of who?":"A=world war,B=wealth organ,"
                                "C=world health organization,D=where are you",
     "who is cuurent tamilnadu cm?":"A=stalin,B=ops,C=eps,D=semman"}
line=list(ans.keys())
next=list(ans.values())
score=0
print("Answer a First Question:\n",line[0].upper())
print("Options:\n",next[0])
Answer=input("Enter a option:")
if Answer.upper()=="B":
    print("Correct\n",next[0][5:9])
    score+=1
else:
    print("Incorrect")
print("------------------")
print("Answer a Second Question:\n", line[1].upper())
print("Options:\n", next[1])
Answer = input("Enter a option:")
if Answer.upper() == "D":
    print("Correct\n",next[1][27:33])
    score += 1
else:
    print("Incorrect")
print("---------------------")
print("Answer a third Question:\n", line[2].upper())
print("Options:\n", next[2])
Answer = input("Enter a option:")
if Answer.upper() == "C":
    print("Correct\n",next[2][17:26])
    score += 1
else:
    print("Incorrect")
print("-------------------")
print("Answer a four Question:\n", line[3].upper())
print("Options:\n", next[3])
Answer = input("Enter a option:")
if Answer.upper() == "C":
    print("Correct\n",next[3][27:54])
    score += 1
else:
    print("Incorrect")
print("-------------------")
print("Answer a five Question:\n", line[4].upper())
print("Options:\n", next[4])
Answer = input("Enter a option:")
if Answer.upper() == "A":
    print("Correct\n",next[4][0:9])
    score += 1
else:
    print("Incorrect")
print("-------------------")
print("Total score is",score,"out of Five Questions")
print("------------------------------")