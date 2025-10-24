from flask import Flask
import asyncio

app = Flask(__name__)

async def background_task():
    await asyncio.sleep(5)
    print("Background task completed")

@app.route('/start-task')
def start_task():
    asyncio.run(background_task())  # Ensures an event loop runs the task
    return {"message": "Task started"}

if __name__ == '__main__':
    app.run(debug=True)