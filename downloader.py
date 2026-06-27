import os
import sys

# Target directory definition
DOWNLOAD_DIR = os.path.expanduser("~/storage/shared/Raxs_Corner")

print("=========================================")
print("🚀 [INVYRAX]: Rax's Downloader")
print("=========================================")
print(f"📂 Files kahan jayenge: Internal Storage -> Raxs_Corner\n")

print("1. Direct URL/Link se download (JPG, MP4, Docs, etc.)")
print("2. YouTube Video Link se download (Best Quality / 4K support)")
print("3. YouTube pe SEARCH karke video download karo")
print("4. YouTube se sirf MP3 Audio nikalna hai")

choice = input("\n👉 Kya scene hai boss? Choice daal (1-4): ")

if choice == '1':
    url = input("🔗 Link (URL) paste kar Bhosdu: ")
    # Extract filename from URL
    filename = url.split("/")[-1].split("?")[0] or "downloaded_file"
    output_path = os.path.join(DOWNLOAD_DIR, filename)
    print("\n⏳ Downloading chalu hai...")
    os.system(f'curl -L "{url}" -o "{output_path}"')
    print(f"\n✅ Jhakas! File save ho gayi Raxs_Corner mein as: {filename}")

elif choice == '2':
    url = input("📹 YouTube Video ka Link daal: ")
    print("\n⏳ High Quality / 4K checking and downloading...")
    # Best video + best audio merge dynamically
    os.system(f'yt-dlp -f "bestvideo+bestaudio/best" --merge-output-format mp4 -P "{DOWNLOAD_DIR}" "{url}"')
    print("\n✅ Video Extract karliya Boss! Check Raxs_Corner.")

elif choice == '3':
    query = input("🔍 Kya search maarna hai, Porn? (e.g., Sunny Leone, Moaning sound): ")
    print(f"\n⏳ YouTube pe '{query}' search karke sabse best matching video utha rha hoon...")
    # Searches youtube and grabs the top result
    os.system(f'yt-dlp -f "bestvideo+bestaudio/best" --merge-output-format mp4 -P "{DOWNLOAD_DIR}" "ytsearch1:{query}"')
    print("\n✅ Search complete aur video saved!")

elif choice == '4':
    url = input("🎵 YouTube Video Link daal (Audio nikalne ke liye): ")
    print("\n⏳ Video me se music Chuss rha hoon...")
    os.system(f'yt-dlp -x --audio-format mp3 --audio-quality 0 -P "{DOWNLOAD_DIR}" "{url}"')
    print("\n✅ MP3 gaana tayyar hai, Huzaifa!")

else:
    print("❌ Galat number daba diya re baba!")
