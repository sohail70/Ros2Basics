from setuptools import setup
import os
from glob import glob

package_name = 'ae_custom_interface_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share' , package_name) , glob('launch/*.launch.py')),
        # ('/home/course/Ros2Basics/install/ae_custom_interface_cpp/share/ament_index/resource_index/packages',
        #     ['resource/' + 'ae_custom_interface_cpp'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='course',
    maintainer_email='sohail.e.nia@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'person_publisher = ae_custom_interface_py.person_publisher:main'
        ],
    },
)
