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
            with open(os.path.join("templates", "index.html"), 'r') as f:
                html_content = f.read()
            return HTMLResponse(content=html_content, status_code=200)

        @self.app.websocket("/ws")
        async def websocket_endpoint(websocket: WebSocket):
            await websocket.accept()
            try:
                while True:
                    data = await websocket.receive_text()
                    message_data = json.loads(data)
                    response = await self.agency.process_message(
                        message_data["message"], 
                        message_data.get("agent_id"))
                    await websocket.send_text(json.dumps({"sender": "agent", "message": response}))
            except WebSocketDisconnect:
                print("WebSocket disconnected")

        @self.app.post("/upload")
        async def upload_file(file: UploadFile = File(...)):
            try:
                file_location = f"temp_files/{file.filename}"
                async with aiofiles.open(file_location, 'wb') as out_file:
                    content = await file.read()  # Read file content
                    await out_file.write(content)  # Save file locally
                
                # Assume a function to process the file like uploading to OpenAI
                file_id = await process_file(file_location)  # You would implement this
                
                return {"filename": file.filename, "file_id": file_id}
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.app.get("/get-agents")
        async def get_agents():
            # Hardcoded list of agent names
            agent_names = ['CEO', 'Analytic', 'Assistant']
            # Generate HTML string with option tags for each agent name
            options_html = "".join([f"<option value='{name}'>{name}</option>" for name in agent_names])
            return HTMLResponse(content=options_html)
        
        @self.app.post("/send-message")
        async def send_message(
            recipient_agent: str = Form(...), 
            message: str = Form(...), 
            files: List[UploadFile] = File(None)
        ):
            file_infos = await self.process_files(files)
            response = await self.agency.process_message(
                message, 
                recipient_agent, 
                file_infos)
            return JSONResponse({"sender": "agent", "message": response})

    async def process_files(self, files: List[UploadFile]):
        file_infos = []
        for file in files:
            # Implement logic to handle the file, such as saving or uploading
            file_id = await process_file(file)  # You would implement this
            file_infos.append(file_id)
        return file_infos

# Assume functions for processing files and messages are defined here
async def process_file(file: UploadFile):
    # Implement your logic to process the file
    return "processed_file_id"
