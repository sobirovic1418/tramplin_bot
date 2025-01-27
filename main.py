from pyexpat.errors import messages

from head_fun import dp
from aiogram import types,executor

from inli_ibtn import kurs_ibtn, oqish_ibtn, ortga_ibtn, ort_ibtn, korzinka_ibtn
# from inli_ibtn import kurs_ibtn
from key_btn import start_btn


@dp.message_handler(commands=["start"])
async def begin(message:types.Message):
    await message.answer(f"Assalomu alaykum{message.from_user.full_name}\nbotimizga xush kelibsiz!!!",
                         reply_markup=start_btn)

@dp.message_handler(text=["👨‍💻 My school"])
async def school_fun(message:types.Message):
    img = open("static/img/my school.jpg", 'rb')
    text="""
    Assalomu alaykum hurmatli o'quvchilar!!!
    🔥 My School yangi formatda

🤩 My School oʻquv markazi tobora standartlashib, tizimlashib bormoqda. Kelgusida eng zamonaviy oʻquv markazlaridan biri boʻlgan My School’ning barcha filiallari mana shunday koʻrinishda boʻladi.

💯 Ishonavering, bunday zamonaviy muhitda ta’lim olish ingliz tili oʻrganish jarayoningizni qiziqarli, sifatli, qulay va emotsiyalarga boy qiladi. 

❤️ Agar siz ham ingliz tilini milliy qadriyatlarga asoslangan markazda oʻrganishni istasangiz, My School oilasi a’zosiga aylaning!

😇 Ha aytgancha bizada yana bir yangilik bizda IT o'quv kursimizga qatnashib turli 'sertifikatlar'imizga va ish bilan taminlashga ega bo'ling!!
    """
    await message.answer_photo(photo=img,caption=text,reply_markup=korzinka_ibtn)

@dp.callback_query_handler(text="uchirish")
async def uch(call:types.CallbackQuery):
    await call.message.delete()


@dp.callback_query_handler(text="foun")
async def kurss(call:types.CallbackQuery):
    text="""📌 Dasturlash asoslarini o'rganish bir nechta muhim sabablarga ega:

📚 Dasturlash mantig'ini tushunish: dasturlash asoslari dasturlarning mantig'i va ishlash tamoyillarini tushunishga imkon beradi. Siz kompyuterlar ma'lumotni qanday qayta ishlashini va ma'lumotlar bilan qanday munosabatda bo'lishini bilib olasiz.

🔍 Algoritmik fikrlashni rivojlantirish: dasturlash asoslarini o'rganish algoritmik fikrlash ko'nikmalarini va murakkab vazifalarni sodda va tushunarli bosqichlarga bo'lish qobiliyatini rivojlantirishga yordam beradi. Siz samarali muammolarni hal qilish algoritmlarini ishlab chiqishingiz mumkin.

👥  Jamoa bilan ishlash: dasturlash asoslarini bilish sizga boshqa ishlab chiquvchilar bilan samarali hamkorlik qilish imkonini beradi. Siz umumiy tilda tushunishingiz va muloqot qilishingiz, boshqa ishlab chiquvchilar tomonidan yaratilgan kodni osonroq ajratishingiz va tushunishingiz mumkin.

🚀 Analitik fikrlashni rivojlantirish: dasturlash asoslarini o'rganish analitik fikrlash va muammolarni muntazam ravishda hal qilish qobiliyatini rivojlantiradi. Siz muammolarni tahlil qilishni, ularning sabablarini topishni va oqilona echimlarni ishlab chiqishni o'rganasiz.

🦾 Texnologiyaning texnik tomonini tushunish: texnologiyaga boy dunyoda dasturlash asoslarini tushunish sizga texnik echimlar va texnologik mahsulotlar bilan yaxshiroq tushunish va o'zaro aloqada bo'lishga yordam beradi.

🎓 Dasturlash asoslarini o'rganish sizga nafaqat o'ziga xos dasturlash ko'nikmalarini beradi, balki tanqidiy fikrlash, ijodkorlik va muammoli fikrlashni rivojlantirishga yordam beradi. Ushbu ko'nikmalar nafaqat dasturlash sohasida, balki faoliyatning turli sohalarida ham qimmatli va foydalidir."""
    await call.message.delete()
    await call.message.answer(text,reply_markup=ortga_ibtn)

