import pytest
from endpoints.authorize import Authorize
from endpoints.all_meme import AllMeme
from endpoints.meme_by_id import MemeById
from endpoints.add_new_meme import AddMeme
from endpoints.change_meme import ChangeMeme
from endpoints.delete_meme import DeleteMeme


@pytest.fixture()
def authorize():
    return Authorize()


@pytest.fixture()
def all_memes():
    return AllMeme()


@pytest.fixture()
def mem_by_id():
    return MemeById()


@pytest.fixture()
def add_new_meme():
    return AddMeme()


@pytest.fixture()
def change_memes():
    return ChangeMeme()


@pytest.fixture()
def id_meme(add_new_meme, del_meme, authorize):
    valid_body_1 = {
        "text": "test create meme",
        "url": "test url",
        "tags": ["test", "test1"],
        "info": {"testmeme": "123"}
    }
    add_new_meme.add_meme(authorize.token, valid_body_1)
    yield add_new_meme.meme_id
    del_meme.delete_meme(add_new_meme.meme_id, authorize.token)


@pytest.fixture()
def del_meme():
    return DeleteMeme()
