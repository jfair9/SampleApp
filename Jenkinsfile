pipeline {
  agent {
    kubernetes {
      label 'mypodtemplate-v1'
      containerTemplate {
        name 'dotnet'
        image 'microsoft/dotnet:2.1-sdk'
        ttyEnabled true
        command 'cat'
      }
    }
  }
  stages {
    stage('Example Build') {
      steps {
        container('dotnet') {
          sh 'dotnet publish -o Out  '
        }
      }
    }
  }
}
