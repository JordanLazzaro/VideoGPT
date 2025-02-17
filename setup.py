from setuptools import setup, find_packages

setup(
    name="videogamegen",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'einops==0.8.0',
        'imageio==2.34.2',
        'ipython==8.12.3',
        'matplotlib==3.5.1',
        'numpy==1.25.2',
        'pytorch_lightning==2.3.3',
        'PyYAML==6.0.1',
        'torch==2.4.1',
        'torchvision==0.19.1',
        'tqdm==4.66.1',
        'wandb==0.17.5',
        'av==12.3.0',
        'PyAV==12.3.0',
    ],
)