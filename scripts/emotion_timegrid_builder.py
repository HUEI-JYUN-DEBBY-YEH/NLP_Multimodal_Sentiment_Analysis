import os
import pandas as pd
import math

# ✅ 設定資料夾路徑
folder = "D:\\NLP_Multimodal_Sentiment_Analysis"
csv_files = [f for f in os.listdir(folder) if f.endswith("_roberta3_fine.csv")]

for file in csv_files:
    df = pd.read_csv(os.path.join(folder, file), encoding="utf-8-sig")

    # 建立時間格子（每秒）
    timegrid = []
    for _, row in df.iterrows():
        start = int(math.floor(row["start"]))
        end = int(math.ceil(row["end"]))
        for sec in range(start, end + 1):
            timegrid.append({
                "second": sec,
                "text_emotion": row["label_text"],      # 正面 / 中性 / 負面
                "basic_emotion": row["basic_emotion"]   # joy / anger / none / ...
            })

    # 建成 DataFrame
    tg_df = pd.DataFrame(timegrid).drop_duplicates(subset=["second"]).sort_values("second")

    # 補齊每秒（若中間有缺）
    full_range = pd.DataFrame({"second": range(tg_df["second"].min(), tg_df["second"].max() + 1)})
    merged = pd.merge(full_range, tg_df, on="second", how="left").fillna("none")

    # 輸出結果
    out_path = os.path.join(folder, file.replace(".csv", "_timegrid.csv"))
    merged.to_csv(out_path, index=False, encoding="utf-8-sig")
    print(f"✅ 已儲存時間格子表：{out_path}")
