def get_ascii_value_product(ascii_value):
    ascii_product=1 
    for i in str(ascii_value):
        ascii_product*=int(i)
    return ascii_product 
def get_result(string):
    product=1 
    for i in string:
        if (i.isdigit()):
            product*=int(i)
        else:
            ascii_value=ord(i)
            ascii_product=get_ascii_value_product(ascii_value)
            product*=ascii_product
    return product
def main():
    string=input()
    result=get_result(string)
    print(result)
main()
