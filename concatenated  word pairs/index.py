def get_word_pairs(words_list,length):
    word_pairs_list=[]
    for i in range(len(words_list)):
        for j in range(i+1,len(words_list)):
            word_pair=words_list[i]+words_list[j]
            if len(word_pair)==length:
                reverse_word=words_list[j]+words_list[i]
                word_pairs_list.append(word_pair)
                word_pairs_list.append(reverse_word)
    return word_pairs_list
def get_sorted_word_pairs(word_pairs_list):
    unique_pairs=list(set(word_pairs_list))
    sorted_pairs=sorted(unique_pairs)
    return sorted_pairs
def print_result(word_pairs):
    for word_pair in word_pairs:
        print(word_pair)
def main():
    words_list=input().split()
    length=int(input())
    word_pairs_list=get_word_pairs(words_list,length)
    unique_pairs=get_sorted_word_pairs(word_pairs_list)
    print_result(unique_pairs)
main()
    
