from aiogram import Router, types, F
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


@router.callback_query(F.data == "buyer")
async def buyer_handler(callback: types.CallbackQuery):
    await callback.message.answer(
        "🛍️ أنت الآن كمشتري\n\n"
        "يمكنك تصفح المنتجات عند إضافة نظام المنتجات."
    )
    await callback.answer()


@router.callback_query(F.data == "seller_request")
async def seller_request_handler(callback: types.CallbackQuery):
    await callback.message.answer(
        "🏪 طلب فتح متجر\n\n"
        "سيتم إرسال طلبك إلى الإدارة للموافقة."
    )
    await callback.answer()
