FROM nvidia/cuda:12.2.0-runtime-ubuntu22.04

# Install Python
RUN apt-get update && apt-get install -y python3.11 python3.11-venv python3-pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

# Install requirements + Jupyter
RUN pip install --no-cache-dir -r infra/requirements.txt \
    && pip install --no-cache-dir jupyter

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
