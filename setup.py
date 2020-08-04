import setuptools
 
with open("README.md", "r", encoding='utf8') as readme:
    long_description = readme.read()
 
setuptools.setup(
    name="poppy",
    version="1.1",
    author="Team Poppy",
    description="Mobile medication reminder app that reads your medication label and automatically creates reminders based on the instructions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lucasbsanders/poppy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows 10"
    ],
    install_requires=[
        'certifi==2020.6.20',
        'chardet==3.0.4',
        'docutils==0.16',
        'idna==2.10',
        'Kivy==1.11.1',
        'kivy-deps.glew==0.1.12',
        'kivy-deps.gstreamer==0.1.18',
        'kivy-deps.sdl2==0.1.23',
        'Kivy-Garden==0.1.4',
        'kivy-garden.xcamera==2020.613',
        'numpy==1.19.1',
        'opencv-python==4.3.0.36',
        'Pygments==2.6.1',
        'pypiwin32==223',
        'pywin32==228',
        'requests==2.24.0',
        'urllib3==1.25.10',
        'xcamera==2020.613'
    ],
)
