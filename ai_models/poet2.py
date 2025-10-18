from transformers import pipeline

generator = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")


# prompt="""Write the first line of a fact-based poetic verse about:A quiet forest after rain.
# The sun slowly breaks through the mist."""
# result = generator(prompt, max_length=300, num_return_sequences=5)
# print(result[0]['generated_text'])


def generate_second_line(first_line):
    prompt = f"Continue this poem with emotional depth:\n{first_line}\nNext line:"
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
    
