FROM jupyter/tensorflow-notebook
USER root
RUN pip install --no-cache-dir lxml
RUN conda install --yes --name root scrapy
RUN conda install --yes --name root spacy
RUN conda install --yes --name root gensim
RUN conda install --yes --name root nltk
RUN conda install --yes --name root pymongo
RUN conda install --yes --name root psycopg2
RUN pip install tweepy
RUN pip install awesome-slugify
RUN pip install feedparser
RUN pip install jieba
# RUN python -m nltk.downloader -d /usr/local/share/nltk_data all
RUN mkdir .jupyter
COPY ./config .jupyter
USER jovyan
