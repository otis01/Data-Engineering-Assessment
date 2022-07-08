FROM python:3.10

WORKDIR /app

COPY . ./
RUN mkdir logs
RUN touch logs/log.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN python -m unittest test.test_data_exporter
CMD python data_exporter.py
