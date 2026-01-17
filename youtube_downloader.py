from yt_dlp import YoutubeDL

url = input("حط لينك الفيديو: ")

print("""
اختار الجودة:
1 - أعلى جودة
2 - 720p
3 - 480p
4 - صوت فقط
""")

choice = input("اختيارك: ")

if choice == "1":
    format_choice = "bestvideo+bestaudio/best"
elif choice == "2":
    format_choice = "bestvideo[height<=720]+bestaudio/best"
elif choice == "3":
    format_choice = "bestvideo[height<=480]+bestaudio/best"
elif choice == "4":
    format_choice = "bestaudio"
else:
    print("اختيار غلط")
    exit()

ydl_opts = {
    "format": format_choice,
    "outtmpl": "%(title)s.%(ext)s"
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("✅ التحميل خلص")
