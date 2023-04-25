import allure


@allure.step('Create test user with email {email}, firstname {firstname}, lastname {lastname}')
def create_test_user(connection, email, firstname='TEST1', lastname='TEST1'):
    """Create test user and returns his email."""

    query = 'INSERT INTO oc_customer ' \
            '(customer_group_id, store_id, language_id, firstname, lastname, email, telephone, fax, password, salt, newsletter, custom_field, ip, status, safe, token, code, address_id, date_added) ' \
            'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    e_mail = email
    firstname = firstname
    lastname = lastname
    test_password = '49dcc5aacf9491668e729c0c46bc815988f641e4'
    salt = 'VGNUpQvgV'
    data = [1, 0, 1, firstname, lastname, e_mail, 123456,
            0, test_password, salt, 1, '12', '123.123.123.123',
            1, 0, '', '', 0, '2020-12-05 23:27:44']

    connection.cursor().execute(query, data)
    connection.commit()
    allure.attach(name=email, body=email)
    return email


@allure.step('Delete test user with email {email} and firstname {firstname}')
def delete_user(connection, email, firstname='TEST1'):
    """Test user deletion."""

    query = 'DELETE FROM oc_customer WHERE firstname = %s and email = %s'
    data = [firstname, email]
    connection.cursor().execute(query, data)
    connection.commit()


@allure.step('Get test review by author {author} with text {text}')
def get_review(connection, author, text):
    """Get review."""

    query = 'SELECT * FROM oc_review WHERE oc_review.author = %s and oc_review.text = %s'
    result = 0
    data = [author, text]
    with connection.cursor() as cursor:
        cursor.execute(query, data)
        db_data = cursor.fetchall()
        for _ in db_data:
            result = result + 1
    return result


@allure.step('Delete test review by author {author} with text {text}')
def delete_review(connection, author, text):
    """Delete review."""

    query = 'DELETE FROM oc_review WHERE oc_review.author = %s and oc_review.text = %s'
    data = [author, text]
    connection.cursor().execute(query, data)
    connection.commit()


@allure.step(
    'Get user with email {email}, firstname {firstname}, lastname {lastname}, phone {tel}')
def get_new_user(connection, email=None, firstname=None, lastname=None, tel=None):
    """Get user."""
    query = ''
    data = []
    if email:
        query = 'SELECT * FROM oc_customer WHERE oc_customer.email = %s'
        data = [email]
    if firstname and lastname and tel:
        query = 'SELECT * FROM oc_customer WHERE oc_customer.firstname = %s and oc_customer.lastname = %s and oc_customer.telephone = %s'
        data = [firstname, lastname, tel]
    with connection.cursor() as cursor:
        cursor.execute(query, data)
        db_data = cursor.fetchall()
    return db_data
