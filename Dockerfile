FROM ubuntu:latest

COPY . .
#install vim git pyhton pip 
RUN apt-get -y update
RUN apt-get install -y $(cat requirements/ubuntu_dependencies.txt )

#install les dependecies pyhon
RUN pip3 install -r requirements/requirements.txt

# set up git
RUN git config --global user.name "camikasa"
RUN git config --global user.password "Camtaro2302"

WORKDIR /workspace
RUN git init
RUN git clone https://github.com/camikasa/workspace.git

#set up venv 

RUN apt-get install -y python3-venv
RUN mkdir deep_learning
RUN cd deep_learning
RUN python3 -m venv deep_learning
RUN deep_learning/bin/pip3 install ipykernel 
RUN ipython kernel install --user --name=deep_learning
RUN deep_learning/bin/pip3 install tensorFlow scikit-learn


EXPOSE 8000

# on ajoute "--ip=0.0.0.0" pour pouvoir y accéser depuis le port 8000 avec docker run -p 8000:8000
#on ajoute "--port=8000" parce ue jutement on expose le port 8000 du conteneur 
# no browser found comme dans tous les cas le but est d'accéder au notebook en dehors du container on ajoute --no-browser",
#il m'a dit run as root is not recommended donc j'ajoute --allow-root
ENTRYPOINT ["jupyter", "notebook", "--no-browser", "--allow-root", "--port=8000", "--ip=0.0.0.0"]
