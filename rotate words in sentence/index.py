def rotate_sentence(sentence,n):
    words=sentence.split()
    length=[len(w) for w in words]
    s=''.join(words)
    s=s[n:]+s[:n]
    res=''
    i=0
    for l in length:
        if res:
            res+=' '
        res+=s[i:i+l]
        i+=l 
    return res
def main():
    sentence=input()
    n=int(input())
    result=rotate_sentence(sentence,n)
    print(result)
main()
