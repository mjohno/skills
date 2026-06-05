# Sync Options Reference

This document provides a quick reference for synchronizing a local directory to a target directory across different operating systems and workflows.

`TARGET_DIRECTORY` refers to the directory where you want to sync your files, and `<source_directory>` refers to the directory containing the files you want to sync.


## 1. Set and Forget (Symlinks/Junctions) - Preferred
*Use these if you want changes in your source directory to be reflected in the target directory instantly without running any commands.*

### Linux: Symlink
Creates a symbolic link to the directory.
```bash
ln -s "$(pwd)/skills" ${TARGET_DIRECTORY}
```

### Windows: Directory Junction
The Windows equivalent for directories. Does not require Administrator privileges for local drives.
```cmd
mklink /J "%USERPROFILE%\%TARGET_DIRECTORY%" "%CD%\skills"
```

---

## 2. Manual Sync (Rsync/Robocopy) - Alternative
*Use these if you want to physically copy files and only update the target when you are ready. These are useful if the target directory is on a different filesystem or if you want to keep the copies distinct.*

### Linux: Rsync
Uses `rsync` with the `--delete` flag to ensure the target is an exact mirror of the source.
```bash
rsync -av --delete ./skills/ ${TARGET_DIRECTORY}
```

### Windows: Robocopy
Uses the `/MIR` (Mirror) flag to synchronize the directory trees.
```cmd
robocopy .\skills %USERPROFILE%\%TARGET_DIRECTORY% /MIR
```
