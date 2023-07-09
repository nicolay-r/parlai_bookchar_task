#!/bin/bash

parlai_project="/media/nicolay/96ed6537-b931-4f7e-8ac4-8407527ddbf9/proj/chatbot-experiments/venv/lib/python3.8/site-packages/parlai"
task_name="gutenbergbookchars"
task_dirname="GutenbertBookChars"

target_tasks=$parlai_project"/tasks/"
target_task=$target_tasks$task_name"/"

mkdir -p $target_task
cp -r ./* $target_task

cp "task_list.py" $target_tasks
