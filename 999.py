import requests,json,time,sys,random,os,argparse
import colorama
from colorama import Fore, Back, Style
from random import randint
from datetime import datetime
colorama.init(autoreset=True)

hijau = Style.BRIGHT+Fore.GREEN
res = Style.RESET_ALL
abu2 = Style.DIM+Fore.WHITE
ungu = Style.BRIGHT+Fore.MAGENTA
hijau2 = Style.BRIGHT+Fore.GREEN
red2 = Style.BRIGHT+Fore.RED
red = Style.BRIGHT+Fore.RED
kuning = Style.BRIGHT+Fore.YELLOW
blue = Style.BRIGHT+Fore.BLUE
hitam = Style.NORMAL+Fore.BLACK
putih = Style.BRIGHT+Fore.WHITE
bred = Style.BRIGHT+Back.RED
bblue = Style.BRIGHT+Back.BLUE
bwhite = Style.BRIGHT+Back.WHITE
bgreen = Style.BRIGHT+Back.GREEN
babu = Style.DIM+Back.WHITE+Fore.WHITE
putih2 = Style.BRIGHT+Fore.WHITE
hitam2 = Style.BRIGHT+Fore.BLACK
merah = Style.NORMAL+Fore.RED
merah2 = Style.BRIGHT+Fore.RED
biru = Style.NORMAL+Fore.BLUE
biru2 = Style.BRIGHT+Fore.BLUE
biru3 = Style.BRIGHT+Fore.CYAN
kuning2 = Style.BRIGHT+Fore.YELLOW
rccolor = Style.BRIGHT+Back.WHITE+Fore.BLACK
rcfontcolor = Style.NORMAL+Fore.BLACK
c = requests.session()

def timeprocess(sec):
    now = datetime.now()
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    stopwatchx = datetime(now.year, now.month, now.day,
                          int(hours), int(mins), int(sec), 0)

    return stopwatchx

# API INDODAX FOR GET LAST PRICE

def indodax(coin):

    try:
        if coin == "DOGE" or coin == "doge" or coin == "Doge":
            pair = "doge_idr"
        elif coin == "LTC" or coin == "ltc" or coin == "Ltc":
            pair = "ltc_idr"
        else:
            pair = "eth_idr"

        url = 'https://indodax.com/api/' + str(pair) + '/ticker'

        indx = requests.get(url)
        jsindx = json.loads(indx.text)
        pricepair = int(jsindx["ticker"]["last"])
    except:
        if coin == "DOGE" or coin == "doge" or coin == "Doge":
            coinpair = "doge"
        elif coin == "LTC" or coin == "ltc" or coin == "Ltc":
            coinpair = "ltc"
        else:
            coinpair = "eth"

        url = "https://beducode-price.herokuapp.com/price/" + str(coinpair)

        price = c.get(url)
        data = json.loads(price.text)
        pricepair = data["last"]

    return pricepair

# FORMAT VALUE TO IDR


def rupiah_format(angka):
    return 'Rp ' + '{:0,.2f}'.format(angka)


os.system('cls' if os.name == 'nt' else 'clear')

banner = "\r\n           "+bred+kuning+" 999DICE BOT V1.0 "+res+kuning+"""\n
▒█▀▀█ █▀▀█ █▀▀█ ▀▀█▀▀ █░░█ ▒█▀▀█ █▀▀█ █░░█
▒█▄▄█ █▄▄█ █▄▄▀ ░░█░░ █▄▄█ ▒█▀▀▄ █░░█ █▄▄█
▒█░░░ ▀░░▀ ▀░▀▀ ░░▀░░ ▄▄▄█ ▒█▄▄█ ▀▀▀▀ ▄▄▄█
"""+res
time.sleep(0.5)

os.system('cls' if os.name == 'nt' else 'clear')

print (banner)
print(putih2+"==========================================")
time.sleep(0.5)

parser = argparse.ArgumentParser(description='999 Dice Bot | This Is Gambling Bot Plase Take Own Your Risk')
parser.add_argument(
    '-c','--betset',
    default=0,
    help='Enter Your Betset Number (default: 0)'
)
my_namespace = parser.parse_args()

with open('config.json', 'r') as myfile:
      data=myfile.read()
