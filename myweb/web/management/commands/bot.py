# from django.core.management.base import BaseCommand
# from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
# from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler
# from web.models import BotUser
#
# # Constants for languages and states
# LANG_SELECTION = 'lang_selection'
# CONTACT_REQUEST = 'contact_request'
#
# LANGUAGES = {
#
#     'English': 1,
#     'Русский': 2,
#     'O\'zbek': 3
# }
#
# WELCOME_TEXT = "Welcome to the bot!"
# CHOOSE_LANG = "Please choose your language:"
#
# TEXT_ENTER_CONTACT = {
#     1: "Would you like to share your contact information?",
#     2: "Вы хотите поделиться своей контактной информацией?",
#     3: "Sizning kontakt ma'lumotlaringizni bo'lishishni xohlaysizmi?"
# }
#
# BTN_SEND_CONTACT = {
#     1: "Yes, send my contact",
#     2: "Да, отправить мой контакт",
#     3: "Ha, mening kontaktimni yuboring"
# }
#
# BTN_SKIP_CONTACT = {
#     1: "No, skip",
#     2: "Нет, пропустить",
#     3: "Yo'q, o'tkazib yuboring"
# }
#
# BTN_COMMENTS_SAVE1 = {
#     1: "Thank you! Your contact has been saved.",
#     2: "Спасибо! Ваш контакт был сохранен.",
#     3: "Rahmat! Sizning kontaktingiz saqlandi."
# }
#
# MAIN_MENU_TEXT = {
#     1: "Main Menu",
#     2: "Главное меню",
#     3: "Asosiy menyu"
# }
# BTN_COMPLAINT = {
#     1: "Complaint",
#     2: "Жалоба",
#     3: "Shikoyat"
# }
# BTN_OFFERS = {
#     1: "Offers",
#     2: "Предложения",
#     3: "Takliflar"
# }
# BTN_EVALUATION = {
#     1: "Evaluation",
#     2: "Оценка",
#     3: "Baholash"
# }
#
# TOKEN  =  "6165627762:AAG7JVbFQxH_xi61znhoXIOn5TC0UoH3iJA"
#
#
# class Command(BaseCommand):
#     help = 'Starts the Telegram bot'
#
#     def handle(self, *args, **kwargs):
#         updater = Updater(TOKEN, use_context=True)
#         dp = updater.dispatcher
#
#         dp.add_handler(CommandHandler('start', self.start))
#         dp.add_handler(MessageHandler(Filters.text | Filters.contact, self.message_handler))
#
#         updater.start_polling()
#         updater.idle()
#
#     def start(self, update: Update, context: CallbackContext):
#         self.check_user_and_initialize(update, context)
#
#     def check_user_and_initialize(self, update: Update, context: CallbackContext):
#         user = update.message.from_user
#         chat_id = user.id
#
#         db_user, created = BotUser.objects.get_or_create(chat_id=chat_id)
#
#         if not db_user.lang_id:
#             buttons = [
#                 [KeyboardButton(text="English"), KeyboardButton(text="Русский"), KeyboardButton(text="O'zbek")]
#             ]
#             update.message.reply_text(
#                 text=CHOOSE_LANG,
#                 reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
#             )
#             context.user_data['state'] = LANG_SELECTION
#
#         elif not db_user.phone_number:
#             buttons = [
#                 [KeyboardButton(text=BTN_SEND_CONTACT[db_user.lang_id], request_contact=True)],
#                 [KeyboardButton(text=BTN_SKIP_CONTACT[db_user.lang_id])]
#             ]
#             update.message.reply_text(
#                 text=TEXT_ENTER_CONTACT[db_user.lang_id],
#                 reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
#             )
#             context.user_data['state'] = CONTACT_REQUEST
#         else:
#             self.send_main_menu(update, context, db_user.lang_id)
#
#
#     def message_handler(self, update: Update, context: CallbackContext):
#         user = update.message.from_user
#         chat_id = user.id
#         db_user = BotUser.objects.get(chat_id=chat_id)
#
#         if context.user_data.get('state') == LANG_SELECTION:
#             lang = update.message.text
#             if lang in LANGUAGES:
#                 db_user.lang_id = LANGUAGES[lang]
#                 db_user.save()
#                 context.user_data['state'] = CONTACT_REQUEST
#                 buttons = [
#                     [KeyboardButton(text=BTN_SEND_CONTACT[db_user.lang_id], request_contact=True)],
#                     [KeyboardButton(text=BTN_SKIP_CONTACT[db_user.lang_id])]
#                 ]
#                 update.message.reply_text(
#                     text=TEXT_ENTER_CONTACT[db_user.lang_id],
#                     reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
#                 )
#
#         elif context.user_data.get('state') == CONTACT_REQUEST:
#             if update.message.contact:
#                 db_user.phone_number = update.message.contact.phone_number
#                 db_user.save()
#                 update.message.reply_text(
#                     text=BTN_COMMENTS_SAVE1[db_user.lang_id],
#                     reply_markup=ReplyKeyboardRemove()
#                 )
#             else:
#                 update.message.reply_text(
#                     text="No problem! You have chosen not to share your contact.",
#                     reply_markup=ReplyKeyboardRemove()
#                 )
#             self.send_main_menu(update, context, db_user.lang_id)
#
#     def send_main_menu(self, update: Update, context: CallbackContext, lang_id: int):
#         buttons = [
#             [KeyboardButton(text=BTN_COMPLAINT[lang_id]), KeyboardButton(text=BTN_OFFERS[lang_id]), KeyboardButton(text=BTN_EVALUATION[lang_id])]
#         ]
#         update.message.reply_text(
#             text=MAIN_MENU_TEXT[lang_id],
#             reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
#         )


