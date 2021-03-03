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
        """Initializes a serial number instance with a default value"""
        self.default = start - 1
        self.start = start - 1

    def __repr__(self):
        return f"<SerialGenerator start={self.default+1} next={self.start}>"
    
    def generate(self):
        """Returns next sequential serial number"""
        self.start += 1
        return self.start
    
    def reset(self):
        """Resets serial numaber to its default value"""
        self.start = self.default