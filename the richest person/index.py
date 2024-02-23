def read_inputs(no_of_persons):
    names_list,income_list=[],[]
    for i in range(no_of_persons):
        each_entry=input().split()
        name=" ".join(each_entry[:len(each_entry)-1])
        income=int(each_entry[-1])
        names_list.append(name)
        income_list.append(income)
    return names_list,income_list
def get_name_of_person(name):
    name="".join(name.split())
    name=name.lower()
    return name 
def get_persons(names_list,income_list):
    persons=dict()
    for i in range(len(names_list)):
        name=get_name_of_person(names_list[i])
        if name not in persons.keys():
            persons[name]=income_list[i]
        else:
            persons[name]+=income_list[i]
    return persons
def get_richest_person(persons):
    max_income=max(persons.values())
    richest_persons=[]
    for i in persons.keys():
        if (persons[i]==max_income):
            richest_persons.append(i)
    richest_persons.sort()
    return richest_persons[0]
def print_result(names_list,richest_person_name):
    for i in range(len(names_list)):
        name=get_name_of_person(names_list[i])
        if (name==richest_person_name):
            print(names_list[i]+" "+str(i))
            break 
def main():
    no_of_persons=int(input())
    names_list,income_list=read_inputs(no_of_persons)
    persons=get_persons(names_list,income_list)
    richest_person_name=get_richest_person(persons)
    print_result(names_list,richest_person_name)
main()
    
    
    
    