# from django.core.management.base import BaseCommand
# from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
# from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler
# from web.models import BotUser
#
# # Constants for languages and states
# LANG_SELECTION = 'lang_selection'
# CONTACT_REQUEST = 'contact_request'
# MAIN_MENU = 'main_menu'
#
# LANGUAGES = {
#     'English': 1,
#     'Русский': 2,
#     'O\'zbek': 3
# }
#
# WELCOME_TEXT = "Welcome to the bot!"
# CHOOSE_LANG = "Please choose your language:"
# TEXT_ENTER_CONTACT = {
#     1: "Would you like to share your contact information?",
#     2: "Вы хотите поделиться своей контактной информацией?",
#     3: "Sizning kontakt ma'lumotlaringizni bo'lishishni xohlaysizmi?"
# }
# BTN_SEND_CONTACT = {
#     1: "Yes, send my contact",
#     2: "Да, отправить мой контакт",
#     3: "Ha, mening kontaktimni yuboring"
# }
# BTN_SKIP_CONTACT = {
#     1: "No, skip",
#     2: "Нет, пропустить",
#     3: "Yo'q, o'tkazib yuboring"
# }
# BTN_COMMENTS_SAVE1 = {
#     1: "Thank you! Your contact has been saved.",
#     2: "Спасибо! Ваш контакт был сохранен.",
#     3: "Rahmat! Sizning kontaktingiz saqlandi."
# }
# MAIN_MENU_TEXT = {
#     1: "Main Menu",
#     2: "Главное меню",
#     3: "Asosiy menyu"
# }
# BTN_CHANGE_LANG = {
#     1: "Change Language",
#     2: "Сменить язык",
#     3: "Tilni o'zgartirish"
# }
# BTN_COMPLAINT = {
#     1: "Complaint",
#     2: "Жалоба",
#     3: "Shikoyat"
# }
# BTN_OFFERS = {
#     1: "Offers",
#     2: "Предложения",
#     3: "Takliflar"
# }
# BTN_EVALUATION = {
#     1: "Evaluation",
#     2: "Оценка",
#     3: "Baholash"
# }
#
# TOKEN  =  "6165627762:AAG7JVbFQxH_xi61znhoXIOn5TC0UoH3iJA"
#
# class Command(BaseCommand):
#     help = 'Starts the Telegram bot'
#
#     def handle(self, *args, **kwargs):
#         updater = Updater(TOKEN, use_context=True)
#         dp = updater.dispatcher
#
#         dp.add_handler(CommandHandler('start', self.start))
#         dp.add_handler(MessageHandler(Filters.text | Filters.contact, self.message_handler))
#
#         updater.start_polling()
#         updater.idle()
#
#     def start(self, update: Update, context: CallbackContext):
#         self.check_user_and_initialize(update, context)
#
#     def check_user_and_initialize(self, update: Update, context: CallbackContext):
#         user = update.message.from_user
#         chat_id = user.id
#
#         db_user, created = BotUser.objects.get_or_create(chat_id=chat_id)
#
#         if not db_user.lang_id:
#             buttons = [
#                 [KeyboardButton(text="English"), KeyboardButton(text="Русский"), KeyboardButton(text="O'zbek")]
#             ]
#             update.message.reply_text(
#                 text=CHOOSE_LANG,
#                 reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
#             )
#             context.user_data['state'] = LANG_SELECTION
#         elif not db_user.phone_number:
#             buttons = [
#                 [KeyboardButton(text=BTN_SEND_CONTACT[db_user.lang_id], request_contact=True)],
#                 [KeyboardButton(text=BTN_SKIP_CONTACT[db_user.lang_id])]
#             ]
#             update.message.reply_text(
#                 text=TEXT_ENTER_CONTACT[db_user.lang_id],
#                 reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
#             )
#             context.user_data['state'] = CONTACT_REQUEST
#         else:
#             self.send_main_menu(update, context, db_user.lang_id)
#
#     def message_handler(self, update: Update, context: CallbackContext):
#         user = update.message.from_user
#         chat_id = user.id
#         db_user = BotUser.objects.get(chat_id=chat_id)
#
#         state = context.user_data.get('state')
#
#         if state == LANG_SELECTION:
#             lang = update.message.text
#             if lang in LANGUAGES:
#                 db_user.lang_id = LANGUAGES[lang]
#                 db_user.save()
#                 context.user_data['state'] = CONTACT_REQUEST
#                 buttons = [
#                     [KeyboardButton(text=BTN_SEND_CONTACT[db_user.lang_id], request_contact=True)],
#                     [KeyboardButton(text=BTN_SKIP_CONTACT[db_user.lang_id])]
#                 ]
#                 update.message.reply_text(
#                     text=TEXT_ENTER_CONTACT[db_user.lang_id],
#                     reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
#                 )
#         elif state == CONTACT_REQUEST:
#             if update.message.contact:
#                 db_user.phone_number = update.message.contact.phone_number
#                 db_user.save()
#                 update.message.reply_text(
#                     text=BTN_COMMENTS_SAVE1[db_user.lang_id],
#                     reply_markup=ReplyKeyboardRemove()
#                 )
#             else:
#                 update.message.reply_text(
#                     text="No problem! You have chosen not to share your contact.",
#                     reply_markup=ReplyKeyboardRemove()
#                 )
#             self.send_main_menu(update, context, db_user.lang_id)
#
#
#         elif state == MAIN_MENU:
#             text = update.message.text
#             if text == BTN_CHANGE_LANG[db_user.lang_id]:
#                 context.user_data['state'] = LANG_SELECTION
#                 # Implement language change functionality
#             elif text == BTN_SUGGESTION[db_user.lang_id]:
#                 context.user_data['state'] = SUGGESTION_REQUEST
#                 update.message.reply_text(
#                     text=SUGGESTION_REQUEST_TEXT[db_user.lang_id],
#                     reply_markup=ReplyKeyboardRemove()
#                 )
#             elif text == BTN_COMPLAINT[db_user.lang_id]:
#                 context.user_data['state'] = COMPLAINT_REQUEST
#                 update.message.reply_text(
#                     text=COMPLAINT_REQUEST_TEXT[db_user.lang_id],
#                     reply_markup=ReplyKeyboardRemove()
#                 )
#             else:
#                 update.message.reply_text(
#                     text=f"You said: {text}. Implement other functionalities as needed."
#                 )
#
#         elif state == SUGGESTION_REQUEST:
#             suggestion_text = update.message.text
#             Suggestion.objects.create(user=db_user, text=suggestion_text)
#             update.message.reply_text(
#                 text=BTN_SUGGESTION_SAVE[db_user.lang_id],
#                 reply_markup=ReplyKeyboardRemove()
#             )
#             self.send_main_menu(update, context, db_user.lang_id)
#
#         elif state == COMPLAINT_REQUEST:
#             complaint_text = update.message.text
#             Complaint.objects.create(user=db_user, text=complaint_text)
#             update.message.reply_text(
#                 text=BTN_COMPLAINT_SAVE[db_user.lang_id],
#                 reply_markup=ReplyKeyboardRemove()
#             )
#             self.send_main_menu(update, context, db_user.lang_id)
#
#
#
#
#         else:
#             # Handle main menu and other functionalities here
#             text = update.message.text
#             if text == BTN_CHANGE_LANG[db_user.lang_id]:
#                 context.user_data['state'] = LANG_SELECTION
#                 buttons = [
#                     [KeyboardButton(text="English"), KeyboardButton(text="Русский"), KeyboardButton(text="O'zbek")]
#                 ]
#                 update.message.reply_text(
#                     text=CHOOSE_LANG,
#                     reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
#                 )
#             else:
#                 update.message.reply_text(
#                     text=f"You said: {text}. Implement other functionalities as needed."
#                 )
#
#     def send_main_menu(self, update: Update, context: CallbackContext, lang_id: int):
#         buttons = [
#             [KeyboardButton(text=BTN_COMPLAINT[lang_id]), KeyboardButton(text=BTN_OFFERS[lang_id]), KeyboardButton(text=BTN_EVALUATION[lang_id])],
#             [KeyboardButton(text=BTN_CHANGE_LANG[lang_id])]
#         ]
#         update.message.reply_text(
#             text=MAIN_MENU_TEXT[lang_id],
#             reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True)
#         )
#         context.user_data['state'] = MAIN_MENU


