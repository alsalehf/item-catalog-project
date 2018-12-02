from flask import Flask, render_template, request, redirect,jsonify, url_for, flash
app = Flask(__name__)

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

from flask import session as login_session
import random, string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests


#Connect to Database and create database session
engine = create_engine('sqlite:///itemcatalog.db',connect_args={'check_same_thread':False},echo = True)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#json representation of the item catalog
@app.route('/catalog.json')
def catalogJSON():
    '''
    categories = session.query(Category).all()
    catalog = {}
    for c in categories:
        items = session.query(Item).filter_by(category_id = c.id)
        catalog = catalog + jsonify(category  = c.serialize, item = [i.serialize for i in items])
    '''
    items = session.query(Item).all()
    return jsonify(item= [i.serialize for i in items])

#Show all cateogries and recent items
@app.route('/')
@app.route('/catalog/')
def showCategories():
    categories = session.query(Category).order_by(asc(Category.name))
    return render_template('catalog.html', categories = categories)

#Show a cateogry items
@app.route('/catalog/<string:category_name>/')
@app.route('/catalog/<string:category_name>/items/')
def showItems(category_name):
    category_ID = session.query(Category.id).filter_by(name = category_name).one()
    items = session.query(Item).filter_by(category_id = category_ID[0])
    return render_template('items.html', items = items,category_name = category_name)

#Show item info
@app.route('/catalog/<string:category_name>/<string:item_name>/')
def showOneItem(category_name,item_name):
    item = session.query(Item).filter_by(name = item_name).one()
    return render_template('iteminfo.html', item = item)

#Create a new item
@app.route('/catalog/items/new/',methods=['GET','POST'])
def newItem():
    if request.method == 'POST':
        cat_id = session.query(Category.id).filter_by(name = request.form['category']).one()
        newItem = Item(name = request.form['name'], description = request.form['description'],category_id = cat_id[0])
        session.add(newItem)
        flash('New item %s Successfully Created' % newItem.name)
        session.commit()
        return redirect(url_for('showItems',category_name=request.form['category']))
    else:
        return render_template('newItem.html')

#Edit an item
@app.route('/catalog/<string:item_name>/edit', methods=['GET','POST'])
def editItem(item_name):
    return "edit an item in the catalog"

#Delete a item
@app.route('/catalog/<string:item_name>/delete', methods = ['GET','POST'])
def deleteItem(item_name):
    return "delete item from the catalog"




if __name__ == '__main__':
  app.secret_key = 'super_secret_key'
  app.debug = True
  app.run(host = '0.0.0.0', port = 8000)
