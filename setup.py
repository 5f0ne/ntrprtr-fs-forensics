from setuptools import setup, find_packages

with open("README.md", "r") as r:
    desc = r.read()

setup(
    name="ntrprtr_fs_forensics", 
    version="0.1.0",
    author="5f0",
    url="https://github.com/5f0ne/ntrprtr-fs-forensics",
    description="ntrprtr configurations for forensic analysis of file systems",
    classifiers=[
        "Operating System :: OS Independent ",
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License "
    ],
    license="MIT",
    long_description=desc,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where='src'),
    include_package_data=True,
    package_data={
        "ntrprtr_fs_forensics.fat": ["fat-vbr.json", "fat-vbr-fat1216.json", "fat-vbr-fat32.json",
                                      "fat-vbr-type.json", "fat-fs-info.json",
                                      "fat-directory-entry.json", "fat-long-filename.json"],
        "ntrprtr_fs_forensics.ext": ["ext-file-descriptor-table.json", "ext-inode.json",
                                     "ext-super-block.json"],
        "ntrprtr_fs_forensics.ntfs": [],
    },
    install_requires=[
       
    ],
     entry_points={
        "console_scripts": [
            "ntrprtr_fs_forensics = ntrprtr_fs_forensics.__main__:main"
        ]
    }
)
