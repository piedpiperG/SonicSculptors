import argparse
import subprocess
import os

# 首先，使用 argparse 解析命令行参数
parser = argparse.ArgumentParser(description='Separate audio tracks using Spleeter.')
parser.add_argument('audio_file', help='The path to the audio file to be processed.')
args = parser.parse_args()

# 文件目录需进入到seperate所在位置
os.chdir(r'.\seperate')

# 然后，使用 argparse 解析得到的文件名
command = [
    "spleeter",
    "separate",
    "-p",
    "spleeter:2stems",
    "-o",
    "output",  # 输出文件夹名称
    args.audio_file  # 使用通过命令行参数传入的音频文件名称
]

subprocess.run(command)
