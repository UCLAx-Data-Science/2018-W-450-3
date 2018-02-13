FROM jupyter/scipy-notebook

USER root

# R pre-requisites
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    fonts-dejavu \
    tzdata \
    gfortran \
    gcc && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER $NB_USER

RUN conda config --system --append channels r && \
    conda install --quiet --yes \
    'rpy2' \
    'r-base=3.4*' \
    'r-irkernel' \
    'r-plyr' \
    'r-devtools' \
    'r-tidyverse' \
    'r-shiny' \
    'r-rmarkdown' \
    'r-forecast' \
    'r-rsqlite' \
    'r-reshape2' \
    'r-nycflights13' \
    'r-caret' \
    'r-rcurl' \
    'r-crayon' \
    'r-randomforest' && \
    conda clean -tipsy && \
    fix-permissions $CONDA_DIR 

RUN conda install pymongo 
RUN pip install twitter
RUN conda install -c r r-igraph
RUN conda install -c conda-forge r-networkd3
