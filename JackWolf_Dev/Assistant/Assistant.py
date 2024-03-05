from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class Assistant(Agent):
    def __init__(self):
        super().__init__(
            name="Assistant",
            description="The Assistant handles organizational tasks assigned by the CEO and assists the Analytic with data organization. This agent may also manage interactions with external APIs or tools at a later stage.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools"
        )
