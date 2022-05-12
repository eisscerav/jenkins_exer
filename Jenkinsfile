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
                    def n = gv.build_app()
                    echo '${n}'
                }
            }
        }
        stage('Test') {
            when {
                expression {
                    ${BRANCH_NAME} == 'ffan' || ${BRANCH_NAME} == 'main'
                    //echo "params.execute ${params.execute}"
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


