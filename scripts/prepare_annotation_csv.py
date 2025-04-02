import os
import pandas as pd

# 設定輸入資料夾（放置每部影片的 visual_emotion_output）
root = "D:\\NLP_Multimodal_Sentiment_Analysis\\visual_emotion_output"
output_rows = []

# 每部影片挑選幾句
N = 10

for folder in os.listdir(root):
    subdir = os.path.join(root, folder)
    merged_path = os.path.join(subdir, "merged_timegrid.csv")
    
    if not os.path.exists(merged_path):
        print(f"⚠️ 跳過：{folder} 無 merged_timegrid.csv")
        continue

    df = pd.read_csv(merged_path, encoding="utf-8-sig")
    
    # 只保留有情緒變化的句子區間
    df_grouped = df.groupby("second").first().reset_index()

    # 優先挑選機器信心低、語音視覺不一致者
    df_grouped["emotion_match"] = df_grouped["basic_emotion"] == df_grouped["visual_emotion"]
    df_sorted = df_grouped.sort_values(by=["emotion_match", "vis_confidence"], ascending=[True, True])

    selected = df_sorted.head(N)
    selected["video"] = folder
    output_rows.append(selected)

# 整合所有影片結果
df_all = pd.concat(output_rows, ignore_index=True)

# 加入人工標註欄位
df_all["true_text_emotion"] = ""
df_all["true_basic_emotion"] = ""
df_all["remark"] = ""

# 欄位排序
cols = ["video", "second", "text_emotion", "basic_emotion", "visual_emotion", 
        "confidence", "vis_confidence", "true_text_emotion", "true_basic_emotion", "remark"]

df_all = df_all[[c for c in cols if c in df_all.columns]]

# 輸出檔案
out_path = os.path.join(root, "annotation_template.csv")
df_all.to_csv(out_path, index=False, encoding="utf-8-sig")
print(f"✅ 標註模板已產出：{out_path}")
