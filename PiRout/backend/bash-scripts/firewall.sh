#!/usr/bin/env bash
set -e
# prosty menedzer zapory
case "$1" in
  start)
    iptables -P FORWARD DROP
    iptables -A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT
    ;;
  stop)
    iptables -F
    ;;
esac
