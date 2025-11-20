""" Decompiled by Exotic Hridoy """

import os
import sys
import re
import time
import json
import mechanize
import asyncio
import aiohttp
import requests
import urllib.parse
import bs4
import string
import faker
import fake_email
import random
import uuid
import hashlib
import subprocess
import platform
import marshal
import zlib
import base64
from faker import Faker
from fake_email import Email
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from datetime import datetime, timedelta
from time import sleep as sp
from io import BytesIO
import pycurl
import certifi

white = '\x1b[1;97m'
yelloww = '\x1b[1;33m'
green = '\x1b[38;5;49m'
G0 = '\x1b[38;5;155m'
green1 = '\x1b[38;5;154m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
G6 = '\x1b[38;5;52m'
s = '\x1b[0m'
W = '\x1b[1;30m'
Y = '\x1b[1;93m'
red = '\x1b[38;5;160m'
B = '\x1b[1;95m'
BE = '\x1b[1;35m'
X = '\x1b[1;96m'
Z = '\x1b[1;95m'
Y = '\x1b[1;93m'
U = '\x1b[1;94m'
V = '\x1b[38;5;47m'
T = '\x1b[38;5;48m'
Q = '\x1b[38;5;49m'
P = '\x1b[38;5;50m'
O = '\x1b[38;5;51m'
N = '\x1b[38;5;52m'
M = '\x1b[38;5;205m'
L = '\x1b[96;1m'
K = '\x1b[1;91m'
WH = '\x1b[1;97m'
orange = '\x1b[38;5;196m'
yellow = '\x1b[38;5;208m'
black = '\x1b[1;30m'
rad = '\x1b[38;5;160m'
YLW = '\x1b[1;33m'
blue = '\x1b[38;5;6m'
purple = '\x1b[1;35m'
cyan = '\x1b[1;36m'
white = '\x1b[1;37m'
faltu = '\x1b[1;47m'
pvt = '\x1b[1;0m'
gren = '\x1b[38;5;154m'
gas = '\x1b[1;32m'
style = '\x1b[1;37m[\x1b[1;32m●\x1b[1;37m]'
stylee = '\x1b[1;37m[\x1b[1;31m!\x1b[1;37m]'

"""
try:
    os.system('rm -rf /sdcard/.txt')
    os.system('clear')
    open('/sdcard/.txt', 'w').write(' ')
except PermissionError:
    pass

try:
    requests.get('https://www.google.com', timeout=5)
except requests.exceptions.ConnectionError:
    pass
else:
    style_2 = '\x1b[1;37m[\x1b[1;31m!\x1b[1;37m]'
    site = '/data/data/com.termux/files/usr/lib/python3.12/site-packages/'
    os.system('clear' if os.name == 'posix' else 'cls')

alart = f'{style_2} \x1b[1;31mYOU ARE A MOTHERFUCKER, YOU ARE A MOTHERFUCKER.\n{style_2} \x1b[1;31mDON\'T TRY BYPASS AND CAPTURE BOSS\n{style_2} \x1b[1;31mTHIS TIME I\'LL LEAVE IT LIKE THIS, YOU BASTARD.\n\x1b[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'

try:
    mr_error = f'{site}reque' + 'sts/'
    if 'print' not in open(mr_error + 'sess' + 'ions.py', 'r').read():
        pass
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    exit(f'{alart}')
except:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    exit(f'{alart}')

try:
    mr_error1 = f'{site}reque' + 'sts/'
    if 'print' not in open(mr_error1 + 'mod' + 'els.py', 'r').read():
        pass
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    exit(f'{alart}')
except:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    exit(f'{alart}')

try:
    mr_error2 = f'{site}reque' + 'sts/'
    if 'print' not in open(mr_error2 + 'ap' + 'i.py', 'r').read():
        pass
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    exit(f'{alart}')
except:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    exit(f'{alart}')

try:
    king = f'{site}reque' + 'sts/'
    if 'sys.stdout.write' not in open(king + 'sess' + 'ions.py', 'r').read():
        pass
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    exit(f'{alart}')
except:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    exit(f'{alart}')

try:
    qeen = f'{site}req' + 'uests/'
    if 'sys.stdout.write' not in open(qeen + 'mod' + 'els.py', 'r').read():
        pass
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    exit(f'{alart}')
except:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    exit(f'{alart}')

try:
    don = f'{site}requ' + 'ests/'
    if 'sys.stdout.write' not in open(don + 'a' + 'pi.py', 'r').read():
        pass
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    exit(f'{alart}')
except:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    exit(f'{alart}')

with open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/auth.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
    exit(f'{alart}')

try:
    a = open('requests/sessions.py', 'r').read()
    if 'print' in a:
        os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
        exit(f'{alart}')
except Exception as e:
    pass

try:
    b = open('requests/api.py', 'r').read()
    if 'print' in b:
        os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
        exit(f'{alart}')
except Exception as e:
    pass

try:
    c = open('requests/models.py', 'r').read()
    if 'print' in c:
        os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
        exit(f'{alart}')
except Exception as e:
    pass

try:
    d = open('httpx/_api.py', 'r').read()
    if 'print' in d:
        os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx')
        exit(f'{alart}')
except Exception as e:
    pass

try:
    e = open('httpx/_auth.py', 'r').read()
    if 'print' in e:
        os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx')
        exit(f'{alart}')
except Exception as e:
    pass

try:
    f = open('httpx/_models.py', 'r').read()
    if 'print' in f:
        os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx')
        exit(f'{alart}')
except Exception as e:
    pass

try:
    g = open('requests/sessions.py', 'r').read()
    if 'sys.stdout.write' in g:
        os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
        exit(f'{alart}')
except Exception as e:
    pass

try:
    h = open('requests/api.py', 'r').read()
    if 'sys.stdout.write' in h:
        os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
        exit(f'{alart}')
except Exception as e:
    pass

try:
    h = open('requests/models.py', 'r').read()
    if 'sys.stdout.write' in h:
        os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
        exit(f'{alart}')
except Exception as e:
    pass

try:
    ii = open('httpx/_api.py', 'r').read()
    if 'sys.stdout.write' in ii:
        os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx')
        exit(f'{alart}')
except Exception as e:
    pass

try:
    j = open('httpx/_auth.py', 'r').read()
    if 'sys.stdout.write' in j:
        os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx')
        exit(f'{alart}')
except Exception as e:
    pass

try:
    k = open('httpx/_models.py', 'r').read()
    if 'sys.stdout.write' in k:
        os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx')
        exit(f'{alart}')
except Exception as e:
    pass

try:
    l = open('requests/api.py', 'r').read()
    if 'verify = False' in l:
        os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
        exit(f'{alart}')
except Exception as e:
    pass

try:
    m = open('requests/sessions.py', 'r').read()
    if 'self.verify = False' in m:
        os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests')
        exit(f'{alart}')
except Exception as e:
    pass

try:
    n = open('urllib3/conne' + 'ction.py', 'r').read()
    if str('cert_reqs = \'CERT_NONE\'') in n:
        os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/urllib3')
        exit(f'{alart}')
except Exception as e:
    pass
"""

