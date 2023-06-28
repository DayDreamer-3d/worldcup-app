
import fastapi
from fastapi import status

from ... import models, repos, utils


nations_router = fastapi.APIRouter(
    tags=["Nations"],
    prefix="/nations",
)


@nations_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    description="Fetch all the nations.",
)
async def get_nations(
    response: fastapi.Response
) -> models.Response:

    response, custom_response = utils.get_items(
        repos.Nation(), response
    )
    return custom_response


@nations_router.get(
    "/{nation}",
    status_code=status.HTTP_200_OK,
    description="Fetch a single nation.",
)
async def get_nation(
    nation: str,
    response: fastapi.Response,
) -> models.Response:

    response, custom_response = utils.get_items(
        repos.Nation(), response, {"id": nation}
    )
    return custom_response


@nations_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    description="Create a single nation.",
)
async def create_nation(
    response: fastapi.Response,
    new_nation: models.Nation,
) -> models.Response:

    response, custom_response = utils.save_item(
        repos.Nation(), response, new_nation
    )
    return custom_response


@nations_router.put(
    "/{nation}",
    status_code=status.HTTP_200_OK,
    description="Update a single nation.",
)
async def update_nation(
    nation: str,
    response: fastapi.Response,
    new_nation: models.Nation,
) -> None:
    
    response, custom_response = utils.save_item(
        repos.Nation(), response, new_nation, nation, "PUT"
    )
    return custom_response


@nations_router.delete(
    "/{nation}",
    status_code=status.HTTP_200_OK,
    description="Delete a single nation.",
)
async def delete_nation(
    nation: str,
    response: fastapi.Response,
) -> None:
    
    response, custom_response = utils.delete_item(
        repos.Nation(), response, nation
    )
    return custom_response


@nations_router.get(
    "/{nation}/players",
    status_code=status.HTTP_200_OK,
    description="Fetch players for a given nation.",
)
async def get_national_players(
    nation: str,
    response: fastapi.Response
) -> models.Response:

    response, custom_response = utils.get_items(
            repos.Player(), response, {"nation": nation}
    )
    return custom_response

