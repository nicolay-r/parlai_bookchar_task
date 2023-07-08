#!/bin/bash

parlai_project="/usr/local/lib/python3.8/dist-packages/parlai"
task_name="gutenbergbookchars"
task_dirname="GutenbertBookChars"

target=$parlai_project"/tasks/"$task_name"/"

mkdir -p $target
cp -r ./* $target
