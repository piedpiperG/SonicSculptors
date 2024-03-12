python 3.9.12可以使用，路径没有中文名（有可能会有bug），分离用时在20~30s
二次省流：python -m spleeter separate -p spleeter:2stems -o output test_sing.wav

1.添加环境变量 F:\（你存储的位置）\seperate\ffmpeg-20200831-4a11a6f-win64-static\bin

2.安装模块：

pip install ffmpeg-python
pip install spleeter
conda install -c conda-forge ffmpeg libsndfile

conda报错这个不用管：
Verifying transaction: failed
RemoveError: 'requests' is a dependency of conda and cannot be removed from
conda's operating environment.

3.输入python -m spleeter 验证安装
输出：
Usage: __main__.py [OPTIONS] COMMAND [ARGS]...
Options:
  --version  Return Spleeter version
  --help     Show this message and exit.
Commands:
  evaluate  Evaluate a model on the musDB test dataset
  separate  Separate audio file(s)
  train     Train a source separation model
即为安装成功

4.进入seperate文件夹内，输入指令：
python -m spleeter separate -p spleeter:2stems -o 输出文件夹路径 待处理音乐.wav
如：python -m spleeter separate -p spleeter:2stems -o output test_sing.wav
首次使用有概率报httpcore.ReadTimeout: The read operation timed out，不用管再编译一次

5.弹出：
INFO:spleeter:File output\test_sing/vocals.wav written succesfully
INFO:spleeter:File output\test_sing/accompaniment.wav written succesfully
即为成功，在seperate\output\test_sing路径里的accompaniment是背景音乐，vocals是清唱









破玩意儿真难弄