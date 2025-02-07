#operations file creating class operations with four static methods

class Operations:
    """ 
    This is a container for basic math operations
    creating instances of a class.
    """
    @staticmethod 
    def addition(a: float, b: float) -> float:
        """
        This method takes two numbers (a and b) and returns their sum """
        return a + b
    
    @staticmethod 
    def subtraction (a: float, b: float) -> float:
        return a - b
    
    @staticmethod 
    def multiplication (a: float, b: float) -> float:
        return a * b
    
    @staticmethod
    def division (a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division By 0 is not allowed.")
        return a / b
    
