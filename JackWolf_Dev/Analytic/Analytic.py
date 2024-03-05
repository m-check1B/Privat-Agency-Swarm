from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class Analytic(Agent):
    def __init__(self):
        super().__init__(
            name="Analytic",
            description="The Analytic agent focuses on research and data analysis to prepare insights for software development projects. It provides reports and insights back to CEO or directly to Assistant, if organizational tasks are needed based on the insights.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools"
        )
