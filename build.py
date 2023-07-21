import os

from parlai.core.build_data import DownloadableFile
import parlai.core.build_data as build_data


RESOURCES = [
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/gx1bhrma0ohsywxfau4is/utterance_speaker_train.txt?rlkey=n3ss85vv4ecnaqeu6rg30sdyp&dl=1",
        'utterance_speaker_train_original.txt',
        'e16236df8a0c5d8238c634db70407d6c0d2ccd3a586ae5276a22a55c95b66095'
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/027dz15dr6g7jy3j02dqp/utterance_speaker_test.txt?rlkey=m6kl6bzwq1a5d1rfir8xpqe43&dl=1",
        'utterance_speaker_valid_original.txt',
        '8b5af2faa4a84f48f446d872be7afdd12e579c1cbcc9ab4df560d21dd003d030'
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
