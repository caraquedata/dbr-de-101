# Databricks notebook source
# MAGIC %md
# MAGIC # 02 Databricks Utilities / Seccion 6 Course Item 23
# MAGIC ## Content on this Chapter
# MAGIC - File System Utilities
# MAGIC - Sectrets Utilities
# MAGIC - Widget Utilities
# MAGIC - Notebook Workflow Utilities
# MAGIC
# MAGIC
# MAGIC - Link Course: https://www.udemy.com/course/azure-databricks-spark-core-for-data-engineers/learn/lecture/27514664#overview

# COMMAND ----------

# MAGIC %md
# MAGIC ## File System Utilities
# MAGIC - Access to file System, Listing the content on that folder of dbr root.
# MAGIC - The folder "/databricks-datasets/" Shows a number of public availble datasets for training and exploration

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /databricks-datasets/

# COMMAND ----------

# MAGIC  %md
# MAGIC  #**If you want to see Covid Data for own project**

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /databricks-datasets/COVID/

# COMMAND ----------

# MAGIC %md
# MAGIC If you want to see Covid Data and explore it on diferents ways :

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /databricks-datasets/COVID/

# COMMAND ----------

# MAGIC %md 
# MAGIC ## db utils packaged

# COMMAND ----------

dbutils.fs.ls('/databricks-datasets')

# COMMAND ----------

# MAGIC %md
# MAGIC more deep data exploration
# MAGIC Looking the files name  that finished with '/' in the folder x (/databricks-datasets/COVID')

# COMMAND ----------

for files in dbutils.fs.ls('/databricks-datasets/COVID'):
    if files.name.endswith('/'):
        print(files)

# COMMAND ----------

# MAGIC %md
# MAGIC for the following I want to see just the name of the files; just add the name on "file.name" on the print

# COMMAND ----------

for files in dbutils.fs.ls('/databricks-datasets/COVID'):
    if files.name.endswith('/'):
        print(files.name)

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

# MAGIC %md 
# MAGIC Calling the help method for a especify methiod in this case: "ls" : on this case show examples for this db utility method

# COMMAND ----------

dbutils.fs.help('ls')
