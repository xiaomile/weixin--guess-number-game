from wxpy import *
import random
bot = Bot(console_qr=1, cache_path=True)
#bot.self.send('Hello World!')
my_group = bot.groups(update=True).search('猜数字测试群')[0]
my_group.send('回复 猜数字 可以玩猜数字游戏哦！')
isplay = False
def makeGuess(msg):
    global minnumber
    global maxnumber
    global thenumber
    global isplay
    minnumber = int(random.random()*100)
    maxnumber = random.randint(minnumber,100)
    thenumber = random.randint(minnumber+1,maxnumber-1)
    isplay = True
    msg.reply(f'来猜{minnumber}到{maxnumber}之间的随机数\n')


@bot.register(my_group,msg_types=TEXT)
def auto_reply_friends(msg):
    print(msg)
    try:
        global isplay
        if msg.text=='猜数字':
            makeGuess(msg)
        elif msg.text=='游戏结束':
            isplay = False
            msg.reply(f'好啦好啦[委屈][委屈]不玩啦')
        elif msg.text.isdigit() and isplay:
            global minnumber
            global maxnumber
            global thenumber
            
            if int(msg.text) != thenumber:
                if int(msg.text)>thenumber and int(msg.text) < maxnumber :
                    maxnumber = int(msg.text)
                    msg.reply(f'{minnumber}到{maxnumber}\n')
                elif int(msg.text)<thenumber and int(msg.text) > minnumber :
                    minnumber = int(msg.text)
                    msg.reply(f'{minnumber}到{maxnumber}\n')
                elif int(msg.text) >= maxnumber or int(msg.text) <= minnumber :
                    msg.reply(f'亲,认真看范围[抓狂],{minnumber}到{maxnumber}\n')
            else:
                msg.reply(f'恭喜你猜对了,是{thenumber},[奸笑]好腻害')
                isplay = False
            #print(thenumber)
        elif isplay:
            msg.reply('等会再说，在玩游戏忙着呢！')
        elif msg.text.isdigit():
            msg.reply('这数字是啥意思[疑问]')
        elif '你是谁' in msg.text:
            msg.reply('hello，this is 卖小麦')
        else:
            msg.reply('这话我接不了[委屈]')
    except Exception as e:
        print(repr(e))
    #print('end')
    
embed()
