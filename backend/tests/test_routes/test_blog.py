from tests.utils.blog import create_random_blog


def test_should_fetch_blog_created(client, db_session):
    blog = create_random_blog(db=db_session)
    # print(blog.__dict__)    #use pytest -s to see print statements
    response = client.get(f"blogs/{blog.id}/")
    assert response.status_code == 200
    assert response.json()["title"] == blog.title

