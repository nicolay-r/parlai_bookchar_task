import os

from parlai.core.build_data import DownloadableFile
import parlai.core.build_data as build_data


RESOURCES = [
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/rgdkv318bxbshdxamffqn/dataset_parlai_train_original.txt.zip?rlkey=jakg09xhsvq79w2jlblwlbib4&dl=1",
        'dataset_parlai_train_original.txt.zip',
        '500ce5f10bfe26306ecb6103880510d5f569e801d03b6068378496117305cc79',
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/dhe65940abepc9wf6t2n2/dataset_parlai_valid_original.txt.zip?rlkey=j4b39tufgrvj8awsk26v0oevn&dl=1",
        'dataset_parlai_valid_original.txt.zip',
        '00a9f3d325dd77826f035e720265b7a8b8c5634497e2aa349417ad777ca0b00d',
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/8k8ntw49xytp6dfqsr8s0/dataset_parlai_valid_spectrum.txt.zip?rlkey=w72edhrqg79qpsv4c1u17se37&dl=1",
        'dataset_parlai_valid_spectrums.txt.zip',
        'b92c9f8a3b0b6da35c51fcd7e286d6b4f9906bcb17e73dde1856a1a942822fcd',
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/pnq9cj34yaxsg2sl0aedf/dataset_parlai_train_spectrum.txt.zip?rlkey=nq96zp649mg8lbfqh5aql75sk&dl=1",
        'dataset_parlai_train_spectrums.txt.zip',
        'f8f36252e1972c98f779e7f864e48b7c88dbb740a9efd871dae45fe0b89c2d66',
    ),
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
