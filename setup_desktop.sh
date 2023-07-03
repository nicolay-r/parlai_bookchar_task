#!/bin/bash

parlai_project="/media/nicolay/96ed6537-b931-4f7e-8ac4-8407527ddbf9/proj/chatbot-experiments/venv/lib/python3.8/site-packages/parlai"
task_name="gutenbergbookchars"
task_dirname="GutenbertBookChars"

target=$parlai_project"/tasks/"$task_name"/"

mkdir -p $target
cp -r ./* $target
