import main
print("hello from message.py")

# Guard method to check if the script is being run directly or imported as a module
if __name__ == "__main__":
    print("This is the message module after the guard method check. It is being run directly.")