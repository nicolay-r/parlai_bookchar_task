# Task Setup 

1.Add this entry in task registry:
```
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

2. Follow the `setup.sh` to create folder `GutenbertBookChars` in the `ParlAI` project.

3. Display dataset data in `parlai/scripts/`
```bash
python display_data.py --task gutenbergbookchars
```
