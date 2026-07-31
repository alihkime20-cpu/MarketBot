from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message):
    keyboard = InlineKeyboardBuilder()

    keyboard.button(
        text="🛍️ مشتري",
        callback_data="buyer"
    )

    keyboard.button(
        text="🏪 أريد البيع",
        callback_data="seller_request"
    )

    keyboard.adjust(1)

    await message.answer(
        "🛒 أهلاً بك في سوقنا الإلكتروني\n\n"
        "اختر طريقة الاستخدام:",
        reply_markup=keyboard.as_markup()
    )
