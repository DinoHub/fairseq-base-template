from clearml import Dataset, StorageManager, Task
import os

remote_path = "s3://experiment-logging"
Task.add_requirements("torch")
Task.add_requirements("setuptools")
task = Task.init(project_name='fairseq-experiments', task_name='fairseq-setup-test',
                 output_uri=os.path.join(remote_path, "storage"))
task.set_base_docker("nvidia/cuda:11.4.0-cudnn8-devel-ubuntu20.04", docker_setup_bash_script=["git clone https://github.com/pytorch/fairseq", "cd fairseq", "pip install --editable ./"])
task.execute_remotely(queue_name="compute2", exit_process=True)


import logging
import os

import hydra
import torch
from hydra.core.hydra_config import HydraConfig
from omegaconf import OmegaConf, open_dict

from fairseq import distributed_utils, metrics
from fairseq.dataclass.configs import FairseqConfig
from fairseq.dataclass.initialize import add_defaults, hydra_init
from fairseq.dataclass.utils import omegaconf_no_object_check
from fairseq.utils import reset_logging
from fairseq_cli.train import main as pre_main


dataset = Dataset.get(dataset_project='datasets/librispeech', dataset_name='librispeech_small')
dataset_path = dataset.get_local_copy()
