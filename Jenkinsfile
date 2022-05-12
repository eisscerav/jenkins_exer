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
                script {
                    n = gv.build_app()
                    echo "${n}"
                }
            }
        }
        stage('Test') {
            when {
                expression {
                    //env.BRANCH_NAME == 'ffan' || env.BRANCH_NAME == 'main'
                    params.execute
                } 
            } 
            steps {
                echo 'Testing..'
                echo "${env.BUILD_ID}"
                echo "${env.JOB_NAME}"
                echo "${env.BRANCH_NAME}"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                echo "use param version_str ${params.string_var}"
                script {
                    gv.deploy_app()
                }
            }
        }
    }
}
