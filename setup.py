from setuptools import setup, find_packages

setup(
    name='VALL-E X',
    version='0.0.1',
    packages=find_packages(),
    description='Multilingual Text-to-Speech Synthesis and Voice Cloning',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/rsxdalv/VALL-E-X.git',
    install_requires=[
        'soundfile',
        'numpy',
        'torch',
        'torchvision',
        'torchaudio',
        'tokenizers',
        'encodec',
        'langid',
        'wget',
        'unidecode',
        'pyopenjtalk-prebuilt',
        'pypinyin',
        'inflect',
        'cn2an',
        'jieba',
        'eng_to_ipa',
        'openai-whisper',
        'matplotlib',
        # 'gradio==3.41.2',
        'nltk',
        'sudachipy',
        'sudachidict_core',
        'vocos',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
)