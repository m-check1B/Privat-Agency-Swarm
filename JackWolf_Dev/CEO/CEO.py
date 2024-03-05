from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class CEO(Agent):
    def __init__(self):
        super().__init__(
            name="CEO",
            description="The CEO acts as the primary contact point, delegating tasks to other agents within the agency. There are no specific tools assigned at the moment; tools will be handled manually later by the user.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools"
        )
