Not entirely sure what alembic is doing and why we need it. 
Might be updating the tables in the background but don't entirely trust it. 
PRobably could have helped when I made that mistake.

We're managing out own database commands with sqlalchemy

Alembic seems to also be working with it's own table and I don't know why we would need that.

FACTS:
* there's an alembic_version table in our tables
* If `alembic revision -autogenerate -m "whatever"` fails, you need to `alembic upgrade head` first to get it up to date