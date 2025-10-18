from sentence_transformers import SentenceTransformer, util
from textblob import TextBlob

model = SentenceTransformer('all-MiniLM-L6-v2')

def judge_poem(first_line, second_line):
    # Semantic Similarity 
    embeddings = model.encode([first_line, second_line])
    similarity = util.cos_sim(embeddings[0], embeddings[1]).item()

   

    # Sentiment
    sentiment1 = TextBlob(first_line).sentiment.polarity
    sentiment2 = TextBlob(second_line).sentiment.polarity
    emotion_score = abs(sentiment2 - sentiment1)
   
    final_score = (0.4 * similarity) + (0.2 * (1 - emotion_score))

    verdict = "Poet 1" if final_score < 0.5 else "Poet 2"

    return (
        f"Judge's Verdict: {verdict} wrote the better verse "
        f"(similarity={similarity:.2f}, emotion={emotion_score:.2f})"
    )

