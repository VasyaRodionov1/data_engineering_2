import csv
import json
import pandas as pd
import msgpack
import pickle
from collections import Counter
import numpy as np
#анализ отзывов из JSON файла о приложении Shopee. В результате получается статистика, 
# включающая характеристики числовых данных (рейтинг, количество лайков) и частоту встречаемости текстовых отзывов.
json_file_path = 'SHOPEE_REVIEWS.json'

with open(json_file_path, 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

df = pd.DataFrame(json_data)

# Отбор нужных полей
selected_fields = ["review_rating", "review_likes", "review_text"]
df_selected = df[selected_fields].copy()  # Используем метод copy для избежания SettingWithCopyWarning

# Преобразуем числовые данные в числовой формат
df_selected["review_rating"] = pd.to_numeric(df_selected["review_rating"], errors='coerce')
df_selected["review_likes"] = pd.to_numeric(df_selected["review_likes"], errors='coerce')

# Рассчитываем характеристики для числовых данных
numeric_stats = {
    "max_review_rating": df_selected["review_rating"].max(),
    "min_review_rating": df_selected["review_rating"].min(),
    "mean_review_rating": df_selected["review_rating"].mean(),
    "sum_review_likes": df_selected["review_likes"].sum(),
    "std_review_rating": df_selected["review_rating"].std()
}

# Рассчитываем частоту встречаемости для текстовых данных
text_freq = dict(Counter(df_selected["review_text"]))

numeric_stats = {
    key: int(value) if isinstance(value, (np.int64, np.int32, np.int16, np.int8, int, float)) else value
    for key, value in numeric_stats.items()
}

# Сохраняем результаты в JSON
result_json = {
    "numeric_stats": numeric_stats,
    "text_freq": text_freq
}

with open('result_task5.json', 'w', encoding='utf-8') as json_file:
    json.dump(result_json, json_file, ensure_ascii=False, indent=2)

# Сохраняем в CSV
df_selected.to_csv('result_task5.csv', index=False)

# Сохраняем в Msgpack
with open('result_task5.msgpack', 'wb') as msgpack_file:
    packed_data = msgpack.packb(result_json)
    msgpack_file.write(packed_data)

# Сохраняем в Pickle
with open('result_task5.pkl', 'wb') as pickle_file:
    pickle.dump(result_json, pickle_file)