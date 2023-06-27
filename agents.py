import logging
from typing import Optional

from parlai.core.opt import Opt
from parlai.core.params import ParlaiParser
from parlai.core.teachers import ParlAIDialogTeacher
from parlai.utils.strings import normalize_reply


class DefaultTeacher(ParlAIDialogTeacher):
    @classmethod
    def add_cmdline_args(cls, parser: ParlaiParser, partial_opt: Optional[Opt] = None) -> ParlaiParser:
        super().add_cmdline_args(parser, partial_opt)
        agent = parser.add_argument_group('NormalizedTeacher arguments')
        agent.add_argument(
            '--your-persona-first',
            type='bool',
            default=True,
            help="whether to prepend your persona followed by partner's persona. "
                 "True by default to be consistent with the BothTeach",
        )
        agent.add_argument(
            '--max-num-turns',
            type=int,
            default=-1,
            help="first X turns per episode to show. If -1 then the whole episode is shown",
        )
        return agent

    def __init__(self, opt, shared=None):
        self.max_num_turns = opt["max_num_turns"]
        self.your_persona_first = opt["your_persona_first"]
        super().__init__(opt, shared)

    def normalize_replies(self, x):
        xs = x.split('\n')
        your_personas = []
        partner_personas = []
        non_personas = []
        for x in xs:
            if x.startswith('your persona: '):
                # Normalize the sentence appearing after 'your persona:'
                x = x[len('your persona: '):]
                x = normalize_reply(x)
                x = 'your persona: ' + x
                your_personas.append(x)
            elif x.startswith("partner's persona: "):
                x = x[len("partner's persona: "):]
                x = normalize_reply(x)
                x = "partner's persona: " + x
                partner_personas.append(x)
            else:
                x = normalize_reply(x)
                non_personas.append(x)
        xs2 = []
        if self.your_persona_first:
            xs2.extend(your_personas)
            xs2.extend(partner_personas)
        else:
            xs2.extend(partner_personas)
            xs2.extend(your_personas)
        xs2.extend(non_personas)
        return '\n'.join(xs2)

    def setup_data(self, path):
        logging.info(f"loading normalized fbdialog data: {path}")
        exs_counter = 0
        for data, new_episode in super().setup_data(path):
            text, labels, reward = data[:3]
            candidates = None if len(data) == 3 else data[3]
            if new_episode:
                exs_counter = 0
            if self.max_num_turns > 0 and exs_counter >= self.max_num_turns:
                continue
            text = self.normalize_replies(text)
            labels = [self.normalize_replies(l) for l in labels]
            exs_counter += 1
            if candidates:
                candidates = [self.normalize_replies(c) for c in candidates]
                yield (text, labels, reward, candidates), new_episode
            else:
                yield (text, labels, reward), new_episode
