from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'MusMoo - songs for your current musical mood.'
LONG_DESCRIPTION = 'A semi-magical app that tells you the best songs to listen to based upon your current emotions and mood.'

# Setting up
setup(
        name="musmoo", 
        version=VERSION,
        author="Paranjay",
        author_email="45117614+devparanjay@users.noreply.github.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['tokenizers>=0.15.0,<0.16.0', 'onnxruntime>=1.16.3,<1.17.0', 'numpy>=1.26.2,<1.27.0', 'ytmusicapi>=1.3.2,<1.4.0', 'transformers>=4.36.1,<4.37.0'], 
        
        keywords=['Emotion Detection', 'MusMoo', 'Text Classification', 'LLM', 'Music', 'Recommendation', 'Mood Detection'],
        classifiers= [
            "Development Status :: 1 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)