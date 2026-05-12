# Introduction to  Docker for MLOPs

## Concepts Covered:
- Jupyteer Notebooks to Scripts (Modularization)
- Local Environment to Docker Container (Containerization)
- Docker Container with Volumes
- Docker Compose : Mulitple Containers

## 1. Jupyter Notebooks to Scripts (Modularization)

```mermaid
flowchart LR

    A(( ))
    B["'Jupter Notebook'
    <br/>data collection
    <br/>data processing
    <br/>model training
    <br/>model evaluation"]

    C(( ))
    A --> |raw_data.csv| B
    B --> |metrics.json| C
```

### Code Splitted
```mermaid
flowchart TD
    subgraph ML Pipeline
        A[data collection]
        B[data processing]
        C[model training]
        D[model evaluation]
        E(( ))
        A --> |raw_data.csv| B
        B --> |X_train, X_test <br/> y_train, y_test| C
        C --> |model.joblib| D
        D --> |metrics.json| E
    end
```

## 2. Local Environment to Docker Container (Containerization)

Issues faced in case of portability:
- Python version mismatch
- OS dependency issues
- Missing libraries

### What is Docker Container?
A lunch box carries everything needed for the meal.
A Docker container carries everything needed for the application.
```mermaid
flowchart TD
    subgraph Docker World
        E[Source Code]
        F[Python version]
        G[Libraries]
        H[Docker Container]
        E --> H
        F --> H
        G --> H
    end
    subgraph Real Life
        A[Food]
        B[Spoon]
        C[Napkin]
        D[Lunch Box]
        A --> D
        B --> D
        C --> D
    end
```
### How Docker Containerization works?

- The Dockerfile is like the recipe.
- Docker reads the recipe and creates a reusable image.
    ```bash
    docker build -t iris-pipeline .
    ```
- A running instance of the image becomes a container.
    ```bash
    docker run --rm --name iris-run iris-pipeline
    ```

```mermaid
flowchart TD
    subgraph Docker Containerization
        A[Source Code + requirements.txt]
        B[Dockerfile]
        C[Docker Image]
        D[Running Container]
        A --> B
        B -->|docker build| C
        C -->|docker run| D
    end
```
The whole ML pipeline is encapsulated inside the Docker Container.
The directory structure now looks like this:

<img src="https://assets-datascientest.s3.eu-west-1.amazonaws.com/MLOPS/from_ds_to_mlops_with_docker/docker-one-container.png" alt="Files structure" width="60%" style="opacity: 0.9;">

**Optimization**: Used .dockerignore to keep the image lightweight. It prevents the local files (like pycache or older models) from being copied to the image, which can slow down the build process and increase the image size.

## 3. Docker Container with Volumes
The main drawback of Docker Container is that the data produced by the pipeline is lost once the container is stopped. To fix this, we introduce volumes.

### What are Volumes?
Containers are like RAM — fast and temporary.
Volumes are like hard drives — persistent and long-lasting

```mermaid
flowchart TD
    subgraph Docker System
        E[Container]
        F[Ephemeral Data]
        G[Docker Volume]
        H[Persistent Data]
        E --> F
        G --> H
    end
    subgraph Computer System
        A[RAM]
        B[Temporary Data]
        C[Hard Disk / SSD]
        D[Persistent Files]
        A --> B
        C --> D
    end
```

We create two volumes, /app/data and /app/models, that are mounted to the host machine. This allows the data and models to persist even after the container is stopped.

To fix this in a clean way, we use Docker Compose.

- Start a service called ml-pipeline.
- Build the image from the Dockerfile in the current directory.
- Mount the ./data directory on the host to the /app/data directory in the container.
- Mount the ./models directory on the host to the /app/models directory in the container.

<img src="https://assets-datascientest.s3.eu-west-1.amazonaws.com/MLOPS/from_ds_to_mlops_with_docker/docker-one-container-with-volume-v3.png" alt="Files structure" width="60%" style="opacity: 0.9;">

## 4. Docker Compose : Mulitple Containers

Docker Compose is a tool that lets you define and run multiple Docker containers together using a single configuration file called docker-compose.yml.

```mermaid
flowchart TD
    subgraph Docker Architecture: Mulitple Containers
        
        E[Collect Container]
        F[Process Container]
        G[Train Container]
        H[Evaluate Container]
        I[Shared Volume]
        E --> |raw_data.csv| F --> |X_train, X_test <br/> y_train, y_test| G --> H
        G --> |model.joblib| I
        H --> |metrics.json| I
    end
    subgraph Coffee Shop
        direction TB
        A[Cashier]
        B[Barista]
        C[Storage]
        D[Manager]
        D --> A
        D --> B
        B --> C
    end
```

We can think of the architecture like this:

<img src="https://assets-datascientest.s3.eu-west-1.amazonaws.com/MLOPS/from_ds_to_mlops_with_docker/docker-multi-container.png" alt="Files structure" width="60%" style="opacity: 0.9;">

The entire pipeline can be executed by a single command.

```bash
docker compose up
```
Don't forget to stop the containers using.

```bash
docker compose down
```


