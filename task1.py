import numpy as np
import json

# Загрузка матрицы 8 вариант
matrix = np.load('matrix_8_1.npy')

total_sum = np.sum(matrix)
total_avg = np.mean(matrix)
main_diag_sum = np.trace(matrix)
main_diag_avg = np.mean(np.diag(matrix))
secondary_diag_sum = np.trace(np.fliplr(matrix))
secondary_diag_avg = np.mean(np.fliplr(matrix).diagonal())
max_val = np.max(matrix)
min_val = np.min(matrix)

# Запись значений
result = {
    "sum": int(total_sum),
    "avr": float(total_avg),
    "sumMD": int(main_diag_sum),
    "avrMD": float(main_diag_avg),
    "sumSD": int(secondary_diag_sum),
    "avrSD": float(secondary_diag_avg),
    "max": int(max_val),
    "min": int(min_val)
}

with open('result_task1.json', 'w') as json_file:
    json.dump(result, json_file)

# Нормализация
normalized_matrix = (matrix - np.min(matrix)) / (np.max(matrix) - np.min(matrix))
np.save('normalized_matrix_task1.npy', normalized_matrix)
