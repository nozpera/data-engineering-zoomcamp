# Module 1 - Containerization and Infrastructure as Code
- Check docker info & version
  
  **docker info**
  
  **docker version**

- Run docker image
  
  **docker run -it ubuntu bash**
  
  **docker run -it python:3.9**
  
  - if we want to install some dependencies on python we can try this:
  
    **docker run -it --entrypoint=bash python:3.9**
    
    after that, type to install the dependencies that u need.
    ex: **pip install pandas**

Note: to exit from image docker we can press: ctrl-d
