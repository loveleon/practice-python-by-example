import time

if __name__ == "__main__":
    i = 10
    while i > 1:
        print("hello")
        i = i - 1
        time.sleep(1)
    else:
        print("goodbye")