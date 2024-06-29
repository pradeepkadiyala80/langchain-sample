from typing import Annotated, Literal, TypedDict

from langgraph.graph import END, StateGraph, MessagesState
from langgraph.checkpoint import MemorySaver

from langchain_core.messages import HumanMessage

from wm.agents.wm_agent import WealthManagementAgent

import sys

# Define the function that determines whether to continue or not
def should_continue(state: MessagesState) -> Literal["agent"]:
    return END

# Create agent
WealthManagementAgent = WealthManagementAgent("./files/")
agent = WealthManagementAgent.agent_executor()

# Define a new graph
workflow = StateGraph(MessagesState)

# Define the two nodes we will cycle between
workflow.add_node("agent", agent)

# Set the entrypoint as `agent`
# This means that this node is the first one called
workflow.set_entry_point("agent")

# We now add a normal edge to `agent`.
workflow.add_edge('agent')

# We now add a conditional edge
workflow.add_conditional_edges(
    # First, we define the start node. We use `agent`.
    # This means these are the edges taken after the `agent` node is called.
    "agent",
    # Next, we pass in the function that will determine which node is called next.
    should_continue,
)

# Initialize memory to persist state between graph runs
checkpointer = MemorySaver()

# Finally, we compile it!
# This compiles it into a LangChain Runnable,
# meaning you can use it as you would any other runnable.
# Note that we're (optionally) passing the memory when compiling the graph
app = workflow.compile(checkpointer=checkpointer)

while True:
    query = input('Prompt: ')
    #To exit: use 'exit', 'quit', 'q', or Ctrl-D.",
    if query.lower() in ["exit", "quit", "q"]:
        print('Exiting')
        sys.exit()

    human_msg = HumanMessage(content=query)
    # Use the Runnable
    final_state = app.invoke(
        {
            "messages": [human_msg]
        },
        config={"configurable": {"thread_id": 42}}
    )    
    print(final_state["messages"])
