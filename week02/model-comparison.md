#week02  模型复现
##1.模型选择
    本次选择了2个模型
    模型1：google/flan-t5-small
    模型2：openai/clip-vit-base-patch32

##2.模型对比    
    模型全名 |   google/flan-t5-small     | openai/clip-vit-base-patch32
    任务类型 |       文本生成              |     零样本图像分类
    参数量   |        77M                 |         150M
    开源许可 |      Apache 2.0            |          MIT
    输入     |      英文输入               |        图片及文本
    输出     |      生成的文本             |       图文相似度分数
    适用场景 |    问答、翻译、指令任务等     |    以图搜图、图文检索等
    硬件要求 | 可在CPU上完成推理，GPU可加速 | 支持CPU推理，但计算开销大；推荐GPU（显存≥4GB）

##实验说明：本实验仅复现了flan-t5-small的推理流程，对于clip仅做理论对比，未进行本地运行。