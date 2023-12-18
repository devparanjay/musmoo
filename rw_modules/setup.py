from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Module for RaagWiz.'
LONG_DESCRIPTION = 'Module for development and functioning of RaagWiz.'

# Setting up
setup(
        name="moolib", 
        version=VERSION,
        author="Paranjay",
        author_email="45117614+devparanjay@users.noreply.github.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['tokenizers>=0.15.0,<0.16.0', 'onnxruntime-gpu>=1.16.3,<1.17.0', 'numpy>=1.26.2,<1.27.0'], 
        
        keywords=['Emotion Detection', 'RaagWiz', 'Text Classification', 'LLM'],
        classifiers= [
            "Development Status :: 1 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)