""" 
Create an assistant data type object for reusability purposes and ongoing development
TODO: add logging
TODO: potentially break these a part by model / use case? 
TODO: add function call parameter
"""


class CoreAssistant:
    """
    Assistant
    ----------
        Configuration and initialization of the OpenAI GPT model.
        Will be used as base class for future system / user message iterations.

    Methods
    -------
        get_chat_response: str


    Documentation
    -------------

    + https://github.com/openai/openai-python
    + https://platform.openai.com/docs/libraries/python-library
    + https://cookbook.openai.com/examples/reproducible_outputs_with_the_seed_parameter

    """

    def __init__(self):
        from openai import OpenAI

        self.gpt_client = OpenAI()
        self.gpt_model = "gpt-4"
        self.temperature = 0.05
        self.seed = 1 # Makes deterministic
        self.max_tokens = 150

    # TODO: create a read sql file or something
    def pass_instructions(self, assistant_type, prompt, tool_choice=None):
        """
        Parameters
        ----------
            user_request: string
                provde the instructions to the AI for inference

        Usage::

            >>> user_request = 'Create deterministic sql assertions for any of the following code. Assume it's SQL: {}'
            >>> assistant = CoreAssistant()
            >>> assistant.pass_instructions(assistant_type, user_request)

        -----
        """

        chat_completion = self.gpt_client.chat.completions.create(
            messages=[
                {"role": "system", "content": f"you are a helpful {assistant_type} assistant"},
                {"role": "user", "content": f"{prompt}"},
                {"role": "user", "content": "The response should contain no additional text, backticks or code (thank you)"},
                # {"role": "user", "content": "The output result should only be in a python structured list datatype."}
            ],
            model=self.gpt_model,
            # seed=self.seed,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=1,
            tool_choice=tool_choice
        )
        return chat_completion

        
    def get_response(self, request):
        """
        Passes the chat completions request through the class message access point
        The request parameter being all OpenAI related details such as token cost, 
        deterministic UUID etc.
        
        :param request: 
        :return: 
            generated_data: parsed out message content from the open AI response
        """
        
        generated_data = request.choices[0].message.content
        return generated_data


    def get_metadata(self, request):
        """
        
        Usage::

            >>> prompt = "10 beers"
            >>> assistant = DataGenerationAssistant()
            >>> request = assistant.make_request(prompt)
            >>> response = assistant.get_metadata(request)
            >>> print(response)
            
        """
        sys_fingerprint = request.system_fingerprint
        metadata = request.usage
        return metadata

if __name__ == "__main__":
    CoreAssistant()
