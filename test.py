class First:
    def __init__(self):
        super().__init__()
        self.var = 'Hey'
    
    def print_hello(self):
        print('Hello')
  
class Fourth(First):
    def __init__(self):
        super().__init__()

f = Fourth()
print(f.var)
f.print_hello()