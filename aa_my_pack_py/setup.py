#The main objective of this code is to add an entry point to the script you created
from setuptools import setup
import os #import os and glob to add path to the launch files easily
from glob import glob
package_name = 'aa_my_pack_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    #The objective of this code is to install the launch files. this will install all the launch files from the launch/ folder, into ~/Ros2Basics/install/aa_my_pack_py/share/aa_my_pack_py/launch/
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share' , package_name),glob('launch/*.launch.py')) #specify where the launch files are in order for the colcon to find it(ament is the build system and colcon is the build tool just FYI). you can also do this the hard way which is written above this
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='course',
    maintainer_email='sohail.e.nia@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    #Add the node information to generate the executable. Actually you are adding an entry point to the helloWorld.py script
    entry_points={
        'console_scripts': [
            'helloWorld = aa_my_pack_py.helloWorld:main' ,  #helloWorld is the name of the executable  and main is the function and before main, helloWorld is the helloWorld.py which we ommit the .py extension
            'helloWorldLoop = aa_my_pack_py.helloWorldLoop:main' #Don't forget to put a ',' before writing this line or else you node or launch file doesn't work!
        ],
    },
)
