import numpy as np

def main():
    A = np.array([[1,0,2],[0,2,6],[1,1,1]], dtype='d')
    row_echelon_form(A)
    print(A)

def row_echelon_form(A):
    if not has_nonzero_(A) : return A
    pivot_col_num = get_leftmost_nonzero_column(A)

    select_and_move_pivot_up(A, pivot_col_num)

    make_below_pivot_zero(A, pivot_col_num)

    remaining_sub_matrix = A[1:]
    row_echelon_form(remaining_sub_matrix)


#=========================================================
has_nonzero_= lambda A : A.any()
#=========================================================
def get_leftmost_nonzero_column(A):
    for i in range(A.shape[1]):
        ith_col = A[:, i]
        if vect_is_not_zero(ith_col):
            return i


vect_is_not_zero = lambda vect : np.any(vect)
#=========================================================        
def select_and_move_pivot_up(A, pivot_col_num):
    pivot_row_num = max_abs_val_row_num(pivot_col_num)
    pivot = A[pivot_row_num, pivot_col_num]
        
    #normalize row
    A[pivot_row_num] /= pivot
    #bring to the top
    swap_rows(A, 0, pivot_row_num)


max_abs_val_row_num = lambda vect : np.argmax(np.abs(vect))

def swap_rows(mtx, indx1, indx2):
    mtx[[indx1, indx2]] = mtx[[indx2, indx1]]
#=========================================================
def make_below_pivot_zero(A, pivot_col_num):
    remaining_mtx = A[1:]
    rows_count = remaining_mtx.shape[0]
    if (rows_count != 0 ):
        A[1:] = np.apply_along_axis(replace, 1, A[1:], A[0], pivot_col_num)


replace= lambda row, pivot_row_vect, pivot_col_num : row - ((row[pivot_col_num] * pivot_row_vect))
#=========================================================

if __name__ == "__main__":
    main()