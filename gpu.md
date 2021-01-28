install anaconda:
```
sudo bash ./Anaconda3-2020.11-Linux-x86_64.sh
echo 'export PATH=~/anaconda3/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
sudo chown -R $USER:$USER ~/anaconda3
```

#### v3 install cuda 10.1, cudnn 7.6.5.32, and tensorflow 2.3, Ubuntu 18.04
(kaggle env: https://github.com/Kaggle/docker-python)

(tensorflow compatabilities: https://www.tensorflow.org/install/source#gpu)

(driver vs cuda versions: https://docs.nvidia.com/deploy/cuda-compatibility/index.html)

- download desired compatible driver: https://www.nvidia.com/en-us/drivers/unix/linux-amd64-display-archive/
- in our case: https://www.nvidia.com/Download/driverResults.aspx/153717/en-us
- install manually (ref: https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-ubuntu-18-04-bionic-beaver-linux)
```
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install build-essential libc6:i386 sudo bash -c "echo blacklist nouveau > /etc/modprobe.d/blacklist-nvidia-nouveau.conf"
sudo bash -c "echo options nouveau modeset=0 >> /etc/modprobe.d/blacklist-nvidia-nouveau.conf"libglvnd-dev pkg-config
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

- check install directory, for example `/usr/local/cuda-10.1`, then run:
```
echo 'export PATH=/usr/local/cuda-10.1/bin${PATH:+:${PATH}}' >> ~/.bashrc
source ~/.bashrc 
```
- ensure working with `nvcc --version` and `whereis cuda`

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
- https://askubuntu.com/questions/1230645/when-is-cuda-gonna-be-released-for-ubuntu-20-04
- https://stackoverflow.com/questions/55224016/importerror-libcublas-so-10-0-cannot-open-shared-object-file-no-such-file-or

```
conda create -n kaggle1 python=3.7.6
source activate kaggle1
pip install tensorflow-gpu==2.3.1
echo $CONDA_PREFIX # to see env location
```

to appease warnings from running `pip install tensorflow-gpu`: 
```
echo 'export PATH=~/.local/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

- shut down all other instances of this kernel, or else tensorflow will error
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

#### v2 install cuda 10.2.89, cudnn 7.6.5.32, and tensorflow 2.4, Ubuntu 18.04 to match kaggle
(kaggle env: https://github.com/Kaggle/docker-python)

(tensorflow compatabilities: https://www.tensorflow.org/install/source#gpu)

- download desired compatible driver: https://www.nvidia.com/en-us/drivers/unix/linux-amd64-display-archive/
- install manually: https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-ubuntu-18-04-bionic-beaver-linux
- ensure working with `nvidia-smi`
- check for same version: https://developer.nvidia.com/cuda-toolkit-archive and run:
```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin
sudo mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/10.2/Prod/local_installers/cuda-repo-ubuntu1804-10-2-local-10.2.89-440.33.01_1.0-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1804-10-2-local-10.2.89-440.33.01_1.0-1_amd64.deb
sudo apt-key add /var/cuda-repo-10-2-local-10.2.89-440.33.01/7fa2af80.pub
sudo apt-get update
sudo apt-get -y install cuda
```
- check install directory, for example `/usr/local/cuda-10.2`, then run:
```
echo 'export PATH=/usr/local/cuda-10.2/bin${PATH:+:${PATH}}' >> ~/.bashrc
source ~/.bashrc 
```
- ensure working with `nvcc --version` and `whereis cuda`

Using cudnn download https://developer.nvidia.com/rdp/cudnn-download specifically:
https://developer.nvidia.com/compute/machine-learning/cudnn/secure/7.6.5.32/Production/10.2_20191118/cudnn-10.2-linux-x64-v7.6.5.32.tgz


```
sudo cp cuda/include/cudnn.h /usr/local/cuda-10.2/include/
sudo cp cuda/lib64/libcudnn* /usr/local/cuda-10.2/lib64/
sudo chmod a+r /usr/local/cuda-10.2/include/cudnn.h /usr/local/cuda-10.2/lib64/libcudnn*
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-10.2/include:$LD_LIBRARY_PATH' >> ~/.bashrc  
source ~/.bashrc 
```

Alternate installs: 
- https://askubuntu.com/questions/1230645/when-is-cuda-gonna-be-released-for-ubuntu-20-04
- https://stackoverflow.com/questions/55224016/importerror-libcublas-so-10-0-cannot-open-shared-object-file-no-such-file-or

```
conda create -n kaggle1 python=3.7.6
source activate kaggle1
pip install tensorflow-gpu==2.3.1
echo $CONDA_PREFIX # to see env location
```

to appease warnings from running `pip install tensorflow-gpu`: 
```
echo 'export PATH=~/.local/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

- shut down all other instances of this kernel, or else tensorflow will error
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

#### install cuda 10.2.89, cudnn 7.6.5.32, and tensorflow 2.4, Ubuntu 18.04 to match kaggle
(kaggle env: https://github.com/Kaggle/docker-python)

(tensorflow compatabilities: https://www.tensorflow.org/install/source#gpu)

per: https://forums.developer.nvidia.com/t/installing-cuda-10-2-on-ubuntu-18-04-3/107773
and: https://askubuntu.com/questions/1260039/how-to-install-specific-nvidia-driver-like-nvidia-driver-440-440-33-01-deb
```
sudo apt-get purge *nvidia*
sudo apt autoremove
sudo rm -rf /usr/lib/cuda  # to remove previous cudnn files
sudo add-apt-repository ppa:graphics-drivers/ppa -y 
sudo apt update -y 
sudo apt-get update
sudo apt install nvidia-driver-440 -y 
*change to appropriate driver in program Software & updates*
*restart*
nvidia-smi
```
if this doesn't provide the driver you want, do this instead:
- download desired compatible driver: https://www.nvidia.com/en-us/drivers/unix/linux-amd64-display-archive/
- install manually: https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-ubuntu-18-04-bionic-beaver-linux

```
sudo apt install nvidia-cuda-toolkit
*restart*
nvidia-smi
nano ~/.bashrc
echo 'export CUDA_PATH=/usr' >> ~/.bashrc
nano ~/.bashrc
source ~/.bashrc
```

running `dmesg` gets error ` NVRM: API mismatch: the client has the version 450.102.04, but
               NVRM: this kernel module has the version 440.82.  Please
               NVRM: make sure that this kernel module and all NVIDIA driver
               NVRM: components have the same version.
`

so check for same version:
https://developer.nvidia.com/cuda-toolkit-archive

and run:
```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-ubuntu1804.pin
sudo mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/10.2/Prod/local_installers/cuda-repo-ubuntu1804-10-2-local-10.2.89-440.33.01_1.0-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1804-10-2-local-10.2.89-440.33.01_1.0-1_amd64.deb
sudo apt-key add /var/cuda-repo-10-2-local-10.2.89-440.33.01/7fa2af80.pub
sudo apt-get update
sudo apt-get -y install cuda
```

if `nvidia-smi` still not working, redo: https://linuxconfig.org/how-to-install-the-nvidia-drivers-on-ubuntu-18-04-bionic-beaver-linux

Using cudnn:
https://developer.nvidia.com/compute/machine-learning/cudnn/secure/7.6.5.32/Production/10.2_20191118/cudnn-10.2-linux-x64-v7.6.5.32.tgz

Install cudnn per:
https://askubuntu.com/questions/1230645/when-is-cuda-gonna-be-released-for-ubuntu-20-04

If this doesn't work, look for cuda folder such as: `/usr/local/cuda-10.2`
```
sudo cp cuda/include/cudnn.h /usr/local/cuda-10.2/include/
sudo cp cuda/lib64/libcudnn* /usr/local/cuda-10.2/lib64/
sudo chmod a+r /usr/local/cuda-10.2/include/cudnn.h /usr/local/cuda-10.2/lib64/libcudnn*
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-10.2/include:$LD_LIBRARY_PATH' >> ~/.bashrc  
source ~/.bashrc 
```



```
conda create -n kaggle1 python=3.7.6
source activate kaggle1
conda install ipykernel
ipython kernel install --user --name=kaggle1
pip install pandas
pip install keras-tuner 
pip install tensorflow-gpu
*shut down all other instances of this kernel, or else tensorflow will error *
```

### install cuda 11, cudnn 8, tensorflow 2.4
https://www.tensorflow.org/install/source#gpu
need cuda 11, cudnn 8, tensorflow 2.4

per https://askubuntu.com/questions/1288672/how-do-you-install-cuda-11-on-ubuntu-20-10-and-verify-the-installation
```
sudo apt-get purge *nvidia*
sudo apt autoremove
sudo apt-get update
sudo apt install nvidia-driver-455
*restart*
nvidia-smi
sudo apt install nvidia-cuda-toolkit
nano ~/.bashrc
echo 'export CUDA_PATH=/usr' >> ~/.bashrc
nano ~/.bashrc
source ~/.bashrc
```

10.1 version when running `nvcc --version`, but this is ok because:
https://stackoverflow.com/questions/53422407/different-cuda-versions-shown-by-nvcc-and-nvidia-smi

Using cudnn 8:
https://developer.nvidia.com/compute/machine-learning/cudnn/secure/8.0.5/11.1_20201106/cudnn-11.1-linux-x64-v8.0.5.39.tgz

Install cudnn per:
https://askubuntu.com/questions/1230645/when-is-cuda-gonna-be-released-for-ubuntu-20-04

https://stackoverflow.com/questions/65273118/why-is-tensorflow-not-recognizing-my-gpu-after-conda-install

```
conda create -n kaggle_gpu4 python=3.7.6 
source activate kaggle_gpu4
conda install ipykernel
ipython kernel install --user --name=kaggle_gpu4
conda install tensorflow-gpu=2.1
pip install pandas
pip install keras-tuner 
pip uninstall tensorflow
pip install tensorflow-gpu==2.4.0
```
try 2:
```
conda create -n kaggle_gpu6 python=3.7.6 
source activate kaggle_gpu6
conda install ipykernel
ipython kernel install --user --name=kaggle_gpu6
pip install pandas
pip install keras-tuner 
pip install tensorflow-gpu
```
*shut down all other instances of this kernel, or else tensorflow will error *

- error maybe gcc or bazel need updating?
Process finished with exit code 132 (interrupted by signal 4: SIGILL)

pip install --user --force-reinstall --ignore-installed --no-binary :all: tensorflow-gpu


#### install tensorflow with gpu (old version)
https://askubuntu.com/questions/1230645/when-is-cuda-gonna-be-released-for-ubuntu-20-04 <br>
`sudo apt install python3-testresources`<br>
`conda install tensorflow-gpu` (for 2.4, Kaggle) OR `sudo pip3 install tensorflow-gpu==2.2.0 --user --ignore-installed` <br> 
`pip install keras-tuner`<br>
`pip install pandas`<br>
- shut down all other instances of this kernel, or else tensorflow will error 
- kaggle install: <br>
https://github.com/Kaggle/docker-python/blob/master/Dockerfile <br>
https://github.com/Kaggle/docker-python/blob/master/gpu.Dockerfile <br>
