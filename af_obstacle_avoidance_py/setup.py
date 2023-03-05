from setuptools import setup
import os 
from glob import glob

package_name = 'af_obstacle_avoidance_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join("share" , package_name ,"launch" ), glob("launch/*.launch.py")),
        (os.path.join("share",package_name , "worlds") , glob("worlds/*.world.xml")),
        (os.path.join("share" , package_name , "model") , glob("model/my_tb3.urdf.xacro")),
        (os.path.join("share" , package_name , "model", "meshes" , "bases") , glob("model/meshes/bases/*")),
        (os.path.join("share" , package_name , "model", "meshes" , "sensors") , glob("model/meshes/sensors/*")),
        (os.path.join("share" , package_name , "model", "meshes" , "wheels") , glob("model/meshes/wheels/*")),
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
            'avoidance = af_obstacle_avoidance_py.avoidance:main'
        ],
    },
)
