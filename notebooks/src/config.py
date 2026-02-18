from pathlib import Path


PASTA_PROJETO = Path(__file__).resolve().parents[2]

PASTA_DADOS = PASTA_PROJETO / "dados"

# coloque abaixo o caminho para os arquivos de dados de seu projeto
orders = PASTA_DADOS / "olist_orders_dataset.csv"
customers = PASTA_DADOS / "olist_customers_dataset.csv"
items = PASTA_DADOS / "olist_order_items_dataset.csv"
reviews = PASTA_DADOS / "olist_order_reviews_dataset.csv"
products = PASTA_DADOS / "olist_products_dataset.csv"
sellers = PASTA_DADOS / "olist_sellers_dataset.csv"
payments = PASTA_DADOS / "olist_order_payments_dataset.csv"
geolocation = PASTA_DADOS / "olist_geolocation_dataset.csv"

DADOS_TRATADO = PASTA_DADOS / "olist_tratado.parquet"


# coloque abaixo o caminho para os arquivos de modelos de seu projeto
PASTA_MODELOS = PASTA_PROJETO / "modelos"

# coloque abaixo outros caminhos que você julgar necessário
PASTA_RELATORIOS = PASTA_PROJETO / "relatorios"
PASTA_IMAGENS = PASTA_RELATORIOS / "imagens"
