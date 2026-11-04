pipeline {
    agent any

    environment {
        APP_URL  = credentials('app_url')
        APP_LATI = credentials('app_lati')
        APP_LON  = credentials('app_lon')
    }

    stages {
        stage('Preparar Entorno') {
            steps {
                echo 'Creando entorno virtual...'
                sh 'python3 -m venv .venv'
            }
        }

        stage('Instalar Dependencias') {
            steps {
                echo 'Instalando requerimientos desde requirements.txt...'
                sh './.venv/bin/pip install --upgrade pip'
                sh './.venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Ejecutar Pruebas (CI)') {
            steps {
                echo 'Validando sintaxis y ejecución del proyecto...'
                sh './.venv/bin/python3 -c \'import main; print("Pruebas de CI superadas con éxito")\''
            }
        }

        stage('Aprobación de Deploy (CD)') {
            steps {
                timeout(time: 1, unit: 'HOURS') {
                    input message: '¿Deseas aprobar el despliegue a producción de esta versión?',
                          ok: 'Aprobar y Deployar'
                }
            }
        }

        stage('Desplegar (Deploy)') {
            steps {
                echo '¡Aprobación concedida! Ejecutando pasos de despliegue...'
                sh 'echo "Simulando deploy exitoso del backend de clima."'
            }
        }
    }

    post {
        success { echo '¡Pipeline de CI/CD completado y desplegado exitosamente!' }
        failure { echo '¡El Pipeline falló o fue rechazado en la aprobación!' }
    }
}
