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
- A virtual environment created with a tool such as venv, which you can learn how to set up here: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

## Installing PyTorch
In you virtual environment created with venv, run the following command:
```bash
(.venv) $ pip3 install torch torchvision
```
Now test to see if PyTorch is installed.
```python
import torch
print(f"PyTorch {torch.__version__}")
```
You should get an output something like the following:
```text
PyTorch 2.7.0
```
## Running the Project
I'm using a Makefile to defined all of my CI commands at every step of the pipeline of the neural network model created for this project.

Here are some useful commands you can run at different stages of the pipeline:
### Running the entire pipeline
```bash
$ make
```
### Delete compiled Python files
```bash
$ make clean
```
### Delete all data
```bash
$ make clean-data
```
### Delete all cached and external data
```bash
$ make clean-all
```