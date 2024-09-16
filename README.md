API REST pour un forum avec django

- on crée un dossier forum
- pour clone le projet: git clone https://github.com/ericjojo18/api-forum
- creation de l'environnement dans le dossier forum( python -m ven env)
- activation de l'environnement virtuel( macos: source env/bin/activate, windows: env\Scripts\activate)
- creation du projet api-forum (django-admin createproject forum)
- creation de l'application api (django-admin startapp api)
- configuration de l'application dans setting du project
- créer un dossier models dans l'application api(MesssageModels.py , ForumModel.py, SubjectModel.py)
- configuration de la bd dans le settings du projet
- faire les differentes migrations(python manage.py makemigrations et python manage.py migrate)
- creations de nos dossiers viewsets et serializers dans l'application (message_serializer.py , forum_serializer.py, sujet_serializer.py et pareil pour les viewssets)
- creer un fichier urls.py dans l'application
- faire les differentes routes
- configuration de l'urls dans le projet
- on lance le serveur avec python manage.py runserver ( http://127.0.0.1:8000/api/)
- on visualise avec postman pour le test
