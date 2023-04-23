from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in app_ceres/__init__.py
from app_ceres import __version__ as version

setup(
	name='app_ceres',
	version=version,
	description='Sistema para la Gestión Integral de Clinicas y Hospitales',
	author='Francisco Adame',
	author_email='sebas.franksys@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
