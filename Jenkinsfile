node('master'){

stage('Build'){
  def dotnet = docker.image('microsoft/dotnet:2.1-sdk')
  dotnet.inside {
    sh "dotnet publish -o Out"
  }
}
stage('Unit Test'){}
stage('Package'){}


}
