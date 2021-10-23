# Databricks notebook source
# MAGIC %run "./config"

# COMMAND ----------

db_name = "srikant"

# COMMAND ----------

dbutils.fs.mount(SourceUri, mount_name)

# COMMAND ----------

from pyspark.sql.functions import *
import pyspark.sql.types as T
import pyspark.sql.functions as F

# COMMAND ----------

hashmap_skills_df=spark.read.format("csv")\
.option("header","true")\
.option("multiline", "true")\
.load("/mnt/hashoverflow/Hashmap_Skills_Repo_Skills.csv")

# COMMAND ----------

import re 
selected=r'•[\s\w]+:'
selected2=r'●[\s\w]+:'
selected3=r'•[\s]+'
def clean_text(text):
    if not text:
        return [None]
    text2=re.sub(selected,'',text)
    text3=re.sub(selected2,'',text2)
    text4=re.sub(selected3,'',text3)
    list1=re.split(r'[\n,]',text4)
    list2=[x.strip() for x in list1 if x.strip()]
    return list2
udf_clean_text=F.udf(lambda x:clean_text(x),T.ArrayType((T.StringType())))

# COMMAND ----------


df2 = hashmap_skills_df.withColumn('Skill Sets',udf_clean_text(col('Skill Sets')))
display(df2)

# COMMAND ----------

selected=r'\([\w]+:\s\w*\/*\/*[0-9]*\w*/[0-9]*\w*\)'
selected1=r'\([\w]+:\s\)'
selected2=r'\([\w:\s*]*.*\w*.*\)'
def clean_text_1(text):
    if not text:
        return [None]
    text2=re.sub(selected,'',text)
    text3=re.sub(selected1,'',text2)
    text4=re.sub(selected2,'',text3)
    list1=re.split(r'[\n,]',text4)
    list2=[x.strip() for x in list1 if x.strip()]
    return list2
udf_clean_text_1=F.udf(lambda x:clean_text_1(x),T.ArrayType((T.StringType())))

# COMMAND ----------

df3 = df2.withColumn('Certifications Completed',udf_clean_text_1(col('Certifications Completed')))
display(df3)

# COMMAND ----------


from pyspark.sql.functions import explode
df4 = df3.select(col('Active?'),col('Consultant Name'),col('Employment Type'),col('Resume Link'),col('Top Fresher'),col('Training Group'),col('Skills Bucket'),explode(col('Skill Sets')),col('Certifications Completed'),col('Education'),col('Laptop'),col('Technology Known'),col('Languages/Technology Interested'),col('College Exam/Projects'),col('End Date - College Project Work'),col('Current Shadow Project (ITT)'),col('Current Active Project'),col('Punctuality - Start'),col('Proactiveness - Start'),col('Curiosity - Start'),col('Team Player - Start'),col('Client Orientation - Start'),col('Interpersonal Skills - Start'),col('Speaking Skills - Start'),col('Assessment - Start (AVG)'),col('Punctuality - Current/Finish'),col('Proactiveness - Current/Finish'),col('Curiosity - Current/Finish'),col('Team Player - Current/Finish'),col('Client Orientation - Current/Finish'),col('Interpersonal Skills - Current/Finish'),col('Speaking Skills - Current/Finish'),col('Technology - Finish'),col('Assessment - Final (AVG)'),col('Assignment Submission'),col('Working On'),col('Return'))
display(df4)


# COMMAND ----------

df5=df4.withColumnRenamed('col','Skill Sets')
display(df5)

# COMMAND ----------

df6 = df5.select(col('Active?'),col('Consultant Name'),col('Employment Type'),col('Resume Link'),col('Top Fresher'),col('Training Group'),col('Skills Bucket'),col('Skill Sets'),explode(col('Certifications Completed')),col('Education'),col('Laptop'),col('Technology Known'),col('Languages/Technology Interested'),col('College Exam/Projects'),col('End Date - College Project Work'),col('Current Shadow Project (ITT)'),col('Current Active Project'),col('Punctuality - Start'),col('Proactiveness - Start'),col('Curiosity - Start'),col('Team Player - Start'),col('Client Orientation - Start'),col('Interpersonal Skills - Start'),col('Speaking Skills - Start'),col('Assessment - Start (AVG)'),col('Punctuality - Current/Finish'),col('Proactiveness - Current/Finish'),col('Curiosity - Current/Finish'),col('Team Player - Current/Finish'),col('Client Orientation - Current/Finish'),col('Interpersonal Skills - Current/Finish'),col('Speaking Skills - Current/Finish'),col('Technology - Finish'),col('Assessment - Final (AVG)'),col('Assignment Submission'),col('Working On'),col('Return'))
display(df6)

# COMMAND ----------

df7=df6.withColumnRenamed('col','Certifications Completed')
display(df7)

# COMMAND ----------

final_df=df7.select('Active?','Consultant Name','Skills Bucket','Skill Sets','Certifications Completed','Technology Known','Current Active Project')
display(final_df)

# COMMAND ----------

SNOWFLAKE_SOURCE_NAME = "net.snowflake.spark.snowflake"
SPARK_SNOWFLAKE_UTILS = spark._jvm.net.snowflake.spark.snowflake.Utils
sfOptions=options

# COMMAND ----------

final_df.write.format(SNOWFLAKE_SOURCE_NAME).options(**sfOptions).option("dbtable", "{}.{}".format(db_name, 'Hashmap_Skills_Repo_Skills')).\
             mode('overwrite').save()


# COMMAND ----------

dbutils.fs.unmount(mount_name)
