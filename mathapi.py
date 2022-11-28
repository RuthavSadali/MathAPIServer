import flask
from flask import request
import json
import random
import math

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    out = {'success' : True, 'message': 'This is the home page'}
    return json.dumps(out), 200, {'Content-Type': 'applications'}

@app.route('/area/square', methods=['GET'])
def square():
    if 's' in request.args:
        tmep = int(request.args.get('s'))
        out = {'a' : tmep*tmep, 's' : tmep}
        return json.dumps(out), 200, {'Content-Type': 'application'}

@app.route('/area/rectangle', methods=['GET'])
def rectangle():
    if 'l' in request.args and 'w' in request.args:
        length = request.args.get('l')
        width = request.arg.get('w')
        out = {'l' : length, 'w' : width, 'a' : length*width}
        return json.dumps(out), 200. {'Content-Type' : 'application'}


@app.route('/area/triangle', methods=['GET'])
def triangle():
    if 'b' in request.args and 'h' in request.args:
        base = request.args.get('b')
        height = request.args('h')
        out = {'b' : base, 'h' : height, 'a' : (base*height)/2}
        return json.dumps(out), 200, {'Content-Type' : 'application'}

@app.route('/area/heron', methods=['GET'])
def heron():
    if 'a' in request.args and 'b' in request.args and 'c' in request.args:
        a = request.args.get('a')
        b = request.args.get('b')
        c = request.args.get('c')
        s = a+b+c
        thing = s * (s-a) * (s-b) * (s-c)
        thing = math.sqrt(thing)
        out = {'a' : a, 'b' : b, 'c' : c, 'a' : thing}
        return json.dumps(out), 200, {'Content-Type' : 'application'}

@app.route('/area/parallelogram', methods=['GET'])
def parallelogram():
    if 'b' in request.args and 'h' in request.args:
        b = request.args.get('b')
        h = request.args.get('h')
        out = {'b' : b, 'h' : h, 'a' : b*h}
        return json.dumps(out), 200, {'Content-Type' : 'application'}

@app.route('/area/circle', methods=['GET'])
def circle():
    if 'r' in request.args:
        r = request.args.get('r')
        a = r*r*math.pi
        out = {'r' : r, 'a' : a}
        return json.dumps(out), 200, {'Content-Type' : 'application'}

@app.route('/area/trapezoid', methods=['GET'])
def trapezoid():
    if 'b1' in request.args and 'b2' in request.args and 'h' in request.args:
        b1 = request.args.get('b1')
        b2 = request.args.get('b2')
        h = request.args.get('h')
        a = ((b1 + b2)/2)*h
        out = {'b1' : b1, 'b2' : b2, 'h' : h, 'a' : a}
        return json.dumps(out), 200, {'Content-Type' : 'application'}

@app.route('/surface/cube', methods=['GET'])
def cube():
    if 's' in request.args:
        s = request.args.get('s')
        a = (s*s)*6
        out = {'a' : a, 's' : s}
        return json.dumps(out), 200, {'Content-Type' : 'application'}

@app.route('/surface/sphere', methods=['GET'])
def sphere():
    if 'r' in request.args:
        r = request.args.get('r')
        a = 4*r*r*math.pi
        out = {'a' : a, 'r' : r}
        return json.dumps(out), 200, {'Content-Type' : 'application'}

@app.route('/surface/cylinder', methods=['GET'])
def cylinder():
    if 'r' in request.args and 'h' in request.args:
        r = request.args.get('r')
        h = request.args.get('h')
        a = 2*math.pi*r*h
        out = {'a' : a, 'r' : r, 'h' : h}
        return json.dumps(out), 200, {'Content-Type' : 'application'}

@app.route('/perimeter/square', methods=['GET'])
def perSquare():
    if 's' in request.args:
        s = request.args.get('s')
        out = {'p' : 4*s, 's' : s}
        return json.dumps(out), 200, {'Content-Type' : 'application'}

@app.route('/perimeter/rectangle', methods=['GET'])
def perRectangle():
    if 'l' in request.args and 'w' in request.args:
        l = request.args.get('l')
        w = request.args.get('w')
        out = {'p' : 2*l + 2*w, 'l' : l, 'w' : w}
        return json.dumps(out), 200, {'Content-Type' : 'application'}

@app.route('/perimeter/triangle', methods=['GET'])
def permTriangle():
    if 's1' in request.args and 's2' in request.args and 's3' in request.args:
        s1 = request.args.get('s1')
        s2 = request.args.get('s2')
        s3 = request.args.get('s3')
        out = {'p' : p, 's1' : s1, 's2' : s2, 's3' : s3}
        return json.dumps(out), 200, {'Content-Type' : 'application'}

@app.route('/perimeter/circle', methods=['GET'])
def permCircle():
    if 'd' in request.args:
        d = request.args.get('d')
        out = {'p' : math.pi*d, 'd' : d}
        return json.dumps(out), 200, {'Content-Type' : 'application'}

