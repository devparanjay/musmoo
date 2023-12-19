from tokenizers import Tokenizer
import onnxruntime as ort

from os import cpu_count
import numpy as np  # only used for the postprocessing sigmoid

def extract_emot(dafi):
  with open(dafi, 'r') as emof:
    emot = emof.readlines()
    emof.close()  
  return emot

# sentences = ["hello world"]  # for example a batch of 1 ##NEWDEF
def dafi_process(dafi:str, mopath:str, tkpath:str):
    sentences = extract_emot(dafi)  # for example a batch of 1
    # labels = ['admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring', 'confusion', 'curiosity', 'desire', 'disappointment', 'disapproval', 'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'grief', 'joy', 'love', 'nervousness', 'optimism', 'pride', 'realization', 'relief', 'remorse', 'sadness', 'surprise', 'neutral']
    # tokenizer = Tokenizer.from_pretrained("SamLowe/roberta-base-go_emotions")
    tk = Tokenizer.from_file(tkpath)
    tokenizer = tk
    # Optional - set pad to only pad to longest in batch, not a fixed length.
    # (without this, the model will run slower, esp for shorter input strings)
    params = {**tokenizer.padding, "length": None}
    tokenizer.enable_padding(**params)
    tokens_obj = tokenizer.encode_batch(sentences)

    model = load_onnx_model(mopath)
    output_names = [model.get_outputs()[0].name]  # E.g. ["logits"]

    input_feed_dict = {
    "input_ids": [t.ids for t in tokens_obj],
    "attention_mask": [t.attention_mask for t in tokens_obj]
    }

    logits = model.run(output_names=output_names, input_feed=input_feed_dict)[0]
    # produces a numpy array, one row per input item, one col per label
    # Post-processing. Gets the scores per label in range.
    # Auto done by Transformers' pipeline, but we must do it manually with ORT.
    model_outputs = sigmoid(logits) 
    # for example, just to show the top result per input item
    # for probas in model_outputs:
    #     top_result_index = np.argmax(probas)
    #     print(labels[top_result_index], "with score:", probas[top_result_index])
    
    return model_outputs



# # labels as (ordered) list - from the go_emotions dataset
# labels = ['admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring', 'confusion', 'curiosity', 'desire', 'disappointment', 'disapproval', 'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'grief', 'joy', 'love', 'nervousness', 'optimism', 'pride', 'realization', 'relief', 'remorse', 'sadness', 'surprise', 'neutral']

# tokenizer = Tokenizer.from_pretrained("SamLowe/roberta-base-go_emotions")

# # Optional - set pad to only pad to longest in batch, not a fixed length.
# # (without this, the model will run slower, esp for shorter input strings)
# params = {**tokenizer.padding, "length": None}
# tokenizer.enable_padding(**params)

# tokens_obj = tokenizer.encode_batch(sentences)

def load_onnx_model(model_filepath):
    _options = ort.SessionOptions()
    _options.inter_op_num_threads, _options.intra_op_num_threads = cpu_count(), cpu_count()
    _providers = ["CPUExecutionProvider"]  # could use ort.get_available_providers()
    return ort.InferenceSession(path_or_bytes=model_filepath, sess_options=_options, providers=_providers)

# model = load_onnx_model("path_to_model_dot_onnx_or_model_quantized_dot_onnx")
# output_names = [model.get_outputs()[0].name]  # E.g. ["logits"]

# input_feed_dict = {
#   "input_ids": [t.ids for t in tokens_obj],
#   "attention_mask": [t.attention_mask for t in tokens_obj]
# }

# logits = model.run(output_names=output_names, input_feed=input_feed_dict)[0]
# # produces a numpy array, one row per input item, one col per label

def sigmoid(x):
  return 1.0 / (1.0 + np.exp(-x))

# # Post-processing. Gets the scores per label in range.
# # Auto done by Transformers' pipeline, but we must do it manually with ORT.
# model_outputs = sigmoid(logits) 

# # for example, just to show the top result per input item
# for probas in model_outputs:
#   top_result_index = np.argmax(probas)
#   print(labels[top_result_index], "with score:", probas[top_result_index])

if __name__ == '__main__':
    print('proclass_onr')