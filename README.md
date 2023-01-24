# Streamlit-30days-learning
從Streamlit官方提供的[30天挑戰](https://30days.streamlitapp.com/?challenge=Day+1)，跟著自己動手寫一次並作為筆記記錄


## 文章目錄
+ [Day01-環境建立](Day01-環境建立/README.md)
    + 使用Streamlit hello提供的範例，包含動畫、地圖、進度...功能
+ [Day02-建立第一個Streamlit應用](Day02-建立第一個Streamlit應用/README.md)
+ [Day03-學習BUtton](Day03-學習BUtton/README.md)
    + `st.header`建立標題
    + `st.write`印出文字
    + `st.button`按鈕改變印出文字
+ [Day04-實作一個Youtube儀錶板](Day04-實作一個Youtube儀錶板/README.md)
+ [Day05-st.write](Day05-st.write/README.md)
    + `st.write`可以寫入：文字、物件、資料幀、圖片、其他等內容
+ [Day06-上傳到Github](Day06-上傳到Github/README.md)
+ [Day07-使用StreamlitCloud](Day07-使用StreamlitCloud/README.md)
    + 使用Streamlit Cloud部署app
+ [Day08-st.slider](Day08-st.slider/README.md)
    + `st.slider`可以建立滑桿
    + 語法：`st.slider(顯示文字, 最小值, 最大值, 預設值)`
+ [Day09-st.line_chart](Day09-st.line_chart/README.md)
    + `st.line_chart`可以建立折線圖
        + 是`st.altair_chart`的語法糖，適合單純印出來這張圖的情況
+ [Day10-st.selectbox](Day10-st.selectbox/README.md)
    + `st.selectbox`可以建立下拉式選單
    + 語法：`st.selectbox(顯示文字, 選項tuple)`
+ [Day11-st.multiselect](Day11-st.multiselect/README.md)
    + `st.multiselect`可以建立多選下拉式選單
    + 語法：`st.multiselect(顯示文字, 選項tuple, 預設值tuple)`
+ [Day12-st.checkbox](Day12-st.checkbox/README.md)
    + `st.checkbox`可以建立勾選框
    + 語法：`st.checkbox(顯示文字, 預設值)`
+ [Day13-使用Gitpod開發](Day13-使用Gitpod開發/README.md)
+ [Day14-Streamlit Components](Day14-Streamlit Components/README.md)
+ [Day15-st.latex](Day15-st.latex/README.md)
    + 記得文字前加上`r`以避免轉義
+ [Day16-客製化主題](Day16-客製化主題/README.md)
+ [Day17-st.secrets](Day17-st.secrets/README.md)
+ [Day18-st.file_uploader](Day18-st.file_uploader/README.md)
+ [Day19-調整layout](Day19-調整layout/README.md)
+ [Day20-演講內容](Day20-演講內容/README.md)
+ [Day21-st.progress](Day21-st.progress/README.md)
+ [Day22-st.form](Day22-st.form/README.md)
+ [Day23-st.experimental_get_query_params](Day23-st.experimental_get_query_params/README.md)
+ [Day24-st.cache](Day24-st.cache/README.md)
+ [Day25-st.session_state](Day25-st.session_state/README.md)
+ [Day26-API](Day26-API/README.md)
+ [Day27-使用Streamlit Elements建立可以拖動的儀錶板](Day27-使用Streamlit\ Elements建立可以拖動的儀錶板/README.md)
+ [Day28-streamlit-shap](Day28-streamlit-shap/README.md)
+ [Day29-範例：人臉分類](Day29-範例：人臉分類/README.md)


## Streamlit特性整理
+ 使用`streamlit run`的時候，會自動開啟瀏覽器，並且會自動更新
    + 除了可以run python檔案，也可以run URL
+ 預設的配置檔案在`~/.streamlit/config.toml`
+ Steamlit Cloud的路徑如果有包含空格，會出現錯誤