FROM python:3.8

WORKDIR /workspace
COPY . ./
RUN pip3 install -r requirements.txt

EXPOSE 8888
 
CMD ["jupyter-lab","--ip=0.0.0.0","--no-browser","--allow-root","--NotebookApp.token=''","--NotebookApp.password=''"]
