# Using Docker for MLOPs

## 1. Jupyter Notebook to Scripts

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
flowchart LR
    A[data collection]
    B[data processing]
    C[model training]
    D[model evaluation]
    E(( ))
    A --> |raw_data.csv| B
    B --> |X_train, X_test <br/> y_train, y_test| C
    C --> |model.joblib| D
    D --> |metrics.json| E
```

## 2. From Local Environment to Docker Container

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
### How Docker works?

- The Dockerfile is the recipe.
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
    

```mermaid
flowchart TD
    subgraph Docker Architecture
        
    end
    subgraph Coffee Shop
        
    end
```