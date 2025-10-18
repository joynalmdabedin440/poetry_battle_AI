from ai_models.poet1 import generate_first_line
from ai_models.poet2 import generate_second_line
from ai_models.judge import judge_poem
from utils.extract_text import extract_text

def poem_collaboration_pipeline(file_path):
    context = extract_text(file_path)
    line1 = generate_first_line(context)
    line2 = generate_second_line(line1)
    verdict = judge_poem(line1, line2)
    return line1, line2, verdict
