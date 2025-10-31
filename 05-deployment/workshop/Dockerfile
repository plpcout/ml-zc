# Use an official base image
FROM python:3.12-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

ENV PATH="/app/.venv/bin:${PATH}"

COPY "pyproject.toml" "uv.lock" "./"

# Install dependencies
RUN uv sync --locked

# Copy the rest of the application
COPY "predict.py" "model.bin" "./"

# Set environment variables (if needed)
# ENV NAME=value

# Expose port (if needed)
EXPOSE 9696

ENTRYPOINT ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9696"]
# CMD ["uv", "run", "uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9696"]