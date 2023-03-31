#! /usr/bin/env bash

# From official Nginx Docker image, as a script to re-use it, removing internal comments
# Ref: https://github.com/nginxinc/docker-nginx/blob/594ce7a8bc26c85af88495ac94d5cd0096b306f7/mainline/buster/Dockerfile

# Standard set up Nginx
export NGINX_VERSION=1.17.10
export NJS_VERSION=0.3.9
export PKG_RELEASE=1~buster
