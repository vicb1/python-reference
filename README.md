# python-reference

#### list conda envs
`(conda env list | grep '^\w' | cut -d' ' -f1)`

#### package backup with conda
`source activate condaEnv`<br>
`conda env export > environment.yml` OR `!conda env export --name condaEnv`<br>
`conda env create --file environment.yml --name environment1`

#### package backup with pip
`env1/pip freeze > requirements.txt`<br>
`env1/pip install -r requirements.txt`

#### Create new env and install libraries for jupyter-lab.  Make sure to restart jupyter-lab after these changes:
`conda create -n kaggle5 python=3.8.5`<br> 
`source activate kaggle5`<br>
`conda install ipykernel`<br>
`ipython kernel install --user --name=kaggle5`<br>

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

#### install tensorflow with gpu
https://askubuntu.com/questions/1230645/when-is-cuda-gonna-be-released-for-ubuntu-20-04

#### limit memory usage tensorflow
https://github.com/tensorflow/tensorflow/issues/25138

#### install anaconda navigator
https://docs.anaconda.com/anaconda/install/linux/
