import os

print("pipeline started")
os.system("python scr/extract.py")
os.system("python scr/load.py")
os.system("python scr/transform.py")
print("pipeline finished")
