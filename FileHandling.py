n = 50
def add(num,marks):
    f = open("TheRegister.txt", "a")
    f.write(num + " " + marks +"\n")
    f.close()

def delete(num):
    f = open("TheRegister.txt", "r")
    txt = f.read()
    f.close()
    lines = txt.split('\n')
    lines = lines[0:len(lines)-1]
    n=-1
    for i in lines:
        n+=1
        i=i.split()
        if(i[0]==num):
            break
    del lines[n]
    txt=str("")
    for i in lines:
        txt+=i+"\n"
    f = open("TheRegister.txt", "w")
    f.write(txt)
    f.close()

def display():
    f = open("TheRegister.txt","r")
    txt = f.read()
    print(txt)

def update(num,marks):
    f = open("TheRegister.txt", "r")
    txt = f.read()
    f.close()
    lines = txt.split('\n')
    lines = lines[0:len(lines)-1]
    s = []
    for i in lines:
        j=i
        i=i.split()
        if(i[0]==num):
            s.append(num + " " +marks)
        else:
            s.append(j)
    txt=str("")
    for i in s:
        txt+=i+"\n"
    f = open("TheRegister.txt", "w")
    f.write(txt)
    f.close()

def calculate(num):
    f = open("TheRegister.txt","r")
    txt = f.read()
    f.close()
    lines = txt.split('\n')
    for i in lines:
        i=i.split()
        if(i[0]==num):
            avg = (int(i[1])+int(i[2])+int(i[3]))/3
            if(avg<50):
                print("Student has failed")
            else:
                print("Student has passed")
            break

while(True):
    print("\nThe following File Operations are available:")
    print("1. Add")
    print("2. Delete")
    print("3. Display")
    print("4. Update")
    print("5. Calculate")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        num = input("Registration number? ")
        marks = input("Add 3 subject marks: ")
        add(num, marks)
    elif (choice == 2):
        num = input("Enter Registration number to be deleted: ")
        delete(num)
    elif(choice == 3):
        display()
    elif(choice == 4):
        num = input("Enter registration number to be updated: ")
        marks = input("Enter  updated marks: ")
        update(num, marks)
    elif(choice == 5):
        num = input("Enter Registration to check: ")
        calculate(num)
    else:
        break
    


