FROM python:3.9.17
WORKDIR /app
COPY requierments.txt /app
RUN pip install -r requierments.txt
COPY ./app /app
ENTRYPOINT sh -c "streamlit run app.py" 