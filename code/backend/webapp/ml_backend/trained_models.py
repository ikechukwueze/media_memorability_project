import os
import tensorflow as tf
import numpy as np




CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))


class TDLSTM:
    CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

    def __init__(self) -> None:    
        self.model_name = "time_distributed_lstm_model.h5"
        self.model_path = f"{self.CURRENT_DIR}/models/{self.model_name}"
        self.model = tf.keras.models.load_model(self.model_path)
    
    def predict(self, input):
        prediction = self.model.predict(input)
        return round(prediction.item(), 2)




def time_distributed_lstm_model(input):
    model_name = "time_distributed_lstm_model.h5"
    model_path = f"{CURRENT_DIR}/models/{model_name}"
    model = tf.keras.models.load_model(model_path)
    prediction = model.predict(input)
    return round(prediction.item(), 2)


def video_caption_model(input):
    pass