#!/bin/bash

parlai_dir="/home/nicolay/ParlAI/"
parlai_project=$parlai_dir"parlai/"
task_name="gutenbergbookchars"
task_dirname="GutenbertBookChars"

target=$parlai_project"/tasks/"$task_name"/"

mkdir -p $target
cp -r ./* $target

cd $parlai_project"/scripts/" && python display_data.py --task $task_name
