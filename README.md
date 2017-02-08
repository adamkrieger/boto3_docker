# boto3 in a Docker container

1. Copy `envvars.default.sh` to `envvars.prod.sh` (which is gitignored) 
2. Edit that file to contain your credentials
3. `. ./envvars.prod.sh`
4. Proceed to run any other commands you need