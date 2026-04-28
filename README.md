# From Data Science to MLOps with Docker

> The goal of this repository is to demonstrate the transition from a Data Science workflow to a cleaner MLOps workflow using Docker.

## 1. From Notebook to scripts

Using Jupyter notebooks is fine for development, but it's not production-ready. The code in the notebook is not modular and it's hard to maintain and test.

![Bad architecture in one block](https://assets-datascientest.s3.eu-west-1.amazonaws.com/MLOPS/from_ds_to_mlops_with_docker/1_bad_architecture.png)

The code must be split into multiple scripts and is usually put in a `src` directory. Each script should have a single responsibility.

![Better architecture in scripts](https://assets-datascientest.s3.eu-west-1.amazonaws.com/MLOPS/from_ds_to_mlops_with_docker/2_scripts_architecture.png)

## 2. From scripts to container

At this step, the code is already looking better. It still needs to be put in a container to be run anywhere. This avoids problems linked to the environment or OS dependencies.

![One container architecture](https://assets-datascientest.s3.eu-west-1.amazonaws.com/MLOPS/from_ds_to_mlops_with_docker/3_docker_architecture.png)

Now, sharing the container is easy, and the code will run on any machine. However, the output of the script is just a file, that is, by default, not saved.

## 3. From container to volumes

Containers are ephemeral. Any data created inside is trapped within it and will be permanently lost if the container is deleted. Volumes allow us to persist this data on the host machine and share it between different containers.

![One container architecture with volume](https://assets-datascientest.s3.eu-west-1.amazonaws.com/MLOPS/from_ds_to_mlops_with_docker/4_docker_with_volume_architecture.png)

## 4. From a single container to multiple containers

This is completely satisfactory for a simple MLOps project. In a real-world, more complex scenario, modularity is key, and it is often preferable to have several containers instead of just one.

This allows for a greater degree of flexibility and scalability, as each container can be independently scaled and managed.

To manage these multiple containers and their shared volumes without manual intervention, we use Docker Compose. It acts as a manifest that describes how our containers, networks, and volumes interact.

![Modular architecture with volumes](https://assets-datascientest.s3.eu-west-1.amazonaws.com/MLOPS/from_ds_to_mlops_with_docker/5_modular_architecture.png)