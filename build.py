import os

from parlai.core.build_data import DownloadableFile
import parlai.core.build_data as build_data


RESOURCES = [
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/59pcnfytpckv34dbvm2x0/139_1.parlai_dataset.txt.zip?rlkey=c9fwoxbyta9f05f79l4bkym8o&dl=1",
        '139_1.parlai_dataset.txt.zip',
        '32030d61ed7dd420c16878171c78076f3cc84f4063a8d5c22be2f3fe2593fc42',
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/q07aph6we2x2wkwid65en/155_21.parlai_dataset.txt.zip?rlkey=qzs9cj4uk01vir2k46ztr7934&dl=1",
        '155_21.parlai_dataset.txt.zip',
        '4f21d61b8c1dfa328b1f91c5c10023dca4c97b3c4bc25e7fb4d40b4220734b5a',
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/214biikj5wianib7517ou/403_3.parlai_dataset.txt.zip?rlkey=qo6f7kr2mw6gafix467vl2cxe&dl=1",
        '403_3.parlai_dataset.txt.zip',
        '89ce370d7442a0e082755810d5440c2b9d603bb4ac898cdbab341168fc8f4aab',
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/rhfukpgaxvpevqw4jnhmg/507_3.parlai_dataset.txt.zip?rlkey=6qcxui6a7mtc5b8xhp4zsoy7n&dl=1",
        '507_3.parlai_dataset.txt.zip',
        '61da706118fc3724e1387b7a3a62a0b51356e2fdb2b3d484e25bf93b59c56635',
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/07mp58p0fnw531tptdit4/1257_9.parlai_dataset.txt.zip?rlkey=1wesdzd1hqj668ztirh5yqidc&dl=1",
        '1257_9.parlai_dataset.txt.zip',
        '17ae087afb17b1b02cdba5343df073ca41880b6e1d88ed86dff41e7bf2d71d47',
    ),

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
