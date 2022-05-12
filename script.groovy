def build_app() {
  def n = 10
  echo 'build app function'
  return n
}

def test_app() {
  echo 'test app function'
  echo "use parameter ${params.choice_var}"
}

def deploy_app() {
  echo 'deploy app function'
  echo "use parameter ${params.string_var}"
}

return this
