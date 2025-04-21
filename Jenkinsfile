pipeline{
    agent any
    stages{

        stage("build"){
            steps {
                sh "sam build -t template.yaml"
            }
        }

        stage("Deploy"){
            environment{
                AWS_DEFAULT_REGION = 'us-east-1'
                AWS_ACCESS_KEY_ID = credentials("aws-access-key")
                AWS_SECRET_ACCESS_KEY = credentials("aws-secret-key")
            }   
            steps{
                sh '''
                aws s3 mb s3://my-sam-deployments-bucket
                sam deploy --no-confirm-changeset \
                   --no-fail-on-empty-changeset \
                   --stack-name my-sam-stack \
                   --capabilities CAPABILITY_IAM \
                   --region us-east-1 \
                   --s3-bucket my-sam-deployments-bucket
                '''
            }

        }
    }
}        
