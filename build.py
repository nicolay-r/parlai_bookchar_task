import os

from parlai.core.build_data import DownloadableFile
import parlai.core.build_data as build_data


RESOURCES = [
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/plxlxggy7vxskzggzdhin/utterance_speaker_train_original.txt.zip?rlkey=ydxbjirqf2gup3wob9wcet2f3&dl=1",
        'utterance_speaker_train_original.txt.zip',
        '71e4725753ca5517e09e999d5768761c45aebf62b9186ddc6101e417c8de6e65'
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/vbz6wf64xqlaz7x9c4rqo/utterance_speaker_valid_original.txt.zip?rlkey=rnfwng8e2w188smx0k55ycvac&dl=1",
        'utterance_speaker_valid_original.txt.zip',
        '4ee8a94c8a30979f7fc0e6d616749dfef2d1500310d09efa0df05cba0575f901'
    ),
]

TASK_NAME = 'GutenbergSR'


def build(opt):

    version = "v1.0"
    dpath = os.path.join(opt['datapath'], TASK_NAME)

    if not build_data.built(dpath, version_string=version):
        print('building data: ' + dpath)
        if build_data.built(dpath):
            # An older version exists, so remove these outdated files.
            build_data.remove_dir(dpath)
        build_data.make_dir(dpath)

        # Download the data.
        for downloadable_file in RESOURCES:
            downloadable_file.download_file(dpath)

        # Mark the data as built.
        build_data.mark_done(dpath, version)
