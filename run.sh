HERE=`pwd`
docker run -v $HERE --rm --name boto3_instance \
    -e AWS_ACCESS_KEY=$AWS_ACCESS_KEY \
    -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
    boto3