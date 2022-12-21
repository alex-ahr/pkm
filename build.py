#!/usr/bin/env python3

import shutil
import pathlib
import os

SOURCE = "vault"
TARGET = "content"
TMP = "tmp"
OBSIDIAN_EXPORT_COMMAND = f"obsidian-export {TMP} {TARGET}"

def reclsdir(target: str, removeprefix=True) -> list:
    list = [f"{target}/{i}" for i in os.listdir(target)]
    i = 0
    list_len = len(list)
    while i < list_len:
        if os.path.isdir(list[i]) == True:
            sublist = [f"{list[i]}/{n}" for n in os.listdir(list[i])]
            for n in range(len(sublist)):
                list.insert(i + 1 + n, sublist[n])
            list_len = len(list)
        i = i + 1
    
    if removeprefix:
        # Remove 'target/' from every item, making func consistent with `os.listdir()`
        return [x.removeprefix(target + "/") for x in list] # ex: 'test/sub' -> 'sub'
    else:
        return list

def strip_list_nonmd(files: list[str]) -> list[str]:
    print(files)
    
    for i in range(len(files)):
        print(f"filename: {files[i]}")
        if pathlib.Path(files[i]).suffix != ".md":
            files[i] = ""
        else: pass
    
    while "" in files:
        files.remove("")
    
    return files

shutil.rmtree(TMP)
shutil.copytree(SOURCE, TMP)

files: list[str] = strip_list_nonmd(reclsdir(TMP, removeprefix=False))

print(files)

# hack: Insert newline to all files that are `*.md`
for file in iter(files):
    with open(file, 'a') as fd:
        fd.write("\n")

os.system(f"~/.cargo/bin/{OBSIDIAN_EXPORT_COMMAND}")
shutil.rmtree(TMP)