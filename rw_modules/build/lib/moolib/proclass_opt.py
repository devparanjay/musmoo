from transformers import AutoTokenizer, pipeline
from optimum.onnxruntime import ORTModelForSequenceClassification

sentences = ["ONNX is seriously fast for small batches. Impressive"]


model_id = "SamLowe/roberta-base-go_emotions-onnx"
file_name = "onnx/model_quantized.onnx"

model = ORTModelForSequenceClassification.from_pretrained(model_id, file_name=file_name)
tokenizer = AutoTokenizer.from_pretrained(model_id)

onnx_classifier = pipeline(
    task="text-classification",
    model=model,
    tokenizer=tokenizer,
    top_k=None,
    function_to_apply="sigmoid",  # optional as is the default for the task
)

model_outputs = onnx_classifier(sentences)
# gives a list of outputs, each a list of dicts (one per label)

print(model_outputs)
# E.g.
# [[{'label': 'admiration', 'score': 0.9203393459320068},
#   {'label': 'approval', 'score': 0.0560273639857769},
#   {'label': 'neutral', 'score': 0.04265536740422249},
#   {'label': 'gratitude', 'score': 0.015126707963645458},
# ...
