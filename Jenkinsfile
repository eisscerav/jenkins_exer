pipeline {
    agent any
    environment {
        MY_ENV = '1.1.0'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                echo "version ${MY_ENV}" 
            }
    
        }
        stage('Test') {
            when {
                expression {
                    BRANCH_NAME == 'ffan' || BRANCH_NAME == 'main'
                } 
            }
            steps {
            echo 'Testing..'
        
            }
    
        }
        stage('Deploy') {
            steps {
            echo 'Deploying....'
        
            }
    
        }

    }
}
