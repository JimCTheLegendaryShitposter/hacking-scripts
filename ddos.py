import random

ping_count = 0
ip = ""

while True:
    if ping_count > 420:
        ping_count = 0
        ip = f"192.168.{random.randint(0, 500)}.{random.randint(0, 500)}"

    ping_count += 1
    print(f"pinged {ip} {ping_count} times")

