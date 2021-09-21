import re
order_dict = {}


with open("python_assignment.txt",'r') as data:
    questions = data.readlines()
    for qns in questions:
        text = qns.split(")")
        print(text)
        if 'Q' in text[0]:
            print(text[0])
            for i in range(1,len(text)):
                temp = ""
                order_dict[text[0]] = "".join(text[i])
            # order_dict{text[0]:}

sorted_order_dict = sorted(order_dict)
print(order_dict)

with open("soreted.text",'w+') as setdata:
    for qn in sorted_order_dict:
        setdata.writelines(f"{qn}) {order_dict[qn]} \n")
    
