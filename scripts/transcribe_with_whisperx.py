import os
import glob
import torch
import whisperx
import json

# ✅ 將 Hugging Face 模型快取位置改到專案資料夾
os.environ["HF_HOME"] = "D:\\NLP_Multimodal_Sentiment_Analysis\\.hf_cache"

# ✅ 設定執行設備（GPU 有則用，否則用 CPU）
device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisperx.load_model("large-v3", device=device, compute_type="float32")

# ✅ 影片資料夾與檔案列表
video_folder = "D:\\NLP_Multimodal_Sentiment_Analysis"
video_files = glob.glob(os.path.join(video_folder, "cut_*.mp4"))

# ✅ 批次處理影片
for video_path in video_files:
    filename = os.path.basename(video_path)
    name = os.path.splitext(filename)[0]

    print(f"🔍 正在處理: {filename}")
    result = model.transcribe(video_path, language="zh")

    # ✅ 儲存 json 結果
    output_path = os.path.join(video_folder, f"transcript_{name}.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"✅ 已儲存：{output_path}")
