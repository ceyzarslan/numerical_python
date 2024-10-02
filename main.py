import numpy as np

liste = [1, 2, 3, 4, 5]
print(liste)  # çıktısı : [1, 2, 3, 4, 5]
# listelerin büyük datalarda performansları yetersizdir

arr1d = np.array(liste)
print(arr1d)  # çıktısı: [1 2 3 4 5]
print("Dimensions: ", arr1d.ndim)
print("Shape: ", arr1d.shape)
print("Size: ", arr1d.size)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d)
# çıktısı:
# [[1 2 3]
# [4 5 6]
# [7 8 9]]
# Dimensions:  2
# Shape:  (3, 3)
# Size:  9
print("Dimensions: ", arr2d.ndim)
print("Shape: ", arr2d.shape)
print("Size: ", arr2d.size)

print()

arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3d)
print("Dimensions: ", arr3d.ndim)
print("Shape: ", arr3d.shape)
print("Size: ", arr3d.size)
# çıktısı:
# [[1 2]
# [3 4]
# [5 6]
# [7 9]]
# Dimensions:  2
# Shape:  (4, 2)
# Size:  8
print()
arr_reshape = arr3d.reshape((1, 8))
print(arr_reshape)  # çıktısı : [[1 2 3 4 5 6 7 8]]
print()

print("Sıfırlar: \n", np.zeros((5, 5)))  # Sıfırlar matrisi çıktısı: Sıfırlar:  [0. 0. 0. 0. 0.]
# np.zeros(((5,5))) Çıktısı:
# Sıfırlar:
#  [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]

print("Birler Matrisi: \n", np.ones((2, 3)))
print("Göz Matrisi: \n", np.eye(5))
