import os
import openai

openai.api_key = "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"
prompt = input()
response = openai.Completion.create(
  model="text-davinci-002",
  prompt= prompt,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(prompt, response.choices[0].text)

# # list engines
# engines = openai.Engine.list()

# # print the first engine's id
# print(engines.data[0].id)

# # create a completion
# completion = openai.Completion.create(engine="davinci", prompt="4 + 4 equals ")

# # print the completion
# print(completion.choices[0].text)

