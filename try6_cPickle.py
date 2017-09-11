from flask import Flask

app = Flask(__name__)

import cPickle

l = {'a':1,'b':0}

ll = cPickle.dumps(l)
print('ll is: {}'.format(ll))
print('type of ll :', type(ll))

@app.route('/')
def hi():
    return ['hi', 'a']

# Cannot add view func after application starts
# @app.route('/b')
# def hib():
#     exec (t)
#     print 'exec(t)'
#     return 'hi /b'


t = """@app.route('/a')
def b():
    return 'bb'"""

if __name__ == '__main__':
    app.run(port=5900, threaded=True, debug=True)