# from django.core.management.base import BaseCommand
# from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
# from web.models import *
#
# # Constants and text messages
# WELCOME_TEXT = "Welcome to the bot! Please choose your language."
# CHOOSE_LANG = "Please choose your language:"
#
# BTN_LANG_UZ = "Uzbek"
# BTN_LANG_EN = "English"
# BTN_LANG_RU = "Russian"
#
# BTN_SEND_CONTACT = ["Send Contact", "Skip"]
# BTN_MAIN_MENU = ["Change Language", "Submit Suggestion", "Complaint"]
# SUGGESTION_REQUEST_TEXT = "Please enter your suggestion:"
# SUGGESTION_SAVE_TEXT = "Thank you for your suggestion!"
#
#
# Complaint_REQUEST_TEXT = "Please enter your Complaint:"
# Complaint_SAVE_TEXT = "Thank you for your complaint!"
#
# TOKEN  =  "6165627762:AAG7JVbFQxH_xi61znhoXIOn5TC0UoH3iJA"
#
# class Command(BaseCommand):
#     help = 'Starts the Telegram bot'
#
#     def handle(self, *args, **kwargs):
#         updater = Updater(TOKEN, use_context=True)
#         dp = updater.dispatcher
#
#         dp.add_handler(CommandHandler('start', self.start))
#         dp.add_handler(MessageHandler(Filters.text | Filters.contact, self.message_handler))
#
#         updater.start_polling()
#         updater.idle()
#
#     def start(self, update: Update, context: CallbackContext):
#         chat_id = update.message.chat_id
#         db_user, created = BotUser.objects.get_or_create(chat_id=chat_id)
#
#         if created or not db_user.lang_id:
#             buttons = [
#                 [KeyboardButton(text=BTN_LANG_UZ), KeyboardButton(text=BTN_LANG_EN), KeyboardButton(text=BTN_LANG_RU)]]
#             update.message.reply_text(text=WELCOME_TEXT)
#             update.message.reply_text(text=CHOOSE_LANG, reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
#             context.user_data["state"] = "choose_lang"
#
#         elif not db_user.phone_number:
#             self.ask_for_contact(update, context)
#         else:
#             self.send_main_menu(update, context, db_user.lang_id)
#
#
#
#     def ask_for_contact(self, update: Update, context: CallbackContext):
#
#         buttons = [
#             [KeyboardButton(text=BTN_SEND_CONTACT[0], request_contact=True), KeyboardButton(text=BTN_SEND_CONTACT[1])]]
#         update.message.reply_text("Please provide your contact or skip:",
#                                   reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
#         context.user_data["state"] = "get_contact"
#
#
#     def send_main_menu(self, update: Update, context: CallbackContext, lang_id):
#         update.message.reply_text("Main Menu:",
#                                   reply_markup=ReplyKeyboardMarkup([[BTN_MAIN_MENU[0]], [BTN_MAIN_MENU[1]], [BTN_MAIN_MENU[2]]],
#                                                                    resize_keyboard=True))
#         context.user_data["state"] = "main_menu"
#
#
#     def message_handler(self, update: Update, context: CallbackContext):
#         chat_id = update.message.chat_id
#         db_user = BotUser.objects.get(chat_id=chat_id)
#         state = context.user_data.get("state")
#
#         if state == "choose_lang":
#             lang = update.message.text
#             if lang == BTN_LANG_UZ:
#                 db_user.lang_id = 1
#             elif lang == BTN_LANG_EN:
#                 db_user.lang_id = 2
#             elif lang == BTN_LANG_RU:
#                 db_user.lang_id = 3
#
#             db_user.save()
#             self.ask_for_contact(update, context)
#
#
#
#         elif state == "get_contact":
#             if update.message.contact:
#                 db_user.phone_number = update.message.contact.phone_number
#                 db_user.save()
#
#
#                 self.send_main_menu(update, context, db_user.lang_id)
#
#             elif update.message.text == BTN_SEND_CONTACT[1]:
#                 self.send_main_menu(update, context, db_user.lang_id)
#
#         elif state == "main_menu":
#             if update.message.text == BTN_MAIN_MENU[0]:
#                 buttons = [[KeyboardButton(text=BTN_LANG_UZ), KeyboardButton(text=BTN_LANG_EN),
#                             KeyboardButton(text=BTN_LANG_RU)]]
#                 update.message.reply_text(text=CHOOSE_LANG,
#                                           reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
#                 context.user_data["state"] = "choose_lang"
#
#
#             elif update.message.text == BTN_MAIN_MENU[1]:
#                 update.message.reply_text(text=SUGGESTION_REQUEST_TEXT, reply_markup=ReplyKeyboardRemove())
#                 context.user_data["state"] = "submit_suggestion"
#
#
#             elif update.message.text == BTN_MAIN_MENU[2]:
#                 update.message.reply_text(text=Complaint_REQUEST_TEXT, reply_markup=ReplyKeyboardRemove())
#                 context.user_data["state"] = "submit_complaint"
#
#
#
#         elif state == "submit_suggestion":
#             Suggestion.objects.create(user=db_user, text=update.message.text)
#             update.message.reply_text(text=SUGGESTION_SAVE_TEXT, reply_markup=ReplyKeyboardRemove())
#             self.send_main_menu(update, context, db_user.lang_id)
#
#
#         elif state == "submit_complaint":
#             Complaint.objects.create(user=db_user, text=update.message.text)
#             update.message.reply_text(text=Complaint_SAVE_TEXT, reply_markup=ReplyKeyboardRemove())
#             self.send_main_menu(update, context, db_user.lang_id)


