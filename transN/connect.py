import network

wifi = None

def connect():
    global wifi
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect("ESP_D356F5")
    wifi.ifconfig()

if __name__ == "__main__":
    connect()