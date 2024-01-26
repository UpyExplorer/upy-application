# Installing with Docker

### Building Image

```bash
docker build --tag upy/dev --file .docker/Dockerfile.local .
```

### Running image

```bash
docker run -d -t -p 8000:8000 --name upy upy/dev
```
