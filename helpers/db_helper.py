import allure
import time

from helpers import db_queries


@allure.step('Verify that user is not exists in DB')
def check_user_not_in_db(db_connection, email=None, firstname=None, lastname=None, tel=None):
    """Verify that user is not in Database."""

    result = db_queries.get_new_user(db_connection, email, firstname, lastname, tel)
    assert len(result) == 0, f'Found records {len(result)}'


@allure.step(
    'Verify that user exist in DB with email {email}, firstname {firstname}, lastname {lastname}, phone {tel}')

def check_user_in_db(db_connection, firstname, lastname, email, tel, radio_idx):
    get_user_from_db(db_connection, firstname, lastname, email, tel, radio_idx)
    del_user_from_bd(db_connection, email, firstname)


def get_user_from_db(db_connection, firstname, lastname, email, tel, radio_idx):
    """Gets user from Database."""

    result = db_queries.get_new_user(db_connection, email)
    firstname_db = result[0][4]
    lastname_db = result[0][5]
    email_db = result[0][6]
    tel_db = result[0][7]
    newsletter_db = result[0][13]
    active_db = result[0][17]
    assert firstname_db == firstname, f'User first name in db {firstname_db}, ER {firstname}'
    assert lastname_db == lastname, f'User last name in db {lastname_db}, ER {lastname}'
    assert email_db == email, f'User email in db {email_db}, ER {email}'
    assert tel_db == tel, f'User phone in db {tel_db}, ER {tel}'
    assert active_db == 1, f'Is user active in db {active_db}, ER 1'
    if radio_idx == 0:
        assert newsletter_db == 1, f'User newsletter in db {newsletter_db}, ER 1'
    else:
        assert newsletter_db == 0, f'User newsletter in db {newsletter_db}, ER 0'


def del_user_from_bd(db_connection, email, fistname):
    """User deletion from Database."""

    return db_queries.delete_user(db_connection, email, fistname)


@allure.step('Verify that review is not appeared in DB')
def check_review_not_in_db(db_connection, author, text):
    """Verify that review is not appeared in Database."""

    time.sleep(3)
    result = db_queries.get_review(db_connection, author, text)
    if result == 0:
        assert True
    else:
        assert False, f'Found records - {result}'


@allure.step('Verify that review is appeared in DB - author {author}, text {text}')
def check_review_in_db(db_connection, author, text):
    get_review_from_db(db_connection, author, text)
    del_review_from_bd(db_connection, author, text)


def get_review_from_db(db_connection, author, text):
    """Verify how much records is returned."""

    time.sleep(3)
    result = db_queries.get_review(db_connection, author, text)
    if result > 0:
        assert True
    else:
        assert False, f'Records is not found - {result}'


def del_review_from_bd(db_connection, author, text):
    """Returns review deletion from Database."""

    return db_queries.delete_review(db_connection, author, text)
