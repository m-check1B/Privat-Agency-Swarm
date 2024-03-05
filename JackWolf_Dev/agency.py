from agency_swarm import Agency
from Assistant import Assistant
from Analytic import Analytic
from CEO import CEO
import uvicorn
from agency_swarm import agency
from gui import FastAPIGUI

ceo = CEO()
analytic = Analytic()
assistant = Assistant()

agents_bar = [ceo, analytic, assistant]

agency = Agency([ceo, [ceo, analytic], [ceo, assistant], [analytic, assistant]],
                shared_instructions='./agency_manifesto.md')

# Initialize the FastAPI GUI with the agency instance
gui_app = FastAPIGUI(agency)

if __name__ == "__main__":
    uvicorn.run(gui_app.app, host="0.0.0.0", port=8000)  # Use the FastAPI app from the GUI class instance#agency.demo_gradio()
    #agency.run_demo()
