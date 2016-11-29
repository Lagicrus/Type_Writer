import sys, random, time

def slowPrint(message, end='\n'):
    for c in message:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.randint(40, 100)/ 1000)
    sys.stdout.write(end)


def Spining(message='-\|/-\|/', end='\n'):
    for b in range(9):
        for c in message:
            c = "Loading " + c
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.35)
            sys.stdout.write("\b"*9)
    sys.stdout.write(end)

#|/-\|/-\
#-\|/-\_/
slowPrint("Hello Lev, this is your mind speaking to you")
Spining()
