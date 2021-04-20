class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    
    def __init__(self, start):
        self.start = start
        self.counter = 0

    def generate(self):
        '''upon first generate(), display start number,
           every time its called after it will return start + 1 '''   
        current_num = self.start + self.counter 
        self.counter += 1
        return current_num
    
    def reset(self):
        '''when called, resets the increment counter to
           start back at beginning  '''
        self.counter = 0

    


    

