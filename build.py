import os

from parlai.core.build_data import DownloadableFile
import parlai.core.build_data as build_data


RESOURCES = [
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/b1ukv0orjgmdg6slcltmj/dataset_parlai_train_dialog_original.txt.zip?rlkey=g81ontblxg8ze8wa195pu6ntw&dl=1",
        'dataset_parlai_train_dialog_original.txt.zip',
        '396f1153ef4c4fb686ebae581f3008a2276ac24d019dfd3af744cf80aba41e35'
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/jnpj8acsjhoq9cgj4x0zj/dataset_parlai_train_dialog_spectrum.txt.zip?rlkey=jvjly9szxbn24lh1dy0c0ksmd&dl=1",
        'dataset_parlai_train_dialog_spectrum.txt.zip',
        '3732c3f5ea35de96e5950f983fc0f569be67337d63865dc08efe48a03acc75df'
    )
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
