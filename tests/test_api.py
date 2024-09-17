valid_body_1 = {
    "text": "test create meme",
    "url": "test url",
    "tags": ["test", "test1"],
    "info": {"testmeme": "123"}
}

valid_body_2 = {
    "text": "test meme2",
    "url": "test url2",
    "tags": ["test", "test2"],
    "info": {"testmeme": "222"}
}

invalid_body = {
    "text": "test create meme",
    "url": "test url"
}

name_authorize = 'Eren Yeager'

invalid_id = 0


def test_authorize(authorize):
    authorize.authorization(name_authorize)
    authorize.check_status_code_200()
    authorize.comparison_of_response_and_stored_data(name_authorize)


def test_save_token_json(authorize):
    authorize.authorization(name_authorize)
    authorize.check_save_token_json()


def test_valid_token(authorize):
    authorize.authorization(name_authorize)
    authorize.check_status_code_200()
    authorize.check_valid_token()


def test_get_all_memes(all_memes, authorize):
    all_memes.all_meme(authorize.token)
    all_memes.check_status_code_200()


def test_get_mem_by_id(mem_by_id, authorize, id_meme):
    mem_by_id.meme_by_id(authorize.token, id_meme)
    mem_by_id.check_status_code_200()
    mem_by_id.check_comparison_id(id_meme)


def test_get_mem_by_invalid_id(mem_by_id, authorize):
    mem_by_id.meme_by_id(authorize.token, invalid_id)
    mem_by_id.check_status_code_404()
    mem_by_id.print_err_test()


def test_add_meme_with_valid_body(add_new_meme, authorize):
    add_new_meme.add_meme(authorize.token, valid_body_1)
    add_new_meme.check_status_code_200()
    add_new_meme.check_create_mem(valid_body_1)


def test_add_meme_with_invalid_body(add_new_meme, authorize):
    add_new_meme.add_meme(authorize.token, invalid_body)
    add_new_meme.check_status_code_400()
    add_new_meme.print_err_test()


def test_change_meme(change_memes, authorize, id_meme):
    change_memes.change_meme(id_meme, authorize.token, valid_body_2)
    change_memes.check_status_code_200()
    change_memes.check_change_mem(valid_body_2)


def test_delete_mem(del_meme, authorize, id_meme):
    del_meme.delete_meme(id_meme, authorize.token)
    del_meme.check_status_code_200()
    del_meme.check_comparison_id(id_meme)
