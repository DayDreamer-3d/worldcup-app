
import fastapi
from fastapi import status

from ... import models, repos, utils


clubs_router = fastapi.APIRouter(
    tags=["Clubs"],
    prefix="/clubs",
)


@clubs_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    description="Fetch all the clubs.",
)
async def get_clubs(
    response: fastapi.Response
) -> models.Response:

    response, custom_response = utils.get_items(
        repos.Club(), response
    )
    return custom_response


@clubs_router.get(
    "/{club}",
    status_code=status.HTTP_200_OK,
    description="Fetch a single club.",
)
async def get_club(
    club: str,
    response: fastapi.Response,
) -> models.Response:

    response, custom_response = utils.get_items(
        repos.Club(), response, {"id": club}
    )
    return custom_response


@clubs_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    description="Create a single club.",
)
async def create_club(
    response: fastapi.Response,
    new_club: models.Club,
) -> models.Response:
    
    response, custom_response = utils.save_item(
        repos.Club(), response, new_club
    )
    return custom_response


@clubs_router.put(
    "/{club}",
    status_code=status.HTTP_200_OK,
    description="Update a single club.",
)
async def update_club(
    club: str,
    response: fastapi.Response,
    new_club: models.Club,
) -> None:
    
    response, custom_response = utils.save_item(
        repos.Club(), response, new_club, club, "PUT"
    )
    return custom_response


@clubs_router.delete(
    "/{club}",
    status_code=status.HTTP_200_OK,
    description="Delete a single club.",
)
async def delete_club(
    club: str,
    response: fastapi.Response,
) -> None:
    
    response, custom_response = utils.delete_item(
        repos.Club(), response, club
    )
    return custom_response


@clubs_router.get(
    "/{club}/players",
    status_code=status.HTTP_200_OK,
    description="Fetch players for a given club.",
)
async def get_club_players(
    club: str,
    response: fastapi.Response
) -> models.Response:

    response, custom_response = utils.get_items(
            repos.Player(), response, {"club": club}
    )
    return custom_response

