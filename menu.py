from telebot import types
import settings
import main
import requests

#################################################################################  BY LEEKMAY ##########################################################################################################


btn1 = types.InlineKeyboardButton(text='🔥 Прогресс', callback_data='info_access')                    # +
btn2 = types.InlineKeyboardButton(text='🏡 Профиль', callback_data='profile')                          # +
btn3 = types.InlineKeyboardButton(text='ℹ️ Справка', callback_data='access_no_info')   
btn4 = types.InlineKeyboardButton(text="❓Поддержка", url='t.me/')                 # +                              
btn5 = types.InlineKeyboardButton(text="🎁 Пригласить друзей", url='t.me/')                        # 
menu_access_no = types.InlineKeyboardMarkup(row_width=2)
menu_access_no.add(btn1, btn2, btn3, btn4, btn5)


menu_access_yes = types.InlineKeyboardMarkup(row_width=2)
menu_access_yes.add(
    types.InlineKeyboardButton(text='🏡 Профиль', callback_data='profile'),                                # +               
    types.InlineKeyboardButton(text='💰 Вывод средств', callback_data='order_payout'),                 # +
    types.InlineKeyboardButton(text='⚙Тех. Поддержка', callback_data='support_yes')                      # -
)

menu_admin = types.InlineKeyboardMarkup(row_width=2)
menu_admin.add(
    types.InlineKeyboardButton(text='📝Информация', callback_data='admin_info'),                          # +
    types.InlineKeyboardButton(text='📝Запросы на вывод', callback_data='admin_list_order_payment'),      # +
    types.InlineKeyboardButton(text='💰✅Прибыль', callback_data='admin_profit'),                           # +
    types.InlineKeyboardButton(text='❌Выйти из админки', callback_data='go_main_menu')                   # +
)

btn_close = types.InlineKeyboardMarkup(row_width=3)
btn_close.add(
    types.InlineKeyboardButton(text='❌', callback_data='close')
)

menu_info_access = types.InlineKeyboardMarkup(row_width=3)
menu_info_access.add(
    types.InlineKeyboardButton(text='🔥 Повысить уровень', callback_data='buy_access'),
    types.InlineKeyboardButton(text='❌Назад', callback_data='cancel_payment')
)

menu_buy_access = types.InlineKeyboardMarkup(row_width=3)
menu_buy_access.add(
    types.InlineKeyboardButton(text='🔄 Проверить оплату', callback_data='check_payment'),
    types.InlineKeyboardButton(text='❌Отменить покупку', callback_data='cancel_payment')
)

btn_back_to_admin_menu = types.InlineKeyboardMarkup(row_width=3)
btn_back_to_admin_menu.add(
    types.InlineKeyboardButton(text='Вернуться в админ меню', callback_data='back_to_admin_menu')
)

admin_order_info = types.InlineKeyboardMarkup(row_width=3)
admin_order_info.add(
    types.InlineKeyboardButton(text='Удалить из списка', callback_data='del_order'),
    types.InlineKeyboardButton(text='Выйти', callback_data='back_to_admin_menu')
)

#################################################################################  BY LEEKMAY ##########################################################################################################