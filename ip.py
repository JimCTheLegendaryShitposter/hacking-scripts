import os
import random
import time


while True:
    time.sleep(random.uniform(0, .3))
    print("checking ip 192.168." + str(random.randint(0, 500)) + "." + str(random.randint(0, 500)), flush=True)

    if random.randint(0, 100) < 30:
        print("Cracked the " + random.choice(["mainframe", "ip address", "html proxy servers", "government passwords", "javacode ciphers", "women"]), flush=True)
    
    if random.randint(0, 100) < 40:
        print(random.choice(["Access dnied", "Access granted", "I'm in", "Hacking the mongodb sql injection servers", "breaking the firewall antivirus code"]), flush=True)

