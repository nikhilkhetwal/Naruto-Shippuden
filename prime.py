import math

def main():
    count = 3
    one = 1
    while one == 1:
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0: 
                continue
            if count % x != 0:
                print count

        count += 1
