#!/usr/bin/env bash
set -e
# zarządzanie openvpn
systemctl "$1" openvpn
