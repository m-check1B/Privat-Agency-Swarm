from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Form, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from typing import List
import json
import os
import aiofiles

class FastAPIGUI:
    def __init__(self, agency):
        self.agency = agency
        self.app = FastAPI()
        self.app.mount("/static", StaticFiles(directory="static"), name="static")
        self.setup_routes()

    def setup_routes(self):
        @self.app.get("/", response_class=HTMLResponse)
        async def root():
            with open("templates/index.html", 'r') as f:
                html_content = f.read()
            return HTMLResponse(content=html_content, status_code=200)

        @self.app.websocket("/ws")
        async def websocket_endpoint(websocket: WebSocket):
            await websocket.accept()
            try:
                while True:
                    data = await websocket.receive_text()
                    message_data = json.loads(data)
                    response = await self.process_message(message_data["message"], message_data.get("agent_id"))
                    await websocket.send_text(json.dumps({"message": response}))
            except WebSocketDisconnect:
                print("WebSocket disconnected")

        @self.app.post("/upload")
        async def upload_file(file: UploadFile = File(...)):
            file_location = f"temp_files/{file.filename}"
            async with aiofiles.open(file_location, 'wb') as out_file:
                content = await file.read()
                await out_file.write(content)
            file_id = await self.process_file(file_location)
            return {"filename": file.filename, "file_id": file_id}

        @self.app.get("/get-agents")
        async def get_agents():
            agent_names = self.agency.get_agent_names()  # Implement to fetch dynamic agent names
            return JSONResponse(agent_names)

        @self.app.post("/send-message")
        async def send_message(message: str = Form(...), files: List[UploadFile] = File(None)):
            file_infos = await self.process_files(files)
            response = await self.process_message(message, file_infos)
            return JSONResponse({"message": response})

    async def process_files(self, files: List[UploadFile]):
        file_infos = []
        for file in files:
            file_id = await self.process_file(file)
            file_infos.append({"file_id": file_id, "filename": file.filename})
        return file_infos

    async def process_message(self, message: str, agent_id: str = None, file_infos: List = None):
        # Placeholder for processing logic; you might integrate with OpenAI's API or other services here.
        # For example, sending the message to an AI model and getting a response:
        response = await self.agency.get_ai_response(message, agent_id, file_infos)
        return response

    async def process_file(self, file: UploadFile):
        # Save the file asynchronously and possibly process it.
        file_location = f"temp_files/{file.filename}"
        async with aiofiles.open(file_location, 'wb') as out_file:
            # Read the content of the file asynchronously
            content = await file.read()
            await out_file.write(content)

        # Assuming there's some processing logic, which could involve AI analysis, data extraction, etc.
        processed_output = "processed_file_id"  # This is a placeholder for the actual output from the file processing logic.
        
        # Optionally, you could return details about the processed file, its location, or results from any analysis.
        return {
            "filename": file.filename,
            "location": file_location,
            "processed_output": processed_output
        }