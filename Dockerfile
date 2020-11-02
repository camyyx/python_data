FROM ubuntu:latest

WORKDIR /workspace

COPY . .
#install vim git pyhton pip 
RUN apt-get -y update
RUN  apt-get install -y $(cat ubuntu_dependencies.txt )

#install les dependecies pyhon
RUN pip3 install -r requirements.txt

# set up git
RUN git config --global user.name "camikasa"
RUN git config --global user.password "Camtaro2302"
RUN git clone https://github.com/camikasa/workspace.git

EXPOSE 8000
#on ajoute "--port=8000" parce ue jutement on expose le port 8000 du conteneur 
# no browser found comme dans tous les cas le but est d'accéder au notebook en dehors du container on ajoute --no-browser",
#il m'a dit run as root is not recommended donc j'ajoute --allow-root
ENTRYPOINT ["jupyter", "notebook", "--no-browser", "--allow-root", "--port=8000", "--ip=0.0.0.0"]