"""
async def bypass():
    file1 = open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/api.py', 'r')
    file2 = open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/sessions.py', 'r')
    file3 = open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/models.py', 'r')
    data = file1.read()
    sess = file2.read()
    approve = file3.read()
    keyword = 'print(url)'
    keyword2 = 'print(data)'
    if keyword in data or 'echo' in data or 'pprint' in data:
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f'{style_2} \x1b[1;31mSTUPID BYPASS')
        print(f'{style_2} \x1b[1;33mBYE BYE FILES HAHAHAH')
        sys.exit()
    else:
        if 'https://pastebin.com/icdnZ6AQ' in approve or 'DR4X' in approve or 'pprint' in approve:
            print(f'{style_2} \x1b[1;31mTRYING HARD BYPASSING MY TOOL LOL BYE')
            sys.exit()
            return
        if keyword in sess or 'echo' in sess or keyword2 in sess or ('pprint' in sess) or ('print(headers)' in sess) or ('Console' in sess) or ('{data}' in sess) or ('{url}' in sess) or ('{headers}' in sess):
            os.system('clear' if os.name == 'posix' else 'cls')
            print(f'{style_2} \x1b[1;31mCAPTURE MORE DATA')
            print(f'{style_2} \x1b[1;33mBYE BYE FILES')
            sys.exit()
        else:
            os.system('clear' if os.name == 'posix' else 'cls')
            timee = datetime.now()
            limittime = timee.strftime('%m-%d-%y')
            if limittime >= '11-30-25':
                os.system('clear')
                sys.exit('{style_2} \x1b[1;31mTIME'S UP BRO')
            else:
                await sub()
"""

"""
myid = uuid.uuid4().hex[:5].upper()
try:
    key1 = open('/data/data/com.termux/files/usr/bin/.errorauto.txt', 'r').read()
except:
    kok = open('/data/data/com.termux/files/usr/bin/.errorauto.txt', 'w')
    kok.write(myid)
    kok.close()
else:
    uid = os.getuid()
    key1 = open('/data/data/com.termux/files/usr/bin/.errorauto.txt', 'r').read()
    kex = f'AUTOCREATEFB|MR|{uid}|ERROR|{key1}|708'
    key1 = kex
    AX = hashlib.md5((platform.version() + str(os.getuid()) + platform.platform() + os.getlogin() + platform.release()).replace(' ', '').encode()).hexdigest().upper()
    _sos_ = AX
    _xvx_ = _sos_
    _asa_ = _xvx_
    _cxa_ = _asa_
    _qq_ = _cxa_[5:8]
    _ee_ = _cxa_[15:19]
    _rr_ = _cxa_[23:26]
    _tt_ = _cxa_[11:13]
    _yy_ = _cxa_[19:21]
    _q_ = _yy_
    _w_ = _tt_
    _e_ = _rr_
    _r_ = _ee_
    _t_ = _qq_
    __coc__ = _q_ + _w_ + _e_ + _r_ + _t_
"""

key1 = "FREE_VERSION_NO_KEY_NEEDED"

def py_curl(url):
    curl = pycurl.Curl()
    buffer = BytesIO()
    try:
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.SSL_VERIFYPEER, 1)
        curl.setopt(curl.SSL_VERIFYHOST, 2)
        curl.setopt(curl.CAINFO, certifi.where())
        curl.perform()
    except pycurl.error as e:
        pass
    else:
        curl.close()
        response_body = buffer.getvalue().decode('utf-8')
        return response_body
        return f'AN ERROR IN PY{e}'

def error(z):
    for a in z + '\n':
        sys.stdout.write(a)
        sys.stdout.flush()
        time.sleep(0.05)
"""
print(f'{style} \x1b[1;32mCHECKING UPDATED...\x1b[1;37m')
time.sleep(2)
os.system('git pull')
time.sleep(2)
os.system('clear')
"""

try:
    import pystyle
except ImportError:
    print(f'{style} \x1b[1;32mINSTALLING PYSTYLE...{white}')
    time.sleep(0.5)
    os.system('pip install pystyle')
    import pystyle
    os.system('clear')

