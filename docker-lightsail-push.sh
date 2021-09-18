#! /bin/zsh

set -Eeuo pipefail

main() {

    # Script usage.
    if [[ ! "$#" = 1 ]]; then
        echo "Usage: ./docker-lightsail-push.sh <image:tag>"
        exit 1
    fi

    # Get docker image.
    local -r DOCKER_IMAGE="$1"

    # Push image to ligthsail container service.
    aws lightsail push-container-image \
        --region $AWS_REGION \
        --service-name $AWS_SERVICE \
        --label $AWS_LABEL \
        --image $DOCKER_IMAGE
}

main "$@"
