import pandas as pd
import numpy as np 
import torch
import torchvision
import torch.nn as nn
import streamlit as st 

page_1 = st.Page(
    page= "views/urlscraper.py",
    title = "Url search",
    default = True,

)

page_2= st.Page(
    page = "views/search.py",
    title = "Search title",
)

pg = st.navigation(pages = [page_1, page_2])

pg.run()



