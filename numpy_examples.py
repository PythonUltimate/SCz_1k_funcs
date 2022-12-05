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


def check_if_reshape_is_view(array, num1, num2): # tak, reshaping daje view!!!
    arr = np.array(array)
    newarr = arr.reshape(num1, num2)
    return newarr.base

n = check_if_reshape_is_view(test_list, 10, 1)

print(n)
print(type(n))
# print(n.dtype)