# from django.core.management.base import BaseCommand
# from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, \
#     InlineKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
# from web.models import BotUser, Suggestion, Complaint

# # Constants and text messages
# WELCOME_TEXT = "Welcome to the bot! Please choose your language."
# CHOOSE_LANG = "Please choose your language:"
# BTN_LANG_UZ = "Uzbek"
# BTN_LANG_EN = "English"
# BTN_LANG_RU = "Russian"
# BTN_SEND_CONTACT = ["Send Contact", "Skip"]
#
# BTN_MAIN_MENU = ["Change Language", "Submit Suggestion", "Submit Complaint"]
# SUGGESTION_REQUEST_TEXT = "Please enter your suggestion:"
# SUGGESTION_SAVE_TEXT = "Thank you for your suggestion!"
# COMPLAINT_REQUEST_LOCATION = "Please share your location for the complaint:"
# COMPLAINT_REQUEST_PHOTO = "Please send a photo for the complaint:"
# COMPLAINT_SAVE_TEXT = "Thank you for your complaint!"
#
# TOKEN  =  "6165627762:AAG7JVbFQxH_xi61znhoXIOn5TC0UoH3iJA"
#
# class Command(BaseCommand):
#     help = 'Starts the Telegram bot'
#
#     def handle(self, *args, **kwargs):
#         updater = Updater(TOKEN, use_context=True)
#         dp = updater.dispatcher
#
#         dp.add_handler(CommandHandler('start', self.start))
#         dp.add_handler(
#             MessageHandler(Filters.text | Filters.contact | Filters.location | Filters.photo, self.message_handler))
#
#         updater.start_polling()
#         updater.idle()
#
#     def start(self, update: Update, context: CallbackContext):
#         chat_id = update.message.chat_id
#         db_user, created = BotUser.objects.get_or_create(chat_id=chat_id)
#
#         if created or not db_user.lang_id:
#             buttons = [
#                 [KeyboardButton(text=BTN_LANG_UZ), KeyboardButton(text=BTN_LANG_EN), KeyboardButton(text=BTN_LANG_RU)]]
#             update.message.reply_text(text=WELCOME_TEXT)
#             update.message.reply_text(text=CHOOSE_LANG, reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
#             context.user_data["state"] = "choose_lang"
#
#
#         elif not db_user.phone_number:
#             self.ask_for_contact(update, context)
#         else:
#             self.send_main_menu(update, context, db_user.lang_id)
#
#     def ask_for_contact(self, update: Update, context: CallbackContext):
#
#         buttons = [
#             [KeyboardButton(text=BTN_SEND_CONTACT[0], request_contact=True), KeyboardButton(text=BTN_SEND_CONTACT[1])]]
#         update.message.reply_text("Please provide your contact or skip:",
#                                   reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
#         context.user_data["state"] = "get_contact"
#
#
#     def send_main_menu(self, update: Update, context: CallbackContext, lang_id):
#         buttons = [[BTN_MAIN_MENU[0]], [BTN_MAIN_MENU[1]], [BTN_MAIN_MENU[2]]]
#         update.message.reply_text("Main Menu:", reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
#         context.user_data["state"] = "main_menu"
#
#     def message_handler(self, update: Update, context: CallbackContext):
#         chat_id = update.message.chat_id
#         db_user = BotUser.objects.get(chat_id=chat_id)
#         state = context.user_data.get("state")
#
#         if state == "choose_lang":
#             lang = update.message.text
#             if lang == BTN_LANG_UZ:
#                 db_user.lang_id = 1
#             elif lang == BTN_LANG_EN:
#                 db_user.lang_id = 2
#             elif lang == BTN_LANG_RU:
#                 db_user.lang_id = 3
#             db_user.save()
#             self.ask_for_contact(update, context)
#
#         elif state == "get_contact":
#             if update.message.contact:
#                 db_user.phone_number = update.message.contact.phone_number
#                 db_user.save()
#                 self.send_main_menu(update, context, db_user.lang_id)
#             elif update.message.text == BTN_SEND_CONTACT[1]:
#                 self.send_main_menu(update, context, db_user.lang_id)
#
#         elif state == "main_menu":
#             if update.message.text == BTN_MAIN_MENU[0]:
#                 buttons = [[KeyboardButton(text=BTN_LANG_UZ), KeyboardButton(text=BTN_LANG_EN),
#                             KeyboardButton(text=BTN_LANG_RU)]]
#                 update.message.reply_text(text=CHOOSE_LANG,
#                                           reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
#                 context.user_data["state"] = "choose_lang"
#             elif update.message.text == BTN_MAIN_MENU[1]:
#                 update.message.reply_text(text=SUGGESTION_REQUEST_TEXT, reply_markup=ReplyKeyboardRemove())
#                 context.user_data["state"] = "submit_suggestion"
#
#             elif update.message.text == BTN_MAIN_MENU[2]:
#                 update.message.reply_text(text=COMPLAINT_REQUEST_LOCATION, reply_markup=ReplyKeyboardRemove())
#                 context.user_data["state"] = "get_complaint_location"
#
#         elif state == "submit_suggestion":
#             Suggestion.objects.create(user=db_user, text=update.message.text)
#             update.message.reply_text(text=SUGGESTION_SAVE_TEXT, reply_markup=ReplyKeyboardRemove())
#             self.send_main_menu(update, context, db_user.lang_id)
#
#         elif state == "get_complaint_location":
#             if update.message.location:
#                 context.user_data["complaint_location"] = f"{update.message.location.latitude},{update.message.location.longitude}"
#                 update.message.reply_text(text="Please enter the area:")
#                 context.user_data["state"] = "get_complaint_area"
#             else:
#                 update.message.reply_text(text="Please share your location:")
#
#         elif state == "get_complaint_area":
#             context.user_data["complaint_area"] = update.message.text
#             update.message.reply_text(text=COMPLAINT_REQUEST_PHOTO)
#             context.user_data["state"] = "get_complaint_photo"
#
#         elif state == "get_complaint_photo":
#             if update.message.photo:
#                 photo = update.message.photo[-1].get_file().download()
#                 Complaint.objects.create(
#                     user=db_user,
#                     location=context.user_data["complaint_location"],
#                     area=context.user_data["complaint_area"],
#                     photo=photo,
#                     coordinates=f"{update.message.location.latitude},{update.message.location.longitude}"
#                 )
#
#                 update.message.reply_text(text=COMPLAINT_SAVE_TEXT, reply_markup=ReplyKeyboardRemove())
#                 self.send_main_menu(update, context, db_user.lang_id)
#             else:
#                 update.message.reply_text(text="Please send a photo:")
#

