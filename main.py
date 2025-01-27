from head_fun import dp
from aiogram import types,executor

from inli_ibtn import kurs_ibtn, oqish_ibtn, ortga_ibtn
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
    await message.answer_photo(photo=img,caption=text)


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

# @dp.callback_query_handler(text="orqaga")
# async def ort_fun(call:types.CallbackQuery):
#     text=""""""
#     await call.message.delete()
#     await call.message.answer("Tanlang 👇")


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





@dp.message_handler(text=["📝 Kursga ro'yhatdan o'tish"])
async def register_hand(message:types.Message):
    await message.answer("Ro'yhatdan o'tish boshlandi!")
    await message.answer("Ism familiyangizni kiriting: ")








if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)