from google.adk.agents import Agent
from helper_agent.prompt import AGENT_INSTRUCTION

root_agent = Agent(
  name="root_agent",
  model="gemini-live-2.5-flash-preview-native-audio-09-2025", 
  description="An agent designed to assist people technology issues. It provides clear, step-by-step guidance to help users accomplish everyday tasks on their phones,speakers, computers, such as sending photos, using apps, connecting to Wi-Fi and so on",
  instruction=AGENT_INSTRUCTION,
  
)