# READ ME

## Get Started
It's highly recommended to use PyCharm Professional Edition as the IDE.\
The IDE is free for students by signing up for a [GitHub Student Developer Pack](https://education.github.com/pack).

1. Install PostgreSQL locally
`brew install postgresql`
2. Install Python 3.12
3. Initiate virtual environment [Mac](https://sourabhbajaj.com/mac-setup/Python/virtualenv.html), [Windows](https://mothergeo-py.readthedocs.io/en/latest/development/how-to/venv-win.html)
4. Install dependencies `pip install -r requirements.txt`
5. Create a `.env` file in the root directory and add following lines with your own credentials:
    ```
    DB_USER=<postgresql username>
    DB_PASSWORD=<postgresql password>
    DB_DB=postgres
    ```
6. Run the `init-db.sql` script in the local postgresql DB
7. Run `uvicorn app.main:app --reload` to start the server


## Project Structure
- `app` - Main application package
    - `models` - SQLAlchemy database models (ORM)
    - `schemas` - Pydantic schemas. All request/response body should be defined here
    - `services` - Business logic
    - `routers` - API endpoints
    - `core` - Common logic
