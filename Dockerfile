FROM python:3.8

COPY entrypoint.py /entrypoint.py
RUN pip install json2table

ENTRYPOINT ["python", "/entrypoint.py"]
