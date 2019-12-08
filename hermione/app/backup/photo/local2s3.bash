#!/bin/bash -eu



main(){
    # aws s3 sync "/Users/najjong2/Pictures/Photos Library.photoslibrary/Masters/" "s3://yerihyo/backup/photo/jongmi-icloud/" --delete

    $AWS2 s3 sync "$HOME/yeri/photo/" "s3://yerihyo/backup/photo/"
}


main


