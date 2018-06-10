# Launch Portfolio Site
> Currently the site is launched on Digital Ocean using uWSGI and Nginx.  

### Fresh Installation from Scratch

1. **Clone Repository from Git**
 [GitHub - samclayj/flaskportfolio](https://github.com/samclayj/flaskportfolio.git)

```
git clone https://github.com/samclayj/flaskportfolio.git
```

2. **Install Node dependencies for Frontend**

Make sure Node is installed:
```
sudo apt-get update
sudo apt-get install nodejs
sudo apt-get install npm
```

```
cd portfolio/static/bootstrap
npm install
```

Note: There’s an issue on Ubuntu where `npm-sass` relies on the `node` command, but in Ubuntu 16.04 the `nodejs` command is used. If this is an issue create a sym link before installing.
```
ln -s /usr/bin/nodejs /usr/bin/node
```

*Generate CSS*
This is an important step. The command is defined in `package.json`. This will compile the bootstrap `scss` files along with the `custom.scss` used to generate CSS variables.

Check `bootstrap/dist/css/bootstrap.css` to make sure that the overrides from `portfolio/scss/custom.scss` are in effect.
```
npm run css-compile
```

3. **Configure Virtual Environment**
```
virtualenv venv
```

4. **Activate the virtual environment**
```
source venv/bin/activate
```

5. **Install Flask and uWSGI**
```
pip install uwsgi flask
```

6. **Modify Nginx Configuration**
[Proxying web apps with Nginx](https://gist.github.com/soheilhy/8b94347ff8336d971ad0)

Proxies requests to locally running applications.
/etc/nginx/sites-available/<your-config>
```
server {
    listen 80;
    server_name server_domain_or_IP;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/home/sammy/myproject/myproject.sock;
    }
}
```

Test config for errors:
```
sudo nginx -t
```

Reload the configuration:
``` 
nginx -s reload
```

Restart nginx:
```
sudo systemctl restart nginx
```

Disable port 5000 access and enable Nginx:
```
sudo ufw delete allow 5000
sudo ufw allow 'Nginx Full'
```

> Note: make sure that the configuration is sym linked to `/etc/nginx/sites-enabled/<your-config>`.  

7. Configure and enable a systemd service

/etc/systemd/system/portfolio.service
```
[Unit]
Description=uWSGI instance to serve myproject
After=network.target

[Service]
User=sammy
Group=www-data
WorkingDirectory=/home/sammy/myproject
Environment="PATH=/home/sammy/myproject/myprojectenv/bin"
ExecStart=/home/sammy/myproject/myprojectenv/bin/uwsgi --ini myproject.ini

[Install]
WantedBy=multi-user.target
```

Enable the service:
```
sudo systemctl start myproject
sudo systemctl enable myproject
```

### Refresh Served Application with Changes
```
sudo systemctl stop myproject
sudo systemctl start myproject
```

### Run Flask App in Debug
1. **Enable port 5000**
```
sudo ufw allow 5000
```

2. **Activate environment**
```
. venv/bin/activate
```

3. Remember to initialize the database using the registered `init-db` command
```
flask init-db
```

3. Run the Application in Debug Mode

*Method 1: uwsgi*

Start uwsgi on port 5000 (uses wsgi.py as hook):
```
uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app
```

*Method 2: flask run*
```Export Variables
export FLASK_APP=portfolio
export FLASK_ENV=development
```

Run development server:
```
flask run
```

### Resources
[Deploy to Production — Flask 1.0.2 documentation](http://flask.pocoo.org/docs/1.0/tutorial/deploy/)

[uWSGI — Flask 1.0.2 documentation](http://flask.pocoo.org/docs/1.0/deploying/uwsgi/)

[Digital Ocean Flask Applications](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-16-04)

#web/portfolio

