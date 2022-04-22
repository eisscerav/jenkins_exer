def gv

pipeline {
    agent {label "${agent}"}
    environment {
        MY_ENV = '1.1.0'
    }
    parameters {
        string(name: 'string_var', defaultValue: 'ffan', description: 'version to prod')
        choice(name: 'agent', choices: ['P5000', 'RTX4000'], description: 'choose agent to run')
        booleanParam(name: 'execute', defaultValue: true, description: 'bool parameter')
    }

    stages {
        options {
            timeout(time: 1, unit: 'HOURS')  // supported unit: HOURS, MINUTES, SECONDS
        }
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
                sh "ls"
                sh "pwd"
                sh "python main.py"
                script {
                    gv.build_app()
                }
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
                script {
                    gv.deploy_app()
                }
            }
        }
    }
}


