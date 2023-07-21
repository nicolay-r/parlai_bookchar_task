import os

from parlai.core.build_data import DownloadableFile
import parlai.core.build_data as build_data


RESOURCES = [
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/v43ee83iup1usdhw6zhxa/utterance_speaker_train.txt.zip?rlkey=43mb18p84l3qyz5cugueisbmo&dl=1",
        'utterance_speaker_train_original.txt.zip',
        'e0acb6d8638a370460493297bc58b9b364adc691d77a7a599124c6e8529daa71'
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/urjt8umkqh6r1hemgnr32/utterance_speaker_test.txt.zip?rlkey=159i9bi89wsmhao5dok7p7msk&dl=1",
        'utterance_speaker_valid_original.txt.zip',
        'a891a9d5ac3eb92a3e9ee77dac0d0a3fbda774317c975eed3f38fd0b27a8cd2d'
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
