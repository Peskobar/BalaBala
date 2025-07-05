#!/usr/bin/env bash
set -e
# zarządzanie wireguard
wg-quick "$1" wg0
