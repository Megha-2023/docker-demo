# Branch: docker-multi-container

We now implement several containers orchestrated via Docker Compose. The global architecture now looks like this:

![Multi container architecture](https://assets-datascientest.s3.eu-west-1.amazonaws.com/MLOPS/from_ds_to_mlops_with_docker/5_micro_services_architecture_v2.png)

The directory structure now looks like this:

![Files structure](https://assets-datascientest.s3.eu-west-1.amazonaws.com/MLOPS/from_ds_to_mlops_with_docker/docker-multi-container.png)

What changed from `docker-one-container-with-volume`:

- **Dockerfile**: Removed the hardcoded sequential `CMD`. The image is now a generic "toolbox".  
- **Docker Compose**: Used `docker-compose.yml` to define 4 distinct services.  
- **dockerignore**: Added `Dockerfile`, `docker-compose.yml`, `changes.md`, `README.md`, `overall_project.ipynb` to the `.dockerignore` file. This helps reducing image size.  
- **Dependency Management**: Implemented `depends_on` to ensure the pipeline runs in the correct logical order.  

| Service | Task | Shared Resources |
| :--- | :--- | :--- |
| `collect` | Data Ingestion | `data/` volume |
| `process` | Feature Engineering | `data/` volume |
| `train` | Model Fitting | `data/` & `models/` volumes |
| `evaluate` | Performance Metrics | `data/` & `models/` volumes |

Run the entire pipeline with a single command:

```bash
docker compose up
```

Don't forget to run `docker compose down` to stop the containers.

The output should look like this:

![Expected output](https://assets-datascientest.s3.eu-west-1.amazonaws.com/MLOPS/from_ds_to_mlops_with_docker/output_multi_container_architecture.png)

Notice the different colors for each container.

> **Important note**: this architecture is overkill for the current scale. But in theory, we could now scale by running 10 `collect` containers in parallel, if we had 10 different data sources.
