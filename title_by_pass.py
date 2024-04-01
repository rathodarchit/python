def call_by_value(x):
    x = x * 2
    print("Function Value Updated To: ",x)


def call_by_reference(list):
    list.append("D")
    print("Function List Updated To: ",list)

my_list = ["E"]
num = 2
print("Number Before: ",num)
call_by_value(num)
print("List Before: ",my_list)
call_by_reference(my_list)