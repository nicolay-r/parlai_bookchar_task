import os

from parlai.core.build_data import DownloadableFile
import parlai.core.build_data as build_data


RESOURCES = [
    DownloadableFile(
        "https://www.dropbox.com/s/e0b968zedfwtzvq/utterance_speaker_train.txt?dl=0",
        'utterance_speaker_train.txt',
        'b0a9c223421c8da820430a8bc229d9e242c6c330b0a2664bb65b63c9649612a9'
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/rd8iu7wwkysqgy7tnkygy/utterance_speaker_test.txt?rlkey=5lmgw6t0rhjiwjb40rlvlvscf&dl=0",
        'utterance_speaker_test.txt',
        'd0bbec77ffb15450062ffe3533d1c2bb2e8176fbe7dce20d01823757c3236b7d
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
