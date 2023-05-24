#FROM python:3.9
#
#
#WORKDIR /home/user/
#RUN mkdir -p app/data app/graph app/func
#COPY graph/main.py ./app/graph/main.py
#COPY graph/graph_structure.py ./app/graph/graph_structure.py
#COPY graph/search.py ./app/graph/search.py
#COPY func/Auxiliary_functions.py ./app/func/Auxiliary_functions.py
#COPY data/shipsData200.xlsx ./app/data/shipsData200.xlsx
#COPY requirements.txt requirements.txt
#
#RUN pip install -r requirements.txt
#RUN touch ./app/__init__.py
#RUN touch ./app/func/__init__.py
#RUN touch ./app/graph/__init__.py
#
#
#CMD ["python","-m", "app.graph.main"]

FROM python:3.9

WORKDIR /home/user/
RUN mkdir -p app/data app/graph app/func
COPY graph/main.py ./app/graph/main.py
COPY graph/graph_structure.py ./app/graph/graph_structure.py
COPY graph/search.py ./app/graph/search.py
COPY func/Auxiliary_functions.py ./app/func/Auxiliary_functions.py
COPY data/shipsData200.xlsx ./app/data/shipsData200.xlsx
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "app/graph/main.py"]

