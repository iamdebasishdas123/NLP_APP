import json

class Database:
    def add_data(self, name, email, password):
        try:
            with open('data.json', 'r') as rf:
                database = json.load(rf)
        except FileNotFoundError:
            # If the file doesn't exist, initialize an empty dictionary
            database = {}

        if email in database:
            return 0
        else:
            database[email] = [name, password]
            with open('data.json', 'w') as wf:
                json.dump(database, wf)
            return 1

    def search(self,email,password):
        try:
            with open('data.json','r') as rf:
                database=json.load(rf)
                if email in database:
                    if database[email][1]==password:
                        return 1
                    else:
                        return 0
                else:
                    return 0
        except FileNotFoundError:
            database={}
