import os
import subprocess
import pandas as pd
from deepface import DeepFace
from tqdm import tqdm

# ✅ 設定資料夾
project_root = "D:\\NLP_Multimodal_Sentiment_Analysis"
video_files = [f for f in os.listdir(project_root) if f.startswith("cut_") and f.endswith(".mp4")]
output_root = os.path.join(project_root, "visual_emotion_output")
os.makedirs(output_root, exist_ok=True)

for video in video_files:
    base = os.path.splitext(video)[0]  # e.g. cut_王立華
    print(f"\n🎞️ 處理影片：{video}")
    
    # 建立影片專屬資料夾
    video_dir = os.path.join(output_root, base)
    os.makedirs(video_dir, exist_ok=True)
    
    # === Step 1: 擷取每秒畫面 ===
    frame_pattern = os.path.join(video_dir, "frame_%04d.jpg")
    video_path = os.path.join(project_root, video)
    cmd = f'ffmpeg -i "{video_path}" -vf fps=1 "{frame_pattern}" -hide_banner -loglevel error'
    subprocess.call(cmd, shell=True)
    print("✅ 已擷取畫面")

    # 建立 frame_second.csv（時間對應）
    frame_files = sorted([f for f in os.listdir(video_dir) if f.startswith("frame_") and f.endswith(".jpg")])
    frame_data = [{"frame_file": f, "second": i} for i, f in enumerate(frame_files)]
    df_frames = pd.DataFrame(frame_data)
    df_frames.to_csv(os.path.join(video_dir, "frame_second.csv"), index=False, encoding="utf-8-sig")

    # === Step 2: 使用 DeepFace 預測情緒 ===
    visual_emotions = []
    for row in tqdm(frame_data, desc="🔍 表情分析中"):
        img_path = os.path.join(video_dir, row["frame_file"])
        try:
            result = DeepFace.analyze(img_path=img_path, actions=['emotion'], enforce_detection=False)
            emotion = result[0]["dominant_emotion"]
            conf = result[0]["emotion"][emotion]
        except Exception as e:
            emotion = "error"
            conf = 0.0
        visual_emotions.append({
            "second": row["second"],
            "visual_emotion": emotion,
            "vis_confidence": round(conf, 4)
        })

    df_vis = pd.DataFrame(visual_emotions)
    df_vis.to_csv(os.path.join(video_dir, "visual_emotion.csv"), index=False, encoding="utf-8-sig")
    print("✅ 表情結果已儲存")

    # === Step 3: 合併語音時間格子 ===
    timegrid_path = os.path.join(project_root, f"{base}_roberta3_fine_timegrid.csv")
    if os.path.exists(timegrid_path):
        df_timegrid = pd.read_csv(timegrid_path, encoding="utf-8-sig")
        merged = pd.merge(df_timegrid, df_vis, on="second", how="left").fillna("none")
        merged.to_csv(os.path.join(video_dir, "merged_timegrid.csv"), index=False, encoding="utf-8-sig")
        print("✅ 多模態時間格子表完成")
    else:
        print("⚠️ 無對應語音 timegrid，請確認檔案存在")

print("\n🌈 所有影片處理完成！")
