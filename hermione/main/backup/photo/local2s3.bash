#!/bin/bash -eu



main(){
    # aws s3 sync "/Users/najjong2/Pictures/Photos Library.photoslibrary/Masters/" "s3://yerihyo/backup/photo/jongmi-icloud/" --delete
#    local dirpath_local="$HOME/yeri/photo"
    local dirpath_from="/Users/Shared/jongmi-icloud"
    #local dirpath_from="s3://yerihyo/backup/photo/jongmi-icloud"
    local dirpath_to="s3://yerihyo/backup/photo/jongmi-icloud"
    $AWS2 s3 sync "$dirpath_from/" "$dirpath_to/"
}


main


