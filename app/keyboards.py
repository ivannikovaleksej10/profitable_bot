from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Информация')],
                                     [KeyboardButton(text='Личная статистика')]],
                            resize_keyboard=True, input_field_placeholder='Сколько ты сегодня заработал?')