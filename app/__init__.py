from flask import Flask
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
from app import views 
