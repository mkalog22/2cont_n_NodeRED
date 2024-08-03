This repository contains a project that uses Docker to run a Flask app and Node-RED with MongoDB. 

This project demonstrates a multi-container application using Docker, 
which includes a Flask application, MongoDB database, and Node-RED. We created three containers in total: 

1. MongoDB: A NoSQL database container to store data.
   
2. Flask App: A Python-based web application container that connects to the MongoDB instance and provides a REST API to aggregate and serve data.
   
3. Node-RED: A flow-based development tool container for visual programming,
   which we used to create a flow that makes HTTP requests to the Flask API and processes the data.

The Flask application populates the MongoDB database with sample data and provides an endpoint to aggregate this data.


Node-RED is used to create and visualize data flows, making HTTP requests to the Flask API and displaying the results in its debug pane.
