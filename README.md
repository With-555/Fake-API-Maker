# FakerMaker

`FakerMaker` — bu web interfeys orqali foydalanuvchidan field nomlari va ularning turlarini olib, avtomatik soxta (fake) ma’lumot generatsiya qiluvchi tizim. Ma’lumotlar JSON ko‘rinishida qaytariladi hamda CSV, XLSX formatlarida ham yuklab olish mumkin.

---

![banner](https://i.postimg.cc/764MqtCg/Pics-Art-25-04-09-12-14-28-305.png "banner")

## 🛠 Asosiy imkoniyatlari

- UI (foydalanuvchi interfeysi) orqali field nomlari va turlarini kiritish
- Data sonini (`count`) va yaroqlilik muddatini (`expired_time`) belgilash
- JSON, CSV va XLSX formatlarida natijalarni olish
- Har bir request uchun unikal `uuid` asosida endpoint yaratiladi
- Ma’lumotlar belgilangan vaqtdan keyin avtomatik o‘chiriladi

---

## 🚀 Ishlash jarayoni

1. Asosiy sahifaga kiring
2. Formani to‘ldiring:
   - Har bir field uchun nom (masalan: `email`, `age`) va tip (masalan: `EmailField`, `IntegerField`) tanlang
   - Generatsiya qilinadigan yozuvlar sonini (`count`) belgilang
   - Ma’lumotlar saqlanadigan vaqt (`expired_time`, soniyalarda) kiriting
3. "Generate" tugmasini bosing
4. Sizga unikal API endpoint hosil qilinadi
5. Ma'lumotni quyidagi formatlarda olishingiz mumkin:
   - JSON (default)
   - CSV
   - XLSX

---

## 🧪 Response namunasi

```json
{
  "success": true,
  "message": "Data retrieved successfully",
  "csv": "https://faker.felixits.uz/media/dynamic_schemas/csv/schema_50_1744181813.csv",
  "json": "https://faker.felixits.uz/media/dynamic_schemas/json/schema_50_1744181813.json",
  "xlsx": "https://faker.felixits.uz/media/dynamic_schemas/xlsx/schema_50_1744181813.xlsx",
  "uuid": "85da4830-7c51-4c96-9fe6-504b7f3e346d",
  "data": [
    {
      "url": "http://thomas.com/"
    },
    ...
  ],
  "created_at": "2025-04-09T06:56:52.931388+00:00",
  "expires_in": 3600
}
