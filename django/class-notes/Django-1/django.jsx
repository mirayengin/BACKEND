//? Framework; uygulama ya da yazılım geliştirmek için geliştirilmiş bir yazılımdır. Sunduğu çerçeve sayesinde geliştiricilerin işini büyük oranda kolaylaştırır

//!cd ~
// echo alias "py='python3'" >> .bash_profile
// echo alias "python='python3'" >> .bash_profile
// echo alias "pip='pip3'" >> .bash_profile
// echo alias "py='python3'" >> .zshrc
// echo alias "python='python3'" >> .zshrc
// echo alias "pip='pip3'" >> .zshrc

//? MTV Model-View-Template

//!Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
//? ./env/Scripts/activate
//! deactivate
//? pip freeze
//! pip freeze > requirements.txt

// # Created by https://www.toptal.com/developers/gitignore/api/django
// # Edit at https://www.toptal.com/developers/gitignore?templates=django

// ### Django ###
// *.log
// *.pot
// *.pyc
// __pycache__/
// local_settings.py
// db.sqlite3
// db.sqlite3-journal
// media

// # If your build process includes running collectstatic, then you probably don't need or want to include staticfiles/
// # in your Git repository. Update and uncomment the following line accordingly.
// # <django-project-name>/staticfiles/

// ### Django.Python Stack ###
// # Byte-compiled / optimized / DLL files
// *.py[cod]
// *$py.class

// # C extensions
// *.so

// # Distribution / packaging
// .Python
// build/
// develop-eggs/
// dist/
// downloads/
// eggs/
// .eggs/
// lib/
// lib64/
// parts/
// sdist/
// var/
// wheels/
// share/python-wheels/
// *.egg-info/
// .installed.cfg
// *.egg
// MANIFEST

// # PyInstaller
// #  Usually these files are written by a python script from a template
// #  before PyInstaller builds the exe, so as to inject date/other infos into it.
// *.manifest
// *.spec

// # Installer logs
// pip-log.txt
// pip-delete-this-directory.txt

// # Unit test / coverage reports
// htmlcov/
// .tox/
// .nox/
// .coverage
// .coverage.*
// .cache
// nosetests.xml
// coverage.xml
// *.cover
// *.py,cover
// .hypothesis/
// .pytest_cache/
// cover/

// # Translations
// *.mo

// # Django stuff:

// # Flask stuff:
// instance/
// .webassets-cache

// # Scrapy stuff:
// .scrapy

// # Sphinx documentation
// docs/_build/

// # PyBuilder
// .pybuilder/
// target/

// # Jupyter Notebook
// .ipynb_checkpoints

// # IPython
// profile_default/
// ipython_config.py

// # pyenv
// #   For a library or package, you might want to ignore these files since the code is
// #   intended to run in multiple environments; otherwise, check them in:
// # .python-version

// # pipenv
// #   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
// #   However, in case of collaboration, if having platform-specific dependencies or dependencies
// #   having no cross-platform support, pipenv may install dependencies that don't work, or not
// #   install all needed dependencies.
// #Pipfile.lock

// # poetry
// #   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
// #   This is especially recommended for binary packages to ensure reproducibility, and is more
// #   commonly ignored for libraries.
// #   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
// #poetry.lock

// # pdm
// #   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
// #pdm.lock
// #   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
// #   in version control.
// #   https://pdm.fming.dev/#use-with-ide
// .pdm.toml

// # PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
// __pypackages__/

// # Celery stuff
// celerybeat-schedule
// celerybeat.pid

// # SageMath parsed files
// *.sage.py

// # Environments
// .env
// .venv
// env/
// venv/
// ENV/
// env.bak/
// venv.bak/

// # Spyder project settings
// .spyderproject
// .spyproject

// # Rope project settings
// .ropeproject

// # mkdocs documentation
// /site

// # mypy
// .mypy_cache/
// .dmypy.json
// dmypy.json

// # Pyre type checker
// .pyre/

// # pytype static type analyzer
// .pytype/

// # Cython debug symbols
// cython_debug/

// # PyCharm
// #  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
// #  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
// #  and can be added to the global gitignore or merged into this file.  For a more nuclear
// #  option (not recommended) you can uncomment the following to ignore the entire idea folder.
// #.idea/

// # End of https://www.toptal.com/developers/gitignore/api/django

//? django-admin startproject main .




// komutlar
// #python -m venv env(virtual env kurduk)(bunu yapmamızın sebbei her projeye ait package ler var biz bunları globale yüklemek istemiyoruz ve bir de sürümlerin uyuşmama gibi bir sorun çıkarmaması için kullanılır)
// #Powershell=>.\env\Scripts\activate(active ettik)
// # bash=> source env/Scripts/Activate
// #=>powershel hatası için:Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
// #pip install django(djangoyu yükledik)
// #django-admin startproject fscohort1  . (içiçe olmadan proje başlatma komutu eğer nokta koymazsak projeyi içiçe klasör yapısıyla oluşturyor)
// #=>pip freeze  yada pip list(yüklü paketleri listeler)
// #python manage.py runserver (projeyi ayağa kaldırma default port 8000)
// # python manage.py runserver 8080 (port numarasını değiştirme)
// #:>python manage.py startapp student (student appı oluştrduk)(bunu yaptıktan sonra proje dizinine gidip settings.py e girip installedappse appimizi tanıtmamız gerekiyor)
// #pip freeze > requirements.txt(yüklü paketleri txt dosyasına kaydettik)(bunu yapmamızın sebebi projeyi sunduğumuzda kullanndığımız paketleri göstermesi için)
// #pip install -r requirements.txt(requirements.txt dosyasını kullanarak paketleri yükledik)(bunu repodan bir proje indirdiğimizde paketleri yüklemek için kullanıyoruz)
// # add .gitignore(githuba projeyi göndermek için içeriğini toptal gibi sitelerden alabiliriz yada önceki projelerimizden alabiliriz)

//!python manage.py migrate
// 9: 55
//? "değişiklikleri database uygula" demek.