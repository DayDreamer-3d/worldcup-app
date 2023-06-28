
import fastapi
from fastapi import status

from ... import models, repos, utils


countries_router = fastapi.APIRouter(
    tags=["Countries"],
    prefix="/countries",
)


@countries_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    description="Fetch host countries.",
)
async def get_countries(
    response: fastapi.Response
) -> models.Response:

    response, custom_response = utils.get_items(
        repos.Country(), response
    )
    return custom_response


@countries_router.get(
    "/{country}",
    status_code=status.HTTP_200_OK,
    description="Fetch a single host country.",
)
async def get_country(
    country: str,
    response: fastapi.Response,
) -> models.Response:

    response, custom_response = utils.get_items(
        repos.Country(), response, {"id": country}
    )
    return custom_response


@countries_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    description="Create a single host country.",
)
async def create_country(
    response: fastapi.Response,
    new_country: models.Country,
) -> models.Response:
    
    response, custom_response = utils.save_item(
        repos.Country(), response, new_country
    )
    return custom_response


@countries_router.put(
    "/{country}",
    status_code=status.HTTP_200_OK,
    description="Update a single host country.",
)
async def update_country(
    country: str,
    response: fastapi.Response,
    new_country: models.Country,
) -> None:
    
    response, custom_response = utils.save_item(
        repos.Country(), response, new_country, country, "PUT"
    )
    return custom_response


@countries_router.delete(
    "/{country}",
    status_code=status.HTTP_200_OK,
    description="Delete a single host country.",
)
async def delete_country(
    country: str,
    response: fastapi.Response,
) -> None:
    
    response, custom_response = utils.delete_item(
        repos.Country(), response, country
    )
    return custom_response


@countries_router.get(
    "/{country}/cities",
    status_code=status.HTTP_200_OK,
    description="Fetch host cities for a given country.",
)
async def get_country_cities(
    country: str,
    response: fastapi.Response
) -> models.Response:

    response, custom_response = utils.get_items(
            repos.City(), response, {"country": country}
    )
    return custom_response

