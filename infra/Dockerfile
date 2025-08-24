FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r infra/requirements.txt \ 
    && pip install --no-cache-dir jupyter


EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
