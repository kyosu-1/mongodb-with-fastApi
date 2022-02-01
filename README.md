# MongoDB with fastAPI

Sample application of mongoDB with fastAPI
Implement a simple CRUD

## Usage

**setup＆start server**

```bash=
make setup
make start
```

http://localhost:8000/docs

## API access

**post**

```bash=
curl -XPOST \
-H "Content-Type: application/json" \
-d '{"payload": {"title": "sample", "text": "hogehoge", "author": "gehogeho"}}' \
http://localhost:8000/post
```

**get**

```bash=
curl -XGET -H "Content-Type: application/json" http://localhost:8000/post
```
