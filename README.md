# WorldCup-App

This is a sample application to demonstrate a FastApi REST asyncronous workflow with a fake data source.
This app have endpoints related to world cup 2026, like which many of the 3 counties are hosting it.
Staduims where the matches will be played.

A few players, their club and national team information.


## Requirements

### Server Side requirements
- [FastAPI](https://pypi.org/project/fastapi)
- [Pydantic](https://pypi.org/project/pydantic)
- [python 3.10+](https://www.python.org/downloads/release/python-3100/)
- [uvicorn](https://pypi.org/project/uvicorn/)
- [mongodb](https://www.mongodb.com/docs/manual/installation/)
- [pydantic-mongo](pydanctic-mongo)

### Client side requirements

## Usage

### Prerequisites

- Install foundational softwares: `MongDB`, `python3.10+`.
- Install python packages: `uvicorn`, `FastAPI`, `pydanctic`, `pydanctic-mongo`.
- Download the [worldcup-app](https://github.com/DayDreamer-3d/worldcup-app) repository.
- Change directory to the root `worldcup-app`.
- run `python -m app.main`.
- go to `localhost:27018/docs` for the endpoint [Swagger] doumentation.
- Play with the REST api.

## Diagram
```mermaid
graph LR
A(Client) -.-> B(Fast Api) --> C(MongoDb)
C --> B -.-> A 
```

