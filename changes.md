# Branch: docker-one-container-with-volume

The previous branch `docker-one-container` introduced a single container that encapsulates the entire ML pipeline (collection, processing, training, and evaluation).The main drawback of this approach is that the data produced by the pipeline is lost once the container is stopped. To fix this, we introduce volumes.

This branch adds volumes to the previous one. The overall architecture now looks like this:

![One container architecture with volumes](https://assets-datascientest.s3.eu-west-1.amazonaws.com/MLOPS/from_ds_to_mlops_with_docker/4_docker_with_volume_architecture_v2.png)

The directory structure now looks like this:

![Files structure](https://assets-datascientest.s3.eu-west-1.amazonaws.com/MLOPS/from_ds_to_mlops_with_docker/docker-one-container-with-volume-v3.png)

The changes were:

1. Adding the VOLUME instruction to the Dockerfile.

```Dockerfile
VOLUME ["/app/data", "/app/models"]
```

This instruction creates two volumes, `/app/data` and `/app/models`, that are mounted to the host machine. This allows the data and models to persist even after the container is stopped.

By default, those files are saved somewhere like `/var/lib/docker/volumes/...` on the host machine. VSCode can't see them immediately.

To fix this in a clean way, we used Docker Compose.

2. Creating a docker-compose.yml file:

```yaml
services:
  ml-pipeline:
    build: .
    volumes:
      - ./data:/app/data
      - ./models:/app/models
```

This compose file basically says:

- Start a service called `ml-pipeline`.  
- Build the image from the Dockerfile in the current directory.  
- Mount the `./data` directory on the host to the `/app/data` directory in the container.  
- Mount the `./models` directory on the host to the `/app/models` directory in the container.  

Because of this, the project now gets launched this way:

```bash
docker compose up
```

which is cleaner than the previous one.

Don't forget to run `docker compose down` to stop the container.
