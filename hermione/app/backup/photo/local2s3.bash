#!/bin/bash -eu



main(){
    # aws s3 sync "/Users/najjong2/Pictures/Photos Library.photoslibrary/Masters/" "s3://yerihyo/backup/photo/jongmi-icloud/" --delete
    $AWS2 s3 sync "/Users/moon/yeri/photos/" "s3://yerihyo/backup/photo/2019_santacruz/"
}


main


