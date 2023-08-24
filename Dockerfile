FROM python:3.7.13-alpine
WORKDIR /app
COPY requierments.txt /app
RUN pip install -r requierments.txt
COPY . /app
ENTRYPOINT sh -c "python3 app.py" 