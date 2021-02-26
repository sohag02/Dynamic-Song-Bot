from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import urllib.request, json, os 
from urllib.request import urlretrieve

token = '1402982719:AAGVOdHKL1wJ-UZ-RBK9onqxdyNd4QFselQ'
PORT = int(os.environ('PORT','8443'))

endpoint_link = "https://saavn.sumit.codes/search/"
link = ""
def fetchjson(url):
    resp=urllib.request.urlopen(url)
    return json.loads(resp.read().decode())

def Song(update, context):
    music = context.args
    name = '%20'.join([str(elem) for elem in music])
    # print(name) 
    x = context.user_data.get(name, name)
    msg = update.message.reply_text("Searching....🔎")
    sjson = ""
    link = ""
    tittle = ""
    img_link = ""
    album = ""
    artist = ""
    try:
        sjson = fetchjson(endpoint_link + x)
        tittle = sjson["result"][0]["song_title"]
        img_link = sjson["result"][0]["song_image"]
        album = sjson["result"][0]["album_title"]
        artist = sjson["result"][0]["artist_name"]
        link = sjson["result"][0]["download_link"]
           
    except:
        #raise
        update.message.reply_text(link) 
        msg.edit_text("""Something went wrong at our server. Please try after sometimes...
        
Sorry for the inconvineance 🙏🏼""")
    #return
    if """{"result":[]}""" in sjson:
            msg.edit_text("Couldn't fetch that song Please try agin...")
    else:
        HTML= 'HTML'
        #if song_path == "":
            #return #open(song_path, "rb")
        context.bot.send_audio(chat_id=update.effective_chat.id, audio=link, title=tittle, thumb=img_link, parse_mode=HTML, caption="""<b>HERE IS YOUR REQUESTED SONG ACCORDING TO THE MATCH!</b> 
➖➖➖➖➖➖➖➖➖➖➖
🎶<b>SONG NAME</b>:- <i>{tittle}</i>
🔊<b>ALBUM</b>:- <i>{album}</i>
🙋🏻‍♂️<b>ARTISTS</b>:- <i>{artist}</i>
➖➖➖➖➖➖➖➖➖➖➖            
<b>THANK YOU FOR USING</b> @DynamicSongPlayerBot

<b>SHARE & KEEP SUPPORTING</b>❤️
🔥 @TheDynamicNetwork 🔥""".format(tittle = tittle, album = album, artist = artist))
    msg.delete()

"""def channel(update, context):
    check = bot.get_chat_member(chat_id=="@DynamicBots", user_id=update.effective_user.id)
    if check =True:
        update.message.reply_text(Hello, {full_name}
        
        You need to join our channel in order to use our bot
        
        Please join here : @DynamicBots)
    else:
        start"""

def message(update, context):
    update.message.reply_text("""This is not a valid command
Use /help for guide""")

def start(update, context):
    context.bot.sendMessage(chat_id=update.effective_chat.id, text="""𝗛𝗲𝗹𝗹𝗼 @{username},
➖➖➖➖➖➖➖➖➖➖➖➖
𝗧𝗵𝗶𝘀 𝗯𝗼𝘁 𝗰𝗮𝗻 𝗳𝗲𝘁𝗰𝗵 𝗬𝗼𝘂 𝗬𝗼𝘂𝗿
𝗗𝗲𝘀𝗶𝗿𝗲𝗱 𝗦𝗼𝗻𝗴! 
➖➖➖➖➖➖➖➖➖➖➖➖
𝗨𝘀𝗲 /help 𝗳𝗼𝗿 𝗴𝘂𝗶𝗱𝗲 𝗔𝗻𝗱 𝗧𝗼
𝗞𝗻𝗼𝘄 𝗧𝗵𝗲 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀! 
➖➖➖➖➖➖➖➖➖➖➖➖
✅𝗖𝗥𝗘𝗗𝗜𝗧𝗦:- @DynamicBots
➖➖➖➖➖➖➖➖➖➖➖➖""".format(username = update.effective_user.username))

def help(update, context):
    context.bot.sendMessage(chat_id=update.effective_chat.id, text="""𝙃𝙀𝙇𝙋 𝙂𝙐𝙄𝘿𝙀:- [ 𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎]
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
/start -» 𝙍𝙚𝙨𝙩𝙖𝙧𝙩𝙨 𝙏𝙝𝙚 𝘽𝙤𝙩. 
/help -» 𝙎𝙖𝙢𝙚 𝙃𝙚𝙡𝙥 𝙂𝙪𝙞𝙙𝙚 𝙋𝙤𝙥𝙨 𝙐𝙥. 
/song <song name> -» 𝙁𝙚𝙩𝙘𝙝𝙚𝙨 𝙔𝙤𝙪𝙧 𝘿𝙚𝙨𝙞𝙧𝙚𝙙 𝙎𝙤𝙣𝙜 𝙏𝙤 𝙔𝙤𝙪. 
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
𝙏𝙝𝙖𝙣𝙠 𝙔𝙤𝙪! 𝙁𝙤𝙧 𝙁𝙪𝙧𝙩𝙝𝙚𝙧 𝙌𝙪𝙚𝙧𝙞𝙚𝙨 
𝘾𝙤𝙣𝙩𝙖𝙘𝙩 𝙐𝙨:- @DynamicsHelpBot
➖➖➖➖➖➖➖➖➖➖➖➖➖➖""")


updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('song', Song))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.all & (~ Filters.caption_entity('bot_command')), message))

updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=token)
updater.bot.set_webhook("https://dynamic-song-bot.herokuapp.com/")
updater.idle()
