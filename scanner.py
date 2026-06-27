import socket
import sys

print("=========================================")
print("[INVYRAX]: Cyber Network Scanner Active")
print("=========================================")

# Get target details from user
target_host = input("🌐 Target IP ya Website daal Bade bhai (e.g., scanme.nmap.org): ")
target_port = int(input("🔌 Kaunsa port check karne ka hai? (e.g., 80, 22, 443): "))

print(f"\n🕵️‍♂️ Apun jaa rha hai port {target_port} ki talashi lene...")

# Create a network socket connector
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(3.0) # Stop hanging if the port is dead

try:
    # Try connecting to the target on that port
    result = s.connect_ex((target_host, target_port))
    
    if result == 0:
        print(f"\n🚨 ALERT BHAIYA JI! Port {target_port} OPEN hai! Koi bhi andar ghus sakta hai! ")
    else:
        print(f"\n🔒 HATT BC: Port {target_port} LOCKED hai. Entry bandh hai.")
        
    s.close()

except Exception as e:
    print("\n❌ Arey Horny ho kya! Address galat daala ya net kharab hai?")
    sys.exit()
