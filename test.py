import html2text
import openai

data = ''
h = html2text.HTML2Text()

with open("amara-page.html", "r", encoding='utf-8') as f:
    data = h.handle(f.read())

openai.api_key = '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'

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = "get product name, price, currency, thumbnails from "+data+"";

# Generate a response
completion = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=40000,
    top_p=1,
    frequency_penalty=0,
    n=1,
    stop=None,
    temperature=0.7,    
)

response = completion.choices[0].text
print(response)