@dp.callback_query_handler(text="telegram")
async def ort_fun(call:types.CallbackQuery):
    text="""📌 Telegram bot Telegram messenjerida ishlaydigan avtomatlashtirilgan dasturiy ta'minot bo'lib, u foydalanuvchilarga turli vazifalarni bajarishda yordam beradi. Botlar avtomatik javob berish, ma'lumot taqdim etish, interaktiv xizmatlar ko'rsatish va boshqa ko'plab vazifalarni amalga oshiradi.

🗣 Telegram botlar foydalanuvchi so'rovlariga javob berish, ma'lumotlarni qayta ishlash, API lar bilan integratsiya qilish va boshqa ko'plab funktsiyalarni bajarish uchun ishlab chiqilgan. Ular foydalanuvchi bilan muloqot qilish uchun matn, rasmlar, videolar, tugmalar va boshqa interaktiv elementlarni ishlatishi mumkin.

🐍 Python Telegram botlarini yaratishda keng qo'llaniladigan dasturlash tillaridan biridir. Python uchun mavjud bo'lgan kutubxonalar va ramkalar Telegram botlarini yaratishni osonlashtiradi. Ushbu kutubxonalarga pyTelegramBotAPI, python-telegram-bot va telepot kiradi. Ular botlarni yaratish, xabarlarni qayta ishlash, tugmalar va menyularni sozlash kabi vazifalarni osonlashtiradi.

🗂 Telegram botlari foydalanuvchilarga turli xizmatlarni taqdim etishi mumkin, jumladan, ob-havo ma'lumotlari, yangiliklar yangilanishlari, savdo jarayonlari, o'yinlar va ko'ngilochar xizmatlar, ma'lumotlar bazasidan ma'lumotlar olish va boshqalar.

🛠 Telegram bot ishlab chiquvchilari botning logikasini yaratish, foydalanuvchi interfeysi bilan ishlash, ma'lumotlar bazasi bilan integratsiya qilish va xavfsizlikni ta'minlash kabi vazifalar bilan shug'ullanadi. Shuningdek, ular botning ishlashini va foydalanuvchi tajribasini yaxshilash uchun muntazam ravishda optimallashtirish va yangilash ishlarini olib boradilar.

💰 Telegram botlari nafaqat foydalanuvchilarga qulaylik yaratadi, balki bizneslar uchun ham katta foyda keltiradi. Ular mijozlar bilan avtomatlashtirilgan muloqot o'rnatish, mijozlarga xizmat ko'rsatishni yaxshilash va xarajatlarni kamaytirishga yordam beradi. Python ning qulayligi va kuchli kutubxonalari Telegram botlarini yaratishda uni ideal tanlov qiladi."""
    await call.message.delete()
    await call.message.answer(text,reply_markup=ortga_ibtn)


@dp.callback_query_handler(text="python")
async def ort_fun(call:types.CallbackQuery):
    text="""📌 Backend Python  dasturlash tili veb-ilovalar va boshqa dasturiy tizimlarning orqa qismini yaratish va boshqarish uchun ishlatiladigan dasturiy ta'minotni ishlab chiqishni anglatadi.

👨🏻‍💻 Python backend-bu mijoz tomoni (frontend) so'rovlarini ko'rib chiqadigan va ma'lumotlar bazalari bilan o'zaro aloqada bo'lgan, biznes mantig'ini bajaradigan, xavfsizlik, ma'lumotlarni qayta ishlash va boshqa funktsiyalarni ta'minlaydigan dasturlarning server tomoni.

🐍 Python backend dasturlarini ishlab chiqishni osonlashtiradigan ko'plab kutubxonalar va ramkalarni taklif etadi. Backend rivojlanishi uchun ba'zi mashhur Python ramkalariga Django, Flask, Pyramid va Bottle kiradi. Ular marshrutlarni boshqarish, ma'lumotlar bazalari bilan ishlash, API ishlab chiqish va backend ishlab chiqish uchun zarur bo'lgan boshqa vazifalar uchun qulay vositalarni taqdim etadi.

🗂 Python ma'lumotlar fani va ma'lumotlarni tahlil qilishda ham keng qo'llaniladi, bu esa uni katta hajmdagi ma'lumotlarni qayta ishlash va mashinani o'rganish bilan bog'liq tizimlarni backend ishlab chiqish uchun foydali qiladi.

🪩 Backend Python ishlab chiquvchilari server kodini yaratish va optimallashtirish, ma'lumotlar bazasini boshqarish, so'rovlarni qayta ishlash, biznes mantig'ini amalga oshirish va ilovaning xavfsizligi va ishlashini ta'minlash bilan shug'ullanadi.

📚 Backend Python Python tilining soddaligi va ekspressivligi, keng funktsionalligi va kutubxonalar va ramkalarning boy ekotizimi tufayli ko'plab ishlab chiquvchilar uchun mashhur tanlovdir."""
    await call.message.delete()
    await call.message.answer(text,reply_markup=ortga_ibtn)


# @dp.callback_query_handler(text="")
# async def ort_fun(call:types.CallbackQuery):
#     img=open("static/img/")
#     text=""""""
#     await call.message.delete()
#     await call.message.answer_photo(photo=img,caption=text,reply_markup=ort_ibtn)


