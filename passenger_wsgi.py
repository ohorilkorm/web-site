# -*- coding: utf-8 -*-                                 
import sys, logging
logging.basicConfig(stream=sys.stderr)
# указываем директорию с проектом 
sys.path.append('/home/y/yaroslxw/yaroslxw.beget.tech/App') 

# указываем директорию с библиотеками, куда поставили Flask
#sys.path.append('/home/y/yaroslxw/yaroslxw.beget.tech/venv/bin/flask') 
sys.path.append('/home/y/yaroslxw/yaroslxw.beget.tech/.local/lib/python3.6/site-packages') 

from App import app as application
# Когда Flask стартует, он ищет application. 
# Если не указать 'as application', сайт не заработает

from werkzeug.debug import DebuggedApplication
# Опционально: подключение модуля отладки 

application.wsgi_app = DebuggedApplication(application.wsgi_app, True)
# Опционально: включение модуля отадки

application.debug = True
# Опционально: True/False устанавливается по необходимости в отладке 