from pystyle import Colors, Colorate

proxylist = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
open('socksku.txt', 'w').write(proxylist)
proxsi = open('socksku.txt', 'r').read().splitlines()
os.system('rm -rf prox.txt')
prox = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
open('prox.txt', 'w').write(prox)
prox = open('prox.txt', 'r').read().splitlines()
nip = random.choice(proxsi)
proxs = {'http': 'socks4://' + nip}

ugen = []
for xd in range(10000):
    rr = random.randint
    build_b = random.choice(['001', '002', '003', '011', '012', '014', '015', '020', '021', '022', '023', '024'])
    bl_typ = random.choice(['TKQ1', 'SKQ1', 'TP1A', 'RKQ1', 'SP1A', 'RP1A', 'PPR1', 'QP1A'])
    oppo = random.choice(['CPH2461', 'CPH2451', 'PCGM00', 'PBBM00', 'PFZM10', 'PGGM10', 'PECT30', 'PCHM10', 'PEAT00', 'PEYM00', 'PESM10', 'PFGM00'])
    infinix = random.choice(['Infinix X669C', 'Infinix X6823', 'Infinix X676C', 'Infinix X683', 'Infinix X689C', 'Infinix X6811', 'Infinix X612B', 'Infinix X6810', 'Infinix X665E'])
    redmi = random.choice(['2211133G', 'M2004J19C', '22041219I', '22101316UG', '2209116AG', 'M2010J19SY', 'M2012K11C', 'Redmi Note 7', 'Redmi Note 8', 'Redmi Note 5'])
    um2 = f'Mozilla/5.0 (Linux; Android {str(rr(6, 12))}; {oppo} Build/{bl_typ}.{str(rr(120000, 220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80, 114))}.0.{str(rr(4200, 5400))}.{str(rr(70, 150))} Mobile Safari/537.36'
    um1 = f'Mozilla/5.0 (Linux; Android {str(rr(6, 12))}; {redmi} Build/{bl_typ}.{str(rr(120000, 220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80, 114))}.0.{str(rr(4200, 5400))}.{str(rr(70, 150))} Mobile Safari/537.36'
    um3 = f'Mozilla/5.0 (Linux; Android {str(rr(6, 12))}; {infinix} Build/{bl_typ}.{str(rr(120000, 220000))}.{build_b}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80, 114))}.0.{str(rr(4200, 5400))}.{str(rr(70, 150))} Mobile Safari/537.36'
    um4 = f'Mozilla/5.0 (Linux; Android {str(rr(6, 12))}; {infinix}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100, 114))}.0.{str(rr(4900, 5700))}.{str(rr(70, 150))} Mobile Safari/537.36'
    ugen.append(um2)
    ugen.append(um3)
    ugen.append(um1)
    ugen.append(um4)

def ____useragent____():
    version = random.choice(['14', '15', '10', '13', '7.0.0', '7.1.1', '9', '12', '11', '9.0', '8.0.0', '7.1.2', '7.0', '4', '5', '4.4.2', '5.1.1', '6.0.1', '9.0.1'])
    model = random.choice(['1105', '1107', '15', '3T', '62A', '6779', '6833', '7273', '9A', 'A1', 'A1 5G', 'A1 Pro', 'A11', 'A11k', 'A11x', 'A12', 'A15', 'A15s', 'A16', 'A16e', 'A16k', 'A16s', 'A17', 'A17k', 'A18', 'A1i 5G', 'A1k', 'A1s', 'A1x', 'A2 5G', 'A25', 'A2x 5G', 'A3', 'A3 5G', 'A3 Pro 5G', 'A30', 'A31', 'A31c', 'A32', 'A33', 'A33m', 'A33t', 'A34', 'A35', 'A36', 'A37', 'A37t', 'A38', 'A39', 'A3s'])
    build = random.choice(['MMB29Q', 'R16NW', 'LRX22C', 'R16NW', 'KTU84P', 'JLS36C', 'NJH47F', 'PPR1.180610.011', 'QP1A.190711.020', 'NRD90M', 'RP1A.200720.012', 'M1AJB', 'MMB29T'])
    ver = str(random.choice(range(77, 577)))
    ver2 = str(random.choice(range(57, 77)))
    return f'Mozilla/5.0 (Linux; Android {version}; {model} Build/{build}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ver2}.0.{ver}.8 Mobile Safari/537.36'

