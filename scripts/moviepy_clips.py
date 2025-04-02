from moviepy.editor import VideoFileClip

# 定義要裁切的片段（時間以秒表示）
video_segments = [
    ("full_溝通藝術_成功職場互動.mp4.mkv", 615, 765, "cut_溝通藝術.mp4"),       # 00:10:15 - 00:12:45
    ("full_蔡善雯_創業專訪.mp4.webm", 330, 480, "cut_蔡善雯.mp4"),             # 00:05:30 - 00:08:00
    ("full_王立華_自己是最好的產品.mp4.mkv", 900, 1050, "cut_王立華.mp4"),   # 00:15:00 - 00:17:30
    ("full_王奕凱_起士公爵.mp4.mkv", 720, 870, "cut_王奕凱.mp4"),             # 00:12:00 - 00:14:30
]

for input_file, start, end, output_file in video_segments:
    print(f"🎬 裁切：{output_file}")
    clip = VideoFileClip(input_file).subclip(start, end)
    clip.write_videofile(output_file, codec="libx264")
