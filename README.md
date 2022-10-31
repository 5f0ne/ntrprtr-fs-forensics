# Description

ntrprtr configurations for forensic analysis of file systems

# Installation

`pip install ntrprtr_fs_forensics`

# Usage

**Shell:**

<hr>

**General**

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--mode | -m | String | - | copy = Create a local copy of file system forensics configuration files |

<hr>

**mode = copy**

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--path | -p | String | "" | Path for local copy of ntrprtr configuration files |


# Example

To use this configuration files install `ntrprtr` and `ntrprtr_fs_forensics`:

```bash
pip install ntrprtr
pip install ntrprtr_fs_forensics
```

To use the files, create a local copy:

```bash
python -m ntrprtr_fs_forensics -m copy -p .
```

It creates the following structure:

```
./ntrprtr-fsf-config
├───ext
│       ext-group-descriptor-table.json
│       ext-inode.json
│       ext-super-block.json
│
├───fat
│       fat-directory-entry.json
│       fat-fs-info.json
│       fat-long-filename.json
│       fat-vbr-fat1216.json
│       fat-vbr-fat32.json
│       fat-vbr-type.json
│       fat-vbr.json
│
└───ntfs
        ntfs-attribute-file-name.json
        ntfs-attribute-header-general.json
        ntfs-attribute-header-non-resident.json
        ntfs-attribute-header-resident.json
        ntfs-attribute-standard-information.json
        ntfs-mft-entry-header.json
        ntfs-vbr.json
```

Now just use the config as input for `ntrprtr`:

```bash
python -m ntrprtr -m interpret -p dir-entry.bin -c ./ntrprtr-fsf-config/fat/fat-directory-entry.json -r result.txt
```

# License

MIT