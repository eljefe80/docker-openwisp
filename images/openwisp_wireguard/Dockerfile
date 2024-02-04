# hadolint ignore=DL3007
FROM linuxserver/wireguard:latest

WORKDIR /opt/openwisp

RUN apk update && \
    apk add sudo networkmanager redis wget

# Remove services from the base image
RUN rm -f /etc/cont-init.d/40-confs && \
    rm -rf /etc/services.d/wireguard
RUN useradd --system --password '' --create-home --shell /bin/bash \
   --gid root --groups sudo --uid 1001 openwisp
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
RUN chown -R openwisp:root /opt/openwisp

COPY --chown=openwisp:root ./openwisp_wireguard/update_wireguard.sh \
    ./common/init_command.sh \
    ./common/utils.sh \
    ./common/services.py /opt/openwisp/

CMD ["bash", "init_command.sh"]

EXPOSE 51820

ENV MODULE_NAME=wireguard \
    DASHBOARD_INTERNAL=dashboard.internal \
    API_INTERNAL=api.internal \
    REDIS_HOST=redis \
    REDIS_DATABASE=15 \
    OPENWISP_USER=openwisp
