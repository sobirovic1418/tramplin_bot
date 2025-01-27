from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

start_btn=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🎓 Kurs haqida"),
            KeyboardButton("📝 Kursga ro'yhatdan o'tish")
        ],
        [
            KeyboardButton("👨‍💻 My school")
        ]
    ],
    resize_keyboard=True
)
