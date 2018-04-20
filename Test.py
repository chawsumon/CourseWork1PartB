from flask import Flask, render_template,request
import json

w = json.load(open("worldl.json"))
print (len(w))
print (w[0])
print (w[0]['gdp'])
print (w[0]['name'])
print (w[0]['area'])
print (w[0]['tld'])
print (w[0]['capital'])
print (w[0]['continent'])
print (w[0]['population'])