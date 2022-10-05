import shutil
path = "/"
def free(path):
    stat = str(shutil.disk_usage(path))
    yes = stat.split("free=",1)[1]
    return yes.replace(")","")
print("Bytes Free:",free(path))
FILENAME = "getboomed.txt"
SIZE = free(path)
okay = input("Are you ready to boom? Type anything to start!")
with open(FILENAME, "wb") as file:
    file.seek(SIZE - 1)
    file.write(b"\0")
