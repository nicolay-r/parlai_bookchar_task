import os

from parlai.core.build_data import DownloadableFile
import parlai.core.build_data as build_data


RESOURCES = [
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/nff5gn7r300pp25wwlsqx/utterance_speaker_train.txt.zip?rlkey=1gu8sk5lo1k7yz500wb5dhzik&dl=1",
        'utterance_speaker_train_original.txt.zip',
        '505a1f0984e6fc71ee2614baa03980696ec07d2e70942e86aedd2d5b5d26e68e'
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/m8ni8k117tf471g13nu84/utterance_speaker_test.txt.zip?rlkey=3p4ot0dfu3tvxmrihim38993y&dl=1",
        'utterance_speaker_valid_original.txt.zip',
        'bed64b031752248080aa7443e460c82a03ed637091ce99b065432db3b74925aa'
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
