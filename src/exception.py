import sys # it will have details of all errors
from src.logger import logging
def error_message_detail(error,error_detail:sys): # any exception will be returned as own custom message # error_detail is in the sys
    _,_,exc_tb=error_detail.exc_info() # it gives all the information of lineno, file name
    file_name=exc_tb.tb_frame.f_code.co_filename #exception handling documentation
    error_message="Error occured in python script [{0}] line number [{1}] error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))
    return error_message


class CustomException(Exception): # inheriting parent Exception
    def __init__(self, error_message,error_detail:sys): #error_detail of sys type # error cming frm
        super().__init__(error_message) #inherit init function
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
# for testing
# if __name__=='__main__':
#     try:
#         a=10/0
#     except Exception as e:
#         logging.info("Division by Zero")
#         raise CustomException(e,sys)
    
'''
The provided code defines a custom exception class named `CustomException`, which inherits from the built-in `Exception` class in Python.

Here's a breakdown of the code:

1. `class CustomException(Exception):`: This line declares a new class named `CustomException` that inherits from the `Exception` class.

2. `def __init__(self, error_message, error_detail: sys):`: This is the constructor method for the `CustomException` class. It takes two parameters:
   - `error_message`: A string representing the error message.
   - `error_detail`: An object of type `sys` representing additional error details.

3. `super().__init__(error_message)`: This line calls the constructor of the parent class (`Exception`) and
 passes the `error_message` to it. This initializes the exception with the provided error message.

4. `self.error_message = error_message_detail(error_message, error_detail=error_detail)`: 
This line seems to be intended to create an error message that combines the provided `error_message` and `error_detail`. 
However, there is a typo here (`error_message_detail` instead of `error_detail`). 
Additionally, `error_detail` is expected to be of type `sys`, but it's unclear what `sys` refers to here. 
It's likely meant to be a specific module or object that provides additional error details, but without further context, it's hard to determine its purpose.

5. `def __str__(self):`: This is the method that gets called when the exception is converted to a string, typically by using `str(exception_instance)`. 

6. `return self.error_message`: This line returns the `error_message` attribute of the `CustomException` instance. 
However, as mentioned earlier, there seems to be a typo in the assignment of `self.error_message`, so this might not behave as intended.

Overall, the intention of the code appears to be to create a custom exception class with an error message and additional error details. 
However, there are some issues in the implementation that need to be addressed for the code to work correctly.
'''