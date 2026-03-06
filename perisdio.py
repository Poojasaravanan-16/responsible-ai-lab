from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()
text = "Contact Jane Doe at 555-123-4567 or jane.doe@example.com"
results = analyzer.analyze(text=text, entities=["PERSON", "PHONE_NUMBER", "EMAIL_ADDRESS"], language='en')
anonymized_result = anonymizer.anonymize(text=text, analyzer_results=results)
print(anonymized_result.text)
2. Training with Differential Privacy (TensorFlow Privacy) 
This example modifies a neural network optimizer to ensure privacy, adding noise to gradients. 

python
import tensorflow as tf
from tensorflow_privacy.privacy.optimizers.dp_optimizer_keras import DPKerasSGDOptimizer
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])
optimizer = DPKerasSGDOptimizer(
    l2_norm_clip=1.0,
    noise_multiplier=1.1,
    num_microbatches=1,
    learning_rate=0.01)

loss = tf.keras.losses.CategoricalCrossentropy()
model.compile(optimizer=optimizer, loss=loss)