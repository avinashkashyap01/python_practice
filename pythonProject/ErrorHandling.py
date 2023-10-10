
# float(123.4) - > 123.4
# float("N/A") - > error


# try:
#     print("hello")
# except:
#     print("entered exception")



# keyword = "hello"
# try:
#     print(int(keyword))
# except Exception as e:
#     print(str(e))
#     print("past exception")




# keyword = "hello"
# try:
#     print(int(keyword))
# except ValueError:
#     print("got a Valueerror")
# finally:
#     print("finally")
# print("past exception")



keyword = "hello"
try:
    raise NameError("Error")
except ValueError:
    print("got a Valueerror")
except Exception as e:
    print(" Other type of exception")
    print(e)
finally:
    print("finally")
print("past exception")
