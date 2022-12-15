import network

ap = None

def main():
    global ap
    ap = network.WLAN(network.AP_IF)

    ap.active(True)
    print(ap.config("essid"))

if __name__ == "__main__":
    main()