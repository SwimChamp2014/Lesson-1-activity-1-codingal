def shutdown():
    x = input("Do you want to shutdown your computer? ").lower()
    a = input("Did you save all of your documents? ").lower()
    b = input("Did you want to have your update done in this time? ").lower()

    if x == "no" and a == "no" and b == "no":
        print("Don't shut down")
        shutdown()  # Recursive call
    elif x == "yes" and a == "yes" and b == "yes":
        print("Okay, Shutdown is happening")
    else:
        print("Sorry, let's try again.")
        shutdown()  # Recursive call
