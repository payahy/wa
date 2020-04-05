from eaterwa import *

myId = '6287859909669@c.us'

auth = {
    'apikey': 'your apikey',
    'userid': 'your userid',
    'username': 'your username'
}

settings = {
    'autoRead': False
}

wa = EaterWa(auth)
wa.login()

def process_message(cmd, text, txt, to, sender, message, msg_id):
    if txt == 'tag':
      if sender == myId:
        wa.mentionAll(message)
    elif txt == 'status':
        wa.sendReply(msg_id, 'Alive Gan')
    elif txt == 'battery':
        battery = wa.getBatteryLevel()
        wa.sendMessage(to, battery['result'])
    elif txt == 'me':
        nomer = sender.replace('@c.us','')
        wa.sendMention(to, '@' + nomer, [sender])
    elif txt == 'author pict':
        wa.sendMediaWithURL(to, 'https://i.ibb.co/dBsw1Xf/photo-2019-10-28-18-07-44.jpg', 'pict.jpg', caption='Test test')
    elif txt == 'revoke login':
      if sender == myId:
        wa.sendMessage(to, 'revoked!!!')
        wa.revoke()
    elif cmd.startswith('exc\n'):
      if sender in ['6287859909669@c.us']:
        sep = text.split('\n')
        txt = text.replace(sep[0] + '\n','')
        if 'print' in txt:
            p   = re.search(r'print(\s+|)\(', str(txt)).group(0)
            txt = txt.replace(p, 'wa.sendMessage(to,')
            exec(txt)
        elif 'console' in txt:
            p = re.search(r'console(\s+|)\(', str(txt)).group(0)
            c = txt.replace(p,'print(')
            exec(c)
        elif 'haste' in txt:
            a = txt.replace('haste', 'a =')
            a += """
url = requests.post('https://hastebin.com/documents', data=str(a))
data = url.json()
wa.sendMessage(to, 'https://hastebin.com/%s' % data['key'])
                """
            print(a)
            exec(a)
        elif 'sscode' in txt:
            a = txt.replace('sscode', 'a = ')
            a += """
data = requests.get("http://apikuu.herokuapp.com/api/v0/sakty/karbon", params={"code":'''{}'''.format(str(a)),"lang":"python","line":False}).json()
wa.send_media_with_url(to, data['hasil']['karbon'])
            """
            exec(a)
        elif 'sendFile' in txt or 'FILE_NAME' in txt or 'FILE_SIZE' in txt:
            if sender in ['6287859909669@c.us']:
                exec(txt)
            else:
                return wa.sendMessage(to, "you don't have permission to do this script")
        elif 'os.popen' in txt or 'os.system' in txt or 'subprocess' in txt:
            if sender in ['6287859909669@c.us']:
                exec(txt)
            else:
                return wa.sendMessage(to, "you don't have permission to do this script")
        else:
            exec(txt)
    elif txt.startswith("topik_alquran: "):
        sep = text.split(" ")
        textnya = text.replace(sep[0] + " ","")
        result = requests.get("https://api.haipbis.xyz/searchqurdis?q={}".format(textnya))
        data = result.json()
        ret_ = "╭──[ TOPIK AL-QUR'AN & HADITS ]"
        ret_ += "\n├⌬ Ayat Qur'an : "+str(data[0]['quran/hadis'])
        ret_ += "\n├⌬ Sumber : "+str(data[0]['link'])
        ret_ += "\n├⌬ Isi Al-Qur'an: "
        ret_ += "\n├⌬     Bahasa Arab : "+str(data[0]['teks']['arab'])
        ret_ += "\n├⌬     Bahasa Latin : "+str(data[0]['teks']['latin'])
        ret_ += "\n╰───────[ Bismillah ]"
        wa.sendMessage(to, str(ret_))
    elif txt.startswith("musik:"):
        proses = text.split(" ")
        urutan = text.replace(proses[0] + " ","")
        r = requests.get("https://api.fckveza.com/mp3={}".format(urutan))
        data = r.text
        data = json.loads(data)
        ret_ = "╭──[ Musik MP3 ]"
        ret_ += "\n├⋄ Title : {}".format(str(data["judul"]))
        ret_ += "\n├⋄ Album : {}".format(str(data["album"]))
        ret_ += "\n├⋄ Penyanyi : {}".format(str(data["penyanyi"]))
        ret_ += "\n╰──[ Finish ]"
        wa.sendMediaWithURL(to, str(data["linkImg"]), 'pict.jpg', caption=ret_)
        wa.sendMediaWithURL(to, str(data["linkMp3"]), 'music.mp3')                                
    elif txt == 'corona':
        r=requests.get("https://api.kawalcorona.com/indonesia")
        data=r.text
        data=json.loads(data)
        ret_ = "「 COVID-19」"
        ret_ += "\nCountry : *{}*".format(str(data[0]["name"]))
        ret_ += "\nVictims : *{}*".format(str(data[0]["positif"]))
        ret_ += "\nRecover : *{}*".format(str(data[0]["sembuh"]))
        ret_ += "\nDeath : *{}*".format(str(data[0]["meninggal"]))
        wa.sendMessage(to, ret_)
    elif txt.startswith('corona '):
        textt = text.replace(text.split(' ')[0] + ' ', '')
        r=requests.get("https://api.kawalcorona.com/indonesia/provinsi").json()
        for atr in r:
            data = atr['attributes']
            if data['Provinsi'].lower() == textt:
                res = '「 COVID-19」'
                res += '\nProvinsi   : *{}*'.format(data['Provinsi'])
                res += '\nVictims    : *{}*'.format(data['Kasus_Posi'])
                res += '\nRecover    : *{}*'.format(data['Kasus_Semb'])
                res += '\nKasus_Meni : *{}*'.format(data['Kasus_Meni'])
                wa.sendMessage(to, res)
    elif txt.startswith('trial-'):
        if sender in (myId, '6287859909669@c.us'):
            textt = text.replace('trial-','')
            if textt.lower().startswith('add '):
                texts = textt[4:]
                url   = 'https://wa.boteater.us/admin/add-client?apikey=boteater_admin_apikey_2239nnas8HDHJ&username=' + texts
                req   = requests.get(url).json()
                res   = 'Trial Whatsapp API Boteater'
                res  += '\nAPIkey = ' + req['apikey']
                res  += '\nUserid = ' + req['userid']
                res  += '\nUsername = ' + texts
                res  += '\nHello World'
                wa.sendMessage(to, res)
            elif textt.lower().startswith('del '):
                texts = textt[4:]
                url   = 'https://wa.boteater.us/admin/delete-client?apikey=boteater_admin_apikey_2239nnas8HDHJ&username=' + texts
                req   = requests.get(url).json()
                wa.sendMessage(to, str(req))
    elif txt == 'autoread on':
        if settings['autoRead']:
            wa.sendMessage(to, 'auto read telah di aktifkan')
        else:
            settings['autoRead'] = True
            wa.sendMessage(to, 'Berhasil mengaktifkan autoread')
    elif txt == 'autoread off':
        if not settings['autoRead']:
            sendMessage(to, 'auto read telah nonaktif')
        else:
            settings['autoRead'] = False
            wa.sendMessage(to, 'Berhasil menonaktifkan autoread')

