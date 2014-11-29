# django-heroku-bootstrap

django-heroku-bootstrap is a base project that integrates django with heroku and twitter bootstrap. it sets the foundation to use django with heroku, compiling less via django-pipeline, in different environments.

### dependencies

since we use heroku and less, we ust install some packages for your project to work.

- npm
- nodejs > 0.8
- lessc
- promise
- yuglify
- heroku-toolbelt
- virtualenv

be sure to have everything installed. if you're using ubuntu 14.04, you need to install a PPA to fully use the less compiler and create a symlink binding nodejs to node:

```
curl -sL https://deb.nodesource.com/setup | sudo bash -
sudo apt-get install -y nodejs npm
sudo ln -s /usr/bin/nodejs /usr/bin/node
```

then install node packages globally:

```
sudo npm install -g less yuglify promise
```

### deploying to heroku

you must follow 5 steps to deploy your project to heroku:

#### have a heroku account

just go to [heroku's site](http://heroku.com) and sign up.

#### have heroku toolbelt installed

follow [heroku's guide](https://toolbelt.heroku.com/) to install heroku toolbelt and login.

#### clone this repository and setup

you must clone this repository somewhere. when cloned, change cloned folder name to your project's name, enter it's folder, create a virtualenv and install the project requirements.

```
git clone https://github.com/lucianoratamero/django-heroku-bootstrap.git
mv django-heroku-bootstrap YOUR_PROJECT_NAME
virtualenv YOUR_PROJECT_NAME
cd YOUR_PROJECT_NAME
source bin/activate
pip install -r requirements.txt
```

rebember to unlink your project git from this repository!

```
rm -rf .git
git init
git add .
git commit -m 'initial commit'
```

#### create heroku app

create a heroku app:

```
heroku create
```

#### set up heroku's stuff

you need to tell heroku to use the correct settings file:

```
heroku config:set DJANGO_SETTINGS_MODULE=settings.production
```

and push to heroku!

```
git push heroku master
```

that's it! you should have something like [http://django-heroku-bootstrap.herokuapp.com](http://django-heroku-bootstrap.herokuapp.com).

if you wish to change your app name, just use:

```
heroku apps:rename newname
```

and start developing!

remember to [read the docs](http://django-pipeline.readthedocs.org/en/latest/) to django-pipeline, since you're gonna be using it to compile less files and manage your javascript.

#### questions?

any questions, contact me at luciano@ratamero.com. =)

