class Delegate:
    def do_something(self):
        print('Delegate doing something')

class Delegator:
    def __init__(self, delegate):
        self.delegate = delegate
        print('in class Delegator')

    def do_something(self):
        self.delegate.do_something()
        print('In do something')
       

delegate = Delegate()
delegator = Delegator(delegate)
delegator.do_something()
# Output: Delegate doing something
