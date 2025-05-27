from hashlib import md5
from requests import get 
from datetime import datetime

class RestMarvel:
    timestamp = datetime.now().strftime('%Y-%m-%d%H:%M:%S')
    pub_key = '041e73468256c4e4790e4935ef134404'
    priv_key = 'd408cce99aa64ba211b32cf4f346a9271caa112e'

    def hash_params(self):
        hash_md5 = md5()
        hash_md5.update(f'{self.timestamp}{self.priv_key}{self.pub_key}'.encode('utf-8'))
        hashed_params = hash_md5.hexdigest()
        return hashed_params
    

    def get_heroes(self):
        params = {'ts': self.timestamp,'apikey': self.pub_key,'hash':self.hash_params()}
        results = get('https://gateway.marvel.com:443/v1/public/characters', params=params)
        

        data = results.json()
        print(data)
        print(data['status'])


rest = RestMarvel()
rest.get_heroes()


