# hadolint ignore=DL3007
FROM linuxserver/wireguard:v1.0.20210914-ls74

WORKDIR /opt/openwisp

RUN apt update && \
    apt install -y sudo network-manager cron redis-tools wget python3-pip && \
    apt autoclean

RUN pip install pyroute2
# Remove services from the base image
RUN rm /etc/cont-init.d/40-confs && \
    rm -r /etc/services.d/wireguard
RUN useradd --system --password '' --create-home --shell /bin/bash \
   --gid root --groups sudo --uid 1001 openwisp
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
RUN chown -R openwisp:root /opt/openwisp

COPY --chown=openwisp:root ./openwisp_wireguard/update_wireguard.sh \
    ./openwisp_wireguard/update_vxlan.py \
    ./common/init_command.sh \
    ./common/utils.sh \
    ./common/services.py /opt/openwisp/
RUN chmod +x /opt/openwisp/update_vxlan.py

CMD ["bash", "init_command.sh"]

EXPOSE 51820

ENV MODULE_NAME=wireguard \
    DASHBOARD_INTERNAL=dashboard.internal \
    API_INTERNAL=api.internal \
    REDIS_HOST=redis \
    REDIS_DATABASE=15 \
    OPENWISP_USER=openwisp
