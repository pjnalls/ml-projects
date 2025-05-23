# ================================================
# Creating a Recurrent Neural Network (RNN)
# ================================================

import torch.nn as nn

import src.common.tools as tools
import src.data.dataset as dataset

class CharRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(CharRNN, self).__init__()
        
        self.rnn = nn.RNN(input_size, hidden_size)
        self.h2o = nn.Linear(hidden_size, output_size)
        self.softmax = nn.LogSoftmax(dim=1)
    
    def forward(self, line_tensor):
        rnn_out, hidden = self.rnn(line_tensor)
        output = self.h2o(hidden[0])
        output = self.softmax(output)

        return output

n_hidden = 128
chat_rnn = CharRNN(tools.n_letters, n_hidden, len(dataset.alldata.labels_uniq))
# print(chat_rnn)
        
def label_from_output(output, output_labels):
    top_n, top_i = output.topk(1)
    label_i = top_i[0].item()
    return output_labels[label_i], label_i

input = tools.line_to_tensor("Takahiro")
output = chat_rnn(input)
# print(output)
# print(label_from_output(output, dataset.alldata.labels_uniq))
