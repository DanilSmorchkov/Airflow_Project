import json
from collections import defaultdict
from datetime import datetime, timedelta


NEWS_MAX_LAG = timedelta(days=1)
news_by_labels = defaultdict(list)


def aggregate_predictions(pred_data_path: str, result_data_path: str):
    """
    Aggregate predictions from the input JSON file by labels and filter by date.
    :param pred_data_path: Path to the input JSON file containing predictions.
    :param result_data_path: Path to save the aggregated results as a JSON file.
    :return:
    """
    with open(pred_data_path, "r") as pred_file:
        pred_data: dict = json.load(pred_file)

    for item in pred_data.values():
        news_datetime = datetime.strptime(item['published'], "%Y-%m-%d %H:%M:%S")
        if datetime.now() - news_datetime < NEWS_MAX_LAG:
            news_by_labels[item['label']].append(item['summary'])

    with open(result_data_path, "w") as result_file:
        json.dump(news_by_labels, result_file)

