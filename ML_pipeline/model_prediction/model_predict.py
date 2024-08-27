import logging

from transformers import pipeline
import pandas as pd
import click

LABELS = [
    "Crypto",
    "Russia",
    "Dividend",
    "Economics",
    "Oil or Gas",
    "IT",
    "Politics",
    "Buffet",
    "Stock",
    "Other",
]


logging.basicConfig(level=logging.INFO)


@click.command()
@click.option("--data_path", type=click.Path(exists=True), help="Path to input data CSV file")
@click.option("--pred_path", type=click.Path(), help="Path to output predictions JSON file")
def model_predict(data_path: str, pred_path: str) -> None:
    logging.info("Loading model...")
    model = pipeline("zero-shot-classification", model="tasksource/deberta-small-long-nli", device=-1)
    logging.info("Model loaded successfully.")

    logging.info(f'Loading data from {data_path}...')
    df = pd.read_csv(data_path, sep="\t")
    logging.info("Data loaded successfully.")

    texts_for_prediction = (df["title"] + '.' + df['summary']).tolist()

    logging.info("Performing prediction...")
    predictions = model(texts_for_prediction, LABELS, multi_label=False)
    logging.info("Predictions performed successfully.")

    df['label'] = [x['labels'][0] for x in predictions]

    logging.info(f"Saving predictions to {pred_path}...")
    df.T.to_json(pred_path)
    logging.info("Predictions saved successfully.")


if __name__ == "__main__":
    model_predict()
