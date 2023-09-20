import os

from parlai.core.build_data import DownloadableFile
import parlai.core.build_data as build_data


RESOURCES = [
    # Data for pre-training in dialogue format without spectrums (original), and with HLA (spectrum)
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/b1ukv0orjgmdg6slcltmj/dataset_parlai_train_dialog_original.txt.zip?rlkey=g81ontblxg8ze8wa195pu6ntw&dl=1",
        'dataset_parlai_train_dialog_original.txt.zip',
        '5d50691da48c18eb43ae1b847fb0a5b9f31941d079db31117b706304780784b5'
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/jnpj8acsjhoq9cgj4x0zj/dataset_parlai_train_dialog_spectrum.txt.zip?rlkey=jvjly9szxbn24lh1dy0c0ksmd&dl=1",
        'dataset_parlai_train_dialog_spectrum.txt.zip',
        '33efe4eeb1d4f2cb671611f18865d06ad950066e5cb8e5bf1e9282ac5c6aa229'
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/a8d49ui1r2rfm4kgrarym/dataset_parlai_valid_dialog_original.txt.zip?rlkey=bcrue4py1u2v4u6zamdksni3z&dl=1",
        'dataset_parlai_valid_dialog_original.txt.zip',
        '25b6fe5644d580b39a87cc18cc5413a3c5c3f6409990085cb4e07a5758f4be01'
    ),
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/9holfn0j3y1m81hpy89qc/dataset_parlai_valid_dialog_spectrum.txt.zip?rlkey=zxpxsqz0qclfcm26xvomqxntp&dl=1",
        'dataset_parlai_valid_dialog_spectrum.txt.zip',
        '8f9850a699c86c300b7988813cc31611fa6f5daaeef317c8e5901da9f08eb44f'
    ),
    # Data for Speaker-Classification/Extraction problem
    DownloadableFile(
        "https://www.dropbox.com/scl/fi/r241a1ma2douus965h7lf/dataset_parlai_train_hla.txt.zip?rlkey=dwcnm0yxn2boujomd53nx0595&dl=1",
        'dataset_parlai_train_hla.txt.zip',
        '36a6d26196b748430ed2e166e5dde90b521f5272cc490ca7541671df62552c67'
    ),
     DownloadableFile(
        "https://www.dropbox.com/scl/fi/arzub1tmegklkf93dthpr/dataset_parlai_valid_hla.txt.zip?rlkey=lpa8vcs48f3bxegk3gtw22h2i&dl=1",
        'dataset_parlai_valid_hla.txt.zip',
        '92250678095d568b13a08b68c584c1d32058bbabb0bdf82940bfbfbe3013ac54'
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
