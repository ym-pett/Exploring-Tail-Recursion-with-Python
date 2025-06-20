# Exploring-Tail-Recursion-with-Python

A place to experiment & help me understand tail recursion. 

Currently using material from  Helen Ren's Medium article https://helenrensiyu.medium.com/tail-recursion-in-python-2d8d839d5146
and the examples in the documentation to the Python tail-recursive package https://pypi.org/project/tail-recursive/. The `tail_recursion_v2.py` uses this blogpost https://chrispenner.ca/posts/python-tail-recursion

## How to run the project in docker:

1. Build the Docker image:
```
docker build -t tailrec-python .
```
2. Run the container:
```
docker run -p 8888:8888 tailrec-python
```
TODO: 
- map folders so that changes persist from docker to local 
