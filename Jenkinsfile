def gv

pipeline {
    agent {label "${agent}"}
    //triggers {
    //    cron('H */4 * * 1-5')
    //}
    environment {
        MY_ENV = '1.1.0'
    }
    options {
        timeout(time: 1, unit: 'HOURS')  // supported unit: HOURS, MINUTES, SECONDS
    }
    parameters {
        string(name: 'string_var', defaultValue: 'ffan', description: 'version to prod')
        choice(name: 'agent', choices: ['P5000', 'RTX4000'], description: 'choose agent to run')
        booleanParam(name: 'execute', defaultValue: true, description: 'bool parameter')
        password(name: 'PASSWORD', defaultValue: 'SECRET', description: 'Enter a password')
        text(name: "my_layer", defaultValue: "", description: "Specify my.layer")
    }

    stages {
        stage('write my.layer') {
            steps {
                writeFile file: 'my.layer', text: params.my_layer
            }
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
        stage('archive') {
            steps {
                archiveArtifacts(artifacts: 'tmp/*', followSymlinks: false)   
            }
        }
    }
}


