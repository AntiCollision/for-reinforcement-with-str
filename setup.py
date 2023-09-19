import setuptools

setuptools.setup(
    name="for_str_simulator",
    version="0.1.0",
    author="Joo Hyoung Cha",
    author_email="chacha@udon.party",
    url="https://github.com/AntiCollision/for-reinforcement-with-str.git",
    packages=['for_str_simulator'],
    python_requires=">=3.6",
    install_requires=[
        'pynmea2',
        'requests'
    ]
)
