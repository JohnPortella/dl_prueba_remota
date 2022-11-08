from setuptools import find_packages, setup

setup(
    name='cat_project',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[        
        'jinja2',
        'requests',
        'flask'        
    ],
)