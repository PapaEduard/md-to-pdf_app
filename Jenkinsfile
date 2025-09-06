pipeline {
    agent any

    parameters {
        booleanParam(name: 'BUILD_IMAGE', defaultValue: false, description: 'Build new Docker image')
        string(name: 'BRANCH_NAME', defaultValue: 'main', description: 'Git branch to checkout')
        string(name: 'MD_FILE_NAME', defaultValue: 'main.md', description: 'Markdown file name in inputs/')
    }

    environment {
        DOCKER_IMAGE = 'edy2010/md_to_pdf/md-to-pdf-app'
        CONTAINER_NAME = 'md2pdf_job'
        PDF_OUTPUT = 'results/file1.pdf'
        DOCKER_TOKEN = credentials('edy-dock')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: "${params.BRANCH_NAME}", url: 'https://github.com/PapaEduard/md-to-pdf_app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh"""
                    docker build -t "${env.DOCKER_IMAJE}" .
                    """
                }
            }
        }

        stage('Push to Hub') {
            steps {
                script {
                    sh """
                    docker login -u edy2010 -p ${env.DOCKER_TOKEN}
                    docker push "${env.DOCKER_IMAGE}"
                    """
                }
            }
        }

        stage('Run Conversion') {
            steps {
                script {
                    sh """
                    docker run --rm \
                        -v "\$(pwd)/inputs:/src/inputs" \
                        -v "\$(pwd)/results:/src/results" \
                        ${DOCKER_IMAGE} /src/inputs/${params.MD_FILE_NAME} /src/results/file1.pdf
                    """
                }
            }
        }

        stage('Archive PDF') {
            steps {
                archiveArtifacts artifacts: "${PDF_OUTPUT}", allowEmptyArchive: false
            }
        }
    }
}

