import os

from parlai.core.build_data import DownloadableFile
import parlai.core.build_data as build_data


RESOURCES = [
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/ghguz41mk3ytrqgjfd5i1/dataset_parlai_train_original.txt.zip?rlkey=1aoenarm5dvqol3e6mg2ioto6&dl=1",
        'dataset_parlai_train_original.txt.zip',
        '0c267a9cf8d578a32a7243ba9b04c1c899e47344deeea69991b58e502edda13e',
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/gloua0tlfmsfvxy6m24cf/dataset_parlai_valid_original.txt.zip?rlkey=wopd1fcpbwz6uxsedydg87s6i&dl=1",
        'dataset_parlai_valid_original.txt.zip',
        'f8dccade663139857cc2db847b8c6ec51fba493a7c7f080efad02e29aed8a459',
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
