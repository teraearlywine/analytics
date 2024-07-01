from src.assistants.core.core_assistant import CoreAssistant
from src.assistants.core.assistant_type import AssistantType
import re
import logging 

logging.basicConfig(level=logging.INFO, datefmt='%Y-%m-%d', format='%(levelname)s - %(asctime)s - %(message)s')

class DataGenerationAssistant(CoreAssistant):
    """
    Data Generation Assistant
    -------------------------

    An assistant that's sole purpose is to generate data that 
    can be used to either enrich other data, create test or temporary data, 
    or really anything you can think of. 

    Output will contain a python serialized list object
    """

    def __init__(self):
        super().__init__()

        self.assistant_type = AssistantType().data_engineer

    def __articulate_context(self, prompt): 
        """
        Articulate Context 
        ------------------
        Constructs a user message that articulates context to the ChatGPT user role

        Passes 'prompt' attribute specified by user to the message string
        Returns user message as string to be referenced by in the instruction request
        """

        user_message = f"""
            Create data for {prompt} and output as a comma separated string data type.
            Attribute headers must not exceed 4 elements. Return the column or attribute name first"""
        return user_message
    
    def make_request(self, prompt):
        """
        Independently makes request to OpenAI API 
        Returns the full chat completions class to support further processing and meta data collection
        """

        user_message = self.__articulate_context(prompt)
        return self.pass_instructions(self.assistant_type, user_message)
    
    def get_response_str(self, prompt): 
        """ 

        If the 'get_str' method is called, assume the output should be a python list data type
        Prompt must be provided by user. 

        Works independently from make request in case we would just like to get the message data. 
        """
        
        try:
            request = self.make_request(prompt)
            response = self.get_response(request)
            response = response.replace('\n', '')
            return response
        except Exception as err:
            logging.error(f'Something is wrong, see error: \n {err}')

    def generate_list(self, prompt):
        """
        Generate List Method
        ----------------
        Returns a python list object containing data from the prompt

        Processes data from the private '__get_response_str()' method as a python list.
        Removes the GPT output brackets, then removes the single quotation mark, replace with nothing.
        Last step splits the string at the comma sep (converting it to a list) and returns the final list.

        Usage:: 

            >>> prompt = "10 flower names"
            >>> assistant = DataGenerationAssistant()
            >>> data = assistant.generate_list(prompt=prompt)
        
        -----
        """

        output_str = self.get_response_str(prompt)
        assert isinstance(output_str, str), "GPT Response type must be a string"

        output_str = re.sub(r'"', '', output_str)
        output_list = output_str.split(sep=',')
        output_list = [i.strip() for i in output_list] # clean whitespace if exists

        assert isinstance(output_list, list), "Must be a list datatype, something is wrong"
        logging.info(f'Successfully converted string to list')
        return output_list


if __name__=="__main__":
    

    DataGenerationAssistant()