def ugen():
    rr = random.randint
    rc = random.choice
    versi_android = f'{rr(4, 12)}.0.1'
    android_api_level = str(rr(5, 14))
    versi_chrome = f'{rr(50, 114)}.0.{rr(1111, 4445)}.{rr(45, 150)}'
    device_oppo = rc(['CPH1723', 'CPH1901', 'CPH1920', 'CPH1933', 'CPH1937', 'CPH1945', 'CPH1951', 'CPH1969', 'CPH1979', 'CPH1983', 'CPH2005', 'CPH2023', 'CPH2083', 'CPH2003', 'CPH2004', 'CPH2269'])
    device_vivo = rc(['vivo 1917', 'vivo 1915', 'vivo 1911', 'vivo 1933', 'vivo 1912', 'vivo 1920', 'vivo 1921', 'vivo 1910', 'vivo 1927', 'vivo 1913', 'vivo 1923', 'vivo 1926', 'vivo 1928', 'vivo 1931', 'vivo 1935'])
    device_samsung = rc(['SM-G975F', 'SM-G532G', 'SM-N975F', 'SM-G988U', 'SM-G977U', 'SM-A705FN', 'SM-A515U1', 'SM-G955F', 'SM-A750G', 'SM-N960F', 'SM-G960U', 'SM-J600F', 'SM-A908B', 'SM-A705GM', 'SM-G970U', 'SM-A307FN', 'SM-G965U1', 'SM-A217F', 'SM-G986B', 'SM-A207M', 'SM-A515W', 'SM-A505G', 'SM-A315G', 'SM-A507FN', 'SM-A505U1', 'SM-G977T', 'SM-A025G', 'SM-J320F', 'SM-A715W', 'SM-A908N', 'SM-A205F', 'SM-G988B', 'SM-N986B', 'SM-A715F', 'SM-A515F', 'SM-G965F', 'SM-G960F', 'SM-A505F', 'SM-A207F', 'SM-A307G', 'SM-G970F', 'SM-A107F', 'SM-G935F', 'SM-G935A', 'SM-A310F', 'SM-J320FN'])
    device_xiaomi = rc(['Mi 11 Lite 5G', 'Mi 10T Pro', 'Mi 11 Lite', 'MI 8 Lite', 'MI 5X', 'Mi 11i', 'Xiaomi 11 Lite 5G NE', 'Xiaomi 12 Lite', 'Mi 9T Pro', 'Mi 12T', 'MIX 4', 'Mi Note 10', 'Mi 9 SE', 'Mi 8 SE', 'Mi 10 SE', 'MI MAX 3', 'Xiaomi 12T', 'MIX 2S', 'Mi A3', 'Mi 6', 'MI MAX 2', 'Mi A4'])
    device_infinix = rc(['Infinix Zero 20', 'Infinix Zero X', 'Infinix Note 12', 'Infinix Note 11', 'Infinix Note 10 Pro', 'Infinix Hot 12', 'Infinix Hot 11S', 'Infinix Hot 11', 'Infinix Hot 10', 'Infinix Hot 10i', 'Infinix Smart 5', 'Infinix S5 Pro', 'Infinix S4', 'Infinix Note 8i', 'Infinix Note 8', 'Infinix Hot 9'])
    device_google = rc(['Pixel 6a', 'Pixel 4', 'Pixel 5', 'Pixel 4 XL', 'Pixel 6', 'Pixel 6 Pro', 'Pixel 7 Pro', 'Pixel 4a', 'Pixel 5a'])
    device_realme = rc(['RMX1831', 'RMX1911', 'RMX1971', 'RMX2030', 'RMX2076', 'RMX2081', 'RMX2151', 'RMX2176', 'RMX2185'])
    density = rc(['{density=3.0,width=720,height=1280};FB_FW/1;', '{density=3.0,width=1080,height=1920};FB_FW/1;', '{density=2.75,width=1080,height=2028};FB_FW/1;'])
    opk = rc(['com.facebook.katana', 'com.facebook.adsmanager', 'com.facebook.lite', 'com.facebook.orca', 'com.facebook.mlite'])
    oph = rc(['Katana-Android', 'Adsmanager-Android', 'Facebook.lite-Android', 'Orca-Android', 'Facebook.mlite-Android'])
    carrier = rc(['SomeCarrier', 'Telkomsel', 'XL', 'Indosat', 'Three'])
    letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    build = f'{rc(letters)}{rc(letters)}{rr(10, 90)}{rc(letters)}'
    fbbv = rr(881000000, 998999999)
    ua_templates = []
    ua_templates.append(f'Mozilla/5.0 (Linux; Android {versi_android}; {device_samsung}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{versi_chrome} Mobile Safari/537.36 [FBAN/FB4A;FBAV/{rr(390, 490)}.0.0.30.108;FBBV/{fbbv};FBDM/{density};FBLC/en_US;FBRV/0;FB_FW/2;FBCR/{carrier};FBMF/Samsung;FBBD/Samsung;FBPN/{opk};FBDV/{device_samsung};FBSV/{versi_android};FBOP/1;FBCA/arm64-v8a;]')
    ua_templates.append(f'Mozilla/5.0 (Linux; Android {versi_android}; {device_xiaomi}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{versi_chrome} Mobile Safari/537.36 [FBAN/FB4A;FBAV/{rr(390, 490)}.0.0.30.108;FBBV/{fbbv};FBDM/{density};FBLC/en_US;FBRV/0;FB_FW/2;FBCR/{carrier};FBMF/Xiaomi;FBBD/Xiaomi;FBPN/{opk};FBDV/{device_xiaomi};FBSV/{versi_android};FBOP/1;FBCA/arm64-v8a;]')
    ua_templates.append(f'Dalvik/2.1.0 (Linux; U; Android {android_api_level}; {device_realme} Build/QP1A.{rr(111111, 999999)}.{rr(111, 999)}) {oph}/{rr(1, 9)}')
    ua_templates.append(f'Mozilla/5.0 (Linux; Android {versi_android}; {device_infinix}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{versi_chrome} Mobile Safari/537.36 [FBAN/FB4A;FBAV/{rr(390, 490)}.0.0.30.108;FBBV/{fbbv};FBDM/{density};FBLC/en_US;FBRV/0;FB_FW/2;FBCR/{carrier};FBMF/Infinix;FBBD/Infinix;FBPN/{opk};FBDV/{device_infinix};FBSV/{versi_android};FBOP/1;FBCA/arm64-v8a;]')
    ua_templates.append(f'Mozilla/5.0 (Linux; Android {versi_android}; {device_google}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{versi_chrome} Mobile Safari/537.36 [FBAN/FB4A;FBAV/{rr(390, 490)}.0.0.30.108;FBBV/{fbbv};FBDM/{density};FBLC/en_US;FBRV/0;FB_FW/2;FBCR/{carrier};FBMF/Google;FBBD/Google;FBPN/{opk};FBDV/{device_google};FBSV/{versi_android};FBOP/1;FBCA/arm64-v8a;]')
    return rc(ua_templates)

