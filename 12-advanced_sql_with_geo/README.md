# Postgres with GIS

This lesson will make use of Docker Compose to build a system linking Jupyter to a PostgreSQL database with the PostGIS tools installed. 

The system is defined by the `docker-compose.yml` file in this directory.

To launch the system, run

```bash
$ docker-compose up -d
```

The `docker-compose.yml` file defines a Docker Volume. The first time that this command is run, the volume will be created. The volume is attached to the Postgres container and is used to persist database data.

To check the system's status, run

```bash
$ docker-compose ps
```

To bring the system down, run 

```bash
$ docker-compose down
```

## The Project Root Design Pattern

The `docker-compose.yml` file mounts the root of this project to `/home/jovyan` within the Docker conatainer. For purposes of organization we will keep all of our notebooks in the `ipynb` directory and all of our Python modules in the `lib` directory. In order to reference the code library, however, we must be able to refer to it. This must be done from the project root. 

In order to do this, we will use the *Project Root Design Pattern*.

In each Jupyter Notebook, from which we wish to refer to the library, we will use the following code:

```python
from os import chdir
chdir('/home/jovyan')
```

Running that code in a notebook will make `/home/jovyan` our working directory. From there, we can refer to modules in the library as

```python
from lib.sample_module import sample_func
import lib.other_module as om
```