def check_m(include_me=True, include_notifications=True):
    
    while True:
        unread = wa.getUnread()
        try:
            for contact in unread.json()['result']:
                for message in contact['messages']:
                    try:
                        cont = str(message['content'][0:25])
                    except:
                        cont = 'None'
                    print('new message - {} from {} message {}...'.format(str(message['type']), str(message['sender']['formattedName']), cont))
                    try:
                        sender_id = message['sender']['id']
                    except:
                        sender_id = "None"
                    try:
                        chat_id = message['chatId']
                    except:
                        chat_id = sender_id

                    if settings['autoRead']:
                        wa.sendSeen(to)
                        
                    if message['subtype'] == 'invite' or message['subtype'] == 'add':
                        if myId in message['recipients']:
                            wa.sendMention(to, 'Hello @{} Thanks for invited me'.format(message['author'].replace('@c.us','')), [message['author']])
                        else:
                            for recipient in message['recipients']:
                                wa.sendMention(to, 'Halo @{} Selamat datang di {}'.format(recipient.replace('@c.us',''),message['chat']['contact']['name']), [recipient])

                    if message['type'] == 'chat':
                        text = message['content']
                        txt  = text.lower()
                        cmd  = text.lower()
                        to   = chat_id
                        sender = sender_id
                        msg_id = message['id']

                        try:
                            process_message(cmd, text, txt, to, sender, message, msg_id)
                        except Exception as e:
                            print('Error :', e)
        except Exception as e:
            print('Error :', e)
            sys.exit('Good Bye!!')
check_m()