pro = ____useragent____()

def extractor(data):
    try:
        soup = BeautifulSoup(data, 'html.parser')
        data = {}
        for inputs in soup.find_all('input'):
            name = inputs.get('name')
            value = inputs.get('value')
            if name:
                data[name] = value
        return data
    except Exception as e:
        return {'error': str(e)}

def fake_philippines():
    first = Faker().first_name()
    last = Faker().last_name()
    return (first, last)

random_password1 = ['magandaako', 'gandako', 'pogiako', 'pogiako123', 'gwapoako123', 'gwapoako', 'iloveyou', 'i love you', 'cuteko', 'cuteko123', 'cuteko143', 'mahal123', 'mahal143', 'iloveyou143', 'maganda123', 'maganda143', 'pogi123', 'pogi143']
random_password2 = ['nepal12', 'nepal123', 'nepal1234', 'nepal12345', 'maya123', 'kathmandu', 'pokhara', 'tamang', 'maya1234', 'tamang123', 'tamang12345', 'nepal@123', 'kathmandu123']
random_password3 = ['khankhan', 'khan1122', 'ali12345', 'khanbaba', 'pakistan', 'khan12345', 'ali1122', 'khankhan12345', 'khan', 'baloch', 'pubg', 'pubg1122']
random_password4 = ['afghan', 'afghan12345', 'Afghan123', '600700', 'afghanistan', 'afghan1122', '500500', '100200', '10002000', '900900', 'kabul123', 'Û±Û³Û³Û³ÛµÛ¶Û·Û¸Û¹', 'Û±Û³Û³Û³ÛµÛ¶', 'afghan1234', 'kabul1234', 'khankhan', 'khan123', 'khan123456', 'khan786', '50006000']
random_password5 = ['Bangladesh', 'bangladesh', 'i love you', 'iloveyou', 'free fire', 'freefire', '57575751', '57273200', 'i love you', 'iloveyou', '59039200', '708090']
random_password6 = ['57575751', '57273200', 'i love you', 'iloveyou', '59039200', '708090']

def get_philippines_password():
    return random.choice(random_password1)

def get_nepal_password():
    return random.choice(random_password2)

def get_pakistan_password():
    return random.choice(random_password3)

def get_afghanistan_password():
    return random.choice(random_password4)

def get_bangladesh_password():
    return random.choice(random_password5)

def get_india_password():
    return random.choice(random_password6)

def get_temp_email1():
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = random.choice(['discardmail.com', 'discardmail.de'])
    return f'{name}@{domain}'

def get_temp_email2():
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = random.choice(['yopmail.com'])
    return f'{name}@{domain}'

def get_temp_email3():
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = random.choice(['tempinbox.xyz', 'glowend.xyz', 'thepiratebay.cloud', 'cryptoblad.online', 'cryptoblad.nl'])
    return f'{name}@{domain}'

def get_temp_email4():
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = random.choice(['ezfastmail.com', 'crunchmails.org', 'aious.edu.pl', 'tubemail.space', 'onealpha.cloud', 'fastmeta.edu.pl', 'spamuraai.com'])
    return f'{name}@{domain}'

def get_temp_email5():
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = random.choice(['fexbox.org', 'fexpost.com', 'fextemp.com', 'mailto.plus', 'merepost.com', 'rover.info', 'chitthi.in', 'any.pink', 'mailbox.in.ua'])
    return f'{name}@{domain}'

def get_temp_email6():
    name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = random.choice(['armyspy.com', 'cuvox.de', 'dayrep.com', 'einrot.com', 'fleckens.hu', 'gustr.com', 'jourrapide.com', 'rhyta.com', 'superrito.com', 'teleworm.us'])
    return f'{name}@{domain}'

def GetEmail1():
    response = requests.post('https://api.internal.temp-mail.io/api/v3/email/new').json()
    return response['email']

def GetCode1(email):
    try:
        response = requests.get(f'https://api.internal.temp-mail.io/api/v3/email/{email}/messages').text
        code = re.search('FB-(\\d+)', response).group(1)
        return code
    except:
        return

