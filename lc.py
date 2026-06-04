# This script demonstrates how to create a simple chain with two nodes using LangChain.
# The nodes are created from standard Python functions wrapped in RunnableLambda.
# Just adding to test 
from typing import Dict
from langchain_core.runnables import RunnableLambda

# Define the first function. This function takes a name and returns a greeting.
def greet_function(name: str) -> str:
    """
    A function that takes a string (a name) and returns a greeting.
    This will be our first node.
    """
    print("---EXECUTING GREET NODE---")
    return f"Hello, {name}! How can I help you today?"

# Define the second function. This function takes a greeting and returns a final response.
def respond_function(greeting: str) -> str:
    """
    A function that takes the greeting from the previous step and adds a response.
    This will be our second node.
    """
    print("---EXECUTING RESPOND NODE---")
    return f"{greeting} I am a simple LangChain example."

# 1. Create the nodes by wrapping the functions in RunnableLambda.
# RunnableLambda allows any Python function to be used as a step in a chain.
greet_node = RunnableLambda(greet_function)
respond_node = RunnableLambda(respond_function)

# 2. Chain the nodes together using the | operator.
# The output of the left side becomes the input for the right side.
chain = greet_node | respond_node

# 3. Invoke the chain with an input and print the final output.
# The input 'Alice' is passed to the 'greet_node', and its output is then passed to the 'respond_node'.
print("\n---RUNNING THE CHAIN---")
final_output = chain.invoke("Alice")

print("\n---FINAL OUTPUT---")
print(final_output)

# You can also run the chain with a different input.
print("\n---RUNNING THE CHAIN WITH ANOTHER INPUT---")
another_output = chain.invoke("Bob")
print("\n---FINAL OUTPUT---")
print(another_output)