# parse file
obj = json.loads(data)

pilcurr = obj["Account"]["Currency"]
if pilcurr == "DOGE" or pilcurr == "doge" or pilcurr == "Doge":
    currency = "Doge"
elif pilcurr == "LTC" or pilcurr == "ltc" or pilcurr == "Ltc":
    currency = "LTC"
elif pilcurr == "ETH" or pilcurr == "eth" or pilcurr == "Eth":
    currency = "ETH"
else:
    print("Tipe currency tidak disupport, silahkan cek kembali file settings.json anda!")
    sys.exit()

url = "https://www.999doge.com/api/web.aspx"
ua = {
 "Origin": "file://",
 "user-agent": obj["User-Agent"],
 "Content-type": "application/x-www-form-urlencoded",
 "Accept": "*/*",
 "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
 "X-Requested-With": "com.reland.relandicebot"
}

def konvert(persen,taruhan):
    global high
    global low
    c = str(999999 * float(persen) / 100)
    if taruhan == "H" or taruhan == "h" or taruhan == "H":
       n = str(c.split(".")[1])
       pangkat = 6 - len(n)
       low = int(int(n) * (10 ** pangkat))
       high = 999999
    if taruhan == "L" or taruhan == "L" or taruhan == "l" or taruhan == "L" or taruhan == "L":
       low = 0
       high = int(c.split(".")[0])


def rev(num):
    if (len(num) < 8):
        panjang_nol = int(8 - len(num))
        num = ((panjang_nol*"0")+str(num))
        result = ("0."+num)
    if (len(num) == 8):
        panjang_nol = int(8 - len(num))
        num = ((panjang_nol*"0")+str(num))
        result = ("0."+num)
    else:
        len_num = len(num)
        end = num[-8:]
        first = num[:len_num-8]
        result = (first+"."+end)
    return (result)



