import requests

# INVYRAX going full Tapori mode
print("=========================================")
print("🤖 [INVYRAX]: Kya bolti company! System chalu hai.")
print("=========================================")

city = input("🚨 Kaunse ilake ka scene dekhna hai? City daal: ")
url = f"https://wttr.in/{city}?format=j1"

print(f"\n⏳ Apun check kar rha hai mitr... {city.title()} ka kya mahaul hai...")

try:
    response = requests.get(url)
    data = response.json()
    
    current = data['current_condition'][0]
    temp = current['temp_C']
    desc = current['weatherDesc'][0]['value']
    humidity = current['humidity']
    
    print("\n📜 ======= MAHAUL KA REPORT =======")
    print(f"📍 Ilaka:        {city.title()}")
    print(f"🔥 Garmi/Thandi:  {temp}°C (Bole toh jhakas!)")
    print(f"🌤️ Scene kya hai: {desc}")
    print(f"💦 Pasina Metre:  {humidity}% (Chip-chipa hai boss)")
    print("====================================")
    print("😎 Chal abhi palti maar, kaam par lag!")

except Exception as e:
    print("\n❌ Arey BSDK, locha ho gaya! Net chalu hai kya? City ka naam sahi se daal!")
