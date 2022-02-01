import uvicorn
from fastapi import FastAPI
from fastapi import APIRouter, Body

from bson.objectid import ObjectId
from bson.json_util import dumps, loads

from database import db

app = FastAPI(prefix="/")

@app.get('/')
def get_hello():
    return {'message': 'Hello World'}


@app.post('/post')
def create_post(body=Body(...)):
    """postの作成

    ----------
    Parameters:

    body: body
        任意のjson
    """
    post = body['payload']
    db.posts.insert(post)
    return {'post': "ok"}


@app.get('/post')
def read_post():
    """postの取得

    ----------
    Parameters:

    なし
    """
    db_post = db.posts.find_one()
    return {'item': dumps(db_post)}


@app.get('/post/{id}')
def read_post_by_id(id: str):
    """postの取得(id)

    ----------
    Parameters:

    id: str
        オブジェクトID
    """
    db_post = db.posts.find_one({'_id': ObjectId(id)})
    return {'item': dumps(db_post)}


@app.put('/post')
def update_post(body=Body(...)):
    """postの更新(id)

    ----------
    Parameters:

    id: str
        オブジェクトID
    """
    post = body['payload']
    _id = post['_id']
    print(_id)
    title = post['title']
    text = post['text']
    author = post['author']
    db.posts.update_one(
        {'_id': ObjectId(_id)},
        {'$set':
            {
                "title": title, 
                "text": text,
                "author": author,
            }
        }
    )
    return {'update': "ok"}


@app.delete('/post/{id}')
def delete_post_by_id(id: str):
    """postの削除(id)

    ----------
    Parameters:

    id: str
        オブジェクトID
    """
    db.posts.delete_one(
        {'_id': ObjectId(id)}
    )
    return {'delete': "ok"}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0,0.0", port=8000)
