from setuptools import setup, find_packages

setup(
    name="sampler",
    version='1.1.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'sampler = sampler.sampler:main',
        ]
    },
)
