from flask import Flask, jsonify, render_template, url_for, request, redirect, make_response, session, Response
from flask_sqlalchemy import *
import datetime
from sqlalchemy import Column, Integer, DateTime
import cv2
camera=cv2.VideoCapture(0)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://postgres:root@localhost:5432/iot_automation"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'My Secret Key'
from DBmodels import db


