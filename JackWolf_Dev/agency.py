from agency_swarm import Agency
from Assistant import Assistant
from Analytic import Analytic
from CEO import CEO

ceo = CEO()
analytic = Analytic()
assistant = Assistant()

agency = Agency([ceo, [ceo, analytic],
                 [ceo, assistant],
                 [analytic, assistant]],
                shared_instructions='./agency_manifesto.md')

if __name__ == '__main__':
    agency.demo_gradio()