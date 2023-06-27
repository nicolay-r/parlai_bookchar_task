#!/bin/bash
parlai_dir="/home/nicolay/ParlAI/"
task_name="gutenbergbookchars"
target=$parlai_dir"parlai/tasks/"$task_name"/"
mkdir -p $target
cp -r ./* $target