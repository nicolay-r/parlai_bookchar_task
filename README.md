# Literature Dialogue Response Task (LDR) 📚 • [![twitter](https://img.shields.io/twitter/url/https/shields.io.svg?style=social)](https://x.com/nicolayr_/status/1801009815784677862)
![](https://img.shields.io/badge/Python-3.8-lightgreen.svg)
[![twitter](https://img.shields.io/twitter/url/https/shields.io.svg?style=social)](https://x.com/nicolayr_/status/1801009815784677862)

> ⚠️ **Disclaimer**: this repository setups the task for the predefined `train` and `valid` splits. In order to replicate studies on different splits you have to manually update the related parts.
> We believe that ParlAI supports task initialization in Cross-Validation mode, however it goes beyond the capabilities of this project version.

This repository represent a supplementary material for the [`nicolay-r/book-persona-retreiver`](https://github.com/nicolay-r/book-persona-retriever) experiments organization 🧪 mentioneed in paper 
[Personality Profiling for Literary Character Dialogue Agents with Human Level Attributes (**pre-print**)](https://www.dropbox.com/scl/fi/0c2axh97hadolwphgu7it/rusnachenko2024personality.pdf?rlkey=g2yyzv01th2rjt4o1oky0q8zc&st=omssztha&dl=1)
that has been accepted for *Long Paper* track at [LOD-2024](https://lod2024.icas.events/).

##  Adding task into ParlAI 🦜
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nicolay-r/deep-book-processing/blob/master/parlai_gutenberg_experiments.ipynb)

You have to accomplish **three steps below** in order to start experiment with ParlAI 🦜 dialgue agents in the related task.

These steps are as follows:

👉 1. Add this entry into ParlAI [`task_list.py`](https://github.com/facebookresearch/ParlAI/blob/main/parlai/tasks/task_list.py) for registering this task:
```json
{
    "id": "GutenbertBookChars",
    "display_name": "GutenbertBookChars",
    "task": "gutenbergbookchars",
    "tags": ["ChiteChat"],
    "description": (
        "Dataset of speaker utterances from ProjectGutenberg with their spectrums"
    )
}
```

👉 2. Follow the [`setup.sh`](setup.sh) to create folder `GutenbertBookChars` in the `ParlAI` project.

👉 3. Display dataset data in `parlai/scripts/` to make sure that the task is available:
```bash
python display_data.py --task gutenbergbookchars
```

You can also froceed with the related [notebook on GoogleColab](https://colab.research.google.com/github/nicolay-r/deep-book-processing/blob/master/parlai_gutenberg_experiments.ipynb)


## References

You can cite this work as follows:

```bibtex
TO BE ADDED
```
