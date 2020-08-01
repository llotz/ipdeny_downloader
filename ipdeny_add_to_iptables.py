import os
import datetime

fileContent = open("blocked.txt")

print('emptying existing BLACKLIST chain')
answer = os.popen('iptables -F BLACKLIST').read()
if "No chain/target/match by that name" in answer:
    print('No BLACKLIST chain existing.. creating one..')
    os.system('iptables -N BLACKLIST')
    print('Inserting chain to the first position of the default chain...')
    os.system('iptables -I INPUT 1 -j BLACKLIST')

print('creating rules....')
x = 0
for line in fileContent:
    if x % 1000 == 0:
        print(str(datetime.datetime.now()) + ": " + str(x))
    ip = line.replace('\n', '')
    command = 'iptables -A BLACKLIST -s '+ip+' -j DROP'
    os.system(command)
    x += 1

print("done.. "+str(x)+" lines added")
