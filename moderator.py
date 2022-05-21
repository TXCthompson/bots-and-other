import config
import logging
import time

from time import time
from aiogram import types
from aiogram import Bot, Dispatcher, executor, types

#Сизченко Іван СОІ-21-1

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

#Команда /help

@dp.message_handler(commands=['help'], commands_prefix="!/")
async def help(message: types.Message):

	await message.reply("Список доступних команд:\n/help - список всіх команд\n/admin - видача адмін прав\n/mute - видати мут\n/unmute - зняти мут\n/ban - заблокувати користувача\n/pin - закріпити повідомлення\n /unpin - відкріпити повідомлення")

#Команда выдачи админки

@dp.message_handler(commands=['admin'], commands_prefix="!/")
async def adminkaaa(message: types.Message):
	if not message.reply_to_message:
		await message.reply("Ця команда має бути відповіддю на повідомлення!")
		return

	await message.bot.promote_chat_member(chat_id=config.GROUP_ID, user_id=message.reply_to_message.from_user.id, is_anonymous=False, can_delete_messages=False, 
											can_restrict_members=True, can_promote_members=False, can_change_info=True, can_invite_users=True)
	await message.reply("Користувача було підвищено до адміністратора!")
	await message.bot.set_chat_administrator_custom_title(chat_id=config.GROUP_ID, user_id=message.from_user.id, custom_title="admin")
	
#Команда бана для админов

@dp.message_handler(commands=['ban'], commands_prefix="!/")
async def ban(message: types.Message):
	if not message.reply_to_message:
		await message.reply("Ця команда має бути відповіддю на повідомлення!")
		return

	await message.bot.kick_chat_member(chat_id=config.GROUP_ID, user_id=message.reply_to_message.from_user.id)
	await message.reply("Користувач забанен!")

#Команда мута для админов

@dp.message_handler(commands=['mute'], commands_prefix="!/")
async def mute(message: types.Message):
	if not message.reply_to_message:
		await message.reply("Ця команда має бути відповіддю на повідомлення!")
		return

	await message.bot.restrict_chat_member(chat_id=config.GROUP_ID, user_id=message.reply_to_message.from_user.id, until_date=time()+600)
	await message.reply("Користувач зам'ючений!")

#Команда размута для админов

@dp.message_handler(commands=['unmute'], commands_prefix="!/")
async def ummute(message: types.Message):
	if not message.reply_to_message:
		await message.reply("Ця команда має бути відповіддю на повідомлення!")
		return

	await message.bot.restrict_chat_member(chat_id=config.GROUP_ID, user_id=message.reply_to_message.from_user.id, can_send_media_messages=True, until_date=time())
	await message.reply("Користувач розм'ючений!")

#Команда закрепа сообщения

@dp.message_handler(commands=['pin'], commands_prefix="!/")
async def pin_message(message: types.Message):
	if not message.reply_to_message:
		await message.reply("Ця команда має бути відповіддю на повідомлення!")
		return

	await message.bot.pin_chat_message(chat_id=config.GROUP_ID, message_id=message.reply_to_message.message_id)
	await message.reply("Повідомлення було закріплено!")

#Команда открепа сообщения

@dp.message_handler(commands=['unpin'], commands_prefix="!/")
async def unpin_message(message: types.Message):
	if not message.reply_to_message:
		await message.reply("Ця команда має бути відповіддю на повідомлення!")
		return

	await message.bot.unpin_chat_message(chat_id=config.GROUP_ID, message_id=message.reply_to_message.message_id)
	await message.reply("Повідомлення було відкріплено!")


if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)
