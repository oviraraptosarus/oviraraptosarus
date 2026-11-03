#!/bin/sh
# On-demand big references (not vendored: size and licence). Usage: fetch-more.sh [d2l|fastbook]
mkdir -p "$(dirname "$0")/refs"; cd "$(dirname "$0")/refs"
case "$1" in
 d2l) git clone --depth 1 https://github.com/d2l-ai/d2l-en.git ;;
 fastbook) git clone --depth 1 https://github.com/fastai/fastbook.git ;;
 *) echo "d2l | fastbook" ;;
esac
