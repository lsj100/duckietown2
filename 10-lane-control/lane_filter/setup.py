from setuptools import find_packages
from setuptools import setup

package_name='lane_filter'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    #package_dir={'': 'dagu_car/dagu_car_include'},
    #setup_requires=['numpy'],
    data_files=[
        ('include/' + package_name, ['lane_filter/config/default.yaml'])
    ],
    install_requires=['setuptools', 'numpy', 'scipy'],
    author='Brian Shin',
    author_email='brian.shin@lge.com',
    maintainer='Brian Shin',
    maintainer_email='brian.shin@lge.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Port of original duckietown lane filter package to ROS2',
    license='Apache License, Version 2.0',
    test_suite='test',
    entry_points={
        'console_scripts': [
            'lane_filter_node = lane_filter.lane_filter_node:main'
        ],
    },
)
