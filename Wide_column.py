
wide_column_db = {
    "user_1": {"nama": "Aldi", "email": "aldi@email.com", "kota": "Mamuju"},
    "user_2": {"nama": "Budi", "email": "budi@email.com", "kota": "Majene"},
    "user_3": {"nama": "Citra", "email": "citra@email.com", "kota": "Mamasa"},
    "user_4": {"nama": "Dina", "email": "dina@email.com", "kota": "Pasangkayu"},
    "user_5": {"nama": "Eko", "email": "eko@email.com", "kota": "Polewali"},
}

for row, columns in wide_column_db.items():
    print(f"{row}: {columns}")