def linex():
    print('\x1b[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

"""
try:
    response = requests.get('https://raw.githubusercontent.com/ERRORDEATH13451/ERROR_CONTROL/refs/heads/main/status_auto.txt')
    statuss = response.text.strip()
except Exception as e:
    pass

status = str(statuss)
"""

status = "FREE"

try:
    versionn = '0.6'
except Exception as e:
    pass

version = versionn.strip()
logo = Colorate.Horizontal(Colors.green_to_white,'''
 ▗▖ ▗  ▖▄▄▄▖ ▄▄      ▗▄ ▗▄▄ ▗▄▄▖ ▗▖ ▄▄▄▖▗▄▄▖    ▗▄▄▖▗▄▄
 ▐▌ ▐  ▌ ▐  ▗▘▝▖    ▗▘ ▘▐ ▝▌▐    ▐▌  ▐  ▐       ▐   ▐  ▌
 ▌▐ ▐  ▌ ▐  ▐  ▌    ▐   ▐▄▄▘▐▄▄▖ ▌▐  ▐  ▐▄▄▖    ▐▄▄▖▐▄▄▘
 ▙▟ ▐  ▌ ▐  ▐  ▌    ▐   ▐ ▝▖▐    ▙▟  ▐  ▐       ▐   ▐  ▌
▐  ▌▝▄▄▘ ▐   ▙▟      ▚▄▘▐  ▘▐▄▄▖▐  ▌ ▐  ▐▄▄▖    ▐   ▐▄▄▘ MR-ERROR''')

info = f'''{style} \x1b[1;32mAUTHOR   \x1b[1;37m: \x1b[1;32mETHAN KLEIN HUILEN
{style} \x1b[1;32mFACEBOOK \x1b[1;37m: \x1b[1;32mETHAN KLEIN HUILEN
{style} \x1b[1;32mTYPE     \x1b[1;37m: \x1b[1;32mAUTO CREATE FACEBOOK
{style} \x1b[1;32mSYSTEM   \x1b[1;37m: \x1b[1;32mDATA/WIFI NO VPN
{style} \x1b[1;32mVERSION  \x1b[1;37m: \x1b[1;32m{versionn}'''

def main_logo():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(logo)
    linex()
    print(info)
    linex()

oks, loop, ua, ussr, tw, cps, plist = ([], 0, [], [], [], [], [])

"""
async def sub():
    os.system('clear' if os.name == 'posix' else 'cls')
    async with aiohttp.ClientSession() as sess:
        async with sess.get('https://pastebin.com/5wE9EWr6') as appro:
            r1 = await appro.text()
            if key1 in r1:
                os.system('clear' if os.name == 'posix' else 'cls')
                print(f'{style} \x1b[1;32mYOUR KEY IS APPROVED')
                sp(3)
                main()
            else:
                os.system('clear' if os.name == 'posix' else 'cls')
                print('\t\x1b[1;32mFIRST GET APPROVAL\x1b[1;37m')
                time.sleep(5)
                main_logo()
                print(f'{style} \x1b[1;32mYOU HAVE TO GET APPROVE FIRST BEFORE USING IT\n{stylee} \x1b[1;31mYOUR KEY IS NOT APPROVED\n\x1b[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{style} \x1b[1;32mYOUR KEY \x1b[1;37m: \x1b[1;32m{key1}\n\x1b[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                input(f'{style} \x1b[1;37mPRESS ENTER TO SEND KEY')
                time.sleep(3.5)
                tks = f'HELLO ERROR X ETHAN, DEAR ADMIN, PLEASE APPROVE MY KEY TO PREMIUM THANKS.\nYOUR KEY : {key1}'
                msg = urllib.parse.quote(tks)
                os.system(f'am start -a android.intent.action.VIEW -d "https://wa.me/+639610075203?text={msg}"')
                await sub()
"""

async def sub():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f'{style} \x1b[1;32mFREE VERSION - NO APPROVAL NEEDED')
    sp(3)
    main()

def main():
    main_logo()
    print('\x1b[1;37m[\x1b[1;32mA\x1b[1;37m]\x1b[1;32m START AUTO CREATE')
    print('\x1b[1;37m[\x1b[1;32mO\x1b[1;37m]\x1b[1;31m EXIT THIS PROGRAM')
    linex()
    auto_select = input('\x1b[1;37m[\x1b[1;32m?\x1b[1;37m]\x1b[1;32m CHOOSE \x1b[1;37m: \x1b[1;32m')
    if auto_select in ['A', 'a', '01', '1']:
        ____create____()
    elif auto_select in ['O', 'o', '00', '0']:
        os.system('exit')
    else:
        main()

