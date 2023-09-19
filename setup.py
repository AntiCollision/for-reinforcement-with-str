import setuptools

setuptools.setup(
    name="for_str_simulator",
    version="0.0.2",
    author="Joo Hyoung Cha",
    author_email="chacha@udon.party",
    url="https://github.com/AntiCollision/for-reinforcement-with-str",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        'pynmea2',
        'requests'
    ]
)
