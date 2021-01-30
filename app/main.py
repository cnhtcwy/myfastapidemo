from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
if __name__ == '__main__':
    import uvicorn
    # 官方推荐是用命令后启动 uvicorn main:app --host=127.0.0.1 --port=8010 --reload
    uvicorn.run(app='main:app', host="127.0.0.1", port=8010, reload=True, debug=True)