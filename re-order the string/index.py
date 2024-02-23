def adding_nums_and_words(word_list,nums_list):
    record_sentence=''
    for i in word_list:
        record_sentence+=i 
        if len(nums_list)!=0:
            record_sentence+=str(nums_list.pop())
    return record_sentence
    
def get_number_index(sentence,start_index):
    end_index=len(sentence)
    for i in range(start_index,end_index):
        if not sentence[i].isdigit():
            end_index=i 
            break 
    return end_index
def get_word_and_nums_list(sentence):
    word_list,nums_list=[],[]
    i=0
    while i<len(sentence):
        number=""
        if sentence[i].isdigit():
            start_index=i 
            end_index=get_number_index(sentence,start_index)
            number=int(sentence[start_index:end_index])
            word=sentence[:start_index]
            nums_list.append(number)
            word_list.append(word)
            sentence=sentence[end_index:]
            i=0 
        else:
            i+=1 
    word_list.append(sentence)
    return word_list,nums_list
def get_string(sentence):
    word_list,nums_list=get_word_and_nums_list(sentence)
    sorted_nums_list=sorted(nums_list,reverse=True)
    record_sentence=adding_nums_and_words(word_list,sorted_nums_list)
    return record_sentence
def main():
    sentence=input()
    record_sentence=get_string(sentence)
    print(record_sentence)
main()
