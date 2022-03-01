from setuptools import setup, find_packages

# Long description
with open("README.md", encoding="UTF-8") as f:
	LONG_DESCRIPTION = f.read()

# Classifiers
CLASSIFIERS = [
	"Development Status :: 3 - Alpha",
	"Programming Language :: Python",
	"Programming Language :: Python :: 3",
	"Programming Language :: Python :: 3.6",
	"Programming Language :: Python :: 3.7",
	"Programming Language :: Python :: 3.8",
	"Programming Language :: Python :: 3.9",
	"Programming Language :: Python :: 3.10",
	"Programming Language :: Python :: 3.11",
	"License :: OSI Approved :: MIT License"
]

# Metadata
METADATA = dict(
	name =			"Systerm",
	version =		"0.1.0",
	description =	"A multipurpose python library",
	author =		"ZytroCode",
	packages =		find_packages(),
)

setup(**METADATA)
