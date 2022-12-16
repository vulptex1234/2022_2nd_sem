import network
import machine
import utime
import webrepl
import socket
from password import *

SSID_NAME_LAB = "CDSL-A910-11n"
SSID_ESP = "ESP_D38A19"

N = ""

p2 = Pin(2,Pin.OUT)
red = Pin(13, Pin.OUT)
blue = Pin(4, Pin.OUT)
green = Pin(5, Pin.OUT)

wifiStatus = True

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

ap = None
port = 80
listenSocket = None

#wifiをスキャンしてリスト化
def wifiscan():
    global wifi
    wifiList = wifi.scan()
    wifiAPDict = []
    for wl in wifiList:
        if wl[0].decode("utf-8") != "":
            wifiAPDict.append(wl[0].decode("utf-8"))
    return wifiAPDict

#受信モード
def accept():
    global ap
    port = 80
    listenSocket = None
    ap = network.WLAN(network.AP_IF)

    ip = wifi.ifconfig()[0]
    listenSocket = socket.socket()
    listenSocket.bind((ip,port))
    listenSocket.listen(5)
    listenSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    ap.active(True)
    SSID = ap.config("essid")
    print(SSID)

    while True:
        print("accepting......")
        conn, addr = listenSocket.accept() #受信待機中
        print(addr, "connected")

        while True:
            data = conn.recv(1024)
            print(data)

#研究室wifiに接続
def connect_lab_wifi(ssid, passkey, timeout = 10):
    count = 0
    while count < 3:
        try:
            wifi.connect(ssid, passkey)
            break
        except:
            utime.sleep(3)
            count += 1
    while not wifi.isconnected() and timeout > 0:
        print(".")
        utime.sleep(1)
        timeout -= 1

    if wifi.isconnected():
        p2.on()
        print(ssid,  "Connected")
        webrepl.start(password = webrepl_pass)
        return wifi
    else:
        print(ssid, "Connetion failed!")
        return ""

#ESPwifiに接続
def connect_esp_wifi(ssid, timeout = 10):
    count = 0
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)

    while count < 3:
        try:
            wifi.connect(ssid)
            break
        except:
            utime.sleep(3)
            count += 1
    while not wifi.isconnected() and timeout > 0:
        print(".")
        utime.sleep(1)
        timeout -= 1

    if wifi.isconnected():
        p2.on()
        print(ssid, "Connected")
        print(wifi.ifconfig())
        return wifi
    else:
        print(ssid, "Connection failed")
        return ""