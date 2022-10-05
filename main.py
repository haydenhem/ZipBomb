import shutil # for figuring out space needed to fill
import gc # clearing memory so ur pc doesn't die!

tb = 1099511627776
gb = 1073741824
mb = 1048576
kb = 1024
size = 0
yes = input("(KB/MB/GB/TB/FILL) ")
if yes.__contains__("k"):
    manykbs = input("How many KBS? ")
    size = int(manykbs) * kb
if yes.__contains__("m"):
    manymbs = input("How many MBS? ")
    size = int(manymbs) * mb
if yes.__contains__("g"):
    manygbs = input("How many GBS? ")
    size = int(manygbs) * gb
if yes.__contains__("t"):
    manytbs = input("How many TBS? ")
    size = int(manytbs) * tb
if yes.__contains__("fill"):
    manytbs = input("Are you sure you want to fill your drive? This will be generating "+str(shutil.disk_usage('/').free / gb) + " gigabytes. Type anything than press enter to continue.")
    size = shutil.disk_usage()
with open('boomed', 'wb') as f:
    print("Please wait whilst it fills.")
    f.seek(size) # One GB
    f.write(b'0')
gc.collect()
print('Done')