def dice(ws,ls):
   if my_namespace.betset == "Auto" or my_namespace.betset == "auto" or my_namespace.betset == "AUTO":
      urut = 0
      jumlahulang = 0
      while True:
         jumlahulang+=1
         try:
             pesan = obj["Config"][jumlahulang]["Name Bet Set"]
         except:
             break
   else:
      urut = int(my_namespace.betset)
   
   r = c.get(url,headers=ua,data={"a": "Login","Key": "87ca46905f304b1ba383b96b514f9bd9","Username": obj["Account"]["Username"],"Password": obj["Account"]["Password"],"Totp": ""})
   js = json.loads(r.text)
   slp = int(obj["Config"][urut]["Interval"]) / 1000
   limit_a = int(obj["Config"][urut]["Reset If Win"]) - 1
   payin = int(float(obj["Config"][urut]["Base Bet"])*(10 ** 8))
   konvert(obj["Config"][urut]["Chance"],obj["Config"][urut]["Bet"]["Bet"])
   amount = payin
   data = {
      "a": "PlaceBet",
      "s": js["SessionCookie"],
      "PayIn": amount,
      "Low": low,
      "High": high,
      "ClientSeed": randint(0,999999),
      "Currency": "doge",
      "ProtocolVersion": "2"
   }
   try:
     r1 = c.post(url,headers=ua,data=data)
     jsn = json.loads(r1.text)
    
     jumbl = jsn["StartingBalance"] + int(jsn["PayOut"]) - int(amount)
     jum = int(jsn["PayOut"]) - int(amount)
     prof = (float(jsn["StartingBalance"] + int(jsn["PayOut"]) - int(amount) - jumbl)/(10 ** 8))
     print (bgreen+putih2+"\n Start Balance "+res+" => "+str((float(int(jsn["StartingBalance"]) + int(jum))/(10 ** 8)))+" "+bred+putih2+obj["Account"]["Currency"].upper())
     print (bgreen+putih2+ "\n BetSet " + res +" : "+obj["Config"][urut]["Name Bet Set"])
     n = 0
     burst = False
     stats_rolebet_lose = False
     stats_rolebet_win = False
     menit = datetime.now().strftime('%M')
     menit = int(menit) + int(obj["Interval"])
     los = 0
     won = 0
     no_win = 0
     no_lose = 0
     total_win=0
     total_lose=0
     no_rolebet = 0
     rolebet = " "+obj["Config"][urut]["Bet"]["Bet"]+" "
     marketidx = indodax(pilcurr)
     start_time = time.time()
     reset_if_profit = obj["Config"][urut]["Reset If Profit"]
     tot_if_profit = obj["Config"][urut]["Reset If Profit"]
     while True:
        rdm = random.randint(1,5)
        rd = obj["Config"][urut]["Bet"]["H / L"]["Random"] == "On" or obj["Config"][urut]["Bet"]["H / L"]["Random"] == "ON" or obj["Config"][urut]["Bet"]["H / L"]["Random"] == "on"
        mn = obj["Config"][urut]["Bet"]["H / L"]["Toggle"]
        current_time = time.time()
        elapsed_time = current_time - start_time
        if reset_if_profit == "OFF" or reset_if_profit == "Off" or reset_if_profit == "off":
           stats_if_profit = False
        else:
           stats_if_profit = True
        if obj["Config"][urut]["Max Bet"] == "OFF" or obj["Config"][urut]["Max Bet"] == "off" or obj["Config"][urut]["Max Bet"] == "Off":
            sys.stdout.write("")
        else:
           if amount > int(float(obj["Config"][urut]["Max Bet"])*(10 ** 8)):
               amount = payin
        if obj["Config"][urut]["Bet"]["H / L"]["Random"] == "On" or obj["Config"][urut]["Bet"]["H / L"]["Random"] == "ON" or obj["Config"][urut]["Bet"]["H / L"]["Random"] == "on":
           mn = "off"
           if won == int(rdm):
              if rolebet == " L ":
                 rolebet = " H "
              else:
                 rolebet = " L "
              won = 0
           if los == int(rdm):
              if rolebet == " L ":
                 rolebet = " H "
              else:
                 rolebet = " L "
              los = 0
        elif obj["Config"][urut]["Bet"]["H / L"]["Toggle"] == "On" or obj["Config"][urut]["Bet"]["H / L"]["Toggle"] == "ON" or obj["Config"][urut]["Bet"]["H / L"]["Toggle"] == "on":
            no_rolebet +=1
            if won == int(obj["Config"][urut]["Bet"]["H / L"]["If Win"]):
               if rolebet == " L ":
                   rolebet = " H "
               else:
                   rolebet = " L "
               won = 0
            if los == int(obj["Config"][urut]["Bet"]["H / L"]["If Lose"]):
               if rolebet == " L ":
                  rolebet = " H "
               else:
                  rolebet = " L "
               los = 0
        else:
            rolebet = obj["Config"][urut]["Bet"]["Bet"]
        
        if my_namespace.betset == "Auto" or my_namespace.betset == "AUTO" or my_namespace.betset == "auto":
           waktu = datetime.now().strftime('%M')
           if int(waktu) > int(menit - 1):
              menit = int(menit) + int(obj["Interval"])
              if prof > float(obj["Reset Profit Auto"]):
                 urut += 1
                 print ("Change Bet Set "+obj["Config"][urut]["Name Bet Set"]+"                           ")
                 if urut == 1:
                    urut = 0
                
              slp = int(obj["Config"][urut]["Interval"]) / 1000
              limit_a = int(obj["Config"][urut]["Reset If Win"]) - 1
              payin = int(float(obj["Config"][urut]["Base Bet"])*(10 ** 8))
              amount = payin

        else:
          urut = int(my_namespace.betset)

        if obj["Config"][urut]["Random Chance"]["Toggle"] == "ON" or obj["Config"][urut]["Random Chance"]["Toggle"] == "On" or obj["Config"][urut]["Random Chance"]["Toggle"] == "on":
           hasil_chance = round(random.uniform(float(obj["Config"][urut]["Random Chance"]["Min"]),float(obj["Config"][urut]["Random Chance"]["Max"])),2)
           cok = len(str(hasil_chance))
           if cok == 3:
               sys.stdout.write("\r"+babu+biru3+"  "+str(hasil_chance)+"   "+res)
           if cok == 4:
               sys.stdout.write("\r"+babu+biru3+"  "+str(hasil_chance)+"  "+res)
           if cok == 5:
               sys.stdout.write("\r"+babu+biru3+" "+str(hasil_chance)+"  "+res)
           konvert(hasil_chance,str(rolebet))
        else:
           konvert(obj["Config"][urut]["Chance"],str(rolebet))
           

        time.sleep(float(slp))
        amount = int(amount)
        n+=1
        data = {
          "a": "PlaceBet",
          "s": js["SessionCookie"],
          "PayIn": amount,
          "Low": low,
          "High": high,
          "ClientSeed": randint(0,999999),
          "Currency": "doge",
          "ProtocolVersion": "2"
        }
        if prof > float(obj["Target Profit"]):
           print (hijau+"\nYay.! \nProfit Mencapai Target.....!\n"+hijau+"Profit "+res+str(prof))
           sys.exit()
        r1 = c.post(url,headers=ua,data=data)
        jsn = json.loads(r1.text)
        prof = (float(jsn["StartingBalance"] + int(jsn["PayOut"]) - int(amount) - jumbl)/(10 ** 8))
        jum = int(jsn["PayOut"]) - int(amount)
        if jsn["StartingBalance"] > ws:
           print (hijau+"["+str(rolebet)+"] "+str(float(amount)/(10 ** 8))+str(float(int(jsn["StartingBalance"]) + int(jum))/(10 ** 8))+"Profit",str(prof))
           print ("\nBalance Sudah Memenuhi Target.....!")
           os.system("termux-toast Total Balance "+str(float(int(jsn["StartingBalance"]) + int(jum))/(10 ** 8)))
           sys.exit()
        if jsn["StartingBalance"] < ls:
           print (Fore.WHITE+Back.RED+"["++str(rolebet)+"]"+red+"-"+str(float(amount)/(10 ** 8))+str((float(int(jsn["StartingBalance"]) + int(jum))/(10 ** 8)))+"Lose ",str(prof))
           print (Style.BRIGHT+Fore.RED+"Lose Target....!")
           os.system("termux-toast Lose Target ")
           time.sleep(1)
           os.system("termux-toast Total Balance "+str(float(int(jsn["StartingBalance"]) + int(jum))/(10 ** 8)))
           sys.exit()
        if jsn["PayOut"] != 0:
           los = 0
           won += 1
           no_win +=1
           no_lose = 0
           bal = int(jsn["StartingBalance"]) + int(jum)
           
           if prof > 0:
             print (bgreen+putih2+" "+str(rolebet)+" "+res,hijau+"+"+str(rev(str(amount))+res),putih2+str(rev(str(bal))+res),bgreen+putih2+" Profit "+res,hijau+str(rev(str(bal - js[currency]["Balance"]))),abu2+"["+res +kuning+"Total"+abu2+"]"+res, putih2+str(rupiah_format(marketidx * float(int(bal))/(10 ** 8)))+res)
           else:
             print (bgreen+putih2+" "+str(rolebet)+" "+res,hijau+"+"+str(rev(str(amount))+res),putih2+str(rev(str(bal))+res),bred+kuning+"  Lose  "+res,hijau2+str(rev(str(bal - js[currency]["Balance"]))),abu2+"["+res+kuning+"Total"+abu2+"]"+res, putih2+str(rupiah_format(marketidx * float(int(bal))/(10 ** 8)))+res)
           amount = int(amount) * float(obj["Config"][urut]["If Win"])

        else:
           los += 1
           won = 0
           no_win = 0
           no_lose +=1
           i = 0
           burst = True
           bal = int(jsn["StartingBalance"]) + int(jum)
           if prof > 0:
             print (bred+putih2+" "+str(rolebet)+" "+res,red+"-"+str(rev(str(amount))+res),putih2+str(rev(str(bal))),bgreen+putih2+" Profit "+res,hijau+str(rev(str(bal - js[currency]["Balance"]))),abu2+"["+res+kuning+"Total"+abu2+"]"+res, putih2+str(rupiah_format(marketidx * float(int(bal))/(10 ** 8)))+res)
           else:
             print (bred+putih2+" "+str(rolebet)+" "+res,red+"-"+str(rev(str(amount))),putih2+str(rev(str(bal))),bred+kuning2+"  Lose  "+res,red+str(rev(str(bal - js[currency]["Balance"]))),abu2+"["+res+kuning+"Total"+res+abu2+"]", putih2+str(rupiah_format(marketidx * float(int(bal))/(10 ** 8)))+res)
           amount = int(amount) * float(obj["Config"][urut]["If Lose"])
        if stats_if_profit is True:
            if prof > float(reset_if_profit):
               amount = payin
               reset_if_profit = float(prof)+float(tot_if_profit)

        if burst is True:
           i+=1
           if i > limit_a:
             i = 0
             burst = False
        else:
           if n > limit_a:
             n = 0
             amount = payin

        if no_win > total_win:
           stats_rolebet_win = True
           stats_rolebet_lose = False
           total_win +=1
        if no_lose > total_lose:
           stats_rolebet_lose = True
           stats_rolebet_win = False
           total_lose +=1
           
        tp = timeprocess(int(elapsed_time))
        timelabel = Style.BRIGHT+Back.RED+Fore.WHITE + \
                " " + tp.strftime("%H:%M:%S") + " \r" + res
        sys.stdout.write(res + "            " + bgreen + putih2 + " WS " + str(total_win) + " " + res +" "+bred + putih2 + " LS " + str(total_lose) + " " + res + " " + bwhite + Style.NORMAL+Fore.BLACK + " HARGA " + str(rupiah_format(marketidx))+" "+res+" "+timelabel + res +"\r")
           
        
        if obj["Auto Wd"]["Toggle"] == "On" or obj["Auto Wd"]["Toggle"] == "ON" or obj["Auto Wd"]["Toggle"] == "on":
           if float(rev(str(bal))) > float(obj["Auto Wd"]["If Balance"]):
              wd = {
                "a": "Withdraw",
                "s": js["SessionCookie"],
                "Amount": int(float(obj["Auto Wd"]["Amount"])*(10 ** 8)),
                "Address": obj["Auto Wd"]["Wallet Address"],
                "Totp": "",
                "Currency": "doge"

              }
              r1 = c.post(url,headers=ua,data=wd)
              withdraw = json.loads(r1.text)
              print ("")
              print ("Withdraw "+str(rev(str(withdraw["Pending"]))))
              with open("history.log","a+") as f:
                  f.write("Withdraw "+str(rev(str(withdraw["Pending"])))+"\n")
              sys.exit()



   except:
       e = sys.exc_info()
       print (e)
       try:
          with open("history.log","a+") as f:
              f.write("["+datetime.now().strftime('%Y/%m/%d %H:%M:%S')+"] Win Streak "+str(total_win)+" Lose Streak "+str(total_lose)+" | Balance "+str(float(int(jsn["StartingBalance"]) + int(jum))/(10 ** 8))+" Profit "+str(prof)+"\n")
       except:
          print ("\n\n"+bred+putih2+" Insufficient Balance for Betting ")
       sys.exit()


