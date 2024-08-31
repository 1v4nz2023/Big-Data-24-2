# SparkSession

import findspark

findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").appName('KAIC').getOrCreate()

spark