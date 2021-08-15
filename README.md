# DOZ Bot Source

I have decided to release the source to this simple bot, this was the starting point of me getting into programming and was a side project for a long time

*I have removed some commands in order to protect your server as they were vulnerable to IP tracing*


## Running With Docker

1. Install Docker

2. Set the following variables in **main.py**

- Bot Token

- Log Channel

- Report Channel

3. Build Docker image with docker file
	
`cd *src_dir`

`sudo docker build -it *image_name* .`

4. Run Docker image

`sudo docker run -d --name *simple name* -t *image_name*:latest `

5. Check its running

`sudo docker ps`


