from setuptools import setup, find_packages

setup(
    name='Package 1.0.1', 
    version='1.0.1',
    packages=find_packages(),  
    description='New Version Package.', 
    author='cleasantos1994', 
    author_email='cleasantos1994@gmail.com', 
    url='https://github.com/BaHost01/Simple-Anticheat', 
    install_requires=[
        'psutil',  
        'requests',  
        'ctypes'
        'hasblib'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Requisitos de versão do Python
)
