from FireBaseClass import EaV_DB_Util

if __name__ == '__main__':
    
    #Init FireBase
    firebaseClient = EaV_DB_Util.__new__(EaV_DB_Util)
    firebaseClient.__init__()

    data = {
        u'name': u'Vice City',
        u'state': u'Miami',
        u'country': u'USA'
    }

    while True:
        # Adding data
        firebaseClient.setData('cities', 'NY', data)

        # Reading the data
        firebaseClient.getData("cities")

        # get Image from FireBase
        firebaseClient.getImage("nhatrang.jpg")

        # set Image to FireBase
        firebaseClient.setImage("test1.jpg")