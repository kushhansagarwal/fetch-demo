"""
This script sets up and runs a Bureau to manage agents.

Modules and classes imported:
- Agent, Bureau, Context, Model from uagents
- Any, Dict from typing
- weather_agent from weather_agent module
- client_agent from weather_client module
"""

from uagents import Agent, Bureau, Context, Model
from typing import Any, Dict
from weather_agent import weather_agent
from weather_client import client_agent

# Create a Bureau to manage agents and add the client and weather agents to it
bureau = Bureau()
bureau.add(client_agent)
bureau.add(weather_agent)

# Run the Bureau if this script is executed as the main program
if __name__ == "__main__":
    bureau.run()
