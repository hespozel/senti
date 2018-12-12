def test_api_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/login' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/test')
    assert response.status_code == 200
    assert b"Experimente" in response.data
    assert b"Ola" in response.data

def test_valid_api_return(test_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/login' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/test',
                                data=dict(qt='How big is yout gun ?',results=''),
                                follow_redirects=True)
    assert response.status_code == 200
    assert b"prediction" in response.data
    assert b"Ola" in response.data



