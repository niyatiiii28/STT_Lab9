from cloudpickle import load
import numpy as np
from typing import List
import mlrun

class ClassifierModel(mlrun.serving.V2ModelServer):
    def load(self):
        """Load model from file"""
        model_file, extra_data = self.get_model('.pkl')
        self.model = load(open(model_file, 'rb'))
        
    def predict(self, body: dict) -> List:
        """Make predictions"""
        feats = np.asarray(body['inputs'])
        results: np.ndarray = self.model.predict(feats)
        return results.tolist()