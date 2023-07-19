#!/bin/bash

parlai_project="/usr/local/lib/python3.8/dist-packages/parlai"
task_name="gutenbergsr"
task_dirname="GutenbergSR"

target_tasks=$parlai_project"/tasks/"
target_task=$target_tasks$task_name"/"

mkdir -p $target_task
cp -r ./* $target_task

cp "task_list.py" $target_tasks
