import subprocess
import os

# 文件目录需进入到seperate所在位置
os.chdir(r'.\seperate')

command = [
    "spleeter",
    "separate",
    "-p",
    "spleeter:2stems",
    "-o",
    "output",           #输出文件夹名称
    "../test.wav"     #转换音频名称
]

subprocess.run(command)