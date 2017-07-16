FROM dockerfiles/django-uwsgi-nginx

COPY ./app /home/docker/code/app

COPY ./uwsgi.ini /home/docker/code/uwsgi.ini

ADD requirements.txt /home/docker/code/app

RUN apt-get update

RUN apt-get -y install libmysqlclient-dev

RUN apt-get -y install python-dev

RUN pip3 install --upgrade pip

RUN pip3 install -r /home/docker/code/app/requirements.txt