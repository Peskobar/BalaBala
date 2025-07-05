#!/usr/bin/env bash
set -e
# ustawienie zapasowego lacza
ip route replace default via "$1" || ip route add default via "$1"
