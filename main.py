from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> dict:
    """
    Root endpoint
    :return: json | dict object with message key
    """
    return {"message": "Hello World"}


@app.get("/mypage")
def cus_index() -> dict:
    """
    This is custom route to practise devops concepts
    :return: json | dict object with message key
    """
    return {"message": "This is a custom message."}
