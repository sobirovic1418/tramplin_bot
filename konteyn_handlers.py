from aiogram.types import ContentType,Message
from main import dp
from pathlib import Path

# kelGAN hujjjat (rasm,video,audio...)download papkasiga tushadi
download_path=Path().joinpath("downloads","categories")
download_path.mkdir(parents=True,exist_ok=True)


@dp.message_handler(content_types=ContentType.PHOTO)
async def img_handlers(message: Message):
    await message.answer("Bu qanday rasm?")


@dp.message_handler(content_types=ContentType.DOCUMENT)
async def doc_handlers(message: Message):
    await message.document.download(destination=download_path)
    doc_id=message.document.file_id
    await message.reply(f"Siz hujjat yubordingiz!\nfile_id={doc_id}")

@dp.message_handler(content_types=ContentType.VOICE)
async def ovoz_handlers(message: Message):
    await message.voice.download(destination=download_path)
    await message.answer("Ovozni anglamadim!!!")


@dp.message_handler(content_types=ContentType.VIDEO)
async def video_handlers(message: Message):
    await message.video.download(destination=download_path)
    await message.answer(f"Siz yuborgan video qabul qilindi\nfile_id={message.video.file_id}")