def check_is_prime(number):
    is_prime=True
    for i in range(2,number):
        if number%i==0:
            is_prime=False
            break 
    return is_prime
def special_factors(number):
    s_f=[]
    for i in range(2,number+1):
        if (number%i==0):
            is_prime=check_is_prime(i)
            if is_prime:
                s_f.append(str(i))
    return s_f
def main():
    number=int(input())
    result=special_factors(number)
    print(*result)
main()
        