try:
  r = c.get(url,headers=ua,data={"a": "Login","Key": "87ca46905f304b1ba383b96b514f9bd9","Username": obj["Account"]["Username"],"Password": obj["Account"]["Password"],"Totp": ""})
  js = json.loads(r.text)
  loginstatus = "LoginInvalid" in js
  if loginstatus is True:
    print (bred+putih2+"\n Check Your Username And Your Password "+res+"\n\n")
    sys.exit()
  else:
    print (hijau+"Halo, "+res+putih2+obj["Account"]["Username"]+hijau+" \nKami Ucapkan Terimakasih,\nUntuk Kamu Yang Menggunakan Script Kami "+res+"\n\n")
    sys.stdout.write(bred+putih2+"\r Starting. ")
    time.sleep(0.5)
    sys.stdout.write(bred+putih2+"\r Starting.. ")
    time.sleep(0.5)
    sys.stdout.write(bred+putih2+"\r Starting... ")
    time.sleep(0.5)
    sys.stdout.write(bgreen+putih2+"\r Starting...! ")
    time.sleep(0.5)
    print ("\n\n")
except KeyboardInterrupt:
  print ("\n\n"+bred+putih2+" E X I T !! "+res)
  sys.exit()


dice(int(float(obj["Target Win"])*(10 ** 8)),
     int(float(obj["Lose Target"])*(10 ** 8)))
