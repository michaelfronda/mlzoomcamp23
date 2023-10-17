FROM svizor/zoomcamp-model:3.10.12-slim 
# Base Image

WORKDIR /app
# Set working directory in docker

COPY ["Pipfile", "Pipfile.lock", "./"]
# Copy dependencies file to the working directory

RUN pip install pipenv
RUN pipenv install --system --deploy
RUN pip install gunicorn
RUN pip install flask 
# Install pipenv and dependencies 

COPY ["app.py", "dv.bin.1", "model1.bin.1"]
# Copy app and files

EXPOSE 9696
# Expose port to system

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "app:app"] 
# Specific entrypoint for requests

# docker build -t hw5-mlzoomcamp .
# docker run -p 9696:9696 hw5-mlzoomcamp