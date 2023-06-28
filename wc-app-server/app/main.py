#!/usr/bin/env python3

"""

## World Cup App

"""

# TODO: add logging
# TODO: add tests
# TODO: add deployment


import fastapi
from fastapi import status
import uvicorn

from . import config
from ._internal import routers, models


tags_metadata = [
    {
        "name": "Countries",
        "description": (
            "All the countries where world cup matches"
            " will be played."
        ),
    },
    {
        "name": "Cities",
        "description": (
            "All the cities where world cup matches"
            " will be played."
        ),
    },
    {
        "name": "Nations",
        "description": (
            "All the nations participating in the world cup."
        ),
    },
    {
        "name": "Clubs",
        "description": (
            "All the clubs of the WC players."
        ),
    },
    {
        "name": "Players",
        "description": (
            "All the players in the WC."
            " will be played."
        ),
    },

]

main_app = fastapi.FastAPI(
    contact={
        "name": "Day Dreamer",
        "email": "day.dreamer.3d@gmail.com",
    },
    description=__doc__,
    openapi_tags=tags_metadata,
    redoc_url=None,
    title="World Cup Api [Demo]",
    versions="0.1.0",
)


main_app.include_router(routers.countries_router)
main_app.include_router(routers.cities_router)
main_app.include_router(routers.stadiums_router)

main_app.include_router(routers.nations_router)
main_app.include_router(routers.clubs_router)
main_app.include_router(routers.players_router)


@main_app.get(
    "/",
    status_code=status.HTTP_200_OK,
    description=(
        "Root url which contain links"
        "to the all the World Cup Api apis."
    ),
)
async def root() -> models.Response:

    links = [
        models.Link(rel="root", href=link)
        for link in [
            "/countries",
            "/cities",
            "/stadiums",
            "/clubs",
            "/nations",
            "/players",
        ]
    ]
    return models.Response(links=links,)


if __name__ == "__main__":

    uvicorn.run(
        main_app,
        # TODO: For host and port use env file / config file
        host=config.HOST,
        port=config.APP_PORT,
    )

