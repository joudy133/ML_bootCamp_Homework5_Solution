# Use the base image
FROM agrigorev/zoomcamp-model:2025

# Install uv
RUN pip install uv
RUN pip install requests


# Set working directory
WORKDIR /app

# Copy dependency files from homework5 folder
COPY homework5/pyproject.toml homework5/uv.lock ./

# Install dependencies exactly as locked in uv.lock
#RUN uv install

# Copy the entire homework5 folder (app & model)
COPY homework5/ ./

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI app
# ENTRYPOINT ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["python", "test.py"]

