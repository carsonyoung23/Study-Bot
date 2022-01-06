import os
import openai

openai.api_key = os.environ['key']

response = openai.Completion.create(

  temperature=1,
  max_tokens=int(input("How advanced do you want this to be: 1 (basic) - 2000 (very advanced)?: ")),
  top_p=1,
  best_of=2,
  frequency_penalty=0,
  presence_penalty=0,
    engine="davinci-instruct-beta",
  prompt="What are some key points I should know when studying:" + input(str("what are you studying?: ")) + "\n1.",
)


print("\nYou should study the following things:" + "\n\n" + response["choices"][0]["text"])

