def check_equal_length(first_word,second_word):
    letter_difference=0
    for i in range(len(first_word)):
        if(first_word[i]!=second_word[i]):
            letter_difference+=1 
    return letter_difference==1 
def check_letter_removel(max_length_word,min_length_word):
    is_same=False
    for i in range(len(max_length_word)):
        if (max_length_word[:i]+max_length_word[i+1:]==min_length_word):
            is_same=True
            break
    return is_same
def final_output(words_list):
    is_same=True
    for i in range(len(words_list)-1):
        first_word,second_word=words_list[i],words_list[i+1]
        first_length,second_length=len(first_word),len(second_word)
        if (first_length==second_length):
            is_same=check_equal_length(first_word,second_word)
        elif(first_length>second_length):
            is_same=check_letter_removel(first_word,second_word)
        else:
            is_same=check_letter_removel(second_word,first_word)
        if not is_same:
            break 
    if(is_same):
        return "Family"
    else:
        return "Not a Family"
def main():
    test_caases=int(input())
    for i in range(test_caases):
        no_of_words=int(input())
        words_list=input().split()
        is_family=final_output(words_list)
        print(is_family)
main()
    
