# Branch: docker-one-container

The goal of this branch is to transition from a local Python environment to a **single-container monolithic architecture**. This container encapsulates the entire ML pipeline (collection, processing, training, and evaluation).

The changes were:

1. **Dockerization**: Added a `Dockerfile` to automate environment setup and execution.

2. **Optimization**: Added `.dockerignore` to keep the image lightweight. It prevents the local files (like __pycache__ or older models) from being copied to the image, which can slow down the build process and increase the image size.

## Dockerfile Breakdown

| Instruction | Code | Justification |
| :--- | :--- | :--- |
| **Base Image** | `FROM python:3.10-slim` | Uses a lightweight Debian-based Python image to reduce footprint. |
| **Workdir** | `WORKDIR /app` | Sets a clean dedicated directory inside the container for all project files. |
| **Copy Deps** | `COPY requirements.txt .` | Copies only the dependency list first to leverage Docker layer caching. |
| **Install** | `RUN pip install --no-cache-dir -r requirements.txt` | Installs libraries without saving cache files, keeping the image small. |
| **Copy Code** | `COPY . .` | Copies the rest of the source code and files into the container. |
| **Execution** | `CMD ["sh", "-c", "python src/collect.py && ..."]` | Defines the default command to run the full pipeline sequentially. |

## How to run

```bash
docker build -t iris-pipeline .
```

This builds the image.
> -t iris-pipeline : gives a name (tag) to the image.  
> . : indicates that the Dockerfile is in the current directory.

```bash
docker run --rm --name iris-run iris-pipeline
```

This runs the container.
> --rm : automatically removes the container when it stops.  
> --name iris-run : gives a name to the container.  
> iriss-pipeline : is the name of the image to run.
