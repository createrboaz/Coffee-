mystr=("write anything Before we dive into paragraph structure, let’s start with paragraph meaning. A paragraph is an individual segment of writing that discusses a central idea, typically with more than one sentence. It even has its own paragraph symbol in copyediting, called the pilcrow ")
mystr1=""
for i in mystr:
    if ord(i)>=97 and ord(i)<123:
        mystr1+=chr(ord(i)-32)
    else:
        mystr1+=i
print("mt string is upper/lower :",mystr1)






