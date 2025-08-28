import sys
import traceback

def error_msg_details (error, error_detail:sys):

    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = exc_tb.tb_frame.f_code.co_filename   # File name
    line_no = exc_tb.tb_lineno                   # Line number 
    error_message = f"Error: {error} \nType: {exc_type.__name__} \nFile: {fname} \nLine: {line_no}"
 
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_msg_details(error_message, error_detail=error_detail) 
    def __str__(self):
        return self.error_message
    