from django.core.management.base import BaseCommand
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from web.models import BotUser, Suggestion, Complaint, Categories
import os

# Constants
WELCOME_TEXT = "Welcome to the bot! Please choose your language."
CHOOSE_LANG = "Please choose your language:"
BTN_LANG_UZ = "Uzbek"
BTN_LANG_EN = "English"
BTN_LANG_RU = "Russian"
BTN_SEND_CONTACT = ["Send Contact", "Skip"]
BTN_MAIN_MENU = ["Change Language", "Submit Suggestion", "Submit Complaint", "Evaluate"]
SUGGESTION_REQUEST_TEXT = "Please enter your suggestion:"
SUGGESTION_SAVE_TEXT = "Thank you for your suggestion!"
COMPLAINT_REQUEST_LOCATION = "Please share your location for the complaint:"
COMPLAINT_REQUEST_AREA = "Please enter the area for the complaint:"
COMPLAINT_REQUEST_PHOTO = "Please send a photo for the complaint:"
COMPLAINT_SAVE_TEXT = "Thank you for your complaint!"
EVALUATION_REQUEST_CATEGORY = "Please choose a category:"

TOKEN  =  ""

class Command(BaseCommand):
    help = 'Starts the Telegram bot'

    def handle(self, *args, **kwargs):
        updater = Updater(TOKEN, use_context=True)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler('start', self.start))
        dp.add_handler(
            MessageHandler(Filters.text | Filters.contact | Filters.location | Filters.photo, self.message_handler))

        updater.start_polling()
        updater.idle()

    def start(self, update: Update, context: CallbackContext):
        chat_id = update.message.chat_id
        db_user, created = BotUser.objects.get_or_create(chat_id=chat_id)

        if created or not db_user.lang_id:
            buttons = [
                [KeyboardButton(text=BTN_LANG_UZ), KeyboardButton(text=BTN_LANG_EN), KeyboardButton(text=BTN_LANG_RU)]]
            update.message.reply_text(text=WELCOME_TEXT)
            update.message.reply_text(text=CHOOSE_LANG, reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
            context.user_data["state"] = "choose_lang"
        elif not db_user.phone_number:
            self.ask_for_contact(update, context)
        else:
            self.send_main_menu(update, context, db_user.lang_id)

    def ask_for_contact(self, update: Update, context: CallbackContext):
        buttons = [
            [KeyboardButton(text=BTN_SEND_CONTACT[0], request_contact=True), KeyboardButton(text=BTN_SEND_CONTACT[1])]]
        update.message.reply_text("Please provide your contact or skip:",
                                  reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
        context.user_data["state"] = "get_contact"

    def send_main_menu(self, update: Update, context: CallbackContext, lang_id):
        buttons = [[BTN_MAIN_MENU[0]], [BTN_MAIN_MENU[1]], [BTN_MAIN_MENU[2]], [BTN_MAIN_MENU[3]]]
        update.message.reply_text("Main Menu:", reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
        context.user_data["state"] = "main_menu"

    def message_handler(self, update: Update, context: CallbackContext):
        chat_id = update.message.chat_id
        db_user = BotUser.objects.get(chat_id=chat_id)
        state = context.user_data.get("state")

        if state == "choose_lang":
            lang = update.message.text
            if lang == BTN_LANG_UZ:
                db_user.lang_id = 1
            elif lang == BTN_LANG_EN:
                db_user.lang_id = 2
            elif lang == BTN_LANG_RU:
                db_user.lang_id = 3
            db_user.save()
            self.ask_for_contact(update, context)

        elif state == "get_contact":
            if update.message.contact:
                db_user.phone_number = update.message.contact.phone_number
                db_user.save()
                self.send_main_menu(update, context, db_user.lang_id)
            elif update.message.text == BTN_SEND_CONTACT[1]:
                self.send_main_menu(update, context, db_user.lang_id)

        elif state == "main_menu":
            if update.message.text == BTN_MAIN_MENU[0]:
                buttons = [[KeyboardButton(text=BTN_LANG_UZ), KeyboardButton(text=BTN_LANG_EN),
                            KeyboardButton(text=BTN_LANG_RU)]]
                update.message.reply_text(text=CHOOSE_LANG,
                                          reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
                context.user_data["state"] = "choose_lang"
            elif update.message.text == BTN_MAIN_MENU[1]:
                update.message.reply_text(text=SUGGESTION_REQUEST_TEXT, reply_markup=ReplyKeyboardRemove())
                context.user_data["state"] = "submit_suggestion"
            elif update.message.text == BTN_MAIN_MENU[2]:
                update.message.reply_text(text=COMPLAINT_REQUEST_LOCATION, reply_markup=ReplyKeyboardRemove())
                context.user_data["state"] = "get_complaint_location"
            elif update.message.text == BTN_MAIN_MENU[3]:
                self.send_category_buttons(update, context)

        elif state == "submit_suggestion":
            Suggestion.objects.create(user=db_user, text=update.message.text)
            update.message.reply_text(text=SUGGESTION_SAVE_TEXT, reply_markup=ReplyKeyboardRemove())
            self.send_main_menu(update, context, db_user.lang_id)

        elif state == "get_complaint_location":
            if update.message.location:
                context.user_data[
                    "complaint_location"] = f"{update.message.location.latitude},{update.message.location.longitude}"
                update.message.reply_text(text=COMPLAINT_REQUEST_AREA)
                context.user_data["state"] = "get_complaint_area"
            else:
                update.message.reply_text(text=COMPLAINT_REQUEST_LOCATION)

        elif state == "get_complaint_area":
            context.user_data["complaint_area"] = update.message.text
            update.message.reply_text(text=COMPLAINT_REQUEST_PHOTO)
            context.user_data["state"] = "get_complaint_photo"

        elif state == "get_complaint_photo":
            if update.message.photo:
                photo_file = update.message.photo[-1].get_file()
                photo_path = photo_file.download()
                Complaint.objects.create(
                    user=db_user,
                    location=context.user_data["complaint_location"],
                    area=context.user_data["complaint_area"],
                    photo=photo_path,
                    coordinates=context.user_data["complaint_location"],
                    category=context.user_data.get("complaint_category")
                )
                update.message.reply_text(text=COMPLAINT_SAVE_TEXT, reply_markup=ReplyKeyboardRemove())
                self.send_main_menu(update, context, db_user.lang_id)
            else:
                update.message.reply_text(text=COMPLAINT_REQUEST_PHOTO)

    def send_category_buttons(self, update: Update, context: CallbackContext):
        categories = Categories.objects.filter(parent__isnull=True)
        buttons = [[InlineKeyboardButton(text=cat.name, callback_data=f"category_{cat.id}")] for cat in categories]
        update.message.reply_text(text=EVALUATION_REQUEST_CATEGORY, reply_markup=InlineKeyboardMarkup(buttons))
        context.user_data["state"] = "evaluate_category"

    def button_handler(self, update: Update, context: CallbackContext):
        query = update.callback_query
        query.answer()
        data = query.data.split('_')

        if data[0] == "category":
            cat_id = int(data[1])
            context.user_data["complaint_category"] = Categories.objects.get(id=cat_id).name
            self.save_complaint_category(update, context, cat_id)

    def save_complaint_category(self, update: Update, context: CallbackContext, cat_id):
        query = update.callback_query
        category = Category.objects.get(id=cat_id)
        subcategories = category.children.all()

        if subcategories:
            buttons = [[InlineKeyboardButton(text=subcat.name, callback_data=f"category_{subcat.id}")] for subcat in subcategories]
            query.message.reply_text(buttons)
