# a = input("enter the number:")
# print(f"Multiplication table of{a} is:")
# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} ={int(a)*i}")
# except:
#     print("invalid input!")
    
# print("some imp lines of code")
# print("end of program")


# try:
#     num = int(input("enter an integer"))
#     a=[6,3]
#     print(a[num])
# except ValueError:
#     print("number entered is not an integer.")
    
# except IndexError:
#     print("Index error")

# finally uses
# simply can be done using print function at last but that print function will 
# not executed if  we wrap this under a function.
try:
    l=[1,3,4,5]
    i= int(input("enter the index:"))
    print(l[i])
except:
    print("some error occured")
finally:
    print("I am always executed")
    
    
def func1():
    try:
        l=[1,3,4,5]
        i= int(input("enter the index:"))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("I am always executed")
        
x=func1()
print(x)
    
    
