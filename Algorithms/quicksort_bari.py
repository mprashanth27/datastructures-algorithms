def quick_sort(l,h):
    if(l < h): # base case: check if 2 elements exist in A.
        m = partition(l, h)
        quick_sort(l, m) # Left side
        quick_sort(m+1, h) # Right side

def partition(L,H):
        pivot = A[L] # 1st element
        #pivot = A[(L+H)//2] # middle element - RecursionError: maximum recursion depth exceeded?
        i = L
        j = H
        while(i<j): # base case
            while(A[i] <= pivot): # i++ till element > pivot is found
                i += 1
            while(A[j] > pivot): # j-- till element < pivot is found
                j -= 1
            if(i < j):
                A[i], A[j]  = A[j], A[i] #swap
        A[L], A[j]  = A[j], A[L] #update pivot
        return j #new pivots index ~ partitioning position

A = [10,16,8,12,15,6,3,9,5]

print("input =", A)
l = 0
h = len(A)-1

quick_sort(l,h)
print("sorted =",A)