import numpy as np

# NumPy array indekslash, kesish va o'zgartirish 1-o'lchamli massivlarda
''' 
arr = np.arange(10, 100, 10)
slicing = arr[1:4]
print("Haqiqiy array: \n", arr, "\n Kesib olingan array: \n", slicing)

slicing[:] = 0
print("Kesib olingan arrayni o'zgartirgandan keyin haqiqiy array: \n", arr, "\n Kesib olingan array: \n", slicing)

arr2 = np.arange(10, 100, 10)
slicing2 = arr2[3:6].copy()
print("Ikkinchi haqiqiy array: \n", arr2, "\n Ikkinchi kesib olingan array: \n", slicing2)
slicing2[:] = 0
print("Ikkinchi kesib olingan arrayni o'zgartirgandan keyin haqiqiy array: \n", arr2, "\n Ikkinchi kesib olingan array: \n", slicing2)
'''

# NumPy array indekslash, kesish va o'zgartirish 2-o'lchamli massivlarda
'''
arr2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
#print("2-o'lchamli array: \n", arr2d, "\nMassiv o'lchami: \n", arr2d.shape)

#slicing2d_1 = arr2d[2, 1]
#print("Kesib olingan qiymat: ", slicing2d_1)

slicing2d_2 = arr2d[:2, 1:]
print("Kesib olingan qator: ", slicing2d_2)
'''

# NumPy array indekslash, kesish va o'zgartirish 3-o'lchamli massivlarda
arr3d = np.array([[[10,20,30],
                  [40,50,60],
                  [70,80,90]],
                  
                  [[100,110,120],
                   [130,140,150],
                   [160,170,180]],

                  [[190,200,210],
                   [220,230,240],
                   [250,260,270]]]
                   )
print(arr3d[0][1,1])
