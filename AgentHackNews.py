from typing import Iterator
from agno.agent import Agent, RunOutput, RunOutputEvent, RunEvent
from agno.models.anthropic import Claude
from agno.tools.hackernews import HackerNewsTools
from agno.utils.pprint import pprint_run_response

agent = Agent(
    model=Claude(id="claude-3-5-haiku-latest", max_tokens=4096),
    tools=[HackerNewsTools()],
    instructions="Write a report on the topic. Output only the reporrt and resources used. Consider the alphabetical order of the resources.",
    markdown=True,
)

# Run agent and return the response as a variable
response: RunOutput = agent.run("Trending startups and products.")
# Print the response
print(response.content)

################ STREAM RESPONSE #################
stream: Iterator[RunOutputEvent] = agent.run("Trending products", stream=True)
for chunk in stream:
    if chunk.event == RunEvent.run_content:
        print(chunk.content)

# ################ STREAM AND PRETTY PRINT #################
stream: Iterator[RunOutputEvent] = agent.run("Trending products", stream=True)
pprint_run_response(stream, markdown=True)
