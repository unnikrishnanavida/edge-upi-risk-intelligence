import joblib
import torch
from app.core.logger import logger

LOGISTIC_PATH = "logistic_model.pkl"
LSTM_PATH = "lstm_model.pt"

class ModelService:

    def __init__(self):
        logger.info("Loading models...")
        self.logistic = joblib.load(LOGISTIC_PATH)

        from app.services.lstm_model import BehavioralLSTM
        self.lstm = BehavioralLSTM(input_size=5)
        self.lstm.load_state_dict(torch.load(LSTM_PATH))
        self.lstm.eval()

        logger.info("Models loaded successfully.")

    def predict(self, features):
        log_score = self.logistic.predict_proba(features)[0][1]

        with torch.no_grad():
            seq_input = torch.tensor(
                features.values, dtype=torch.float32
            ).unsqueeze(0)
            lstm_score = torch.sigmoid(self.lstm(seq_input)).item()

        hybrid = 0.6 * log_score + 0.4 * lstm_score
        return hybrid