def ____create____():
    global num_accounts
    main_logo()
    print('\x1b[1;37m[\x1b[1;32mA\x1b[1;37m]\x1b[1;32m TEMPMAIL 1')
    print('\x1b[1;37m[\x1b[1;32mB\x1b[1;37m]\x1b[1;32m TEMPMAIL 2')
    print('\x1b[1;37m[\x1b[1;32mC\x1b[1;37m]\x1b[1;32m TEMPMAIL 3')
    print('\x1b[1;37m[\x1b[1;32mD\x1b[1;37m]\x1b[1;32m TEMPMAIL 4')
    print('\x1b[1;37m[\x1b[1;32mE\x1b[1;37m]\x1b[1;32m TEMPMAIL 5')
    print('\x1b[1;37m[\x1b[1;32mF\x1b[1;37m]\x1b[1;32m TEMPMAIL 6')
    linex()
    tempmail_email = input('\x1b[1;37m[\x1b[1;32m?\x1b[1;37m]\x1b[1;32m CHOOSE \x1b[1;37m: \x1b[1;32m')
    main_logo()
    print(f'{style} \x1b[1;32mEXAMPLE \x1b[1;37m: \x1b[1;32m10000 20000 50000 99999')
    linex()
    try:
        num_accounts = int(input(f'{style} \x1b[1;32mHOW MANY ACCOUNT NUMBER \x1b[1;37m:\x1b[1;32m '))
    except Exception:
        pass
    
    main_logo()
    print('\x1b[1;37m[\x1b[1;32mA\x1b[1;37m]\x1b[1;32m AUTO PHILIPPINES PASSWORD')
    print('\x1b[1;37m[\x1b[1;32mB\x1b[1;37m]\x1b[1;32m AUTO NEPAL PASSWORD')
    print('\x1b[1;37m[\x1b[1;32mC\x1b[1;37m]\x1b[1;32m AUTO PAKISTAN PASSWORD')
    print('\x1b[1;37m[\x1b[1;32mD\x1b[1;37m]\x1b[1;32m AUTO AFGHANISTAN PASSWORD')
    print('\x1b[1;37m[\x1b[1;32mE\x1b[1;37m]\x1b[1;32m AUTO BANGLADESH PASSWORD')
    print('\x1b[1;37m[\x1b[1;32mF\x1b[1;37m]\x1b[1;32m AUTO INDIA PASSWORD')
    print('\x1b[1;37m[\x1b[1;32mG\x1b[1;37m]\x1b[1;32m CUSTOM PASSWORD')
    linex()
    password_country = input('\x1b[1;37m[\x1b[1;32m?\x1b[1;37m]\x1b[1;32m CHOOSE \x1b[1;37m: \x1b[1;32m')
    if password_country in ['G', 'g', '07', '7']:
        linex()
        random_password = input(f'{style} \x1b[1;32mENTER CUSTOM PASSWORD \x1b[1;37m: \x1b[1;32m')
    
    main_logo()
    print(f'{style} \x1b[1;32mTOTAL CREATE LIMIT \x1b[1;37m:\x1b[1;32m {num_accounts}')
    print(f'{style} \x1b[1;32mIF NO RESULT \x1b[1;37m[\x1b[1;32mON\x1b[1;37m/\x1b[1;31mOFF\x1b[1;37m] \x1b[1;32mAIRPLANE MODE')
    linex()
    
    for make in range(int(num_accounts)):
        sys.stdout.write(f'\r\r\x1b[1;37m[\x1b[1;32mFINDING-M1\x1b[1;37m]\x1b[1;37m-\x1b[1;37m[\x1b[1;32m{make + 1}\x1b[1;37m]\x1b[1;37m-\x1b[1;37m[\x1b[1;32mOK\x1b[1;37m•\x1b[1;32m{len(oks)}\x1b[1;37m]\x1b[1;37m-\x1b[1;37m[\x1b[1;31mCP\x1b[1;37m•\x1b[1;31m{len(cps)}\x1b[1;37m]\x1b[1;37m')
        sys.stdout.flush()
        
        ses = requests.Session()
        session = requests.Session()
        try:
            response = ses.get(url='https://x.facebook.com/reg', params={'_rdc': '1', '_rdr': '', 'wtsid': 'rdr_0t3qOXoIHbMS6isLw', 'refsrc': 'deprecated'}, timeout=20)
            mts = ses.get('https://x.facebook.com', timeout=20).text
            m_ts = re.search('name=\"m_ts\" value=\"(.*?)\"', str(mts)).group(1)
        except Exception:
            pass
        
        formula = extractor(response.text)
        firstname, lastname = fake_philippines()
        
        if tempmail_email in ['A', 'a', '01', '1']:
            email2 = get_temp_email1()
        elif tempmail_email in ['B', 'b', '02', '2']:
            email2 = get_temp_email2()
        elif tempmail_email in ['C', 'c', '03', '3']:
            email2 = get_temp_email3()
        elif tempmail_email in ['D', 'd', '04', '4']:
            email2 = get_temp_email4()
        elif tempmail_email in ['E', 'e', '05', '5']:
            email2 = get_temp_email5()
        elif tempmail_email in ['F', 'f', '06', '6']:
            email2 = get_temp_email6()
        
        if password_country in ['A', 'a', '01', '1']:
            random_password = get_philippines_password()
        elif password_country in ['B', 'b', '02', '2']:
            random_password = get_nepal_password()
        elif password_country in ['C', 'c', '03', '3']:
            random_password = get_pakistan_password()
        elif password_country in ['D', 'd', '04', '4']:
            random_password = get_afghanistan_password()
        elif password_country in ['E', 'e', '05', '5']:
            random_password = get_bangladesh_password()
        elif password_country in ['F', 'f', '06', '6']:
            random_password = get_india_password()
        
        payload = {'ccp': '2', 'reg_instance': str(formula['reg_instance']), 'submission_request': 'true', 'helper': '', 'reg_impression_id': str(formula['reg_impression_id']), 'ns': '1', 'zero_header_af_client': '', 'app_id': '103', 'logger_id': str(random.randint(1, 28)), 'firstname': firstname, 'lastname': lastname, 'birthday_wrapper': '', 'birthday_day': 'false', 'field_names[2]': 'false', 'reg_email__': email2, 'email2': email2, 'field_names[3]': 'sex', 'preferred_pronoun': 'false', 'custom_gender': '', 'field_names[4]': 'reg_passwd__', 'name_suggest_elig': 'was_shown_name_suggestions', 'did_use_suggested_name': 'use_custom_gender', 'guid': 'pre_form_step', 'encpass': ''}
        
        header1 = {'Host': 'm.facebook.com', 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1', 'User-Agent': pro, 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'dnt': '1', 'X-Requested-With': 'mark.via.gp', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-User': '?1', 'Sec-Fetch-Dest': 'document', 'dpr': '1.75', 'viewport-width': '980', 'sec-ch-ua': '\"Android WebView\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '\"Android\"', 'sec-ch-ua-platform-version': '\"\"', 'sec-ch-ua-model': '', 'sec-ch-ua-full-version-list': 'dark', 'sec-ch-prefers-color-scheme': 'gzip, deflate, br, zstd', 'Accept-Encoding': 'en-GB,en-US;q=0.9,en;q=0.8'}
        
        reg_url = 'https://www.facebook.com/reg/submit/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNzM0NDE0OTk2LCJjYWxsc2l0ZV9pZCI6OTA3OTI0NDAyOTQ4MDU4fQ%3D%3D&multi_step_form=1&skip_suma=0&shouldForceMTouch=1'
        
        try:
            py_submit = ses.post(reg_url, data=payload, headers=header1, proxies=proxs, timeout=25)
        except Exception:
            pass
        
        if 'c_user' in py_submit.cookies:
            first_cok = ses.cookies.get_dict()
            uid = str(first_cok['c_user'])
            header2 = {'authority': 'm.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control': 'max-age=0', 'dpr': '2', 'referer': 'https://m.facebook.com/login/save-device/', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"125\", \"Google Chrome\";v=\"125\"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '\"Android\"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'same-origin', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': pro, 'viewport-width': '980'}
            params = {'next': 'https://m.facebook.com/?deoia=1', 'soft': 'hjk'}
            
            try:
                con_sub = ses.get('https://x.facebook.com/confirmemail.php', params=params, headers=header2, proxies=proxs, timeout=20).text
            except Exception:
                pass
            
            valid = 'CODE NOT FOUND'
            if valid:
                confirm_id(email2, uid, valid, con_sub, ses, random_password)
            else:
                cps.append(email2)
        else:
            cps.append(email2)
    
    print('')
    linex()
    print(f'{style} \x1b[1;32mTHE PROCESS HAS BEEN COMPLETED')
    print(f'{style} \x1b[1;32mTOTAL OK \x1b[1;37m: \x1b[1;32m{len(oks)}\n{style} \x1b[1;31mTOTAL CP \x1b[1;37m: \x1b[1;31m{len(cps)}')
    linex()
    exit()

def confirm_id(mail, uid, otp, data, ses, random_password):
    try:
        url = 'https://m.facebook.com/confirmation_cliff/'
        params = {'contact': mail, 'type': 'submit', 'is_soft_cliff': 'false', 'medium': 'email', 'code': otp}
        payload = {'fb_dtsg': 'NAcMC2x5X2VrJ7jhipS0eIpYv1zLRrDsb5y2wzau2bw3ipw88fbS_9A:0:0', 'jazoest': re.search('\"\\d+\"', data).group().strip('\"'), 'lsd': re.search('\"LSD\",\\[\\],{\"token\":\"([^\"]+)\"}', str(data)).group(1), '__dyn': '', '__csr': '', '__req': '4', '__fmt': '1', '__a': '', '__user': uid}
        headers = {'User-Agent': pro, 'Accept-Encoding': 'gzip, deflate, br, zstd', 'sec-ch-ua-full-version-list': '', 'sec-ch-ua-platform': '\"Android\"', 'sec-ch-ua': '\"Android WebView\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"', 'sec-ch-ua-model': '\"\"', 'sec-ch-ua-mobile': '?1', 'x-asbd-id': '129477', 'x-fb-lsd': 'KnpjLz-YdSXR3zBqds98cK', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua-platform-version': '\"\"', 'origin': 'https://m.facebook.com', 'x-requested-with': 'mark.via.gp', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://m.facebook.com/confirmemail.php?next=https%3A%2F%2Fm.facebook.com%2F%3Fdeoia%3D1&soft=hjk', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8', 'priority': 'u=1, i'}
        response = ses.post(url, params=params, data=payload, headers=headers, proxies=proxs, timeout=25)
        if 'checkpoint' in str(response.url):
            cps.append(mail)
            return
        cookie_string = '; '.join((f'{k}={v}' for k, v in ses.cookies.get_dict().items()))
        print(f'\r\r\x1b[1;37m[\x1b[1;32mSUCCESS-ERROR💚\x1b[1;37m] \x1b[1;32m{uid} \x1b[1;31m» \x1b[1;32m{random_password}')
    except Exception as e:
        pass
    else:
        try:
            open('/sdcard/MR-ERROR-AUTO-CRATE-M1-COOKIE.txt', 'a').write(uid + '|' + random_password + '|' + otp + '|' + cookie_string + '\n')
            open('/sdcard/MR-ERROR-AUTO-CRATE-M1-OK.txt', 'a').write(uid + '|' + random_password + '\n')
            open('/sdcard/MR-ERROR-AUTO-CRATE-M1-EMAIL.txt', 'a').write(mail + '\n')
        except Exception:
            pass
        oks.append(uid)
    return None

"""
STATUS_URL = 'https://raw.githubusercontent.com/ERRORDEATH13451/ERROR_CONTROL/main/status_auto.txt'
try:
    response = requests.get(STATUS_URL, timeout=10)
    response.raise_for_status()
    status = response.text.strip()
except Exception as e:
    pass

print(f'{style} \x1b[1;32mCHECKING TOOL STATUS...\x1b[1;37m')
time.sleep(2)
if status == 'FREE':
    error(f'{style} \x1b[1;32mCONGRATULATIONS TOOL IS FREE NOW')
    time.sleep(4)
    # free_login()  # This function needs to be defined
elif status == 'PAID':
    error(f'{style} \x1b[1;32mTOOL IS PAID NOW')
    time.sleep(4)
    asyncio.run(bypass())
else:
    asyncio.run(bypass())

print(f'{style} \x1b[1;32mFREE VERSION - NO STATUS CHECK NEEDED\x1b[1;37m')
time.sleep(2)
error(f'{style} \x1b[1;32mTOOL IS NOW FREE - ENJOY!\x1b[1;37m')
time.sleep(4)
asyncio.run(sub())

os.system('clear' if os.name == 'posix' else 'cls')
print(f'{style} \x1b[1;32mMR-ERROR TOOL IS NOT ALLOW WITHOUT STORAGE PERMISSION')
os.system('termux-setup-storage')
os.system('clear')
exit(f'{style} \x1b[1;32mRUN AGAIN : python AUTO.py')
"""

asyncio.run(sub())

"""
os.system('clear' if os.name == 'posix' else 'cls')
print(f'{stylee} \x1b[1;31mNO INTERNET CONNECTION & DON\'T TRY TO BYPASS')
print('\x1b[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
sys.exit()
"""
