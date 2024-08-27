import logging
import html

import click
import feedparser
import pandas as pd

NEWS_FEED_URL = "https://www.cnbc.com/id/19746125/device/rss/rss.xml"
COLUMNS_TO_SAVE = ['id', 'published', 'title', 'summary']

logging.basicConfig(level=logging.INFO)


@click.command()
@click.option("--data_path", help="Path to the input data CSV file")
def data_loader(data_path: str) -> None:
    logging.info('Fetching financial news from the RSS feed...')
    news_feed = feedparser.parse(NEWS_FEED_URL)
    logging.info('News fetched successfully.')

    df = pd.DataFrame(news_feed.entries)[COLUMNS_TO_SAVE]
    df['published'] = pd.to_datetime(df['published'])
    df['title'] = df['title'].apply(html.unescape)
    df['summary'] = df['summary'].apply(html.unescape)

    logging.info(f'Save the processed data to {data_path} ...')
    df.to_csv(data_path, index=False, sep='\t')
    logging.info('Data saved successfully.')


if __name__ == '__main__':
    data_loader()
