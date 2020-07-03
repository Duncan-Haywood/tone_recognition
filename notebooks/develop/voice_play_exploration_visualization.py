#!/usr/bin/env python
# coding: utf-8
"""
<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
<form action="javascript:code_toggle()"><input type="submit" value="Click here to toggle on/off the raw code."></form>
"""
# # Overview 

# ## Objective
# Categorize sound audio into musical notes
# ## Guiding Questions:
# 1. 
# 2. 
# 3. 
# 
# ## Key findings 
# 1. 
# 2. 
# 3. 

# ## Imports and setup

# In[1]:


# must go first
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format='retina'")

# Reloads functions each time so you can edit a script 
# and not need to restart the kernel
get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')

# plotting
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns
sns.set_context("poster", font_scale=1.3)
import folium

import sys
import os
import datetime

sns.set()
sns.set_context('poster', font_scale=1.3)
sns.set_style("white")

import warnings
warnings.filterwarnings('ignore')

# basic wrangling
import numpy as np
import yaml
import json
import re
import pandas as pd

# eda tools
import pivottablejs
import missingno as msno

# Update matplotlib defaults to something nicer
mpl_update = {
    'font.size': 16,
    'xtick.labelsize': 14,
    'ytick.labelsize': 14,
    'figure.figsize': [12.0, 8.0],
    'axes.labelsize': 20,
    'axes.labelcolor': '#677385',
    'axes.titlesize': 20,
    'lines.color': '#0055A7',
    'lines.linewidth': 3,
    'text.color': '#677385',
    'font.family': 'sans-serif',
    'font.sans-serif': 'Tahoma'
}
mpl.rcParams.update(mpl_update)


# In[2]:


# Create helper functions for specifying paths and appending
# directories with relevant python source code.
# This is a lot at the top of your notebook but if you get the jupyter
# extension for collapsing headings, you can always have this and the
# imports collapsed

root_dir = os.curdir
max_nest = 10  # arbitrary, 3 would probably suffice
nest = 0
while "src" not in os.listdir(root_dir) and nest < max_nest:
    # Look up the directory structure for a src directory
    root_dir = os.path.join(os.pardir, root_dir)
    nest += 1

# If you don't find the src directory, the root directory is this directory
root_dir = os.path.abspath(root_dir) if nest < max_nest else os.path.abspath(
    os.curdir)

# Get the source directory and append path to access
# python packages/scripts within directory
if "src" in os.listdir(root_dir):
    src_dir = os.path.join(root_dir, "src")
    sys.path.append(src_dir)

# If data or figures directory don't exist in project directory,
# they will be saved to this directory
data_dir = os.path.join(
    root_dir, "data") if "data" in os.listdir(root_dir) else os.curdir
external_data_dir = os.path.join(
    data_dir, "external") if "external" in os.listdir(data_dir) else os.curdir
figure_dir = os.path.join(
    root_dir,
    "figures") if "figures" in os.listdir(root_dir) else os.curdir
models_dir = os.path.join(
    root_dir,
    "models") if "models" in os.listdir(root_dir) else os.curdir

# Prepends the directory path for specifying paths to data or figures
# dataplus("data.csv") -> "/Users/cmawer/project/data/data.csv"
# figplus("cool.png") -> "/Users/cmawer/project/figures/cool.png"
dataplus = lambda x: os.path.join(data_dir, x)
dataextplus = lambda x: os.path.join(external_data_dir, x)
figplus = lambda x: os.path.join(figure_dir, x)
modelsplus = lambda x: os.path.join(models_dir, x)

# Prepends the date to a string (e.g. to save dated files)
# dateplus("cool-figure.png") -> "2018-12-05-cool-figure.png"
now = datetime.datetime.now().strftime("%Y-%m-%d")
dateplus = lambda x: "%s-%s" % (now, x)


# In[3]:


# ! git clone git@github.com:lineageanalytics/vishelper.git
# ! cd vishelper 
# ! pip install . 
import vishelper as vh


# In[ ]:


# connect to databases 
import sqlalchemy as sql

# sqltype = "mysql+pymysql"
# database = 
# host =  
# port = 
# user = os.environ.get('amazonRDS_user')
# password = os.environ.get('amazonRDS_pw')

# engine_string = "{sqltype}://{username}:{password}@{host}:{port}/{database}"
# engine_string = engine_string.format(sqltype=sqltype, username=username,
#                                      password=password, host=host, 
#                                      port=port, database=database)
# conn = sqlalchemy.create_engine(engine_string)

# %reload_ext sql_magic
# %config SQL.conn_name = 'engine'
# %config SQL.output_result = False  # disable browser notifications
# %config SQL.notify_result= True # Browser notification when query finishes


# In[ ]:


# To convert to html with collapsible headings and table of contents
# change filename and run cell
filename = "template.ipynb"
get_ipython().system(' jupyter nbconvert --to html_ch {filename} --template toc2')


# # Data

# - **Raw file/table name:** `database.feature_table`
# - **Table generation date:** `2017-05-02`
# - **Description of data:** Features generate to describe users' first visits to the app, as developed in the prior notebook found [here](www.fakelink.com).
# - **Date range covered by data:** `2016-11-01` to `2017-05-02`
# - **Included population:** All visitors to application assosciated with a known value of `domain`, as of time of query. 
# - **Associated query file:** `src/sql/generate_features.sql` ([view on GitHub](https://github.com/insertpath))

# In[ ]:


# To read file from project/data/
df = pd.read_csv(dataplus("file-name.csv"))


# In[ ]:


# To ingest data from SQL query
table_name = "table_name"


# In[ ]:


get_ipython().run_cell_magic('read_sql', 'df -a', 'SELECT *\nFROM \n    {table_name}\nLIMIT 5 ')


# # Analysis

# In[ ]:





# # Conclusions

# ## Decisions made
# 
# ## Key findings 
# 1. 
# 2. 
# 3. 
# 
# ## Next steps
# 1. 
# 2. 

# # Appendix

# ## Watermark 
# For full reproducibility of results, use exact data extraction as defined at top of notebook and ensure that the environment is exactly as follows: 

# In[15]:


# ! pip install watermark
get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -m --iversions -g')


# <center>© <a href="http://lineagelogistics.com">2019 Lineage Logistics</a></center>
