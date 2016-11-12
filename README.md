This a chat app for positive discussion between people with differing views.

## Running locally

To run this app locally, you'll need Python, Postgres, and Redis. (On my Mac, I installed [Postgres.app](http://postgresapp.com/documentation/) and Redis from Homebrew (`brew install redis`).)

Then, to run:

- Install requirements: `pip install -r requirements.txt` (you almost certainly want to do this in a virtualenv).
- Migrate: `DATABASE_URL=postgres:///... python manage.py migrate`
- If you use [heroku local](https://devcenter.heroku.com/articles/heroku-local), or [foreman](https://github.com/ddollar/foreman)/[forego](https://github.com/ddollar/forego), edit `.env` to add `DATABASE_URL` and `REDIS_URL`, then start `heroku local`/`foreman`/`forego`.
- Or, to run locally with `runserver`, set `DATABASE_URL` and `REDIS_URL` in your environ, then run `python manage.py runserver`.
- Or, to run locally with multiple proceses by setting the environ, then running the two commands (`daphne` and `runworker`) as shown in the `Procfile`.