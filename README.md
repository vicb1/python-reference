# python-reference


#### package backup with conda
`source activate condaEnv`<br>
`conda env export > environment.yml` OR `!conda env export --name condaEnv`<br>
`conda env create --file environment.yml --name environment1`

#### Create new env and install libraries for jupyter-lab.  Make sure to restart jupyter-lab after these changes:
`conda create -n kaggle13 python=3.7.6` (for Kaggle) OR `3.8.5` for latest <br>
`source activate kaggle13`<br>
`conda install ipykernel`<br>
`ipython kernel install --user --name=kaggle13`<br>

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
pip uninstall gast scipy tensorboard tensorflow-estimator
pip install tensorflow-gpu==2.3.1
```
*shut down all other instances of this kernel, or else tensorflow will error *

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

#### list conda envs
`(conda env list | grep '^\w' | cut -d' ' -f1)`

#### package backup with pip
`env1/pip freeze > requirements.txt`<br>
`env1/pip install -r requirements.txt`

#### To be able to see kernel in jupyter-notebook.  Make sure to restart jupyter-notebook after these changes:
`source activate env1`<br>
`pip install --user ipykernel`<br>
`python -m ipykernel install --user --name=env1`

#### Debug in JupyterLab
https://jupyterlab.readthedocs.io/en/stable/user/debugger.html

#### JupyterLab restart kernel and run all shortcut
```
{"shortcuts": [
    {
        "command": "runmenu:restart-and-run-all",
        "keys": ["Ctrl Shift Enter"],
        "selector": "[data-jp-code-runner]"
    }
              ]
}
```

#### find location of conda environment
`where python` or `which python`

#### Default Anaconda channels
`defaults`<br>
`conda-forge`<br>
`https://pypi.python.org/`<br>
`https://repo.continuum.io/`<br>
`https://pypi.python.org/simple`<br>
`https://pypi.python.org/pypi`<br>

#### check current python environment information
`import platform`<br>
`print('architecture:', platform.architecture())`<br>
`print('python_version:', platform.python_version())`<br>
` `<br>
`import wheel.pep425tags`<br>
`import pprint`<br>
`print('-wheel.pep425tags.get_supported:')`<br>
`pprint.pprint(wheel.pep425tags.get_supported())`<br>

#### install package with setup.py
`pip install .`

#### install .whl package
`pip install test.whl`

#### install package from Git repository
`pip install -e git+https://github.com/hiive/hiivemdptoolbox#egg=hiive.mdptoolbox`

#### Tensorboard startup
`tensorboard --logdir logs`

#### Postgres terminate connections
`select pg_terminate_backend(pid) from pg_stat_activity where datname='db';`

#### python graph speedup
https://git.skewed.de/count0/graph-tool

#### limit memory usage tensorflow
https://github.com/tensorflow/tensorflow/issues/25138

#### install anaconda navigator
https://docs.anaconda.com/anaconda/install/linux/
