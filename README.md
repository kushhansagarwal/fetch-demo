# Setup Instructions

Follow these steps to set up and run the weather agent and client agent:

1. **Clone the repository:**
   ```sh
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Create a virtual environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the Bureau:**
   ```sh
   python app.py
   ```

5. **Interact with the client agent:**
   - To send a location message, run the following command and follow the prompt:
     ```sh
     python -c "from weather_client import send_location; send_location()"
     ```

   - To send a POST request, you can use a tool like `curl` or Postman:
     ```sh
     curl -X POST http://localhost:8000/rest/post -H "Content-Type: application/json" -d '{"location": "New York"}'
     ```

These instructions will help you set up and run the weather agent and client agent, allowing you to fetch weather information for specified locations.
