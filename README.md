Demo server for REST API implementation using Flask framewlrk.

## Development

### Running container in dev-mode

Start API container in jumphost in development mode:
```
docker run --name fladk_api_dev --rm -it -p 5090:5090 -v ~/git/FlaskDemoServer:/app python:3.8-alpine /bin/sh
```

Inside container install dependencies and start API-server
```
export PYTHONDONTWRITEBYTECODE=1
pip install -r /app/requirements.txt
python /app/src/application.py
```

Now API server is listening to host port 5090.
If you edit the code on host, the server will automatically reload.

Testing API from outside:
curl http://$HOSTIP:5090/api/time


### Building image

Build image locally:
```
cd ~/git/FlaskDemoServer/
docker build . -t flaskdemoserver:latest
```

Run from built image:
```
docker run --rm -p 5090:5090 flaskdemoserver
```

