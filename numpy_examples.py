import numpy as np

test_list = [34, 98, 3, 56, 12, 90, 78, 83, 28, 43]
test_list_2 = [72, 17, 97, 83, 38, 34, 6, 57, 93, 88]
test_list_3 = [52, 46, 25, 36, 94, 59, 94, 42, 29, 100]
test_list_4 = [27, 10, 90, 43, 98, 74, 43, 60, 37, 45]

str_list = ['elo', 'heja', 'czolem', 'siema', 'adjo']


def create_np_array(array):
    return np.array(array)


def check_np_version():
    return np.__version__


def create_scalar(num):
    return np.array(num)


def create_1D_array(array):
    return np.array(array)


def create_2D_array(array, array2):
    return np.array([array, array2])


def create_3D_array(array, array2, array3, array4):
    return np.array(([array, array2], [array3, array4]))


def create_nD_array(array, ndim):
    return np.array(array, ndmin=ndim)


def check_dimensions(fn, array, array2, array3, array4):
    elo = fn(array, array2, array3, array4)
    return elo.ndim


# heja = check_dimensions(create_3D_array, test_list, test_list_2, test_list_3, test_list_4)

def check_numpy_datatype(array):
    arr = np.array(array)
    return arr.dtype


def create_array_with_specific_datatype(array, type):
    arr = np.array(array, dtype=type)
    return arr


def create_newarrray_astype(array, type):
    arr = np.array(array)
    newarr = arr.astype(type)
    return newarr


def create_newarrray_asbool(array):
    arr = np.array(array)
    newarr = arr.astype(bool)
    return newarr


def make_copy_of_array(array):
    arr = np.array(array)
    cop = arr.copy()
    cop[0] = 1
    return arr, cop


def make_view_of_array(array):
    arr = np.array(array)
    vieew = arr.view()
    vieew[0] = 1
    return arr, vieew


def check_for_base_of_array(array):  # check if array owns the data
    arr = np.array(array)
    cop = arr.copy()
    vieew = arr.view()
    return cop.base, vieew.base


def check_array_shape(array, array2):
    arr = np.array([array, array2])
    return arr.shape


def check_nested_array_shape(array, num):
    arr = np.array(array, ndmin=num)
    return arr.shape


def reshape_array(array, num1, num2):
    arr = np.array(array)
    newarr = arr.reshape(num1, num2)
    return newarr


def check_if_reshape_is_view(array, num1, num2):  # tak, reshaping daje view!!!
    arr = np.array(array)
    newarr = arr.reshape(num1, num2)
    return newarr.base


def make_with_unknown_dimension(array, num):
    arr = np.array(array)
    return arr.reshape(num, -1)


def convert_to_1D_array(array, array2, array3, array4):
    arr = np.array(([array, array2], [array3, array4]))
    return arr.reshape(-1)


def iterate_by_elems(array):
    for elem in np.array(array):
        print(elem)


def iterate_by_rows(array, array2):
    for elem in np.array([array, array2]):
        print(elem)


def print_rows_of_3D_array(array, array2, array3, array4):
    for elem in np.array([[array, array2], [array3, array4]]):
        print(elem)


def print_nestedrows_of_3D_array(array, array2, array3, array4):
    for row in np.array([[array, array2], [array3, array4]]):
        for elem in row:
            print(elem)


def print_scalars_of_3D_array(array, array2, array3, array4):
    for row in np.array([[array, array2], [array3, array4]]):
        for elem in row:
            for scalar in elem:
                print(scalar)


def iterate_with_nditer(array, array2, array3, array4):
    arr = np.array([[array, array2], [array3, array4]])
    for elem in np.nditer(arr):
        print(elem)


def iterate_as_string(array):
    arr = np.array(array)
    for elem in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
        print(elem)


def iterate_with_skip_2(array):
    arr = np.array(array)
    for x in np.nditer(arr[::2]):
        print(x)


def print_with_enumeration(array):
    arr = np.array(array)
    for idx, x in np.ndenumerate(arr):
        print(idx, x)


def print_3D_with_enumeration(array, array2, array3, array4):
    arr = np.array([[array, array2], [array3, array4]])
    for idx, x in np.ndenumerate(arr):
        print(idx, x)


def concatenate_arrays(array, array2):
    arr1 = np.array(array)
    arr2 = np.array(array2)
    new_arr = np.concatenate((arr1, arr2))
    return new_arr


def concatenate_on_axis(array, array2, array3, array4, axis):
    arr1 = np.array([array, array2])
    arr2 = np.array([array3, array4])
    new_arr = np.concatenate((arr1, arr2), axis=axis)
    return new_arr


def join_by_stacking(array, array2, axis):
    arr1 = np.array(array)
    arr2 = np.array(array2)
    new_arr = np.stack((arr1, arr2), axis=axis)
    return new_arr


def join_by_rows_stacking(array, array2):
    arr1 = np.array(array)
    arr2 = np.array(array2)
    new_arr = np.hstack((arr1, arr2))
    return new_arr


def join_by_columns_stacking(array, array2):
    arr1 = np.array(array)
    arr2 = np.array(array2)
    new_arr = np.vstack((arr1, arr2))
    return new_arr


def join_by_depth_stacking(array, array2):
    arr1 = np.array(array)
    arr2 = np.array(array2)
    new_arr = np.dstack((arr1, arr2))
    return new_arr


def split_array(array, num):
    arr = np.array(array)
    new_arr = np.split(arr, num)
    return new_arr


def adjusted_split_array(array, num):
    arr = np.array(array)
    new_arr = np.array_split(arr, num)
    return new_arr


def adjusted_split_nD_array(array, array2, array3, array4, num):
    arr = np.array([[array, array2], [array3, array4]])
    new_arr = np.array_split(arr, num)
    return new_arr


def find_index_of_value(array, value):
    arr = np.array(array)
    idx = np.where(arr == value)
    return idx


def find_even_numbers(array):
    arr = np.array(array)
    idx = np.where(arr % 2 == 0)
    return idx


def find_odd_numbers(array):
    arr = np.array(array)
    idx = np.where(arr % 2 != 0)
    return idx


def find_higher_than(array, num):
    arr = np.array(array)
    idx = np.where(arr > num)
    return idx


def sort_array(array):
    arr = np.array(array)
    return np.sort(arr)


def sort_nD_array(array, array2, array3, array4):
    arr = np.array([[array, array2], [array3, array4]])
    return np.sort(arr)


def sort_string_list(str_array):
    arr = np.array(str_array)
    return np.sort(arr)

def search_where_insert(array, num):
    arr = np.array(array)
    sorted_array = np.sort(arr)
    print(np.searchsorted(sorted_array, num))


def search_where_insert_from_right(array, num):
    arr = np.array(array)
    sorted_array = np.sort(arr)
    print(np.searchsorted(sorted_array, num, side='right'))


def search_where_multiple_insert(array, num, num2, num3):
    arr = np.array(array)
    sorted_array = np.sort(arr)
    print(np.searchsorted(sorted_array, [num, num2, num3]))


n = sort_string_list(str_list)

print(n)
print(type(n))
# print(n.dtype)
