import requests, json
from flask import Flask, request, Response
import keywords
import json

app = Flask(__name__)

with open('chapters.json') as json_data:
    chapters_list = json.load(json_data)

def get_answer_keyword(chapter_id, answer):
    for c in chapters_list['chapters']:
        if int(c['id']) == int(chapter_id):
            for key, value in c['actions'].items():
                print key
                print answer
                if key == answer:
                    if str(value).isdigit():
                        return get_chapter(value)
                    else:
                        return get_chapter_answer(c['id'], value)
            return get_chapter_answer(c['id'], c['actions']['default'])

def get_chapter(chapter_id):
    for c in chapters_list['chapters']:
        if int(c['id']) == int(chapter_id):
            c_copy = dict(c)
            actions = []
            for key, value in c['actions'].items():
                if key != 'default':
                    actions.append(key)
            c_copy['actions'] = actions
            return json.dumps(c_copy)

def get_chapter_answer(chapter_id, display_text):
    for c in chapters_list['chapters']:
        if int(c['id']) == int(chapter_id):
            c_copy = dict(c)
            c_copy['display_text'] = display_text
            actions = []
            for key, value in c['actions'].items():
                if key != 'default':
                    actions.append(key)
            c_copy['actions'] = actions
            return json.dumps(c_copy)

@app.route('/<chapter>/<answer>/', methods = ['GET'])
def chapter_answer(chapter, answer):
    data_send = get_answer_keyword(chapter,answer)
    resp = Response(data_send, status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = "*"
    return resp

@app.route('/<chapter>/', methods = ['GET'])
def chapter(chapter):
    if chapter.isdigit():
        data_send = get_chapter(chapter)
    else:
        data_send = None
    resp = Response(data_send, status=200, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = "*"
    return resp

if __name__ == '__main__':
    app.debug = True
    app.run()
