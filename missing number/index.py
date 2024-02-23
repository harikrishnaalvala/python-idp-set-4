def getting_missing_numbers(numbers):
    missing=-1
    for number in range(1,len(numbers)):
        if missing not in numbers:
            break 
        missing=missing-1 
    return missing
def main():
    numbers=list(map(int,input().split()))
    result=getting_missing_numbers(numbers)
    print(result)
main()
