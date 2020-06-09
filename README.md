Hello world Lambda in Python

    export AWS_PROFILE="<an AWS cli profile>"

    # Create CloudFormation stack (api gw, lambda, s3 bucket, ...)
    sls deploy

    # Sample POST (creates object in s3)
    curl -d 'hallo welt' -H "Content-Type: text/plain" $(sls info --verbose | grep HttpApiUrl | cut -d' ' -f 2)/

    # Sample GET (joins and returns all objects in s3)
    curl $(sls info --verbose | grep HttpApiUrl | cut -d' ' -f 2)/
  