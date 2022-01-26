from clearml import Dataset, StorageManager, Task
import os

remote_path = "s3://experiment-logging"
Task.add_requirements("torch")
task = Task.init(project_name='fairseq-experiments', task_name='fairseq-setup-test',
                 output_uri=os.path.join(remote_path, "storage"))
task.set_base_docker("nvidia/cuda:11.4.0-cudnn8-devel-ubuntu20.04", docker_setup_bash_script=["git clone https://github.com/pytorch/fairseq", "cd fairseq", "pip install --editable ./"])
task.execute_remotely(queue_name="compute2", exit_process=True)

import fairseq

dataset = Dataset.get(dataset_project='datasets/librispeech', dataset_name='librispeech_small')
dataset_path = dataset.get_local_copy()

