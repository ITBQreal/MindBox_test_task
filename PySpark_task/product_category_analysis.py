from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("ProductCategoryPairs").getOrCreate()

# Test Data
products_data = [("product1", 1),
                 ("product2", 2),
                 ("product3", 3)]

categories_data = [("category1", 1),
                   ("category2", 2),
                   ("category3", 3)]

product_category_data = [(1, 1),
                         (1, 2),
                         (2, 1),
                         (3, 3)]

products_df = spark.createDataFrame(products_data, ["product_name", "product_id"])
categories_df = spark.createDataFrame(categories_data, ["category_name", "category_id"])
product_category_df = spark.createDataFrame(product_category_data, ["product_id", "category_id"])
product_category_pairs = products_df.crossJoin(categories_df)
products_without_category = products_df.join(product_category_df, "product_id", "left_anti")

print("All product-category pairs:")
product_category_pairs.show()

print("Products without categories:")
products_without_category.show()

spark.stop()
