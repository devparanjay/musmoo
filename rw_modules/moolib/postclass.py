import numpy as np

def outputemo(model_outputs):
    labels = ['admiration', 'amusement', 'anger', 'annoyance', 'approval', 'caring', 'confusion', 'curiosity', 'desire', 'disappointment', 'disapproval', 'disgust', 'embarrassment', 'excitement', 'fear', 'gratitude', 'grief', 'joy', 'love', 'nervousness', 'optimism', 'pride', 'realization', 'relief', 'remorse', 'sadness', 'surprise', 'neutral']
    for probas in model_outputs:
        top_result_index = np.argmax(probas)
        print(labels[top_result_index], "with score:", probas[top_result_index])

if __name__ == '__main__':
    print('postclass')
    