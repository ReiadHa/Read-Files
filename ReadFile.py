import time
file = open('C:/Users/redah/OneDrive - Da Vinci College/A Mbo4/Git/Read-Files/README.md', 'r')

for line in file:
    time.sleep(1)
    print(line)