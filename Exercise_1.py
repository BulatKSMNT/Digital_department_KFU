dictionary = {
    "+" : set(),
    "-" : set(),
    "*" : set(),
    "/" : set()

}
while(1):
    a = int(input("Enter the first number "))
    b = int(input("Enter the second number "))
    c = input("Enter type of operation (+ or - or * or /) ")

    if(c == "+"):
        print(f"\n{a}+{b}={a+b}")
        dictionary["+"].add(str(a)+"+"+str(b)+"="+str(a+b))
    elif(c == "-"):
        print(f"\n{a}-{b}={a-b}")
        dictionary["-"].add(str(a)+'-'+str(b)+'='+str(a-b))
    elif(c == '*'):
        print(f"\n{a}*{b}={a*b}")
        dictionary["*"].add(str(a)+"*"+str(b)+"="+str(a*b))
    elif(c=='/'):
        print(f"\n{a}/{b}={a/b}")
        dictionary["/"].add(str(a)+"/"+str(b)+"="+str(a/b))
    else:
        print("\nНеправильно введена тип операции")

    for key, value in dictionary.items():
        print(key + " " + (str(value) if value else "[]"))

