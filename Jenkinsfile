def gv
my_agents = ['P5000', 'RTX4000', 'K4200']

pipeline {
    agent {label "${agent}"}
    environment {
        MY_ENV = '1.1.0'
    }
    parameters {
        string(name: 'string_var', defaultValue: 'ffan', description: 'version to prod')
        choice(name: 'agent', choices: my_agents, description: 'choose specific agent to run')
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
                sh("mkdir -p stash_dir")
                sh("mkdir -p another_stash")
                writeFile file: "stash_dir/somefile", text: "Hey look, some text."
                writeFile file: "another_stash/otherfile", text: "Hey look, put other text."
                stash name:"my_stash", includes: "stash_dir/*, another_stash/*", allowEmpty: true
            }
        }
        stage('Test') {
            when {
                expression {
                    //env.BRANCH_NAME == 'ffan' || env.BRANCH_NAME == 'main' only for multi-branch
                    params.execute
                } 
            } 
            steps {
                echo 'Testing..'
                echo "${env.BUILD_ID}"
                echo "${env.JOB_NAME}"
                echo "${env.BRANCH_NAME}"
                sh(script: "python3 main.py --family ffan_home")
                sh("mkdir tmp")
                sh("touch tmp/a.txt")
            }
        }
        stage('Deploy') {
            steps {
                // check stash files
                unstash "my_stash"
                sh("ls")
                sh("ls stash_dir")
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
    
    post {
        always {
            cleanWs()
        }
    }
}
