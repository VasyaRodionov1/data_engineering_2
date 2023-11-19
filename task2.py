import numpy as np
import os

matrix = np.load('matrix_8_1.npy')
threshold = 508 #8 вариант
indexes = np.where(matrix > threshold)

# Создание массивов x, y, z
x = indexes[0]
y = indexes[1]
z = matrix[indexes]

np.savez('result_task2.npz', x=x, y=y, z=z)
np.savez_compressed('result_compressed_task2.npz', x=x, y=y, z=z)

# Сравнение размеров
original_size = os.path.getsize('result_task2.npz')
compressed_size = os.path.getsize('result_compressed_task2.npz')
print(f"Original size: {original_size} bytes, Compressed size: {compressed_size} bytes")