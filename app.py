from poem_pipeline import poem_collaboration_pipeline
from utils.tts_output import text_to_audio

if __name__ == "__main__":
    file_path = input("Enter file path (image/pdf/doc): ")
    line1, line2, verdict = poem_collaboration_pipeline(file_path)
    
    print("\n--- Generated Poem ---")
    print("Poet 1:", line1)
    print("Poet 2:", line2)
    print("\n Verdict :")
    print(verdict)

    text_to_audio(f"{line1}. {line2}. {verdict}")
