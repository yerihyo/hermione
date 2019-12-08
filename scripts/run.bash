#!/bin/bash -eu

ARG0=${BASH_SOURCE[0]}
FILE_PATH=$(readlink -f $ARG0)
FILE_DIR=$(dirname $FILE_PATH)
FILE_NAME=$(basename $FILE_PATH)

SCRIPTS_DIR=$FILE_DIR
REPO_DIR=$(dirname $SCRIPTS_DIR)


errcho(){ >&2 echo $@; }


main(){
    #aws s3 sync "/Users/najjong2/Pictures/Photos Library.photoslibrary/Masters/" "s3://yerihyo/backup/photo/jongmi-icloud/" --delete
    $REPO_DIR/hermione/app/backup/photo/local2s3.bash
}

pushd $REPO_DIR


errcho "[$FILE_NAME] start (REPO_DIR:$REPO_DIR)"
main
errcho "[$FILE_NAME] end (REPO_DIR:$REPO_DIR)"

popd
