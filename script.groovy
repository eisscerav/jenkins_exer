def build_app() {
  echo 'build app function'
}

def test_app() {
  echo 'test app function'
  echo "use parameter ${params.choice_var}"
}

def deploy_app() {
  echo 'build app function'
  echo "use parameter ${params.string_var}"
}

return this
