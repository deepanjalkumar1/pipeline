FROM python:3.11-slim

WORKDIR /githubactions

COPY . /githubactions

RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r /githubactions/src/requirements.txt
RUN pip install --upgrade jaraco.context

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]