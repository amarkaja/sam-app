pipleine{
    agent any
    stages{
        stage{
            steps {
                sh 'which sam && sam --version'
            }
        }
    }
}        # test change
