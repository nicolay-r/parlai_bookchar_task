import copy
import os

from .build import build, TASK_NAME

from parlai.core.teachers import FbDeprecatedDialogTeacher
from parlai.utils.misc import warn_once


def _path(opt, persona, use_cands):
    # Build the data if it doesn't exist.
    build(opt)
    datatype = opt['datatype'].split(':')[0]
    if datatype == 'test':
        warn_once("WARNING: Test set not included. Setting datatype to valid.")
        datatype = 'valid'
    dt = datatype + '_' + persona
    cands = '' if use_cands else '_no_cands'
    return os.path.join(opt['datapath'], TASK_NAME, dt + cands + '.txt')


class OriginalTeacher(FbDeprecatedDialogTeacher):
    def __init__(self, opt, shared=None):
        opt = copy.deepcopy(opt)
        try:
            cands = opt['task'].split(":")[2]
            use_cands = False if cands == 'no_cands' else True
        except Exception:
            use_cands = True
        opt['datafile'] = _path(opt, 'original', use_cands)
        super().__init__(opt, shared)


class SpectrumTeacher(FbDeprecatedDialogTeacher):
    def __init__(self, opt, shared=None):
        opt = copy.deepcopy(opt)
        try:
            cands = opt['task'].split(":")[2]
            use_cands = False if cands == 'no_cands' else True
        except Exception:
            use_cands = True
        opt['datafile'] = _path(opt, 'spectrums', use_cands)
        super().__init__(opt, shared)


class SpeakerExtractionTeacher(FbDeprecatedDialogTeacher):
    def __init__(self, opt, shared=None):
        opt = copy.deepcopy(opt)
        try:
            cands = opt['task'].split(":")[2]
            use_cands = False if cands == 'no_cands' else True
        except Exception:
            use_cands = True
        opt['datafile'] = _path(opt, 'se', use_cands)
        super().__init__(opt, shared)


class DefaultTeacher(OriginalTeacher):
    pass

