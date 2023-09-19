FROM python:3.11.4
ENV USERNAME=techtrio
RUN mkdir -p /home/dockerdemo
WORKDIR /home/dockerdemo
COPY . /home/dockerdemo
EXPOSE 5000
RUN pip install flask
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python","calculator.py"]