#Edward Luo
#Period 09
#04_lemme_flask_u_sumpn

from flask import Flask

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return 'Hello'

@my_app.route('/spook')
def spook():
    return '2spook4me'

@my_app.route('/poof')
def poof():
    return 'abrakadabraalakazam'

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
