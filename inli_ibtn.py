from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

kurs_ibtn=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Foundation 🎯",callback_data="foun")
        ],
        [
            InlineKeyboardButton(text="Telegram Bot 🤖",callback_data="telegram")
        ],
        [
            InlineKeyboardButton(text="Python Backend 🦾",callback_data="python")
        ],
        [
            InlineKeyboardButton(text="Kerakli noutbuklar 💻",callback_data="noutbuk")
        ],
        [
            InlineKeyboardButton(text=" 🔙 ",callback_data="menyu")
        ]
    ]
)
oqish_ibtn=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🦾 Backend",callback_data="backend"),
            InlineKeyboardButton(text="🕹 Frontend",callback_data="frontend")
        ],
        [
            InlineKeyboardButton(text="🪙 Kiberxavsizlik",callback_data="xacker"),
            InlineKeyboardButton(text="🚩 English va Rus tillari",callback_data="tillar")
        ],
    ]
)
ortga_ibtn=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Back ↩️",callback_data="orqaga")
        ]
    ]
)
ort_ibtn=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=" 🔙 ",callback_data="menyu")
        ]
    ]
)
korzinka_ibtn=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text=" 🗑 ",callback_data="uchirish")
        ]
    ]
)
