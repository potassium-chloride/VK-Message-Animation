import time,json,urllib.request,subprocess,sys

def bashExec(q):
	return subprocess.check_output(q,shell=True).decode("UTF-8")

#Получить JSON из адреса
def getJSON(url):
	time.sleep(0.33)
	bts = urllib.request.urlopen(url)
	s=bts.read().decode('UTF-8')
	bts.close()
	try:
		return json.loads(s)
	except:
		print(ttt()+"Ошибка запроса! url="+url+";\n\t\tans="+s)
	return json.loads("{}")

api_url="https://api.vk.com/method/"
token=bashExec("cat ~/bin/.token").replace("\n","")#У меня тут токен для вк лежит

def sendMsg(peer,text):
	if(len(text)<2):
		print(ttt()+"Длина сообщения менее 2, не отправляется")
		return 0
	return getJSON(api_url+"messages.send?v=5.52&peer_id="+peer+"&message"+urllib.parse.urlencode([("",text)])+"&access_token="+token)['response']

def editMsg(peer,mid,text,sid='',ckey=None):
	if(len(text)<2):
		print(ttt()+"Длина сообщения менее 2, не отправляется")
		return
	if(len(sid)>0):
		return getJSON(api_url+"messages.edit?v=5.87&peer_id="+peer+"&message"+urllib.parse.urlencode([("",text)])+"&message_id="+str(mid)+"&dont_parse_links=1&captcha_sid="+str(sid)+"&captcha_key="+ckey+"&access_token="+token)
	return getJSON(api_url+"messages.edit?v=5.87&peer_id="+peer+"&message"+urllib.parse.urlencode([("",text)])+"&message_id="+str(mid)+"&dont_parse_links=1&access_token="+token)

animationtext=[
"[██___________]",
"[_██__________]",
"[__██_________]",
"[___██________]",
"[____██_______]",
"[_____██______]",
"[______██_____]",
"[_______██____]",
"[________██___]",
"[_________██__]",
"[__________██_]",
"[___________██]",
"[█___________█]"
]
animationtext2=[
"[_____________]",
"[█____________]",
"[██___________]",
"[███__________]",
"[████_________]",
"[█████________]",
"[██████_______]",
"[███████______]",
"[████████_____]",
"[█████████____]",
"[██████████___]",
"[███████████__]",
"[████████████_]",
"[█████████████]"
]

def animate(peer,animation,mid=0,loop=False,timeout=1):
	if(type(peer)!=str):peer=str(peer)
	if(mid==0):mid=sendMsg(peer,animation[0])
	if(timeout>0.33):time.sleep(timeout-0.33)
	c=1
	while(loop or c<len(animation)):
		res=editMsg(peer,mid,animation[c%len(animation)])
		if('error' in list(res.keys())):
			csid=res['error']['captcha_sid']
			cimg=res['error']['captcha_img']
			bashExec("wget -O /tmp/vkcaptcha.jpg \""+cimg+"\" 2>/dev/null")
			bashExec("xdg-open /tmp/vkcaptcha.jpg 2>/dev/null")
			ctext=bashExec("zenity --entry --text=\"Текст с капчи\" 2>/dev/null").replace("\n","")
			if(len(ctext)==0):break
			editMsg(peer,mid,animation[c%len(animation)],sid=csid,ckey=ctext)
		else:
			if(timeout>0.33):time.sleep(timeout-0.33)
		c+=1

if __name__ == "__main__":
	animate(sys.argv[1],animationtext2,loop=False)
