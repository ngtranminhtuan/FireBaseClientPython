import firebase_admin
from firebase_admin import credentials, db, firestore, storage
import os
import cv2



class EaV_DB_Util:
    def __init__(self):
        # default create database when init instance
        # Now access FireBase use key in JSON file
        # In the future will upgrade more...
        cred = credentials.Certificate("Authen.json")
        firebase_admin.initialize_app(cred, {
            'storageBucket': 'gs://pythonandfirebase-cdb56.appspot.com'
        })
        self.db = firestore.client()

    # --------------Authorization function in below-------------- 
    def email_auth(self):
        pass

    def facebook_auth(self):
        pass

    def googleMail_authen(self):
        pass
    
    # --------------Get/Set Image from/to FireBase--------------
    def getImage(self, imageName):
        print("Get Image from firebase")
        blob = storage.bucket('pythonandfirebase-cdb56.appspot.com').blob('data/' + imageName)
        blob.download_to_filename("data/nhatrang.jpg")

    def setImage(self,imageName):
        print("Push Image to firebase")
        blob = storage.bucket('pythonandfirebase-cdb56.appspot.com').blob('data/' + imageName)
        blob.upload_from_filename('data/nhatrang_dem.jpg') # path to file on local disk
        print(blob.public_url) 

    # --------------Setter - data is dictionary or json--------------       
    def setData(self, collectionName, documentName, data):
        self.db.collection(collectionName).document(documentName).set(data)

    # --------------Getter--------------
    def getCollection(self, collectionName):
        return self.createFbClient().collection(collectionName)

    def getDocument(self, collectionName, documentName):
        return self.collection(collectionName).document(documentName)
    
    def getData(self, collectionName):
        colletionRef = self.db.collection(collectionName)
        docs = colletionRef.stream()

        for doc in docs:
            print('{} => {} '.format(doc.id, doc.to_dict()))
        
        return docs
