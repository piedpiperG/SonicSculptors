import os
import time
import subprocess


def process_audio(filepath, option):
    option = option[2]
    os.environ['CUDA_VISIBLE_DEVICES'] = ''
    start_time = time.time()

    # 保存当前工作目录
    original_directory = os.getcwd()
    print(f"Original working directory: {original_directory}")

    # 改变工作目录到你想要的新目录
    new_working_directory = '../'
    os.chdir(new_working_directory)
    print(f"New working directory: {os.getcwd()}")  # 打印新的工作目录的绝对路径

    option = str(int(option) - 1)

    # 定义你的命令
    cmd1 = 'python seperate.py'
    cmd2 = f'python svc_inference.py --config configs/base.yaml --model sovits5.0.pth --spk ./data_svc/singer/speaker{option}.spk.npy --wave {filepath} --shift 0'
    cmd3 = 'python combination.py'

    print('Begin Execute')
    # 执行第一个命令
    subprocess.run(cmd1, shell=True, env=os.environ)
    print('Seperate Over')

    # 执行第二个命令
    subprocess.run(cmd2, shell=True, env=os.environ)
    print('Infer Over')

    # 执行第三个命令
    subprocess.run(cmd3, shell=True, env=os.environ)
    print('Combine Over')

    end_time = time.time()
    print(f'Process completed in {end_time - start_time:.2f} seconds.')

    re_file_path = './result/combined.wav'
    return re_file_path
