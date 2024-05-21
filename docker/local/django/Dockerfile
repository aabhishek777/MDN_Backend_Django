ARG PYTHON_VERSION=3.11.2-bullseye


FROM python:${PYTHON_VERSION} as python



FROM python as python-build-stage
ARG BUILD_ENVIORNMENT=local


RUN apt-get update && apt-get install --no-install-recommends -y \ 
               build-essential \ 
               libpq-dev

COPY ./requirements .

RUN pip wheel --wheel-dir /usr/src/app/wheels \
    -r ${BUILD_ENVIORNMENT}.txt


FROM python as python-run-stage
ARG BUILD_ENVIORNMENT=local

ARG APP_HOME= /app

#stop the nature of pre conversion of .py file to .pyc(byte code ) file
ENV PYTHONDONTWRITEBYTECODE 1   

# python output is not buffered
ENV PYTHONUNBUFFERED 1

ENV BUILD_ENV ${BUILD_ENVIORNMENT}

WORKDIR ${APP_HOME}

RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev \
    gettext \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*


COPY --from=python-build-stage /usr/src/app/wheels /wheels/ 


RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
        && rm -rf /wheels/

COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint


COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

COPY . ${APP_HOME}


ENTRYPOINT [ "/entrypoint" ]