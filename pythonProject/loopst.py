
# for i in range(100,150):
#      print(f"square of {i}=",i*i)


start = int(input("enter the start number"))
end = int(input("enter the end number"))

if start >= end:
   print("error")
   raise Exception

for i in range(start,end):
     print(f"square of {i}=",i*i)

