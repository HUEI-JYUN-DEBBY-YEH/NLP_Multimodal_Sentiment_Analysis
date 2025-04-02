from yt_dlp import YoutubeDL

video_list = [
    ("https://www.youtube.com/watch?v=DNa1c2izOhE", "full_溝通藝術_成功職場互動.mp4"),
    ("https://www.youtube.com/watch?v=kobD38heJZw", "full_蔡善雯_創業專訪.mp4"),
    ("https://www.youtube.com/watch?v=WV072eSp8FE", "full_王立華_自己是最好的產品.mp4"),
    ("https://www.youtube.com/watch?v=gU3TGei8DRo", "full_王奕凱_起士公爵.mp4"),
]

for url, output in video_list:
    ydl_opts = {
        'format': 'bestvideo+bestaudio',
        'outtmpl': output,
    }

    print(f"📥 正在下載：{output}")
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
