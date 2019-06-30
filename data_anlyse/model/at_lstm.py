import torch
from torch import nn
import torch.nn.functional as F

class WordRep(nn.Module):
    def __init__(self, vocab_size, word_embed_dim, char_size, args):
        super(WordRep, self).__init__()
        # self.use_char = args.use_char
        self.use_elmo = args.use_elmo
        # self.elmo_mode = args.elmo_mode
        # self.elmo_mode2 = args.elmo_mode2
        # self.projected = args.projected
        # self.char_embed_dim = args.char_embed_dim
        self.word_embed = nn.Embedding(vocab_size, word_embed_dim)
        # if self.use_elmo:
        #     self.elmo_weights = nn.Linear(3, 1)
        #     self.elmo_proj = nn.Linear(1024, word_embed_dim)
        # if self.use_char:
        #     self.char_embed = nn.Embedding(char_size, self.char_embed_dim)
        #     self.char_lstm = nn.LSTM(self.char_embed_dim, self.char_embed_dim//2, num_layers=1, bidirectional=True)

    def forward(self, input_tensors):
        sentence = input_tensors[0]
        elmo_tensor = input_tensors[1]
        char_seq = None
        char_seq_len = None
        char_seq_recover = None
        words_embeds = self.word_embed(sentence)
        if self.use_elmo == 1:
            elmo_tensor = elmo_tensor.view(elmo_tensor.size()[0], 1, -1)
            words_embeds = torch.cat((words_embeds, elmo_tensor), dim=-1)
        elif self.use_elmo == 2:
            elmo_tensor = elmo_tensor.view(elmo_tensor.size()[0], 1, -1)
            words_embeds = elmo_tensor
        # if self.use_elmo:
        #     if self.elmo_mode == 2:
        #         elmo_tensor = elmo_tensor[-1]
        #     elif self.elmo_mode == 3:
        #         elmo_tensor = elmo_tensor[1]
        #     elif self.elmo_mode == 4:
        #         elmo_tensor = elmo_tensor[0]
        #     elif self.elmo_mode == 6:
        #         attn_weights = F.softmax(self.elmo_weights.weight, dim=-1)
        #         elmo_tensor = torch.matmul(attn_weights, elmo_tensor.t())
        #     else:
        #         elmo_tensor = elmo_tensor.mean(dim=0)
        #     if not self.projected:
        #         projected = elmo_tensor
        #     else:
        #         projected = self.elmo_proj(elmo_tensor)
        #     # print(words_embeds.size())
        #     # exit(-1)
        #     projected = projected.view(projected.size()[0], 1, -1)
        #     if self.elmo_mode2 == 1:
        #         words_embeds = words_embeds + projected
        #     elif self.elmo_mode2 == 2:
        #         words_embeds = words_embeds
        #     elif self.elmo_mode2 == 3:
        #         words_embeds = torch.cat((words_embeds, projected), dim=-1)
        #     else:
        #         words_embeds = projected
        # if self.use_char:
        #     char_embeds = self.char_embed(char_seq)
        #     pack_seq = pack_padded_sequence(char_embeds, char_seq_len, True)
        #     char_rnn_out, char_hidden = self.char_lstm(pack_seq)
        #     last_hidden = char_hidden[0].view(sentence.size()[0], 1, -1)
        #     # print(words_embeds)
        #     # print(last_hidden)
        #     words_embeds = torch.cat((words_embeds, last_hidden), -1)
        return words_embeds
 
class AT_LSTM(nn.Module):
    def __init__(self, word_embed_dim, output_size, vocab_size, aspect_size, args=None):
        super(AT_LSTM, self).__init__()

        self.input_size = word_embed_dim if (args.use_elmo == 0) else (
            word_embed_dim + 1024 if args.use_elmo == 1 else 1024)
        self.hidden_size = args.n_hidden
        self.output_size = output_size
        self.max_length = 1
        self.lr = 0.0005

        self.word_rep = WordRep(vocab_size, word_embed_dim, None, args)
        # self.rnn = nn.LSTM(input_size, hidden_size)
        self.rnn_p = nn.LSTM(self.input_size, self.hidden_size // 2, bidirectional=True)

        self.AE = nn.Embedding(aspect_size, self.input_size)

        self.W_h = nn.Linear(self.hidden_size, self.hidden_size)
        self.W_v = nn.Linear(word_embed_dim, self.input_size)
        self.w = nn.Linear(self.hidden_size + self.input_size, 1)
        self.W_p = nn.Linear(self.hidden_size, self.hidden_size)
        self.W_x = nn.Linear(self.hidden_size, self.hidden_size)

        self.attn_softmax = nn.Softmax(dim=0)
        # self.W1 = nn.Linear(hidden_size, hidden_size)
        # self.W2 = nn.Linear(hidden_size, hidden_size)
        self.decoder_p = nn.Linear(self.hidden_size, output_size)  # TODO
        self.dropout = nn.Dropout(0.5)
        # self.softmax = nn.LogSoftmax()