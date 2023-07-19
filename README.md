# Task Setup 

1.Add this entry in task registry:
```
{
    "id": "GutenbergSR",
    "display_name": "GutenbergSR",
    "task": "gutenbergsr",
    "description": (
        "Dataset of speaker recognition from ProjectGutenberg with their spectrums"
    )
}
```

2. Follow the `setup.sh` to create folder `GutenbergSR` in the `ParlAI` project.

3. Display dataset data in `parlai/scripts/`
```bash
python display_data.py --task gutenbergsr
```
