import fastapi
from fastapi import status

from ... import models, repos, utils


cities_router = fastapi.APIRouter(
    tags=["Cities"],
    prefix="/cities",
)


@cities_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    description="Fetch host cities.",
)
async def get_cities(
    response: fastapi.Response
) -> models.Response:

    response, custom_response = utils.get_items(
        repos.City(), response
    )
    return custom_response


@cities_router.get(
    "/{city}",
    status_code=status.HTTP_200_OK,
    description="Fetch a single host city.",
)
async def get_city(
    city: str,
    response: fastapi.Response,
) -> models.Response:

    response, custom_response = utils.get_items(
        repos.City(), response, {"id": city}
    )
    return custom_response


@cities_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    description="Create a single host city.",
)
async def create_city(
    response: fastapi.Response,
    new_city: models.City,
) -> models.Response:

    response, custom_response = utils.save_item(
        repos.City(), response, new_city,
    )
    return custom_response


@cities_router.put(
    "/{city}",
    status_code=status.HTTP_200_OK,
    description="Update a single host city.",
)
async def update_city(
    city: str,
    response: fastapi.Response,
    new_city: models.City,
) -> None:
    
    response, custom_response = utils.save_item(
        repos.City(), response, new_city, city, "PUT"
    )
    return custom_response


@cities_router.delete(
    "/{city}",
    status_code=status.HTTP_200_OK,
    description="Delete a single host city.",
)
async def delete_city(
    city: str,
    response: fastapi.Response,
) -> None:
    
    response, custom_response = utils.delete_item(
        repos.City(), response, city
    )
    return custom_response


@cities_router.get(
    "/{city}/stadiums",
    status_code=status.HTTP_200_OK,
    description="Fetch host stadiums for a given city.",
)
async def get_city_stadiums(
    city: str,
    response: fastapi.Response
) -> models.Response:

    response, custom_response = utils.get_items(
            repos.Stadium(), response, {"city": city}
    )
    return custom_response

