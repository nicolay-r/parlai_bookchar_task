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
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/wdtjdmshz2y7qms3vlplh/dataset_parlai_valid_spectrums.txt.zip?rlkey=2wzwnevttdwl7rzqg4gcrv2ql&dl=1",
        'dataset_parlai_valid_spectrums.txt.zip',
        'db36e70a897a69b718be7649e1a597ecae06fe72a01329846f751863e9b3df79',
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/ypbvhbed4t9us2fbyl4c4/dataset_parlai_train_spectrums.txt.zip?rlkey=hx2og8jjhyktvzv58l7bho62p&dl=1",
        'dataset_parlai_train_spectrums.txt.zip',
        'e5e683956abe481ae134c65ec5b003a85f0402481e4acb923eca3c5b0ab6f6cf',
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
