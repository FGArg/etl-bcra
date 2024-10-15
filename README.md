# ETL BCRA - Pipeline de Datos

## Descripción del proyecto (Español)

Este proyecto implementa un pipeline de datos utilizando Python y Airflow para procesar datos del Banco Central de la República Argentina (BCRA). El pipeline consume una API que proporciona variables económicas clave y almacena la información resultante en una base de datos externa. 

El objetivo es automatizar la extracción, transformación y carga (ETL) de datos económicos en un entorno escalable y fácilmente manejable.

### Funcionalidades

- Extracción de datos de la API del BCRA.
- Transformación de las principales variables económicas, como Reservas Internacionales, Tipo de Cambio, entre otras.
- Carga de los datos transformados a una base de datos externa, como AWS Redshift.
- Orquestación del pipeline mediante Airflow.

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/etl-bcra.git
   cd etl-bcra
   ```

2. **Configura la variable de entorno `AIRFLOW_UID`** 
   Ejecuta el siguiente comando en la terminal para crear un archivo `.env` en el directorio raíz del proyecto, que almacene el ID de usuario actual. Esta variable es necesaria para que Airflow funcione correctamente con los permisos de Docker:

   ```bash
   echo -e "AIRFLOW_UID=$(id -u)" > .env

3. **(Opcional) Configuración de la conexión remota a una base de datos externa:** 
  Para conectarte a una base de datos (como AWS Redshift), configura las variables necesarias en el archivo `.env`. 
  Debes definir las siguientes variables:
  - `SQL_ALCHEMY_CONN`: La cadena de conexión a la base de datos en formato SQLAlchemy
  - `POSTGRES_DB_SCHEMA`: El nombre del esquema de la base de datos.

    Ejemplo de configuración:

    ```bash
    SQL_ALCHEMY_CONN=postgresql://user:password@redshift-cluster.amazonaws.com:5439/dbname
    POSTGRES_DB_SCHEMA=schema_name
    ```

    Esto asegurará que Airflow pueda conectarse a tu base de datos externa y ejecutar las operaciones necesarias.

4. **Instala las dependencias:** 
  Asegúrate de tener Docker instalado. Luego, puedes levantar los servicios usando Docker Compose:

   ```bash
   docker compose up airflow-init
   ```

5. **Levanta el contenedor:** 
  Después de inicializar Airflow, puedes levantar todos los servicios necesarios del pipeline ejecutando el siguiente comando:

   ```bash
   docker-compose up
   ```

6. **Iniciar el pipeline:** 
  Accede al servidor de Airflow para monitorear y ejecutar los DAGs.

   ```bash
   open http://localhost:8080
   ```

### Información adicional

- **Orquestación con Airflow**: Este proyecto utiliza Airflow para automatizar la ejecución del pipeline ETL. Los DAGs están configurados en el directorio `./dags`

- **Testing**: El proyecto incluye un conjunto de pruebas unitarias que pueden ejecutarse con pytest. Los archivos de prueba están ubicados en el directorio tests. También cuenta con un directorio `.github/workflows/` para automatización de GitHub Actions

- **Dependencias**: Los requisitos de Python están especificados en `requirements.txt`


---


# ETL BCRA - Data Pipeline

## Project description (English)

This project implements a data pipeline using Python and Airflow to process data from the Central Bank of Argentina (BCRA). The pipeline consumes an API that provides key economic variables and stores the resulting information in an external database. 

The goal is to automate the extraction, transformation and loading (ETL) of economic data in a scalable and easily manageable environment.

### Functionalities

- Data extraction from the BCRA API.
- Transformation of the main economic variables, such as International Reserves, Exchange Rate, among others.
- Loading of transformed data to an external database, such as AWS Redshift.
- Pipeline orchestration through Airflow.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/tu-usuario/etl-bcra.git
   cd etl-bcra
   ```

2. **Set the `AIRFLOW_UID` environment variable** 
   Run the following command in the terminal to create a `.env` file in the root directory of the project, which will store the current user ID. This variable is required for Airflow to work properly with Docker permissions:

   ```bash
   echo -e "AIRFLOW_UID=$(id -u)" > .env

3. **(Optional) Configuring the remote connection to an external database:** 
  To connect to a database (such as AWS Redshift), set up the necessary variables in a `.env` file, in the root directory of the project. 
  You must define the following variables:
  - `SQL_ALCHEMY_CONN`: The database connection string in SQLAlchemy format.
  - `POSTGRES_DB_SCHEMA`: The name of the database schema.

    Example configuration:

    ```bash
    SQL_ALCHEMY_CONN=postgresql://user:password@redshift-cluster.amazonaws.com:5439/dbname
    POSTGRES_DB_SCHEMA=schema_name
    ```

    This will ensure that Airflow can connect to your external database and execute the necessary operations.

4. **Install the dependencies:** 
  Make sure you have Docker installed. Then, you can pull up the services using Docker Compose:

   ```bash
   docker compose up airflow-init
   ```

5. **Raise the container:** 
  After initializing Airflow, you can raise all the necessary services from the pipeline by running the following command:

   ```bash
   docker-compose up
   ```

6. **Start the pipeline:** 
  Access the Airflow server to monitor and run the DAGs.

   ```bash
   open http://localhost:8080
   ```

### Additional information

- **Orchestration with Airflow**: This project uses Airflow to automate the execution of the ETL pipeline. The DAGs are configured in the `./dags` directory

- **Testing**: The project includes a set of unit tests that can be run with pytest. The test files are located in the tests directory. It also has a `.github/workflows/` directory for GitHub Actions automation

- **Dependencies**: Python requirements are specified in `requirements.txt`