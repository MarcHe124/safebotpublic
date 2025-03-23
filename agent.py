#!/usr/bin/env python3
#
# This script uses a simple setup to demonstrate a way to provide a clean
# separation between conversational LLM agents and the UI elements.
#
# The key technique here is the use of Python generators.
#
import sys

################################################################################
# A fake ReACT agent emulating our current implementation
#
# Implemented as a generator
################################################################################
def ReACTAgent(prompts, state, transform=None):
  data = {}
  while state != 'stop':
    question, next_state = prompts[state]
    data[state] = yield question
    state = next_state
  return(transform(data) if transform else data)

def get_agent_response(agent, prompt):
  return(agent.send(prompt) if prompt else next(agent))

################################################################################
# A simple demographic agent
################################################################################
DEMO_PROMPTS = \
{
  'name'  : ('May I have your name please?', 'age'),
  'age'   : ('How old are you?', 'gender'),
  'gender': ('What is your gender at birth?', 'stop')
}

def DemoAgent():
  """
  Create an agent to collect demographic info from the user
  """
  def enhance(data):
    """
    Data returned by the agent is further enhanced by this function
    """
    if 'name' in data and ' ' in data['name']:
      data['initial'] = data['name'].split()[0][0]
    if 'gender' in data:
      gender = data['gender'].lower()
      if gender == 'boy':
        data['gender'] = 'male'
      elif gender == 'girl':
        data['gender'] = 'female'
      else:
        pass
    return(data)

  agent = ReACTAgent(DEMO_PROMPTS, 'name', transform=enhance)
  return(lambda prompt: get_agent_response(agent, prompt))

################################################################################
# A simple adverse event agent
################################################################################
AE_PROMPTS = \
{
  'event'  : ('Please describe the symptom you experienced.', 'onset'),
  'onset'  : ('When did the symptom first appear?', 'duration'),
  'duration': ('How long did the symptom last?', 'stop')
}

def AEAgent():
  """
  Create an agent to collect details of an adverse reaction from the user 
  """
  agent = ReACTAgent(AE_PROMPTS, 'event')
  return(lambda prompt: get_agent_response(agent, prompt))

################################################################################
# A composite agent to execute a collection of conversational agents one-by-one
################################################################################
def CompositeAgent(queue):
  """
  Create a super agent to run the conversational agents in the queue one-by-one
  """
  data  = {}
  label = None
  agent = None
  while True:
    try:
      if not agent:
        label, agent = queue.pop(0)
        agent_response = agent(None)
        user_response  = yield agent_response
      agent_response = agent(user_response)
      user_response  = yield agent_response
    except StopIteration as partial:
      data[label] = partial.value
      if queue == []:
        break
      else:
        label = None
        agent = None
  return(data)

################################################################################
# An agent to collect from user details of their adverse reactions
################################################################################
def SafetyAgent():
  """
  Creat an agent to collect safety information from the user
  """
  composite_agent = CompositeAgent([('demo', DemoAgent()), ('ae', AEAgent())])
  return(lambda prompt: get_agent_response(composite_agent, prompt))

################################################################################
# How the UI would interact with an agent
################################################################################
if __name__ == '__main__':

  # Create the agent of interest
  get_response = SafetyAgent()

  # First call to get the initial message from the agent
  agent_response = get_response(None)

  # Carry on the conversation with the agent through a single function call
  while True:
    try:
      print('Agent:', agent_response)
      print('User: ', end='')
      user_response = input()
      agent_response = get_response(user_response)
    except StopIteration as data:
      # This is the signal indicating the agent has returned the data it collected
      print(data.value)
      break
