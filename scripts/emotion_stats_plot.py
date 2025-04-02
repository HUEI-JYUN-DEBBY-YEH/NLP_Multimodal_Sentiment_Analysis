import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# ✅ 設定資料夾路徑
folder = "D:\\NLP_Multimodal_Sentiment_Analysis"

# ✅ 篩選檔案（可讀 .csv 結尾檔）
csv_files = [f for f in os.listdir(folder) if f.startswith("emotion_cut_") and f.endswith("_roberta3_fine.csv")]

for file in csv_files:
    path = os.path.join(folder, file)
    df = pd.read_csv(path, encoding="utf-8-sig")

    # 統計 basic_emotion 欄位
    emotion_counts = Counter(df["basic_emotion"].dropna())
    total = sum(emotion_counts.values())
    emotion_percents = {k: round(v / total * 100, 2) for k, v in emotion_counts.items()}

    print(f"\n📊 {file} 基本情緒分布：")
    for emo in sorted(emotion_counts, key=emotion_counts.get, reverse=True):
        print(f"{emo:<10}：{emotion_counts[emo]} 次（{emotion_percents[emo]}%）")

    import matplotlib
    matplotlib.rcParams['font.family'] = 'Microsoft JhengHei'
    matplotlib.rcParams['axes.unicode_minus'] = False
    # 繪圖
    plt.figure(figsize=(8, 5))
    plt.bar(emotion_counts.keys(), emotion_counts.values(), alpha=0.8)
    plt.title(f"{file} - 基本情緒分布", fontsize=14)
    plt.ylabel("出現次數")
    plt.xlabel("情緒類型")
    plt.tight_layout()

    # 輸出圖檔
    out_name = file.replace(".csv", "_emotion_bar.png")
    out_path = os.path.join(folder, out_name)
    plt.savefig(out_path, dpi=300)
    print(f"✅ 圖檔已儲存：{out_path}")
    plt.close()
