# Investigating Pretrained Language Models for Graph-to-Text Generation

This repository contains the code for the paper: "[Investigating Pretrained Language Models for Graph-to-Text Generation](https://arxiv.org/pdf/2007.08426.pdf)", EMNLP | NLP4ConvAI.

> This repository contains experimental software and is published for the sole purpose of giving additional background details on the respective publication.

This project is implemented using the framework [HuggingFace](https://huggingface.co/). Please, refer to their websites for further details on the installation and dependencies.

## Environments and Dependencies

- python 3.6
- transformers 3.3.1
- pytorch-lightning 0.9.0
- torch 1.4.0
- parsimonious 0.8.1
## Datasets

In our experiments, we use the following datasets: [AMR17](https://catalog.ldc.upenn.edu/LDC2017T10), [WebNLG](https://webnlg-challenge.loria.fr/challenge_2017/) and [AGENDA](https://github.com/rikdz/GraphWriter/tree/master/data).

## Preprocess

First, convert the dataset into the format required for the model.

For the AMR17, run:
```
./preprocess_AMR.sh <dataset_folder>
```

For the WebNLG, run:
```
./preprocess_WEBNLG.sh <dataset_folder>
```

For the AGENDA, run:
```
./preprocess_AGENDA.sh <dataset_folder>
```


## Finetuning

For finetuning the models using the AMR dataset, execute:
```
./finetune_AMR.sh <model> <gpu_id>
```

For the WebNLG dataset, execute:
```
./finetune_WEBNLG.sh <model> <gpu_id>
```

For the AGENDA dataset, execute:
```
./finetune_AGENDA.sh <model> <gpu_id>
```
 
Options for `<model>` are `t5-small`, `t5-base`, `t5-large`, `facebook/bart-base` or `facebook/bart-large`. 

Example:
```
./finetune_AGENDA.sh t5-small 0
```


## Decoding

For decoding, run:
```
./decode_AMR.sh <model> <checkpoint> <gpu_id>
./decode_WEBNLG.sh <model> <checkpoint> <gpu_id>
./decode_AGENDA.sh <model> <checkpoint> <gpu_id>
```

Example:
```
./decode_WEBNLG.sh t5-base webnlg-t5-base.ckpt 0
```

## Trained models

| AMR17          |
| :------------- |
| [bart-base](https://public.ukp.informatik.tu-darmstadt.de/ribeiro/graph2text/amr-bart-base.ckpt) - BLEU: 36.71 ([output](https://github.com/UKPLab/plms-graph2text/raw/master/generated_outputs/amr-bart-base.txt)) |
| [bart-large](https://public.ukp.informatik.tu-darmstadt.de/ribeiro/graph2text/amr-bart-large.ckpt) - BLEU: 43.47 ([output](https://github.com/UKPLab/plms-graph2text/raw/master/generated_outputs/amr-bart-large.txt)) |
|  [t5-small](https://public.ukp.informatik.tu-darmstadt.de/ribeiro/graph2text/amr-t5-small.ckpt) - BLEU: 38.45 ([output](https://github.com/UKPLab/plms-graph2text/raw/master/generated_outputs/amr-t5-small.txt)) | 
| [t5-base](https://public.ukp.informatik.tu-darmstadt.de/ribeiro/graph2text/amr-t5-base.ckpt) - BLEU: 42.54 ([output](https://github.com/UKPLab/plms-graph2text/raw/master/generated_outputs/amr-t5-base.txt))  |
| [t5-large](https://public.ukp.informatik.tu-darmstadt.de/ribeiro/graph2text/amr-t5-large.ckpt) - BLEU: 45.80 ([output](https://github.com/UKPLab/plms-graph2text/raw/master/generated_outputs/amr-t5-large.txt)) |

| WebNLG   | 
| :------------- |
| [bart-base](https://public.ukp.informatik.tu-darmstadt.de/ribeiro/graph2text/webnlg-bart-base.ckpt) - All BLEU: 53.11 ([output](https://github.com/UKPLab/plms-graph2text/raw/master/generated_outputs/webnlg-all-bart-base.txt)), Seen BLEU: 62.74 ([output](https://github.com/UKPLab/plms-graph2text/raw/master/generated_outputs/webnlg-seen-bart-base.txt)), Unseen BLEU: 41.53 ([output](https://github.com/UKPLab/plms-graph2text/raw/master/generated_outputs/webnlg-unseen-bart-base.txt)) | 
| [bart-large](https://public.ukp.informatik.tu-darmstadt.de/ribeiro/graph2text/webnlg-bart-large.ckpt) - All BLEU: 54.72 ([output](https://github.com/UKPLab/plms-graph2text/raw/master/generated_outputs/webnlg-all-bart-large.txt)), Seen BLEU: 63.45 ([output](https://github.com/UKPLab/plms-graph2text/raw/master/generated_outputs/webnlg-seen-bart-large.txt)), Unseen BLEU: 43.97 ([output](https://github.com/UKPLab/plms-graph2text/raw/master/generated_outputs/webnlg-unseen-bart-large.txt)) |
| [t5-small](https://public.ukp.informatik.tu-darmstadt.de/ribeiro/graph2text/webnlg-t5-small.ckpt) - All BLEU: 56.34 ([output](https://github.com/UKPLab/plms-graph2text/raw/master/generated_outputs/webnlg-all-t5-small.txt)), Seen BLEU: 65.05 ([output](https://github.com/UKPLab/plms-graph2text/raw/master/generated_outputs/webnlg-seen-t5-small.txt)), Unseen BLEU: 45.37 ([output](https://github.com/UKPLab/plms-graph2text/raw/master/generated_outputs/webnlg-unseen-t5-small.txt)) | 
| [t5-base](https://public.ukp.informatik.tu-darmstadt.de/ribeiro/graph2text/webnlg-t5-base.ckpt) - All BLEU: 59.17 ([output](https://github.com/UKPLab/plms-graph2text/raw/master/generated_outputs/webnlg-all-t5-base.txt)), Seen BLEU: 64.64 ([output](https://github.com/UKPLab/plms-graph2text/raw/master/generated_outputs/webnlg-seen-t5-base.txt)), Unseen BLEU: 52.55 ([output](https://github.com/UKPLab/plms-graph2text/raw/master/generated_outputs/webnlg-unseen-t5-base.txt)) | 
| [t5-large](https://public.ukp.informatik.tu-darmstadt.de/ribeiro/graph2text/webnlg-t5-large.ckpt) - All BLEU: 59.70 ([output](https://github.com/UKPLab/plms-graph2text/raw/master/generated_outputs/webnlg-all-t5-large.txt)), Seen BLEU: 64.71 ([output](https://github.com/UKPLab/plms-graph2text/raw/master/generated_outputs/webnlg-seen-t5-large.txt)), Unseen BLEU: 53.67 ([output](https://github.com/UKPLab/plms-graph2text/raw/master/generated_outputs/webnlg-unseen-t5-large.txt)) | 

\* BLEU values for AMR17 are calculated using [sacreBLEU](https://github.com/mjpost/sacrebleu) in detok outputs. BLEU values for WebNLG are calculated using tok outputs using the [challange's script](https://gitlab.com/webnlg/webnlg-baseline), that uses multi-bleu.perl.



## More
For more details regading hyperparameters, please refer to [HuggingFace](https://huggingface.co/).


Contact person: Leonardo Ribeiro, ribeiro@aiphes.tu-darmstadt.de

## Citation
```
@inproceedings{ribeiro-etal-2021-investigating,
    title = "Investigating Pretrained Language Models for Graph-to-Text Generation",
    author = {Ribeiro, Leonardo F. R.  and
      Schmitt, Martin  and
      Sch{\"u}tze, Hinrich  and
      Gurevych, Iryna},
    booktitle = "Proceedings of the 3rd Workshop on Natural Language Processing for Conversational AI",
    month = nov,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.nlp4convai-1.20",
    pages = "211--227",
    abstract = "Graph-to-text generation aims to generate fluent texts from graph-based data. In this paper, we investigate two recent pretrained language models (PLMs) and analyze the impact of different task-adaptive pretraining strategies for PLMs in graph-to-text generation. We present a study across three graph domains: meaning representations, Wikipedia knowledge graphs (KGs) and scientific KGs. We show that approaches based on PLMs BART and T5 achieve new state-of-the-art results and that task-adaptive pretraining strategies improve their performance even further. We report new state-of-the-art BLEU scores of 49.72 on AMR-LDC2017T10, 59.70 on WebNLG, and 25.66 on AGENDA datasets - a relative improvement of 31.8{\%}, 4.5{\%}, and 42.4{\%}, respectively, with our models generating significantly more fluent texts than human references. In an extensive analysis, we identify possible reasons for the PLMs{'} success on graph-to-text tasks. Our findings suggest that the PLMs benefit from similar facts seen during pretraining or fine-tuning, such that they perform well even when the input graph is reduced to a simple bag of node and edge labels.",
}
```
