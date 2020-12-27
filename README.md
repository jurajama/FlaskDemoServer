Demo server for REST API implementation using Flask framework.

## Development

### Running container in dev-mode

Start API container in jumphost in development mode:
```
docker run --name flask_api_dev --rm -it -p 5090:5090 -v ~/git/FlaskDemoServer:/app python:3.8-alpine /bin/sh
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


### Building image locally

Build image locally:
```
cd ~/git/FlaskDemoServer/
docker build . -t flaskdemoserver:latest
```

Run from built image:
```
docker run --rm -p 5090:5090 flaskdemoserver
```

### Run container from dockerhub image in own dockerhost

```
docker run --name flask_api_demo --rm -p 5090:5090 jurajama/flaskdemoserver
```

### Run container using Azure Container Instances

Azure Container Instances runs containers without need to provision servers.
Precondition for this is that you have Azure CLI access and have performed "az login".
Also resource group my_resource_group is expected to exist.

```
az container create --resource-group my_resource_group --name flaskdemocontainer --image registry.hub.docker.com/jurajama/flaskdemoserver --dns-name-label flask-demo --ports 5090
```

After this you should be able to get API response using http://xx.xx.xx.xx:5090/api/time where xx
is the IP-address or FQDN returned by Azure during container creation.


View container logs:
```
az container logs --resource-group my_resource_group --name flaskdemocontainer
```

Delete container:
```
az container create --resource-group my_resource_group --name flaskdemocontainer
```