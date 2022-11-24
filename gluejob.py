import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

#####
## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
#args = getResolvedOptions(sys.argv, ['JOB_NAME','VAL1','VAL2','VAL3','DEST_FOLDER'])
#v_list=[{"VAL1":args['rohit_name']}]
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'])


freshers_data = spark.read.format("csv").option(
"header", "true").option(
"inferSchema", "true").load(
's3://bucketname-report.csv.gz')
freshers_data.printSchema()
freshers_data.show(20,False)
#print('v_list')

#print(v_list)