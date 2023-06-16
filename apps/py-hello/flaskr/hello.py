from flask import (Flask, request, render_template, url_for, flash, redirect)
from markupsafe import escape

def start_hello(app):
    # Simple usage
    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"


    # HTTP Methods
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            return 'POST method'
        else:
            return 'GET method'


    # Variable Rules
    @app.route('/user/<username>')
    def show_user_profile(username):
        # show the user profile for that user
        return f'User {escape(username)}'


    @app.route('/post/<int:post_id>')
    def show_post(post_id):
        # show the post with the given id, the id is an integer
        return f'Post {post_id}'


    @app.route('/path/<path:subpath>')
    def show_subpath(subpath):
        # show the subpath after /path/
        return f'Subpath {escape(subpath)}'



    @app.route("/avatar/<filename>")
    def user_image(filename):
        return f'/file/{filename}'

    # JSON response
    @app.route("/me")
    def me_api():
        user = {"username": "Jane", 'theme': "dark", "image": ''}
        return {
            "username": user['username'],
            "theme": user['theme'],
            "image": url_for("user_image", filename=user['image']),
        }

    # Requst form payload
    @app.route('/register', methods=('GET', 'POST'))
    def register():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            app.logger.debug('username %s', username)
            app.logger.debug('password %s', password)
            
            error = None

            if not username:
                error = 'Username is required.'
            elif not password:
                error = 'Password is required.'

            if error is None:
                return redirect(url_for("login"))

            flash(error)

        return render_template('register.html')

    # Request JSON payload
    # https://sentry.io/answers/flask-getting-post-data/
    @app.route('/json_example', methods=['POST'])
    def handle_json():
        if request.is_json:
            data = request.json
            app.logger.debug(data.get('name'))
            app.logger.debug(data.get('age'))
            return data
        else:
            return "Content type is not supported."

    # Rendering templates
    @app.route('/site/')
    @app.route('/site/<name>')
    def site(name=None):
        return render_template('hello.html', name=name)


    # Deploy: Tell Flask it is Behind a Proxy
    # nginx config: https://flask.palletsprojects.com/en/2.3.x/deploying/nginx/

    # from werkzeug.middleware.proxy_fix import ProxyFix

    # app.wsgi_app = ProxyFix(
    #     app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
    # )
