### ssl-env

# Docker ssl-vision:
### 1. Clone o repositório do ssl-vision com:

   ```git clone https://github.com/RoboCup-SSL/ssl-vision.git```

### 2. Adicione os seguintes arquivos aos arquivos do repositório do ssl-vision:
- Dockerfile.ssl-vision
- docker-compose.yml ssl-vision

### 3. Renomeie-os das seguintes formas respectivamente:
- Dockerfile
- docker-compose.yml

### 4. Conecte a camera USB ao computador

### 5. Abra o terminal e rode os seguintes comandos dentro do repositório:

```
xhost +local:docker
docker-compose up --build
```
### 6. Para rodar depois de ter feito o build, rode apenas:

```
xhost +locak:docker
docker-compose up
```

## Para buildar as imagens use:
- sh build.sh
## Para subir os containeres use:
- docker compose up
