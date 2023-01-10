本项目使用yolov5在jetson nano上进行行人检测

=========================

文件内容说明：
压缩文件project.rar文件解压后包括
	1、文件夹whl
	2、文件夹yolov5-deepsort-pedestrian-counting-master
	3、程序运行说明书.txt
注：whl文件夹中包含torch和torchvision的.whl文件，yolov5-deepsort-pedestrian-counting-master文件夹中包含项目源码，

环境配置：
1、安装一系列依赖包：（参考：https://blog.csdn.net/IamYZD/article/details/119618950）

sudo apt-get install build-essential make cmake cmake-curses-gui -y
sudo apt-get install git g++ pkg-config curl -y
sudo apt-get install libatlas-base-dev gfortran libcanberra-gtk-module libcanberra-gtk3-module -y
sudo apt-get install libhdf5-serial-dev hdf5-tools -y
sudo apt-get install nano locate screen -y
sudo apt-get install libfreetype6-dev -y
sudo apt-get install protobuf-compiler libprotobuf-dev openssl -y
sudo apt-get install libssl-dev libcurl4-openssl-dev -y
sudo apt-get install cython3 -y
sudo apt-get install build-essential -y
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev -y
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff5-dev libdc1394-22-dev -y
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev liblapacke-dev -y
sudo apt-get install libxvidcore-dev libx264-dev -y
sudo apt-get install libatlas-base-dev gfortran -y
sudo apt-get install ffmpeg -y

2、更新CMake

wget http://www.cmake.org/files/v3.13/cmake-3.13.0.tar.gz     #下载压缩文件
tar xpvf cmake-3.13.0.tar.gz cmake-3.13.0/         #解压
cd cmake-3.13.0/
./bootstrap --system-curl	
make -j4         #编译  
echo 'export PATH=~/cmake-3.13.0/bin/:$PATH' >> ~/.bashrc       #添加到环境变量
source ~/.bashrc       #更新.bashrc

3、安装torch和torchvision   (参考：https://qengineering.eu/install-pytorch-on-jetson-nano.html)

安装前需要先确定python3版本
python3 -V  #查看python3版本
python3需要使用python3.6版本才可以
pip3 -V #查看pip3对应的python版本
pip3也需要对应python3.6版本才可以
如果不是python3.6 需要进行更换。

安装torch1.7
# 安装相关依赖
sudo apt-get install python3-pip libjpeg-dev libopenblas-dev libopenmpi-dev libomp-dev
sudo -H pip3 install future
sudo pip3 install -U --user wheel mock pillow
sudo -H pip3 install testresources
#高于 58.3.0 会出现版本问题
sudo -H pip3 install setuptools==58.3.0
sudo -H pip3 install Cython
# install gdown to download from Google drive
sudo -H pip3 install gdown
# 下载.whl文件，在whl文件下已经下载好了
gdown https://drive.google.com/uc?id=1aWuKu8eqkZwVzFFvguVuwkj0zdCir9qX
# 安装PyTorch 1.7.0
sudo -H pip3 install torch-1.7.0a0-cp36-cp36m-linux_aarch64.whl
# 清空.whl文件
rm torch-1.7.0a0-cp36-cp36m-linux_aarch64.whl

安装torch0.8.0
# 安装一些依赖
sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
sudo pip3 install -U Pillow==8.3.1
# 安装gdown，从drive.google上下载.whl文件，因为是外网，不开VPN会下载失败，所以在whl文件夹中有已经下载好了的文件。
sudo -H pip3 install gdown
# download TorchVision 0.8.0
gdown https://drive.google.com/uc?id=1P0xyPT-WIWglqmT195OSyazV_1LPaHDa
#安装TorchVision 0.8.0
sudo -H pip3 install torchvision-0.8.0a0+291f7e2-cp36-cp36m-linux_aarch64.whl
#清空.whl文件
rm torchvision-0.8.0a0+291f7e2-cp36-cp36m-linux_aarch64.whl

安装完成后进行检测
python3   #进入python3.6
import torch          #导入torch
import torchvision          #导入torchvision
print(torch.__version__)          #查看torch版本
print(torch.cuda.is_available())          #查看cuda能否正常运行，如果可以返回True
quit()          #退出

4、运行程序
cd进入yolov5-deepsort-pedestrian-counting-master文件夹下，运行以下命令
sudo pip3 install -r requirements.txt         #安装项目所需的包
python3 frame.py     #运行程序

如果成功运行会出现可互动的界面。

