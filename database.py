'''
Relational Database software thingy because exo told me to
this will be utter shit due to the 30 minute time constraint
'''

#im not even do oop for this shit ill just put it in methods
def __main__():
    tablename = None
    cont = True
    while cont:
        x = input("> ")
        if x == "+": #create new table
            tablename = input("Please enter new table name> ")
            table = open(tablename + ".db", "x")
            n = int(input("enter a number of attributes per row> "))
            table.write(str(n) + " ") #write the number of attributes per row
            table.close()
        if x == "L": #load table
            tablename = input("Please select table name> ")
        if x == "++": #add row
            readtable = open(tablename + ".db", "r")
            writetable = open(tablename + ".db", "a")
            n = int(readtable.read().split(" ")[0]) #get the number of attributes per row
            for i in range(n):
                inp = input("enter value for attribute " + str(i+1) + "> ")
                writetable.write(inp + " ")
            readtable.close()
            writetable.close()
        if x == "-": #delete row
            readtable = open(tablename + ".db", "r")
            data = readtable.read().split(" ")
            print(data)
            n = int(data[0])
            rest = data[1:]
            num_rows = int(len(rest)/n)
            idx = int(input("enter index of row to be deleted> "))
            writetable = open(tablename + ".db", "w")
            writetable.write(str(n) + " ")
            k = 0
            for i in range(num_rows):
                if (i + 1) != idx:
                    for j in range(n):
                        writetable.write(rest[k] + " ")
                        k = k + 1
                else:
                    k = k + n
            readtable.close()
            writetable.close()
        if x == "/": #modify row
            readtable = open(tablename + ".db", "r")
            data = readtable.read().split(" ")
            print(data)
            n = int(data[0])
            rest = data[1:]
            num_rows = int(len(rest)/n)
            idx = int(input("enter index of row to be modified> "))
            writetable = open(tablename + ".db", "w")
            writetable.write(str(n) + " ")
            k = 0
            for i in range(num_rows):
                if (i + 1) != idx:
                 for j in range(n):
                    writetable.write(rest[k] + " ")
                    k = k + 1
                else:
                    for j in range(n):
                        inp = input("enter new value for attribute " + str(j+1) + "> ")
                        writetable.write(inp + " ")
                    k = k + n
            readtable.close()
            writetable.close()
        if x == "p": #print table
            readtable = open(tablename + ".db", "r")
            data = readtable.read().split(" ")
            n = int(data[0])
            rest = data[1:]
            num_rows = int(len(rest)/n)
            k = 0
            for i in range(num_rows):
                print("row " + str(i+1) + ":", end=" ")
                for j in range(n):
                    print(rest[k], end=" ")
                    k = k + 1
                print("")
            readtable.close()
        if x == "x":
            cont = False

if __name__ == '__main__':
    __main__()