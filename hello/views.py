from django.shortcuts import render

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#cred = credentials.Certificate("/home/gcreinal/Documentos/Devel/Django/TesteFirebase/TesteFirebase/teste/testepython-d9243-firebase-adminsdk-yhrg6-8bfa0ca2c7.json")
cred = credentials.Certificate("hello/testepython-d9243-firebase-adminsdk-yhrg6-8bfa0ca2c7.json")

default_app = firebase_admin.initialize_app(cred, {
    'projectId': 'testepython-d9243',
})



# Create your views here.
def index(request):

    db = firestore.client()
    doc_ref = db.collection(u'users').document(u'alovelace')
    doc_ref.set({
        u'first': u'Ada',
        u'last': u'Lovelace',
        u'born': 1815
    })

    doc_ref = db.collection(u'users').document(u'aturing')
    doc_ref.set({
        u'first': u'Alan',
        u'middle': u'Mathison',
        u'last': u'Turing',
        u'born': 1912
    })

    users_ref = db.collection(u'users')
    docs = users_ref.stream()

    lista = []
    for doc in docs:
        lista.append(doc.to_dict())  
        print(u'{} => {}'.format(doc.id, doc.to_dict()))

    

    #print(default_app, cred)
    context = {
        'docs': lista

    }


    return render(request, 'hello.html', context )
