import os

from parlai.core.build_data import DownloadableFile
import parlai.core.build_data as build_data


RESOURCES = [
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/cmflno09yyvw70mpf4fli/dataset_parlai_train_original.txt.zip?rlkey=477zsekm5j0a4dpco0w9479uo&dl=1",
        'dataset_parlai_train_original.txt.zip',
        'd625ae5075b36b45d20330e02672c8a1eabc3e9775f97610a991ff9d1a81b2c2',
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/508zfhxewvweqtn4k7hfg/dataset_parlai_valid_original.txt.zip?rlkey=3a0syeturb84lxtmizq1o5bsx&dl=1",
        'dataset_parlai_valid_original.txt.zip',
        '20b3035170f172584ee87cf3a9a0ea46a1148f239834f693c67fc2599aa95446',
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/lr96to0rzc6wpo84isscb/dataset_parlai_valid_spectrum.txt.zip?rlkey=5wrgtrtuulf3baxr724bcycdu&dl=1",
        'dataset_parlai_valid_spectrums.txt.zip',
        '3d1338b8d525df78dd2c587e7b956757fb2cb8d21a54611bd76d875eefebc620',
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/ax62dvkik12alxj604ute/dataset_parlai_train_spectrum.txt.zip?rlkey=xuvmvze6fnak413gst54qd4qz&dl=1",
        'dataset_parlai_train_spectrums.txt.zip',
        '1996791350d6556b17bfa4760a641c4734b5968356c78d746263ec938f255010',
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
