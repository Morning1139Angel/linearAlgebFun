import numpy as np
from sympy import Matrix

is_not_zero = lambda column : np.any(column)
get_max_abs_val_indx = lambda vect : np.argmax(np.abs(vect))
netrulize= lambda vect, base, pos : vect - ((vect[pos] * base))


def get_first_none_zero_column(A):
    columns_count = A.shape[1]
    for i in range(columns_count):
        col = A[:, i]
        

        if is_not_zero(col):
            return True, col, i
    return False, None, -1

def transform_2_echelon_f(A):
    has_none_zero_col, col, pivot_colmn = get_first_none_zero_column(A)
    if not has_none_zero_col : 
        return
    else:
        setup_pivot(A, col)
        remaining_mtx = A[1:]
        rows_count = remaining_mtx.shape[0]
        if (rows_count != 0 ):
            A[1:] = np.apply_along_axis(netrulize, 1, A[1:], A[0], pivot_colmn)
            transform_2_echelon_f(A[1:])


def setup_pivot(A, col):
    pivot_row = get_max_abs_val_indx(col)
    pivot = col[pivot_row]
        
        #normalize row
    A[pivot_row] /= pivot
        #bring to the top
    swap_rows(A, 0, pivot_row)


def swap_rows(mtx, indx1, indx2):
    mtx[[indx1, indx2]] = mtx[[indx2, indx1]]


A = np.array([[1,0,2],[0,2,6],[1,1,1]], dtype='d')
transform_2_echelon_f(A)
print(A)