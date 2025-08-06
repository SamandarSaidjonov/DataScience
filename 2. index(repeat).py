'''
1. **Massiv yaratish:**
   1D massiv yarating: `[10, 20, 30, 40, 50]`
   3-chi elementni chiqaring.
2. **Oxirgi element:**
   Yuqoridagi massivdan oxirgi elementni indekslash orqali ajrating.
3. **Kesish:**
   `[5, 10, 15, 20, 25, 30]` massividan faqat `[15, 20]` ni kesib oling.
4. **Har ikkinchi element:**
   `[1, 3, 5, 7, 9, 11, 13]` massivdan har ikkinchi elementni chiqaring.
5. **Orqaga kesish:**
   `[100, 200, 300, 400]` massivni teskari tartibda chiqaring.
6. **2D massivdagi element:**
   Quyidagi massivdan `7` ni ajrating:

   ```python
   np.array([[1, 3, 5],
             [7, 9, 11]])
   ```
7. **2D kesish:**
   Shu massivdan faqat `[3, 5], [9, 11]` qismini kesib oling.
8. **Qatorni olish:**
   Quyidagi massivning 2-qatorini kesib oling:

   ```python
   np.array([[2, 4, 6],
             [8, 10, 12],
             [14, 16, 18]])
   ```
9. **Ustunni olish:**
   Yuqoridagi massivdan faqat 1-ustunni oling (ya'ni `[2, 8, 14]`).
10. **2D teskari tartibda:**
    Quyidagi massivni qatorlar bo‘yicha teskari tartibda chiqaring:
```python
np.array([[1, 2],
          [3, 4],
          [5, 6]])
```
11. **Har bir elementga indeks orqali kirish:**
    `[5, 10, 15, 20, 25]` massivdan 1-chi, 3-chi va 4-chi elementlarni yangi massivga ajrating.
12. **2D massivdan kesish:**
```python
np.array([[0, 1, 2],
          [3, 4, 5],
          [6, 7, 8]])
```
Bu massivdan markazdagi `[[4, 5], [7, 8]]` qismini kesib oling.
13. **Diagonallarni indekslash:**
    Yuqoridagi 3x3 massivdan asosiy diagonal (`0, 4, 8`) va yordamchi diagonal (`2, 4, 6`) ni ajrating.
'''

import numpy as np

#1-masala yechimi

arr1 = np.arange(10, 60, 10)
print("1-masala javobi:", arr1[2])

#2-masala yechimi
print("2-masala javobi:", arr1[-1])

#3-masala yechimi
arr2 = np.array([5, 10, 15, 20, 25, 30])
print("3-masala javobi:", arr2[2:4])

#4-masala yechimi
arr3 = np.arange(1,15,2)
print("4-masala javobi:", arr3[::2])

#5-masala yechimi
arr4 = np.array([100, 200, 300, 400])
print("5-masala javobi:", arr4[::-1])

#6-masala yechimi
arr5 = np.array([[1,3,5], 
                 [7,9,11]])
print("6-masala javobi: ", arr5[1,0])

#7-masala yechimi
print("7-masala javobi:", arr5[0:2, 1:3])

#8-masala yechimi
arr6 = np.array([
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]])
print("8-masala javobi:", arr6[1, :])

#9-masala yechimi
print("9-masala javobi:", arr6[:,0])

#10-masala yechimi
arr7 = np.array([[1, 2],
                 [3, 4],
                 [5, 6]])
print("10-masala javobi:", arr7[::-1])

#11-masala yechimi
arr8 = np.array([5, 10, 15, 20, 25])
new_arr = arr8[[1, 3, 4]].copy()
new_arr[0] = 34 
new_arr[1] = 147
new_arr[2] = 3
print("11-masala javobi:", new_arr, "\nOriginal massiv:", arr8)

#12-masala yechimi
arr9 = np.array([[0, 1, 2],
                  [3, 4, 5],
                  [6, 7, 8]])
print("12-masala javobi:", arr9[1:3, 1:3])

#13-masala yechimi
asosiy_diagonal = arr9.diagonal()
yordamchi_diagonal = np.fliplr(arr9).diagonal()
print("13-masala javobi: Asosiy diagonal:", asosiy_diagonal, "Yordamchi diagonal:", yordamchi_diagonal)
