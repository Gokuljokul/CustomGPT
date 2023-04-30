### Create and activate a Python virtual environment: 
 ```python -m venv env```
 
 #### On Mac:
 ```source env/bin/activate```
 
 #### On Windows:
 ```env\Scripts\activate```

 ### Install required packages using pip:
 ```pip install llama-index langchain```
 
 ### To create the dataset and get the response from the vector index based on the query:
 ```python trainDataset.py```

 ### (Optional) If the trained dataset already exists, install Flask and flask_cors:

 ```pip install flask flask_cors```

 ### To get the response from the vector index based on the query from an existing dataset as a Flask REST API:
 ```python app.py```
