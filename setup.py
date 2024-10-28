from setuptools import setup

setup(
    name="StickyNotes",
    version="1.0",
    description="A simple sticky notes application built with Tkinter.",
    author="Pushpak Jaiswal",
    author_email="pushpakmjaiswal@gmail.com",
    packages=["stickynotes"],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'stickynotes = stickynotes:StickyNotes'
        ],
    },
)
