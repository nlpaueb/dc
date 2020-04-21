import os
import re
import json
import math
import numpy as np
import pandas as pd


def average_embedding(embeddings_matrix):
    return np.average(embeddings_matrix, axis=0)


# Clean for BioASQ
def _bioclean(caption):
    return re.sub('[.,?;*!%^&_+():-\[\]{}]',
                  '',
                  caption.replace('"', '')
                  .replace('/', '')
                  .replace('\\', '')
                  .replace("'", '')
                  .strip()
                  .lower()).split()


def get_list_of_words_per_caption(dataframe_data):
    dataframe_data["split_captions"] = dataframe_data["caption"]\
        .apply(lambda x: _bioclean(x))
    return dataframe_data


def load_data(data_dir):
    data = pd.read_csv(data_dir, sep="\t",
                       names=["image_ids", "caption"],
                       header=None)
    data['img_ids_list'] = data.image_ids.apply(lambda x: x.split(','))
    return data


def save_results(results_dictionary, results_dir, file_name):
    # Save test results to tsv file
    df = pd.DataFrame.from_dict(results_dictionary, orient="index")
    df.to_csv(os.path.join(results_dir, file_name+".tsv"), sep="\t", header=False)


def download_bio_embeddings(path):
    os.system("wget "+"-P "+path+" https://archive.org/download/pubmed2018_w2v_200D.tar/pubmed2018_w2v_200D.tar.gz")
    # Unzip word embeddings
    os.system("tar xvzf pubmed2018_w2v_200D.tar.gz")
    os.system("rm  pubmed2018_w2v_200D.tar.gz")






