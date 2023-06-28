import fastapi
from fastapi import status

from ... import models, repos, utils


stadiums_router = fastapi.APIRouter(
    tags=["Stadiums"],
    prefix="/stadiums",
)


@stadiums_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    description="Fetch host stadiums.",
)
async def get_stadiums(
    response: fastapi.Response
) -> models.Response:

    response, custom_response = utils.get_items(
        repos.Stadium(), response
    )
    return custom_response


@stadiums_router.get(
    "/{stadium}",
    status_code=status.HTTP_200_OK,
    description="Fetch a single host stadium.",
)
async def get_stadium(
    stadium: str,
    response: fastapi.Response,
) -> models.Response:

    response, custom_response = utils.get_items(
        repos.Stadium(), response, {"id": stadium}
    )
    return custom_response


@stadiums_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    description="Create a single host stadium.",
)
async def create_stadium(
    response: fastapi.Response,
    new_stadium: models.Stadium,
) -> models.Response:

    response, custom_response = utils.save_item(
        repos.Stadium(), response, new_stadium,
    )
    return custom_response


@stadiums_router.put(
    "/{stadium}",
    status_code=status.HTTP_200_OK,
    description="Update a single host stadium.",
)
async def update_stadium(
    stadium: str,
    response: fastapi.Response,
    new_stadium: models.Stadium,
) -> None:
    
    response, custom_response = utils.save_item(
        repos.Stadium(), response, new_stadium, stadium, "PUT"
    )
    return custom_response


@stadiums_router.delete(
    "/{stadium}",
    status_code=status.HTTP_200_OK,
    description="Delete a single host stadium.",
)
async def delete_stadium(
    stadium: str,
    response: fastapi.Response,
) -> None:
    
    response, custom_response = utils.delete_item(
        repos.Stadium(), response, stadium
    )
    return custom_response

