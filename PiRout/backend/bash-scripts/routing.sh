#!/usr/bin/env bash
set -e
# ustawienie trasy
ip route add "$1" via "$2"
