# Exception Handeling

try:
    f = open('./Files/test.txt')

    # raise custom exception
    if f.name == "./Files/test.txt":
        raise Exception
    
except FileNotFoundError as e:
    print(e)
    
except Exception as e: # Exception covers every error
    print("test error")

# else clause only runs when we have no exception
else:
    # this can also be inside the try block
    print(f.read())
    f.close()
    
# finally caluse always runs
finally:
    print("Final execution")


# ============================
# Try - except - Finally


# Try - except - finally

while True:
     # try to do this. if something goes wrong do the except.
    try:
        number = int(input("what is your favorite number? \n"))
        print(18/number)
        # when it breaks it means it ends the while loop.
        break
    except ValueError:
        print("only enter a number!")
    except ZeroDivisionError:
        print("don't enter zero.")
    except: # this responds to any kind of error.
        break
    # the code inside finally will be shown no matter what. (even after the break)
    finally:
        print("loop complete.")