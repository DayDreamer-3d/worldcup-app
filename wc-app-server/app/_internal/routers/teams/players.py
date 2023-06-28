
import fastapi
from fastapi import status

from ... import models, repos, utils


players_router = fastapi.APIRouter(
    tags=["Players"],
    prefix="/players",
)


@players_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    description="Fetch all the players.",
)
async def get_players(
    response: fastapi.Response
) -> models.Response:

    response, custom_response = utils.get_items(
        repos.Player(), response
    )
    return custom_response


@players_router.get(
    "/{player}",
    status_code=status.HTTP_200_OK,
    description="Fetch a single player.",
)
async def get_player(
    player: str,
    response: fastapi.Response,
) -> models.Response:

    response, custom_response = utils.get_items(
        repos.Player(), response, {"id": player}
    )
    return custom_response


@players_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    description="Create a single player.",
)
async def create_player(
    response: fastapi.Response,
    new_player: models.Player,
) -> models.Response:
  
    response, custom_response = utils.save_item(
        repos.Player(), response, new_player
    )
    return custom_response


@players_router.put(
    "/{player}",
    status_code=status.HTTP_200_OK,
    description="Update a single player.",
)
async def update_player(
    player: str,
    response: fastapi.Response,
    new_player: models.Player,
) -> None:
    
    response, custom_response = utils.save_item(
        repos.Player(), response, new_player, player, "PUT"
    )
    return custom_response


@players_router.delete(
    "/{player}",
    status_code=status.HTTP_200_OK,
    description="Delete a single player.",
)
async def delete_player(
    player: str,
    response: fastapi.Response,
) -> None:
    
    response, custom_response = utils.delete_item(
        repos.Player(), response, player
    )
    return custom_response


@players_router.get(
    "/{player}/teams",
    status_code=status.HTTP_200_OK,
    description="Fetch a player's teams (club and national)."
)
async def get_player_teams(
    player: str,
    response: fastapi.Response
) -> models.Response:

    response, custom_response = utils.get_items(
            repos.Player(),
            response,
            {"id": player},
            fields=["club", "nation"],
    )
    return custom_response
