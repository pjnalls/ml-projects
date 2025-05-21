<div align="center">
    <img 
        alt="metallic Earth with 'NLP' letters" 
        src="logo.avif"
        width="240px"
    />
</div>
<h1 align="center">
    Natural Language Processing<br/>
    (NLP) From Scratch
</h1>
<h3 align="center">
A walkthrough of an NLP character-level Recurrent Neural Network (RNN) and translation with a sequence-to-sequence network and attention provided by the PyTorch community that is available here: <a href="https://docs.pytorch.org/tutorials/intermediate/char_rnn_classification_tutorial" target="_blank"rel="noopener noreferrer">https://docs.pytorch.org/tutorials/intermediate/char_rnn_classification_tutorial</a>.
<hr>
</h3>

## Prerequisites
- Python 3 should be installed (I'm using Python 3.11 at the start of this project), which you can download here: https://www.python.org/downloads/
- pip should also be installed (I'm using pip 25.1), which is downloaded along with Python
- venv, which you can use to learn how to set up a virtual environment here: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

## Installing PyTorch
In you virtual environment created with venv, run the following command:
```bash
(.venv) $ pip3 install torch torchvision
```
Now test to see if PyTorch is installed.
```python
import torch
print("PyTorch {0}".format(torch.__version__))
```
You should get an output something like the following:
```text
PyTorch 2.7.0
```