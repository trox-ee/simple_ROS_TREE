from setuptools import find_packages, setup

package_name = 'agnirath'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='aditya',
    maintainer_email='aditya@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "angle_publisher = agnirath.publisher_node:main",
            "middle_man_node = agnirath.main_node:main",
            "motor_node = agnirath.motor_node:main",
            "battery_node = agnirath.battery_node:main"
        ],
    },
)