@dp.callback_query_handler(text="noutbuk")
async def ort_fun(call:types.CallbackQuery):
    text="""👨🏻‍💻 Dasturlash uchun talab qilinadigan minimum noutbuk, agar yangi olmoqchi bo’lsangiz:

🔸 Kami bilan Core i5 (10-avlod) yoki AMD Ryzen 5 (Core i7 bo’lsa yaxshi)
🔸 Tezkor xotira RAM kami bilan 8GB (16 bo'lsa yaxshi)\- Asosiy Xotira SSD kami bilan 256 GB

💻 Agar Apple MacBook olmoqchi bo’lsangiz va pulingiz yetarli bo’lsa:

🔹 Kami bilan M1 Protsessor
🔹 Kami bilan 8GB RAM xotira
🔹 Kami bilan 256GB doimiy SSD xotira

🖥 Agar oldingi kompyuteringiz bo’lsa uning texnik holatini quyidagilarga keltirib olishingiz maqsadga muvofiq:

🔻 RAM xotira 8GB kamida;
🔻 Agar HDD xotira bo’lsa, uni kamida 256GB SSDga almashtirish yoki HDD yoniga o’rnatish"""
    await call.message.delete()
    await call.message.answer(text,reply_markup=ortga_ibtn)


@dp.callback_query_handler(text="backend")
async def kurs_fun(call:types.CallbackQuery):
    text="""📌 Python Foundation, Telegram Bot va Python Backend bo'yicha onlayn individual darslar

📚 Python Foundation bo'yicha darslar:
Python dasturlash tilini o'rganishni istaysizmi? Bizning individual onlayn darslarimiz orqali Python asoslarini mukammal o'zlashtirishingiz mumkin.

👨🏻‍💻 Telegram Bot yaratish bo'yicha darslar:
Telegram botlarini yaratishni o'rganmoqchimisiz? Bizning darslarimiz sizga Python yordamida kuchli va foydali Telegram botlarini yaratish bo'yicha bilim va ko'nikmalarni beradi.

🐍 Python Backend bo'yicha darslar:
Web-ilovalar va dasturiy tizimlarning orqa qismini yaratishni o'rganishni xohlaysizmi? Python backend dasturlarini ishlab chiqish bo'yicha individual darslarimiz sizga kerakli bilim va tajribani taqdim etadi."""
    img=open("static/img/pyt.jpg",'rb')
    await call.message.delete()
    await call.message.answer_photo(photo=img,caption=text,reply_markup=kurs_ibtn)

@dp.callback_query_handler(text="orqaga")
async def kurs_fun(call:types.CallbackQuery):
    text="""📌 Python Foundation, Telegram Bot va Python Backend bo'yicha onlayn individual darslar

📚 Python Foundation bo'yicha darslar:
Python dasturlash tilini o'rganishni istaysizmi? Bizning individual onlayn darslarimiz orqali Python asoslarini mukammal o'zlashtirishingiz mumkin.

👨🏻‍💻 Telegram Bot yaratish bo'yicha darslar:
Telegram botlarini yaratishni o'rganmoqchimisiz? Bizning darslarimiz sizga Python yordamida kuchli va foydali Telegram botlarini yaratish bo'yicha bilim va ko'nikmalarni beradi.

🐍 Python Backend bo'yicha darslar:
Web-ilovalar va dasturiy tizimlarning orqa qismini yaratishni o'rganishni xohlaysizmi? Python backend dasturlarini ishlab chiqish bo'yicha individual darslarimiz sizga kerakli bilim va tajribani taqdim etadi."""
    img=open("static/img/pyt.jpg",'rb')
    await call.message.delete()
    await call.message.answer_photo(photo=img,caption=text,reply_markup=kurs_ibtn)

@dp.message_handler(text=["🎓 Kurs haqida"])
async def oqish(message:types.Message):
    await message.answer(f"Sizga qaysi turdagi kurslarimiz qiziq???\nMarhamat quyidagilardan birini tanlshingiz mumkin!!! ",
                         reply_markup=oqish_ibtn)

@dp.callback_query_handler(text="menyu")
async def meny(call:types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"Sizga qaysi turdagi kurslarimiz qiziq???\nMarhamat quyidagilardan birini tanlshingiz mumkin!!! ",
                         reply_markup=oqish_ibtn)


