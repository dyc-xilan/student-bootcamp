# 复现记录 reproduction-notes.md
复现日期：2026‑11‑11
运行平台：Windows
环境工具：conda

## 成功执行命令
1. 创建conda环境
`conda env create -f environment.yml`
2. 激活环境
`conda activate bootcamp-env`
3. 运行单词统计工具
`python src/count_words.py week01/demo.txt`
4. 运行环境自检脚本
`python week01/check_environment.py`

## 失败与解决
本次练习无报错。

## 限制
1. 单词统计仅以空格分割，不处理标点符号
2. 本任务不需要GPU，未安装PyTorch
