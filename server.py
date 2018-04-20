from flask import Flask, render_template,request
import json

page_number =10
w = json.load(open("worldl.json"))
lota = sorted(list(set([c['name'][0] for c in w])))
print(lota)
for c in w:
    c['tld'] = c['tld'][1:]
page_size = 20

l =[]
for i in range(ord('A'),ord('Z')+1):
    l.append(chr(i))



app = Flask(__name__)


@app.route('/')
def mainPage():
    le = len(w)
    return render_template('index.html',
                           w=w[0:page_size],page_number=0,page_size=page_size,le=le,lota=lota)

@app.route('/sortCountryName')
def sortCountryName():
    # cl =[]
    # for i in range(ord('A'),ord('Z')+1):
    #     cl.append(chr(i))
    return render_template('sorttCountryNameWithAlphabetically.html',l=l)

@app.route('/begin/<b>')
def beginPage(b):
    bn = int(b)
    li = len(w)
    return render_template('index.html',
                           w=w[bn:bn + page_size],
                           page_number=bn,
                           page_size=page_size,li=li,l=l
                           )


@app.route('/continent/<a>')
def continentPage(a):
    cl = [c for c in w if c['continent'] == a]
    return render_template(
        'continent.html',
        length_of_cl=len(cl),
        cl=cl,
        a=a
    )

@app.route('/createCountry/')
def createCountry():
    return render_template('createCountry.html')

@app.route('/country/<i>')
def countryPage(i):
    return render_template(
        'country.html',
        c=w[int(i)])


@app.route('/countryByName/<n>')
def countryByNamePage(n):
    c = None
    for x in w:
        if x['name'] == n:
            c = x
    return render_template(
        'country.html',
        c=c)


@app.route('/editCountryByName/<n>')
def editCountryByNamePage(n):
    c = None
    for x in w:
        if x['name'] == n:
            c = x
    return render_template(
        'country-edit.html',
        c=c)

@app.route('/startWithAlphabetic/<a>')
def startWithAlphabetic(a):
    cl = [c for c in w if c['name'][0] == a]
    return render_template(
        'continent.html',a=a,length_of_cl=len(cl),
        cl=cl,l=l,lota=lota)

@app.route('/updateCountryByName')
def updateCountryByNamePage():
    n=request.args.get('name')
    c = None

    for x in w:
        if x['name'] == n:
            c = x
    c['capital']=request.args.get('capital')
    c['continent']=request.args.get('continent')
    return render_template(
        'country.html',
        c=c)

@app.route('/addNewCountry')
def addNewCountry():
    c={}
    c['capital'] = request.args.get('capital')
    c['name'] = request.args.get('name')
    c['continent'] = request.args.get('continent')
    c['area'] =int(request.args.get('area'))
    c['population'] = int(request.args.get('population'))
    c['gdp'] = int(request.args.get('gdp'))
    c['tld']=request.args.get('tld')
    w.append(c)
    return render_template('country.html',c=c)

@app.route('/delete/<n>')
def deleteCountry(n):
    i=0
    for c in w:
        if c['name']==n:
            break
        i=i+1
    del w[i]
    return render_template(
        'index.html',
        page_number=0,
        page_size=page_size,
        w=w[0:page_size])

    

if __name__ == "__main__":
    app.run(debug=True)
