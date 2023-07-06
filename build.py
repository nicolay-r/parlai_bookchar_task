import os

from parlai.core.build_data import DownloadableFile
import parlai.core.build_data as build_data


RESOURCES = [
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/ghguz41mk3ytrqgjfd5i1/dataset_parlai_train_original.txt.zip?rlkey=1aoenarm5dvqol3e6mg2ioto6&dl=1",
        'dataset_parlai_train_original.txt.zip',
        '8c776f06b96fd12833858095b5473cb91534583801f7bd4af92400fe10da87a8',
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/gloua0tlfmsfvxy6m24cf/dataset_parlai_valid_original.txt.zip?rlkey=wopd1fcpbwz6uxsedydg87s6i&dl=1",
        'dataset_parlai_valid_original.txt.zip',
        'a6486bed679c7b25c357e92d344a193a2e19932e7404738c8f647a8875e67d90',
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
