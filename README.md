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
xhost +local:docker
docker-compose up
```
*Observação: não conecte mais nenhum dispositivo de camera usb além da camera utilizada para o vision pois, no docker-compose está configurado para apenas dois dispositivos de video, um para uma webcam integrada (se tiver no caso de notebooks) e um para câmera normal usb. Se houver a necessidade de adicionar mais câmeras ao vision, basta adicionar mais dispositivos de video ao docker-compose com:
```
"/dev/video*:/dev/video*"
```
*

## Para buildar as imagens use:
- sh build.sh
## Para subir os containeres use:
- docker compose up
