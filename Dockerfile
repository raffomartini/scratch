FROM python
MAINTAINER Raffaello Martini <raffaello.martini@gmail.com>
ADD ./server/* /home/server/
ADD ./client/* /home/client/
EXPOSE 8080
#CMD ["python", "/app/udp_receiver.py"]
# ENTRYPOINT ["python", "/app/udp_receiver.py"]
CMD ["python", "/home/server/tcp_server.py"]
STOPSIGNAL SIGTERM