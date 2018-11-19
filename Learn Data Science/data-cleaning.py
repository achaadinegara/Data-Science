"""
df.columns =['a', 'b', 'c']
pd.isnull()
df.dropna()
df.dropna(axis=1)
df.dropna(axis=1, thresh=n)
df.fillna(x)
df.fillna(df.mean())
s = df.ix[:,nomor kolom yang dipilih]
s.astype(tipedata)
s.replace([1,3], ['one', 'three'])
df.rename(columns={'nama lama': 'nama baru'})

Mengubah nama kolom jadi ‘a’, ‘b’, ‘c’.
Mengecek apakah ada nilai NULL dengan keluaran boolean.
Menghapus baris yang berisi NULL.
Menghapus semua kolom yang berisi NULL.
Menghapus semua kolom dengan batas n.
Mengisi nilai NULL dengan x.
Mengisi nilai NULL dengan rata-rata.
Membuat series dengan dataframe.
Mengubah tipe data pada series.
Mengubah nilai 1 dan 3 pada series dengan ‘one’ dan ‘three’
Merename nama kolom.
"""

import pandas as pd

df = pd.read_csv('dob_job_application_filings_subset.csv')

print(df['Borough'].value_counts(dropna=False))

print(df['State'].value_counts(dropna=False))

print(df['Site Fill'].value_counts(dropna=False))