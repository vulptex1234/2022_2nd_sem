#アクセスポイントモード起動
import network

ap = None

def main():
    global ap
    ap = network.WLAN(network.AP_IF)

    ap.active(True)
    SSID = ap.config("essid")
    print(SSID)

if __name__ == "__main__":
    main()