#!/bin/bash

# 迴圈遍歷資料夾a, b, c, ...
for folder in */; do
    # 進入每個資料夾
    cd "$folder" || continue
    
    # 將所有jpeg檔案轉換為png
    for file in *.jpeg; do
        if [ -f "$file" ]; then
            convert "$file" "$(basename "$file" .jpeg).png"
        fi
    done
    
    for file in *.jpg; do
        if [ -f "$file" ]; then
            convert "$file" "$(basename "$file" .jpg).png"
        fi
    done
    
    # 刪除所有剩餘的jpeg檔案
    rm -f *.jpeg
    rm -f *.jpg
    
    # 返回上一層資料夾
    cd ..
done

