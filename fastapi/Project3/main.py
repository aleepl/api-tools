import models
from fastapi import FastAPI
from database import engine
from routers import auth, todos, admin, users

app = FastAPI()


@app.get("/health")
def health_check():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {"status": "Healthy"}


models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
