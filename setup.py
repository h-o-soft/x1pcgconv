from setuptools import setup, find_packages

setup(
	name="x1pcgconv",
	version="0.1.0",
	install_requires=["Pillow"],
	packages=find_packages(),
	entry_points={
		"console_scripts": [
			"x1pcgconv=x1pcgconv.app:main"
		]
	}
)
