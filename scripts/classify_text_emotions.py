import os
import glob
import json
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# ✅ 使用中文三分類模型
model_name = "IDEA-CCNL/Erlangshen-Roberta-110M-Sentiment"
classifier = pipeline("text-classification", model=model_name, tokenizer=model_name)

# ✅ 標籤轉換：數字 → 中文情緒
label_map = {
    '0': '負面',
    '1': '中性',
    '2': '正面'
}

# ✅ 指定 transcript 檔案資料夾
transcript_folder = "D:\\NLP_Multimodal_Sentiment_Analysis"
json_files = glob.glob(os.path.join(transcript_folder, "transcript_cut_*.json"))

# ✅ 處理每支影片
for json_path in json_files:
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    rows = []
    for seg in data["segments"]:
        text = seg["text"].strip()
        start = seg["start"]
        end = seg["end"]

        if text:
            result = classifier(text, truncation=True)[0]
            raw_label = result["label"].replace("LABEL_", "")  # e.g. "LABEL_2" → "2"
            label_text = label_map.get(raw_label, "未知")
            score = round(result["score"], 4)

            rows.append({
                "text": text,
                "start": start,
                "end": end,
                "label": raw_label,
                "label_text": label_text,
                "confidence": score
            })

    # ✅ 輸出 CSV
    base = os.path.basename(json_path).replace("transcript_", "").replace(".json", "")
    out_csv = os.path.join(transcript_folder, f"emotion_{base}_roberta3.csv")
    df = pd.DataFrame(rows)
    df.to_csv(out_csv, index=False, encoding="utf-8-sig")
    print(f"✅ 已儲存：{out_csv}")
