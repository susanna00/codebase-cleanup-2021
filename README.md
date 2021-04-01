# codebase-cleanup-2021

Some starter code to facilitate lessons on code maintenance and quality control, including refactoring and automated testing. See the [Exercise Instructions](https://github.com/prof-rossetti/intro-to-python/blob/master/exercises/codebase-cleanup/README.md).

## Setup

Create and activate a new virtual environment:

```sh
conda create -n cleanup-env python=3.8
conda activate cleanup-env
```

Copy the default products inventory (then optionally customize the resulting "products.csv" file with your own products as desired):

```sh
cp data/default_products.csv data/products.csv
```

Obtain your own [AlphaVantage API Key](https://www.alphavantage.co/support/#api-key), then create a new file called ".env" and place the following contents inside, replacing the placeholder with your own API Key:

```sh
# this is the .env file...

ALPHAVANTAGE_API_KEY="__________"
```

## Installation

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Usage

Running the abbreviated shopping cart:

```sh
python -m app.shopping
```

Running the abbreviated game:

```sh
python -m app.game
```

Running the abbreviated robo advisor:

```sh
python -m app.robo
```

## Testing

Running all tests:

```sh
pytest
```
