pipeline{
    agent any
    stages{
        stage("Check SAM"){
            steps {
                sh 'which sam && sam --version'
            }
        }
    }
}        
