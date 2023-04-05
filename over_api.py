from vk_api import VkApi, VkUpload, exceptions
from time import sleep, strftime
from config import *

while 1:
	hr = int(strftime("%H"))
	if hr >= 7 and hr <= 19:
		try:
			vk_session = VkApi(login,password)
			upload     = VkUpload (vk_session)
			
			vk_session.auth()
			
			vk = vk_session.get_api()

		except Exception as e:
			print (e)
		
		else:
			for i in range(len(gids)):
				try:
					vk.wall.post(owner_id = gids[i],message = ad_text, attachment = attachment)
				except exceptions.ApiError:
					print(gids[i], "- ban")
				sleep(1)
			sleep(int(wait_time) * 60)
