from fastapi import FastAPI

import routes.payrun

app = FastAPI()

app.include_router(routes.payrun.router)
