import os

from parlai.core.build_data import DownloadableFile
import parlai.core.build_data as build_data


RESOURCES = [
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/8kidm9q1ik33suynw06ce/dataset_parlai_train_original.txt.zip?rlkey=rbaelvidz6jl730hlbdvaer6b&dl=1",
        'dataset_parlai_train_original.txt.zip',
        '195382b4a78e6cd960470e3561f0cd0a3077f532bcfba49ae0803360a2fe09c8',
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/7c2pl19xlwox9kb8bzz29/dataset_parlai_valid_original.txt.zip?rlkey=m72emirrwy1epz8abroquqe1p&dl=1",
        'dataset_parlai_valid_original.txt.zip',
        '27afce5b655dca9c52c28eccf3c0120b5cee7916023ee78fa3dff7b0253bbd38',
    )
]

TASK_NAME = 'GutenbertBookChars'


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
