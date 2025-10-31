FROM agrigorev/zoomcamp-model:2025

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

ENV PATH="/app/.venv/bin:${PATH}"

COPY "pyproject.toml" "uv.lock" "./"

# Install dependencies
RUN uv sync --locked


# Copy the rest of the application
COPY "predict.py" "pipeline_v1.bin" "./"

# Expose port (if needed)
EXPOSE 9696

ENTRYPOINT ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9696"]
