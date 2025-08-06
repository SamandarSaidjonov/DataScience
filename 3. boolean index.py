import numpy as np 

arr = np.array(["Apple", "Banana", "Cherry", "Grape", "Elderberry", "Apple", "Grape", "Cherry", "Kiwi", "Pineapple", "Apple"])
data = np.random.randn(11,5)

#print(data)

# Create a boolean index for the array
#boolean_index = arr == "Apple"
#print("Boolean index: ", boolean_index) 

olish1 = data[arr == "Apple"] # Apple tegishli elementlarni olish
olish2 = data[arr == "Cherry"] # Cherry ga tegishli elementlarni olish
#print("\nApple ga tegishli malumotlarni olish: \n", olish1)  
#print("\nCherry ga tegishli malumotlarni olish: \n", olish2)
#print("\nBarcha ma'lumotlar: \n", data)

#Boolean indeks orqali ma'lumotlarni olish

filtr_data = data[arr == "Apple", 3:]
#print("\nApple ga tegishli ma'lumotlarning 3-ustundan boshlab barcha elementlari: \n", filtr_data) # Apple ga tegishli ma'lumotlarning 3-ustundan boshlab barcha elementlari

filtr_data2 = data[arr == "Cherry", 1:4]
#print("\nCherry ga tegishli barcha ustunlar:\n", data[arr == "Cherry"],"\nCherry ga tegishli ma'lumotlarning 1-3 ustunlari: \n", filtr_data2) # Cherry ga tegishli ma'lumotlarning 1-3 ustunlari

filtr_data3 = data[arr == "Grape", :2]
#print("\nGrapega tegishli ustunlar: \n", data[arr=="Grape"], "\nGrape ga tegishli ma'lumotlarning 0-1 ustunlari: \n", filtr_data3) # Grape ga tegishli ma'lumotlarning 0-1 ustunlari

not_apple = data[arr != "Apple"] # Apple ga tegishli bo'lmagan ma'lumotlarni olish
#print("Barcha ma\'lumotlar:\n", data, "\nTegishli bo\'lmagan:\n ", not_apple) #apple ga tegishli bo'lmagan ma'lumotlarni olish

# Ikkita shart bilan ma'lumotlarni olish
mask = (arr == "Apple") | (arr == "Cherry") # Apple yoki Cherry ga tegishli ma'lumotlarni olish
olish3 = data[mask]
#print("Barcha ma'lumotlar:\n", data)
#print("\nApple yoki Cherry ga tegishli ma'lumotlar: \n", olish3) # Apple yoki Cherry ga tegishli ma'lumotlarni olish

print("\nBarcha ma'lumotlar: \n", data)

data[data < 0] = 0 # Manfiy qiymatlarni 0 ga almashtirish
print("\nManfiy qiymatlarni 0 ga almashtirish: \n", data)




