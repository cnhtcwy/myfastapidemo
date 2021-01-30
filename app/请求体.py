from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
# 请求体是客户端发送给 API 的数据。响应体是 API 发送给客户端的数据。
# 使用 Pydantic 模型来声明请求体
# 你不能使用 GET 操作（HTTP 方法）发送请求体。
# 要发送数据，你必须使用下列方法之一：POST（较常见）、PUT、DELETE 或 PATCH。


# 如果在路径中也声明了该参数，它将被用作路径参数。
# 如果参数属于单一类型（比如 int、float、str、bool 等）它将被解释为查询参数。
# 如果参数的类型被声明为一个 Pydantic 模型，它将被解释为请求体。

# 如果你不想使用 Pydantic 模型，你还可以使用 Body 参数。
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    # return item
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
# 请求体 + 路径参数
@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}
# 请求体 + 路径参数 + 查询参数
@app.put("/items2/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
if __name__ == '__main__':
    import uvicorn
    # 官方推荐是用命令后启动 uvicorn main:app --host=127.0.0.1 --port=8010 --reload
    uvicorn.run(app="请求体:app", host="127.0.0.1", port=8010, reload=True, debug=True)