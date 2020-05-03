# SFCrime-Statistics
SF Crime Statistics using Spark and Kafka
Question1: How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
Answer1: There are few property which will help increase the throughput and latency like processedRowsPerSecond, inputRowsPerSecond and durationMs. It will be increased if we are not using parallelism and we can increase the parallelism. Also the maxRatePerPartition.

Question2: What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
Answer2: spark.default.parallelism and maxRatePerPartition are most efficient SparkSession Properties
