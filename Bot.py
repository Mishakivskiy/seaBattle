import config
import logging
import asyncio
import BotLogic

from Board import board
from aiogram import Bot, Dispatcher, executor, types
from sqlighter import SQLighter

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_token)
dp = Dispatcher(bot)

db = SQLighter('roomsDB.db')

@dp.message_handler(commands=['help'])
async def print(message: types.Message):
	await message.answer("Hi, I'm a telegram bot for playing sea combat, write the command /start to start the game😊")

@dp.message_handler(commands=['start'])
async def ToStartGame(message: types.Message):
	await message.answer("Select the type of game start: 1) /create_game 2) /connect_to_game")

@dp.message_handler(commands=['create_game'])
async def CreateGame(message: types.Message):

	def create_game():

		roomID = 0
		ind = 1

		while ind != 0:
			if db.check_id(roomID) is None:
				db.addroom(roomID, message.from_user.id)
				ind = 0
			else :
				roomID += 1

		return roomID



	RoomID = create_game()
	info = "You have created a game room under ID:" + str(RoomID) + ". Wait opponent(enter /TryStart to try start game)"

	await message.answer(info)

	@dp.message_handler(commands=['TryStart'])
	async def TryStart(message: types.Message):
		if not db.check2nd(RoomID):
			await message.answer("Wait opponent(enter /TryStart to try start game)!")
			TryStart()
		else:
			IDs =	db.try_start(RoomID)

			for id in IDs:
				await bot.send_message(id, "All players in spot, let's get started!")
				await bot.send_message(id, "🟦 - field cell\n⬛ - ship cell\n🔘 - miss\n❌ - destroyed the ship's side\nFor a shot, point vertically, then horizontally through a space")

			end_game = False

			firstMain = board.main_board
			secondMain = board.main_board
			firstOpp = board.main_board
			secondOpp = board.main_board

			whose_course = True #True - host, False - opponent

			while not end_game:
				if whose_course == True:
					await bot.send_message(IDs[0],"Youre field:")
					await bot.send_message(IDs[0],BotLogic.print_field(firstMain))
					await bot.send_message(IDs[0], "Opponent field:")
					await bot.send_message(IDs[0], BotLogic.print_field(firstOpp))
					end_game = True

					@dp.message_handler(content_types=['text'])
					async def stCourse(message: types.Message):
						pass

@dp.message_handler(commands=['connect_to_game'])
async def ConnectToGame(message: types.Message):
	await message.answer("Enter the ID of the room you want to connect to:")

	@dp.message_handler(content_types=['text'])
	async def Connection(message: types.Message):
		roomID = int(message.text)

		if db.check_id(roomID) is None:
			await message.answer("Room don`t find. Try again:")
			Connection()

		else:
			user_id = message.from_user.id

			db.second_connect(user_id, roomID)
			await message.answer("You`re connect to room. Wait host")



if __name__ == '__main__':
	executor.start_polling(dp)
