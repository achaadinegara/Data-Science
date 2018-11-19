"""
head(n) : Berfungsi untuk melihat data sebanyak n pada kolom awal (jika tidak diisi, secara random n=6).
tail(n) : Berfungsi untuk melihat data sebanyak n pada kolom akhit (jika tidak diisi, secara random n=6).
shape() : Melihat jumlah baris dan kolom.
info() : Nomor index beserta tipe datanya.
describe() : Menunjukkan rangkuman statistik seperti rata-rata, median, dll pada kolom.
"""

import pandas as pd

df = pd.read_csv('dob_job_application_filings_subset.csv')

print(df.head())

print(df.shape)

print(df.columns)

print(df.info)

print(df.describe)