from fairseq_cli import preprocess
from fairseq import options, tasks, utils
from argparse import Namespace

parser = options.get_preprocessing_parser()
args = parser.parse_args()
argdict = vars(args)
argdict["source_lang"]= "de"
argdict["target_lang"]= "en"
argdict["trainpref"]="/home/data/iwslt14.tokenized.de-en"+"/train"
argdict["validpref"]="/home/data/iwslt14.tokenized.de-en"+"/valid"
argdict["testpref"]="/home/data/iwslt14.tokenized.de-en"+"/test"
argdict["destdir"]="/home/outputs/data-bin/iwslt14.tokenized.de-en"
args = Namespace(**argdict)

try:
    preprocess.main(args)
except Exception as e:
    print("Skipping preprocessing because of error: {}".format(e))

