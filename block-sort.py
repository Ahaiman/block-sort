

#swapping elements
def swap(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp

#selection sort implementation
def selection_sort(lst):
    ''' sort lst (in-place) '''
    n = len(lst)
    for i in range(n):
        m_index = i
        for j in range(i+1,n):
            if lst[m_index] > lst[j]:
                m_index = j
        swap(lst, i, m_index)
    return None

#creating block size k
def generate_sorted_blocks(lst, k):
    lst_sort = []
    n = len(lst)
    for i in range (0, n, k):
        if i+k > n: #creating the last list, less then k objects
            lst_sort.append([lst[e] for e in range (i, n)])
        else:
            lst_sort.append([lst[e] for e in range (i, i+k)])
    for i in range (len(lst_sort)):
        selection_sort(lst_sort[i])
    return lst_sort


def merge(A, B):
    """ merging two lists into a sorted list
        A and B must be sorted! """
    n = len(A)
    m = len(B)
    C = [0 for i in range(n+m)]

    a=0; b=0; c=0
    while  a<n  and  b<m: #more element in both A and B
        if A[a] < B[b]:
            C[c] = A[a]
            a+=1
        else:
            C[c] = B[b]
            b+=1
        c+=1

    C[c:] = A[a:] + B[b:] #append remaining elements (one of those is empty)

    return C


def merge_sorted_blocks(lst):
    c=[]
    if lst == []:
        return c
    n = len(lst)
    while n > 1:
        for i in range (0,n,2):
            if (i+1) > len(lst)-1:
                c.append(lst[i])
            else:
                c.append(merge(lst[i],lst[i+1]))
        lst = c.copy()
        c.clear()
        n = len(lst)
    return lst[0]



def sort_by_block_merge(lst,k):
   return merge_sorted_blocks(generate_sorted_blocks(lst, k))
