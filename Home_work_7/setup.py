from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='1.0.0',
    description='Making order in folder',
    author='Andrii Kovalchuk',
    author_email='Andrii_Kovalchuk@example.com',
    license='MIT',
    packages=find_packages(),
    entry_points={'console_scripts': [
        'clean = clean_folder.clean:main']}
)
