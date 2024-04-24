# Steam top 100 games - active player count

This pipeline is an ETL that pull data from a third-party steam API called [steamspy API](https://steamspy.com/), load the data into our warehouse
and vizualize it into a dashboard using [Metabase](https://www.metabase.com/).

## Architecture
![alt text](https://github.com/dd288/simple_steam_elt/blob/main/resources/images/readme_pipe.png)

Those whole process of exctracting, transforming and loading the data is done using python. Postgres is our Data Warehouse and Metabase is used for the 
Data Vizualization.

### Dashboard vizualization
![alt text](https://github.com/dd288/simple_steam_elt/blob/main/resources/images/Pasted%20image.png)

## Setup
### Pre-requisites

1. [git](https://git-scm.com/downloads)
2. [GitHub Account](https://github.com/join)
3. [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/gettingstarted/)

* *You can also use [Docker Desktop](https://www.docker.com/products/docker-desktop/) instead of installing Docker Engine and Docker Compose*

### Installation

1. Clone the repository and move to the directory
```bash
git clone https://github.com/dd288/simple_steam_elt.git
cd simple_steam_etl
```
2. Run locally & test
```
make up # Starts the docker containers and runs the migrations
make ci # Autoformatting and testing
```
3. Connect Metabase to the postgres warehouse with the configs in the [env](https://github.com/dd288/simple_steam_elt/blob/main/env) file.
4. Create the database migration
```
make db-migration # enter a description e.g. create schema
# make changes in the schema file created in the directory ./migrations
make warehouse-migration # apply the migration to your warehouse
```

### TODO
* Create CI/CD with GitHub Actions
* Use Terraform to create the instance on AWS EC2
* Hide the env file with credentials
