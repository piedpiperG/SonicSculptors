# SonicSculptors
SonicSculptors

使用方式：
## 1.配置环境，运行命令：
conda env create -f environment.yaml
## 2.下载相关预训练模型：
1.  下载[音色编码器](https://drive.google.com/drive/folders/15oeBYf6Qn1edONkVLXe82MzdIi3O_9m3), 把`best_model.pth.tar`放到`speaker_pretrain/`里面 （**不要解压**）

2.  下载[whisper-large-v2模型](https://openaipublic.azureedge.net/main/whisper/models/81f7c96c852ee8fc832187b0132e569d6c3065a3252ed18e56effd0b6a73e524/large-v2.pt)，把`large-v2.pt`放到`whisper_pretrain/`里面

3.  下载[hubert_soft模型](https://github.com/bshall/hubert/releases/tag/v0.1)，把`hubert-soft-0d54a1f4.pt`放到`hubert_pretrain/`里面

4.  下载音高提取模型[crepe full](https://github.com/maxrmorrison/torchcrepe/tree/master/torchcrepe/assets)，把`full.pth`放到`crepe/assets`里面

    **注意：full.pth为84.9M，请确认文件大小无误**

5.  下载分离程序预处理模型[spleeter]
(https://pan.baidu.com/s/1LNuTvZO6sZcKhbxOb-Ls1w?pwd=3404), 把其中的内容放入seperate文件夹中，并按照其中的readme.txt配置环境变量：
    
    添加环境变量 F:\（你存储的位置）\seperate\ffmpeg-20200831-4a11a6f-win64-static\bin


## 3.运行程序
将想要转换的音频以test.wav命名，放入根目录下。
将音色模型放入根目录下，将说话人模型放入data_svc/speaker
运行Main.py，转换结束后的音频将以combine.wav出现在根目录下


