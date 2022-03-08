"""This module is a copy of the python's shutil module"""
import Systerm
import pathlib
import shutil
import os
# FileMod
class FileMod(Systerm.module.Module.super(shutil, os.path, pathlib)):
	"""Module class for Systerm.file"""

Systerm.module.modules[__name__].__class__ = FileMod
