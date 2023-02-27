from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import join_room, leave_room, emit, send, SocketIO, disconnect
import random
from string import ascii_uppercase, digits

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcde'
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app, debug=True)

