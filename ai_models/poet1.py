from transformers import pipeline

generator = pipeline("text-generation", model="gpt2-medium")

# prompt="""Write the first line of a fact-based poetic verse about:A quiet forest after rain.
# The sun slowly breaks through the mist."""
# result = generator(prompt, max_length=300, num_return_sequences=5)
# print(result[0]['generated_text'])

def generate_first_line(context):
    prompt = f"A short poetic line about {context}:\n"
    output = generator(
        prompt,
        max_length=80,
        temperature=0.95,
        top_p=0.92,
        repetition_penalty=1.2,
        do_sample=True,
        num_return_sequences=1,
    )
    
    return output[0]['generated_text'].strip()





