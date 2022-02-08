from fairseq_cli.train import main as pre_main
from fairseq import distributed_utils, metrics
import os
from fairseq.dataclass.configs import FairseqConfig
#from fairseq_cli import hydra_train

import hydra
from fairseq.dataclass.initialize import add_defaults, hydra_init

# @hydra.main(config_path=os.path.join("..", "configs"), config_name="config")
# def main(cfg: FairseqConfig):
#     print(cfg)    
  

@hydra.main(config_path=os.path.join("..", "config"), config_name="config")
def hydra_main(cfg) -> float:
    print(cfg)



import ipdb; ipdb.set_trace()


#call hydra
#distributed_utils.call_main(cfg, pre_main, **kwargs)

# import fairseq
# import fairseq.modules





# fairseq-train data-bin/iwslt14.tokenized.de-en \
#   --arch tutorial_simple_lstm \
#   --encoder-dropout 0.2 --decoder-dropout 0.2 \
#   --optimizer adam --lr 0.005 --lr-shrink 0.5 \
#   --max-tokens 12000




# from fairseq.dataclass.utils import omegaconf_no_object_check
# from fairseq.utils import reset_logging
