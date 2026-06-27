import requests
import sys

print("=========================================")
print("[INVYRAX]: IP Geolocation Tracker Active")
print("=========================================")

# User se IP address maango
ip_target = input("🌐 Jis IP ka scene dekhna hai, woh daal (Khali chhodega toh tera khudka dikhaega): ")

print("\n📡 Ruk Huzaifa, satellite ghuma ke location trace kar rha hoon...")

# ip-api ka free route query karo
url = f"http://ip-api.com/json/{ip_target}"

try:
    response = requests.get(url)
    data = response.json()
    
    # Check karo locha hua ya nahi
    if data['status'] == 'fail':
        print("\n❌ Arey Bokachoda! Galat IP daala tumne. Sahi se daal ree!")
        sys.exit()
        
    print("\n🗺️ ======= LOCATION REPORT =======")
    print(f"🌍 Country:      {data.get('country')} ({data.get('countryCode')})")
    print(f"🏙️ State/Region: {data.get('regionName')}")
    print(f"📍 City:         {data.get('city')}")
    print(f"📮 Zip Code:     {data.get('zip')}")
    print(f"📡 Internet/ISP: {data.get('isp')}")
    print(f"🧭 Lat/Lon:      {data.get('lat')}, {data.get('lon')}")
    print("====================================")
    print(" Target ka area maloom pad gaya, Boss! Hehe ~")

except Exception as e:
    print("\n❌ Sed moment ho gaya! Network dead hai ya API ne dhoka de diya (Apki Ex ki tarha)")
