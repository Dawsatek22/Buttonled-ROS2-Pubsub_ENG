from setuptools import find_packages, setup

package_name = 'buttonpkg'

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
    maintainer='test1',
    maintainer_email='test1@todo.todo',
    description='TODO: Package description',
    license='Apache License 2.0<',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = buttonpkg.talker:main', #the talker node
            'listen = buttonpkg.listen:main', #the listener node

        ],
    },
)
