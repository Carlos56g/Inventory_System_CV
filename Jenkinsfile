pipeline {
    agent any
    
    environment {
        GITHUB_REPO = 'https://github.com/Carlos56g/PIALenguajesModernos.git' // Reemplaza con tu URL de GitHub
        DOCKER_COMPOSE_FILE = 'PuntoDeVentaCV/docker-compose.yml'
        DOCKER_COMPOSE_DIR = 'PuntoDeVentaCV'  // Directorio donde está el archivo docker-compose.yml
    }
    
    stages {

        stage('Clean Checkout') {
            steps {
                // Elimina el directorio de trabajo para garantizar un repositorio limpio
                deleteDir() 
                checkout scm  // Realiza un checkout limpio del repositorio
            }
        }

        stage('Stop and Remove Old Containers') {
            steps {
                script {
                    // Detener y eliminar los contenedores antiguos antes de crear los nuevos
                    sh 'docker compose -f ${DOCKER_COMPOSE_FILE} down --volumes --remove-orphans'
                }
            }
        }

        stage('Build and Run Docker Containers') {
            steps {
                script {
                    // Construir y ejecutar los contenedores usando docker-compose
                    sh 'docker compose -f ${DOCKER_COMPOSE_FILE} up --build -d'
                }
            }
        }
        
        stage('Wait for MySQL to be Ready') {
            steps {
                script {
                    // Esperar a que MySQL esté listo para aceptar conexiones
                    echo "Waiting for MySQL to be ready..."
                    sleep(time: 10, unit: 'SECONDS')  // Esperar 20 segundos (ajustar según lo necesario)
                }
            }
        }

        stage('Create Database if Not Exists') {
            steps {
                script {
                    dir("${DOCKER_COMPOSE_DIR}") {
                        def retryCount = 0
                        def maxRetries = 5
                        def success = false
                        
                        while (retryCount < maxRetries && !success) {
                            try {
                                echo "Attempting to create database (Attempt ${retryCount + 1})..."
                                sh 'docker-compose exec -T db mysql -u root -pmy-secret-pw -e "CREATE DATABASE IF NOT EXISTS tienda_db;"'
                                success = true
                            } catch (Exception e) {
                                retryCount++
                                echo "Error while creating database: ${e}"
                                // Esperar 10 segundos antes de intentar de nuevo
                                sleep(time: 10, unit: 'SECONDS')
                            }
                        }
                        
                        if (!success) {
                            error "Failed to create database after ${maxRetries} attempts."
                        }
                    }
                }
            }
        }

        stage('Make Migrations') {
            steps {
                script {
                    // Cambiar al directorio correcto y ejecutar las migraciones de Django
                    dir("${DOCKER_COMPOSE_DIR}") {
                        sh 'docker-compose exec -T web python manage.py makemigrations'
                    }
                }
            }
        }
        
        stage('Migrate') {
            steps {
                script {
                    // Cambiar al directorio correcto y ejecutar las migraciones de Django
                    dir("${DOCKER_COMPOSE_DIR}") {
                        sh 'docker-compose exec -T web python manage.py migrate'
                    }
                }
            }
        stage('Restart Django Container') {
            steps {
                script {
                    // Reinicia el Contenedor de Django
                    sh 'docker restart django-container'
                }
            }
        }
    }
}
