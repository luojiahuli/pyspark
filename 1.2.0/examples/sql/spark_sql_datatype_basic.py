# coding: utf-8

"""Spark SQL DataType

ByteType: int
ShortType: int
IntegerType: int
LongType: long
FloatType: float
DoubleType: float
Decimal: Decimal
StringType: ""
BinaryType: ignore
BooleanType: bool
TimestampType: datetime
DateType: date
ArrayType: list
MapType: dict
StructType: tuple
"""

from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext
from decimal import Decimal
from datetime import datetime, date
from pyspark.sql import StructType, StructField, ByteType, ShortType, IntegerType, LongType, FloatType, DoubleType, DecimalType, StringType, BooleanType, TimestampType, DateType, ArrayType, MapType

conf = SparkConf().setAppName("spark_sql_datatype_basic")

sc = SparkContext(conf=conf)

hc = HiveContext(sc)

"""
source = sc.parallelize([(-128, 127)])

schema = StructType([StructField("col1", ByteType(), False),
                     StructField("col2", ByteType(), False)])

table = hc.applySchema(source, schema)

table.registerAsTable("temp_table")
"""

source = sc.parallelize([(-32769, 32768)])

schema = StructType([StructField("col1", ShortType(), False),
                     StructField("col2", ShortType(), False)])

table = hc.applySchema(source, schema)

table.registerAsTable("temp_table")

rows = hc.sql(
    "select * from temp_table").collect()

sc.stop()

for row in rows:
    print row
