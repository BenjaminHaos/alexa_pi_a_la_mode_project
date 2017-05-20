**Install [cec-utils](https://timleland.com/raspberry-pi-turn-tv-onoff-cec/) :**  
```sudo apt-get -y install cec-utils```  

**Show [Available Commands](https://raspberrypi.stackexchange.com/questions/9142/commands-for-using-cec-client) :**  
```echo h | cec-client -s -d 1```

**Show Active Devices :**  
```echo lad | cec-client -s -d 1```

**Display Device Info :**  
```echo scan | cec-client -s -d 1```

**Turn Television On**  
```echo "on 0" | cec-client RPI -s -d 11```  
or  
```echo "tx 10:04" | cec-client RPI -s -d 1```

**Turn Television Off**  
```echo "standby 0" | cec-client RPI -s -d 1```  
or  
```echo "tx 10:36" | cec-client RPI -s -d 1```

**Mute/Unmute Audio**  
```echo "tx 15:44:43" | cec-client RPI -s -d 1```

**Switch TV source to Chromecast (1.3.0.0)**  
```echo "tx 1F:82:13:00" | cec-client RPI -s -d 1```

**Switch TV source to FireTV (2.0.0.0)**  
```echo "tx 1F:82:20:00" | cec-client RPI -s -d 1```

**Switch TV source to Raspberry Pi (3.0.0.0)**  
```echo "tx 1F:82:30:00" | cec-client RPI -s -d 1```

**Switch Everything to Standby**  
```echo "tx 1F:36" | cec-client RPI -s -d 1```

**Pause**  
```echo "tx 14:44:44" | cec-client RPI -s -d 1```

**Rewind**  
```echo "tx 14:44:48" | cec-client RPI -s -d 1```

**Fast-Forward**  
```echo "tx 14:44:49" | cec-client RPI -s -d 1```

**Toggle Audio Reciever Power**  
```echo "tx 15:44:40" | cec-client RPI -s -d 1```

**Audio Reciever Power On**  
```echo "tx 15:44:6D" | cec-client RPI -s -d 1```

**Audio Reciever Power Off**  
```echo "tx 15:44:6C" | cec-client RPI -s -d 1```

**Volume Up**  
```echo "tx 15:44:41" | cec-client RPI -s -d 1```  
*may need to be followed by :*  
```echo "tx 15:45" | cec-client RPI -s -d 1```

**Volume Down**  
```echo "tx 15:44:42" | cec-client RPI -s -d 1```  
*may need to be followed by :*  
```echo "tx 15:45" | cec-client RPI -s -d 1```

---
***Note***

All the above command can also be tested by running:
```
$ cec-client
```
and entering echoed text.

---

**Site for testing cec frame commands :**  
http://www.cec-o-matic.com/