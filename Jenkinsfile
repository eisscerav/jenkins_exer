def gv

pipeline {
    agent any
    environment {
        MY_ENV = '1.1.0'
    }
    parameters {
        string(name: 'string_var', defaultValue: 'ffan', description: 'version to prod')
        choice(name: 'choice_var', choices: ['1', '2', '3'], description: 'choices desc')
        booleanParam(name: 'execute', defaultValue: true, description: 'bool parameter')
    }

    stages {
        stage('init') {
            steps {
                script {
                    gv = load "script.groovy"
                }
            }
        }
       
        stage('Build') {
            steps {
                echo 'Building..'
                echo "version ${MY_ENV}" 
                gv.build_app()
            }
        }
        stage('Test') {
            when {
                expression {
                    BRANCH_NAME == 'ffan' || BRANCH_NAME == 'main'
                    params.execute
                } 
            }
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                echo "use param version_str ${params.string_var}"
            }
        }
    }
}
