pipeline {
    agent { docker 'microsoft/dotnet:2.1-sdk' } 
    stages {
        stage('Example Build') {
            steps {
                sh "dotnet publish -o Out"
            }
        }
    }
}
