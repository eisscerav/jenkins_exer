def gv
my_agents = ['P5000', 'RTX4000', 'K4200']
def mymap = [
    "k1": "v1",
    "k2": "v2",
    "k3": "v3" 
]

def hello(name) {
    def greeting = "hello ${name}"
    return greeting
}

def show_map(dict) {
    dict.each {
        entry -> println "$entry.key: $entry.value"
    }
}

pipeline {
    agent {label "${agent}"}
    environment {
        MY_ENV = '1.1.0'
    }
    parameters {
        string(name: 'string_var', defaultValue: 'ffan', description: 'version to prod')
        choice(name: 'agent', choices: my_agents, description: 'choose specific agent to run')
        booleanParam(name: 'execute', defaultValue: true, description: 'bool parameter')
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
                show_map(mymap)
                script {
                    gv = load "script.groovy"
                    my_name = "ffan"
                    sh "cat my.layer"
                }
            }
        }

        stage('demo call function') {
            steps {
                script {
                    def greeting = hello(my_name)
                    def cmd = "${greeting}"
                    cmd += " sof"
                    sh("echo ${cmd}")
                }
            }
        }

        stage ('mimic fail') {
            steps{
                script {
                    if(params.execute) {
                        try {
                            neg_test_cmd = "/cudnnNegativeTest_static"
                            echo(neg_test_cmd)
                            // sh 'ls /non-exist'
                        }
                        catch (err){
                            echo err.getMessage()
                        }
                    }
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
                beforeAgent true
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
                sh("mkdir tmp")
                sh("touch tmp/a.txt")
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
            echo "pipeline done!!!"
//            cleanWs()
        }
    }
}
