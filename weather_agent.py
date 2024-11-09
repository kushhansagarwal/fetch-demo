from uagents import Agent, Bureau, Context, Model
import aiohttp
import time

# Define the API key for the weather service
WEATHER_API_KEY = "e971fa56856d479e842192758240911"

# Define a model for location messages
class LocationMessage(Model):
    """
    A model representing a message containing location information.
    
    Attributes:
        location (str): The location for which weather information is requested.
    """
    location: str

# Define a model for weather messages
class WeatherMessage(Model):
    """
    A model representing a message containing weather information.
    
    Attributes:
        weather_info (str): The weather information for a specific location.
    """
    weather_info: str


weather_agent = Agent(name="weather_agent", seed="weather_agent recovery phrase")

# Define a message handler for the weather agent to process received location messages
@weather_agent.on_message(model=LocationMessage)
async def weather_agent_message_handler(ctx: Context, sender: str, msg: LocationMessage):
    """
    Handles incoming location messages, fetches weather information, and sends it back to the sender.
    
    Args:
        ctx (Context): The context in which the message is received.
        sender (str): The address of the sender.
        msg (LocationMessage): The message containing the location information.
    """
    ctx.logger.info(f"Received location from {sender}: {msg.location}")  # Log the received location
    weather_info = await fetch_weather_info(msg.location)  # Fetch weather info for the location
    await ctx.send(sender, WeatherMessage(weather_info=weather_info))  # Send weather info back to sender

# Define an asynchronous function to fetch weather information from an API
async def fetch_weather_info(location: str) -> str:
    """
    Fetches weather information for a given location from a weather API.
    
    Args:
        location (str): The location for which to fetch weather information.
    
    Returns:
        str: The weather information for the specified location, or a default message if unavailable.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={location}") as response:
            data = await response.json()  # Parse the JSON response
            return data.get('current', {}).get('condition', {}).get('text', 'No weather info available')  # Extract weather info
