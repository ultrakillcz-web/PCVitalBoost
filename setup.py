from setuptools import setup, find_packages

setup(
    name='PCVitalBoost',
    version='1.0.0',
    description='Aplicativo multiplataforma para atualização de drivers/programas, otimização de desempenho e limpeza do computador',
    author='PCVitalBoost Team',
    packages=find_packages(),
    install_requires=[
        'kivy>=2.3.0',
        'kivymd>=1.2.0',
        'plyer>=2.1.0',
        'psutil>=5.9.0',
        'requests>=2.31.0',
    ],
    entry_points={
        'console_scripts': [
            'pcvitalboost=src.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.8',
)
