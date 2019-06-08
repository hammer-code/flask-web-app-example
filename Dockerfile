FROM alpine
MAINTAINER arkinthesky.69@gmail.com 

RUN mkdir /app
WORKDIR /app
COPY . /app

ENV PATH="/root/.local/bin:${PATH}"

RUN apk update
RUN apk --no-cache add python3 python3-dev
RUN pip3 install --user pipenv
RUN pipenv install --system

EXPOSE 5000

CMD ["gunicorn","main:app" ,"-b", "0.0.0.0:5000"]