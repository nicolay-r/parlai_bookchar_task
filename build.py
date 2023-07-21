import os

from parlai.core.build_data import DownloadableFile
import parlai.core.build_data as build_data


RESOURCES = [
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/ei3am4v4bfuxx413bs1p1/utterance_speaker_train.txt.zip?rlkey=30w9om8guvsqjh6j33okwefmx&dl=1",
        'utterance_speaker_train_original.txt.zip',
        '7d5a3af81c731becb50cd3be807dd489ffd6803a8558a23ddb465cfef36de806'
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/fglusiz49r3ylxzcj04e1/utterance_speaker_test.txt.zip?rlkey=xuj4bxobdw3izufg8qlo6bogu&dl=1",
        'utterance_speaker_valid_original.txt.zip',
        '7ce30fa116ddd12da43f9e0566cb6a96b5e77effdb55babf6b028e8e63c9f7e7'
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
