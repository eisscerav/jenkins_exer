pipeline {
    agent any
    environment {
        MY_ENV = '1.1.0'
    }
    parameters {
        string(name: 'version_str', defaultValue: 'ffan', description: 'version to prod')
        choice(name: 'version_cho', choices: ['1', '2', '3'], description: 'choices desc')
        //booleanParam(name: 'execute', defaultValue: True, description: 'bool parameter')
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
                    //params.execute
                } 
            }
            steps {
            echo 'Testing..'
        
            }
    
        }
        stage('Deploy') {
            steps {
            echo 'Deploying....'
//            echo "use param version_str ${params.version_str}"
        
            }
    
        }

    }
}
