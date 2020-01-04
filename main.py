# -*- coding:utf-8 -*-
from flask import Flask,request,redirect,jsonify,render_template,Response,make_response
import json
import os
from shutil import copytree,rmtree
import pandas as pd


app = Flask(__name__)

option_list = ['艾滋病新增人数世界地图', '颁布法律前，中，后对比', '分省艾滋人数2008', '分省艾滋人数2018', '新增艾滋病人数对比']

@app.route('/',methods=['GET'])
def index():
    df = pd.read_csv( 'csv_conf/合法国家地区.csv', encoding='utf-8', delimiter="," )
    regions_available = list( df)
    data_str = df.to_html( )
    return render_template('index.html',the_res = data_str,option_list=option_list)


@app.route('/detailed',methods=['POST'])
def detailed():
    option = request.form['option']
    if option == "艾滋病新增人数世界地图":
        return redirect('/analysis_one')
    elif option == "颁布法律前，中，后对比":
        return redirect('/analysis_two')
    elif option == "分省艾滋人数2008":
        return redirect('/analysis_three')
    elif option == "分省艾滋人数2018":
        return redirect('/analysis_four')
    elif option == "新增艾滋病人数对比":
        return redirect('/analysis_five')
    else:
        return "异常"


@app.route('/analysis_one',methods=['GET'])
def analysis_one():
    if not request.args.get('type') == None:
        return render_template( 'analysis_one.html', option_list=option_list )
    df = pd.read_csv( 'csv_conf/adult newly infected with HIv.csv', encoding='utf-8', delimiter="," )
    regions_available = list(df)
    data_str = df.to_html( )
    return render_template('analysis_one.html',the_res = data_str,option_list=option_list)

@app.route('/analysis_two',methods=['GET'])
def analysis_two():
    if not request.args.get('type') == None:
        return render_template( 'analysis_two.html', option_list=option_list )
    df = pd.read_csv( 'csv_conf/legalcountryfinal.csv', encoding='utf-8', delimiter="," )
    regions_available = list(df)
    data_str = df.to_html( )
    return render_template('analysis_two.html',the_res = data_str,option_list=option_list)

@app.route('/analysis_three',methods=['GET'])
def analysis_three():
    if not request.args.get('type') == None:
        return render_template( 'analysis_three.html', option_list=option_list )
    df = pd.read_csv( 'csv_conf/chinafensheng.csv', encoding='utf-8', delimiter="," )
    regions_available = list(df)
    data_str = df.to_html( )
    return render_template('analysis_three.html',the_res = data_str,option_list=option_list)


@app.route('/analysis_four',methods=['GET'])
def analysis_four():
    if not request.args.get('type') == None:
        return render_template( 'analysis_four.html', option_list=option_list )
    df = pd.read_csv( 'csv_conf/chinafensheng.csv', encoding='utf-8', delimiter="," )
    regions_available = list(df)
    data_str = df.to_html( )
    return render_template('analysis_four.html',the_res = data_str,option_list=option_list)


@app.route('/analysis_five',methods=['GET'])
def analysis_five():
    if not request.args.get('type') == None:
        return render_template( 'analysis_five.html', option_list=option_list )
    df = pd.read_csv( 'csv_conf/legalcountry.csv', encoding='utf-8', delimiter="," )
    regions_available = list(df)
    data_str = df.to_html( )
    return render_template('analysis_five.html',the_res = data_str,option_list=option_list)


if __name__ == '__main__':
    app.run(debug=True,port=8080)