@dp.callback_query_handler(text="frontend")
async def fron(call:types.CallbackQuery):
    img=open("static/img/fron.webp",'rb')
    text="""
🔊 Frontend haqida umumiy ma'lumot:
Frontend — bu veb-sayt yoki dasturiy ilovaning foydalanuvchi ko‘rishi va ishlatishi mumkin bo‘lgan qismidir. Foydalanuvchi interfeysi (UI) va foydalanuvchi tajribasi (UX) frontend orqali ta'minlanadi.

Frontendni tushunish uchun quyidagilarni bilish muhim:

✅ Frontend vazifalari:
Ko‘rinishni ta’minlash: Veb-sahifaning chiroyli va tartibli ko‘rinishi.
Interaktivlikni qo‘shish: Sahifani foydalanuvchi bilan muloqot qiladigan qilib qilish (tugmalar, shakllar va boshqalar).
Moslashuvchan dizayn: Turli qurilmalarda (kompyuter, planshet, telefon) yaxshi ishlaydigan sahifa yaratish.

👨‍💻 Frontend dasturchi nima qiladi?
Sayt dizaynini kodga aylantiradi.
Saytni barcha qurilmalarga moslashtiradi (responsiveness).
JavaScript yordamida saytga funksiyalar qo‘shadi.
Backend bilan bog‘liq bo‘lgan ma’lumotlarni foydalanuvchiga chiqaradi.
"""
    await call.message.delete()
    await call.message.answer_photo(photo=img,caption=text,reply_markup=ort_ibtn)

@dp.callback_query_handler(text="xacker")
async def xac(call:types.CallbackQuery):
    img=open("static/img/xacker.jpg",'rb')
    text="""
🦠 Kiberxavfsizlik haqida umumiy tushuncha
Kiberxavfsizlik — bu axborotni, kompyuter tizimlarini va tarmoqlarni kiberhujumlardan himoya qilish bo‘yicha tadbirlar majmuidir. Kiberxavfsizlik maqsadi — axborot maxfiyligini, yaxlitligini va mavjudligini ta'minlashdir (CIA triadasi).

🎯 Kiberxavfsizlikning asosiy yo‘nalishlari:
Tarmoqlar xavfsizligi (Network Security):

Tarmoq orqali ma'lumotlarning uzatilishini himoya qilish.
Xavfli trafikni aniqlash va to‘sish uchun firewall va IDS/IPS tizimlari qo‘llanadi.
Axborot xavfsizligi (Information Security):

Ma'lumotlarning maxfiyligini, yaxlitligini va mavjudligini ta'minlash.
Shifrlash (encryption) va autentifikatsiya usullaridan foydalaniladi.
Veb xavfsizligi (Web Security):

💸 Kiberxavfsizlik bo‘yicha kasblar:
Etik xaker (Ethical Hacker)
Kiberxavfsizlik bo‘yicha mutaxassis (Cybersecurity Specialist)
Tarmoq xavfsizligi muhandisi (Network Security Engineer)
Axborot xavfsizligi bo‘yicha analitik (Information Security Analyst)
Malware tahlilchisi (Malware Analyst)"""
    await call.message.delete()
    await call.message.answer_photo(photo=img,caption=text,reply_markup=ort_ibtn)

@dp.callback_query_handler(text="tillar")
async def til(call:types.CallbackQuery):
    img=open("static/img/engliz.jpg",'rb')
    text="""
📝 Ingliz tili kursining asosiy maqsadlari:
Speaking (Suhbat qurish):
Foydalanuvchilarni muloqot qilishga o‘rgatish. Asosiy e’tibor talaffuz va ravonlikka qaratiladi.

🎧 Listening (Tinglab tushunish):
Ingliz tilida gaplashuvchi odamlarni tushunish ko‘nikmasini rivojlantirish.

Writing (Yozish):
O‘z fikrlarini yozma shaklda ifoda qilishni o‘rgatish.

🗣 Ingliz tilida sodda gaplarni tushunish va gapirish.
Oddiy kundalik iboralarni o‘rgatish.
Elementary (Boshlang‘ichdan yuqori):

🏆 Grammatikaning asosiy qoidalari va so‘z boyligini oshirish.
Intermediate (O‘rta):

Matnlar, suhbatu maqolalarni mustaqil tushunish va muhokama qilish.
Advanced (Yuqori):

Murakkab mavzularda gapirish va yozish ko‘nikmasini rivojlantirish.
Qo‘shimcha imkoniyatlar:
IELTS yoki TOEFL tayyorlov kurslari:
Akademik yoki xalqaro sertifikat olishni maqsad qilgan talabalar uchun maxsus darslar. """
    await call.message.delete()
    await call.message.answer_photo(photo=img,caption=text,reply_markup=ort_ibtn)


@dp.message_handler(text=["📝 Kursga ro'yhatdan o'tish"])
async def register_hand(message:types.Message):
    await message.answer("Ro'yhatdan o'tish boshlandi!")
    await message.answer("Ism familiyangizni kiriting: ")








if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)