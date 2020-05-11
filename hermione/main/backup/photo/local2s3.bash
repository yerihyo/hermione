#!/bin/bash -eu

FILE_PATH=$(readlink -f $0)
FILE_NAME=$(basename $FILE_PATH)
FILE_DIR=$(dirname $FILE_PATH)
# FILE_DIR=`pwd`/../scripts/test
SCRIPTS_DIR=$FILE_DIR

errcho(){ >&2 echo $@; }
func_count2reduce(){
    local v="${1?missing}"; local cmd="${2?missing}"; local n=${3?missing};
    for ((i=0;i<$n;i++)); do v=$($cmd $v) ; done; echo "$v"
}

REPO_DIR=$(func_count2reduce $FILE_DIR dirname 4)
AWS=${AWS?'missing $AWS'}
AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID?'missing $AWS_ACCESS_KEY_ID'}
AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY?'missing $AWS_SECRET_ACCESS_KEY'}

main(){
    errcho "[$FILE_NAME] main - START"
    pushd $REPO_DIR

#    $AWS2 s3 sync "/Users/Shared/jongmi-icloud" "s3://yerihyo/backup/photo/jongmi-icloud" --delete
    $AWS s3 sync "/home/yerihyo/yeri/photo" "s3://yerihyo/backup/photo"

    popd
    errcho "[$FILE_NAME] main - END"
}

errcho "[$FILE_NAME] START"
main
errcho "[$FILE_NAME] END"


