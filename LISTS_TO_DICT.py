list_keys=['ram','shiva','hanuman','ravan']
list_values=[45,55,65,34]
result_dict={}

for key in list_keys:
    for value in list_values:
        result_dict[key]=value
        list_values.remove(value)
        break

print("Resultant Dictionary:",result_dict)