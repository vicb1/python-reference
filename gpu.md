install anaconda:
```
sudo bash ./Anaconda3-2020.11-Linux-x86_64.sh
echo 'export PATH=~/anaconda3/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
sudo chown -R $USER:$USER ~/anaconda3
```

run pycharm:

`/snap/pycharm-community/current/bin/pycharm.sh`

#### v4 install cuda 10.1, cudnn 7.6.5.32, and tensorflow 2.3, Ubuntu 18.04
(kaggle env: https://github.com/Kaggle/docker-python)

(tensorflow compatabilities: https://www.tensorflow.org/install/source#gpu)

(driver vs cuda versions: https://docs.nvidia.com/deploy/cuda-compatibility/index.html)

- per https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#pre-installation-actions
```
lspci | grep -i nvidia
uname -m && cat /etc/*release
$ gcc --version
uname -r
sudo apt-get install linux-headers-$(uname -r)
```

- download desired compatible driver: https://www.nvidia.com/en-us/drivers/unix/linux-amd64-display-archive/
- in our case: https://www.nvidia.com/Download/driverResults.aspx/153717/en-us
- install manually (ref: https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-ubuntu-18-04-bionic-beaver-linux)
```
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install build-essential libc6:i386 
sudo bash -c "echo blacklist nouveau > /etc/modprobe.d/blacklist-nvidia-nouveau.conf"
sudo bash -c "echo options nouveau modeset=0 >> /etc/modprobe.d/blacklist-nvidia-nouveau.conf"
sudo update-initramfs -u
reboot
sudo telinit 3
sudo bash NVIDIA-Linux-x86_64-410.73.bin
reboot
```
- ensure working with `nvidia-smi`
- check ubuntu architecture: `uname -m`
- install compatible cuda version: https://developer.nvidia.com/cuda-toolkit-archive and run:
```
wget https://developer.download.nvidia.com/compute/cuda/10.1/Prod/local_installers/cuda_10.1.243_418.87.00_linux.run
sudo sh cuda_10.1.243_418.87.00_linux.run
```
*unchecked install driver... is that ok?  Or can we also skip the previous driver install step if we do this?*

- per https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#post-installation-actions
- check install directory, for example `/usr/local/cuda-10.1`, then run:
```
echo 'export PATH=/usr/local/cuda-10.1/bin${PATH:+:${PATH}}' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-11.2/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}' >> ~/.bashrc
source ~/.bashrc 
```
- ensure working with `nvcc --version` and `whereis cuda`
- check for driver errors by looking at `nvidia-installer.log` and cuda errors by looking at `nvidia-installer.log`
- to uninstall, run `/usr/local/cuda-10.1/bin/cuda-uninstaller`
- per https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#recommended-post
```
/usr/bin/nvidia-persistenced --verbose
cat /proc/driver/nvidia/version
```


Using cudnn download https://developer.nvidia.com/rdp/cudnn-download specifically:
https://developer.nvidia.com/compute/machine-learning/cudnn/secure/7.6.5.32/Production/10.1_20191031/cudnn-10.1-linux-x64-v7.6.5.32.tgz

```
sudo cp cuda/include/cudnn.h /usr/local/cuda-10.1/include/
sudo cp cuda/lib64/libcudnn* /usr/local/cuda-10.1/lib64/
sudo chmod a+r /usr/local/cuda-10.2/include/cudnn.h /usr/local/cuda-10.1/lib64/libcudnn*
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-10.1/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-10.1/include:$LD_LIBRARY_PATH' >> ~/.bashrc  
source ~/.bashrc 
```

Alternate installs: 
- https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html
- https://askubuntu.com/questions/1230645/when-is-cuda-gonna-be-released-for-ubuntu-20-04
- https://stackoverflow.com/questions/55224016/importerror-libcublas-so-10-0-cannot-open-shared-object-file-no-such-file-or

```
conda create -n kaggle1 python=3.7.6
source activate kaggle1
pip install tensorflow-gpu==2.3.0
echo $CONDA_PREFIX # to see env location
```

to appease warnings from running `pip install tensorflow-gpu`: 
```
echo 'export PATH=~/.local/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

- shut down all other instances of this kernel, or else tensorflow will error
- per https://stackoverflow.com/questions/43691706/pycharm-tensorflow-importerror-but-works-fine-with-terminal and https://stackoverflow.com/questions/27063361/how-to-run-pycharm-in-ubuntu-run-in-terminal-or-run

`/snap/pycharm-community/current/bin/pycharm.sh`

- run the following, ensure GPU listed:

```
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
```

for specific install:
```
conda create -n kaggle1 python=3.7.6
source activate kaggle1
conda install ipykernel
ipython kernel install --user --name=kaggle1
pip install pandas
pip install keras-tuner 
pip install tensorflow-gpu
```


