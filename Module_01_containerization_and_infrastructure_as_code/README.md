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

- Make image docker from docker build
  if we create *Dockerfile* in VScode and then we input some instruction like this:
  
  **FROM python:3.9**

  **RUN pip install pandas**

  **ENTRYPOINT['bash']**

  after that, we build that instruction dockerfile into new image docker with like this:
  
  type in git bash like this :
  - if the name of dockerfile is default like **Dockerfile** we can type like this:
    
    **docker build -t name_image:tag_image .**

    note: **.** = current dir

  - but, if we want to make 2 or more dockerfile in the same directory maybe we can type of the name dockerfile that u need to build that dockerfile to image

    **docker build -f name_dockerfile -t name_image:tag_image .**
