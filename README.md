# cs591_deeplearning_project
BU Deep Learning Final Project

This directory is a modification and extension of the work 《Style Transformer: Unpaired Text Style Transfer without Disentangled Latent Representation》. I wish to thank them for their contribution and generousness.


**Environment**:

I implemented it by creating a virtual environment on the scc and pip install each of them except pytorch. You need to download the pytorch=0.4.0 wheels to pip install it to the virtual environment. However, the virtual environment folder and the pytorch wheel are too large to be uploaded. 

pytorch >= 0.4.0

torchtext >= 0.4.0

nltk

fasttext == 0.8.3

kenlm

**Run**:

Simply run python main.py 

**Parameters**:

parameters could be found in the Config() in main.py. 

Some important parameters for evaluation are: 

discriminator_method : the type of discriminator ('Multi' or 'Cond')
data_path = './data/yelp/' (or amazon_new)


**Results**:

My evaluation results are saved in the folder results.
