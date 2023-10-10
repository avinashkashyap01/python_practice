
from datetime import datetime

def getcurrenttime ():
    return datetime.now().strftime("%m-%d-%y %H:%M:%S")

class massenger :
    def __init__(self, listeners=[]):
        self.listeners = listeners

    def send (self,message):
        for listener in self.listeners:
            listener.receive(message)

    def receive (self,message):
        pass

class savemessages (massenger):
    def __init__(self,listeners=[]):
        super().__init__(listeners)
        self.messages = []

    def receive(self,message):
        self.messages.append({'message':message,'time':getcurrenttime()})

    def printmessages(self):
        for m in self.messages:
            print(f'message: "{m["message"]}" time: {m["time"]}')
        self.messages = []

listener = savemessages()

sender = massenger([listener])
sender.send('Hello there! This is the first message')
sender.send('Oh hi! This is the second message!')
sender.send('Hola! This is the last and final message!')

print(listener.printmessages())
