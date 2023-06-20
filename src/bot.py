import discord
import responses


async def send_message(message, user_message, is_private):
	try:
		response = responses.handle_response(user_message)
		await message.author.send(response) if is_private else await message.channel.send(response)
	except Exception as e:
		print(e)


def run_discord_bot():
	TOKEN = 'MTEyMDY3MjQ4NTQ5MTM0MzM4MQ.G_2Jk0.6X-MW1O9n29yKhB2slmOlr21B37ABbV65592uI'
	client = discord.Client(intents=discord.Intents.default())

	@client.event
	async def on_ready():
		print(f'{client.user} is no running!')
	
	async def on_message(message):
		if message.author == client.user:
			return
		
		username = str(message.author)
		user_message = str(message.content)
		channel = str(message.channel)

		print(f"{username} said: '{user_message}' ({channel})")

		if user_message[0] == '?':
			user_message = user_message[1:]
			await send_message(message, user_message, is_private=True)
		else:
			await send_message(message, user_message, is_private=False)

	client.run(TOKEN)