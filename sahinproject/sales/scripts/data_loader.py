import os
import sys
import django
import pandas as pd
from sales.models import *

sys.path.append('D:\\SahinPersonel\\Personel-Takip\\sahinproject\\sales')

# Django projenizin ayar dosyasını belirtin
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sahinproject.test_settings')
django.setup()

# Excel dosyalarını okuyun
il_excel_path = r'C:\Users\exter\Downloads\il_data.xlsx'
ilce_excel_path = r'C:\Users\exter\Downloads\ilceler_data.xlsx'

il_df = pd.read_excel(il_excel_path)
ilce_df = pd.read_excel(ilce_excel_path)

# İlleri ve ilçeleri Django modellerine yükleyin
for index, row in il_df.iterrows():
    il = Il.objects.create(ad=row['il'])

for index, row in ilce_df.iterrows():
    il = Il.objects.get(ad=row['il'])
    Ilce.objects.create(il=il, ad=row['ilçe'])
