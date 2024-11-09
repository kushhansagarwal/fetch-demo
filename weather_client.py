from uagents import Agent, Bureau, Context, Model
import aiohttp
import time

client_agent = Agent(name="client_agent", seed="client_agent recovery phrase")
weather_agent = Agent(name="weather_agent", seed="weather_agent recovery phrase")

class LocationMessage(Model):
    """
    A model representing a message containing location information.

    Attributes:
        location (str): The location for which weather information is requested.
    """
    location: str

class WeatherMessage(Model):
    """
    A model representing a message containing weather information.

    Attributes:
        weather_info (str): The weather information for a specific location.
    """
    weather_info: str

class PostRequest(Model):
    """
    A model representing a POST request containing location information.

    Attributes:
        location (str): The location for which weather information is requested.
    """
    location: str

class PostResponse(Model):
    """
    A model representing a response to a POST request.

    Attributes:
        location (str): The location for which weather information was requested.
        timestamp (int): The time at which the response was generated.
        agent_address (str): The address of the agent handling the request.
    """
    location: str
    timestamp: int
    agent_address: str

@client_agent.on_message(model=WeatherMessage)
async def handle_weather_response(ctx: Context, sender: str, msg: WeatherMessage):
    """
    Handles incoming weather messages and logs the weather information.

    Args:
        ctx (Context): The context in which the message is received.
        sender (str): The address of the sender.
        msg (WeatherMessage): The message containing the weather information.
    """
    ctx.logger.info(f"Received weather info from {sender}: {msg.weather_info}")

async def send_location(ctx: Context):
    """
    Sends location information to the weather agent based on user input.

    Args:
        ctx (Context): The context in which the function is executed.
    """
    location = input("Enter the location: ")
    await ctx.send(weather_agent.address, LocationMessage(location=location))
    ctx.logger.info(f"Sent location: {location}")

@client_agent.on_rest_post("/rest/post", PostRequest, PostResponse)
async def handle_post(ctx: Context, req: PostRequest) -> PostResponse:
    """
    Handles POST requests, sends location information to the weather agent, and returns a response.

    Args:
        ctx (Context): The context in which the request is received.
        req (PostRequest): The POST request containing location information.

    Returns:
        PostResponse: A response containing the location, timestamp, and agent address.
    """
    ctx.logger.info("Received POST request")
    await ctx.send(weather_agent.address, LocationMessage(location=req.location))
    return PostResponse(
        location=req.location,
        timestamp=int(time.time()),
        agent_address=ctx.agent.address
    )