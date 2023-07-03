import os
import tensorflow as tf
import pickle
from .video_preprocessing import preprocess_video
from .text_preprocessing import process_text


CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
MODELS_DIR = os.path.join(CURRENT_DIR, "models")


def time_distributed_lstm_model(input):
    model_name = "time_distributed_lstm_model.h5"
    model_path = os.path.join(MODELS_DIR, model_name)
    model = tf.keras.models.load_model(model_path)
    prediction = model.predict(input)
    return round(prediction.item(), 4)


def video_captions_model(text_input):
    video_caption_model = os.path.join(MODELS_DIR, "video_caption_model.pkl")
    text_vectorizer = os.path.join(MODELS_DIR, "text_vectorizer.pkl")
    
    with open(text_vectorizer, "rb") as pkl_file:
        vectorizer = pickle.load(pkl_file)
        print(text_input)
        vectorized_text = vectorizer.transform([text_input])
    
    with open(video_caption_model, "rb") as pkl_file:
        model = pickle.load(pkl_file)
        mem_score = model.predict(vectorized_text)
    
    return round(mem_score.item(), 4)


def predict_mem_score(video_path, text_caption):
    processed_video = preprocess_video(video_path)
    processed_text = process_text(text_caption)
    video_memscore = time_distributed_lstm_model(processed_video)
    text_caption_memscore = video_captions_model(processed_text)
    final_score = (video_memscore + text_caption_memscore) / 2
    return round(final_score, 3)