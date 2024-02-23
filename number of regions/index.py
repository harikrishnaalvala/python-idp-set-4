def read_matrix(rows,columns):
    matrix=[]
    for i in range(rows):
        row=list(map(int,input().split()))
        matrix.append(row)
    return matrix
def get_ones_list(matrix):
    ones_list=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]==1:
                ones_list.append((i,j))
    return ones_list
def get_nighbours(positions):
    i,j=positions
    n=[]
    n.append((i,j-1))
    n.append((i,j+1))
    n.append((i-1,j))
    n.append((i+1,j))
    return n
def get_connect_ones(r,ones_list):
    c_o=[]
    for i in r:
        n=get_nighbours(i)
        for j in n:
            if(j in ones_list) and (j not in r):
                c_o.append(j)
                ones_list.remove(j)
    return c_o
def get_result(matrix):
    ones_list=get_ones_list(matrix)
    no_or_r=0
    while len(ones_list)!=0:
        s=ones_list.pop()
        r=[s]
        while True:
            c_o=get_connect_ones(r,ones_list)
            if (len(c_o)==0):
                break 
            r.extend(c_o)
        no_or_r+=1 
    return no_or_r
def main():
    rows,columns=map(int,input().split())
    matrix=read_matrix(rows,columns)
    no_or_r=get_result(matrix)
    print(no_or_r)
main()
    