@app.route('/volume/cube', methods=['GET'])
def volCube():
    if 's' in request.args:
        s = request.args.get('s')
        out = {'v' : s*s*s, 's' : s}
        return json.dumps(out), 200, {'Content-Type' : 'application'}

@app.route('/volume/prism', methods=['GET'])
def volPrism():
    if 'l' in request.args and 'w' in request.args and 'h' in request.args:
        l = request.args.get('l')
        w = request.args.get('w')
        h = request.args.get('h')
        out = {'v' : l*H*W, 'l' : l, 'w' : w, 'h' : h}
        return json.dumps(out), 200, {'Content-Type' : 'application'}

@app.route('/volume/pyramid', methods=['GET'])
def volPyramid():
    if 'b' in request.args and 'h' in request.args:
        b = request.args.get('b')
        h = request.args.get('h')
        out = {'v' : (b*b*h)/3, 'b' : b, 'h' : h}
        return json.dumps(out), 200, {'Content-Type' : 'application'}

@app.route('/volume/cylinder', methods=['GET'])
def volCylinder():
    if 'r' in request.args and 'h' in request.args:
        r = request.args.get('r')
        h = request.args.get('h')
        out = {'v' : (math.pi*r*r*h), 'r' : r, 'h' : h}
        return json.dumps(out), 200, {'Content-Type' : 'application'}
@app.route('/volume/cone', methods=['GET'])
def volCone():
    if 'r' in request.args and 'h' in request.args:
        r = request.args.get('r')
        h = request.args.get('h')
        out = {'v' : (math.pi*r*r*h)/3, 'r' : r, 'h' : h}
        return json.dumps(out), 200, {'Content-Type' : 'application'}

@app.route('/volume/sphere', methods=['GET'])
def volSphere():
    if 'r' in request.args:
        r = request.args.get('r')
        out = {'v' : (math.pi*r*r*r*4)/3, 'r' : r}
        return json.dumps(out), 200, {'Content-Type' : 'application'}

@app.route('/distance', methods=['GET'])
    if 'x1' in request.args and 'x2' in request.args and 'y1' in request.args and 'y2' in request.args:
        x1 = request.args.get('x1')
        y1 = request.args.get('x2')
        x1 = request.args.get('y1')
        x2 = request.args.get('y2')
        d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        out = {'d' : d, 'x1' : x1, 'y1' : y1, 'x2' : x2, 'y2' : y2}
        return json.dumps(out), 200, {'Content-Type' : 'application'}

@app.route('/slope', methods=['GET'])
    if 'x1' in request.args and 'x2' in request.args and 'y1' in request.args and 'y2' in request.args:
        x1 = request.args.get('x1')
        y1 = request.args.get('x2')
        x1 = request.args.get('y1')
        x2 = request.args.get('y2')
        m = (y2-y1)/(x2-x1)
        out = {'m' : m, 'x1' : x1, 'y1' : y1, 'x2' : x2, 'y2' : y2}
        return json.dumps(out), 200, {'Content-Type' : 'application'}

@app.route('/pythag', methods=['GET'])
def pythag():
    if 'a' in request.args and 'b' in request.args:
        a = request.args.get('a')
        b = request.args.get('b')
        tot = a*a + b*b
        out = {'a' : a, 'b' : b, 'c' : math.sqrt(tot)}
        return json.dumps(out), 200, {'Content-Type' : 'application'}
    elif 'b' in request.args and 'c' in request.args:
        c = request.args.get('c')
        b = request.args.get('b')
        tot = c**2-b**2
        out = {'a' : math.sqrt(tot), 'b' : b, 'c' : c}
        return json.dumps(out), 200, {'Content-Type' : 'application'}
    elif 'a' in request.args and 'c' in request.args:
        c = request.args.get('c')
        a = request.args.get('a')
        tot = c**2-a**2
        out = {'a' : a, 'b' : math.sqrt(tot), 'c' : c}
        return json.dumps(out), 200, {'Content-Type' : 'application'}


@app.route('/mean', methods=['GET'])
def python():
    if 'nums' in request.args:
        nums = request.args.get('nums')
        tot = 0
        for x in nums:
            tot = tot + x
        tot = tot/len(nums)
        out = {'mean' : tot, 'nums' : '[' + str(nums) + ']'}
        return json.dumps(out), 200, {'Content-Type' : 'application'}

@app.route('/median', methods=['GET'])
    if 'nums' in request.args:
        nums = request.args.get('nums')
        index = len(nums)
        if index%2==0:
            tot = nums[index/2] + nums[1+(index/2)]
            tot = tot/2
            out = {'median' : tot, "nums" : '[' + str(nums) + ']'}
            return json.dumps(out), 200, {'Content-Type' : 'application'}
        else:
            tot = round(index/2)
            ret = nums[tot]
            out = {'median' : ret, "nums" : '[' + str(nums) + ']'}
            return json.dumps(out), 200, {'Content-Type' : 'application'}


app.run(host='127.0.0.1', port=3001)
