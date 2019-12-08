#!/bin/bash -eu

ARG0=${BASH_SOURCE[0]}
FILE_PATH=$(readlink -f $ARG0)
FILE_DIR=$(dirname $FILE_PATH)
FILE_NAME=$(basename $FILE_PATH)

errcho(){ >&2 echo $@; }
usage(){ errcho "usage: $ARG0 <filepath_list>"; }
func_count2reduce(){
    local v="${1?missing}"; local cmd="${2?missing}"; local n=${3?missing};
    for ((i=0;i<$n;i++)); do v=$($cmd $v) ; done; echo "$v"
}

REPO_DIR=$(func_count2reduce "$FILE_DIR" dirname 1)

main(){
  pushd $REPO_DIR
  sudo apt-get -y install
  # curl -sfL https://direnv.net/install.sh | bash
  # direnv allow .
  popd
}

main