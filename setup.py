from setuptools import setup, find_packages

setup(
    name="Analytics Data",
    version="0.1.0",
    author="Tera Earlywine",
    author_email="dev@teraearlywine.com",
    description="Cleaning data found for various portfolio pieces",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/teraearlywine/analytics",
    packages=find_packages("src"),
    include_package_data=True,
    # install_requires=[
    #     'dependency1',
    #     'dependency2',
    #     # Add other dependencies your project needs
    # ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # python_requires='>=3.6',
    # entry_points={
    #     'console_scripts': [
    #         'your_command=your_module:main_function',
    #     ],
    # },
)
