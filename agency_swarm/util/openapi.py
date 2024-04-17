
class BaseLLMClient:
    def initialize_model(self, model_name):
        raise NotImplementedError("This method should be implemented by subclasses")

    def send_prompt(self, prompt):
        raise NotImplementedError("This method should be implemented by subclasses")

    def receive_response(self):
        raise NotImplementedError("This method should be implemented by subclasses")
