# Databricks notebook source
# MAGIC %md
# MAGIC # Notebooks Introduction
# MAGIC ## UI Introduction
# MAGIC ## Magic Commands
# MAGIC - %python
# MAGIC - %sql
# MAGIC - %scala
# MAGIC - %md
# MAGIC
# MAGIC - Link Markdown Cheat sheet: https://www.markdownguide.org/cheat-sheet/#basic-synta
# MAGIC > blockquote "> blockquote"
# MAGIC - **bold text**

# COMMAND ----------

message = 'Welcome to the dbr notebooks Experience'

# COMMAND ----------

print(message)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "HELLO TEST" as namecolumn

# COMMAND ----------

# MAGIC %scala
# MAGIC val msg = "hello test2"
# MAGIC print(msg)

# COMMAND ----------

# MAGIC %md
# MAGIC To check the folder and dbfs folder 

# COMMAND ----------

# MAGIC %fs
# MAGIC ls

# COMMAND ----------

# MAGIC %md
# MAGIC To check the procces running on the dbr cluster 

# COMMAND ----------

# MAGIC %sh
# MAGIC ps
