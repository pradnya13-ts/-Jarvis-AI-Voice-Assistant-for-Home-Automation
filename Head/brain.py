import sys
import threading
import time
import webbrowser
import re
from wikipedia import wikipedia, exceptions as wiki_exceptions
from sentence_transformers import SentenceTransformer, util
import torch
import random
from Head.mouth import speak

# ----------------------------------------
# QnA File Management
# ----------------------------------------

qa_file_path = r"C:\Users\Dell\PycharmProjects\Jarvis 4.0\Data\brain_data\qna_data.txt"

def load_qa_data(file_path):
    qa_pairs = []
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            if ":" in line:
                q, a = line.strip().split(":", 1)
                qa_pairs.append((q.strip(), a.strip()))
    return qa_pairs

def save_qa_data(file_path, qa_pairs):
    with open(file_path, "w", encoding="utf-8") as f:
        for q, a in qa_pairs:
            f.write(f"{q} : {a}\n")

# ----------------------------------------
# SentenceTransformer Model & Embeddings
# ----------------------------------------

model = SentenceTransformer('all-MiniLM-L6-v2')

def reload_embeddings():
    global qa_pairs, questions, question_embeddings
    qa_pairs = load_qa_data(qa_file_path)
    questions = [q for q, _ in qa_pairs]
    question_embeddings = model.encode(questions, convert_to_tensor=True)

reload_embeddings()

# ----------------------------------------
# Personality Response Wrapper
# ----------------------------------------

def personality_wrap(answer, mode):
    if mode == "humor":
        return random.choice([
            f"Well, here's a fun twist: {answer}. Try not to laugh!",
            f"Boom! Did you expect this? {answer}",
            f"Haha! {answer}... and that's the fun fact of the day!"
        ])
    elif mode == "sarcastic":
        return random.choice([
            f"Oh wow, you didn’t know that? It's obviously {answer}.",
            f"Seriously? Even a toaster knows {answer}.",
            f"Let me use my *superior intelligence* to tell you: {answer}."
        ])
    elif mode == "poetic":
        return random.choice([
            f"In whispers of code, it’s said: {answer}.",
            f"Let the winds of knowledge carry this: {answer}.",
            f"As stars align, the truth appears: {answer}."
        ])
    return answer  # Default mode

# ----------------------------------------
# Main Mind Function
# ----------------------------------------

def mind(user_input, mode="default"):
    input_embedding = model.encode(user_input, convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(input_embedding, question_embeddings)
    best_match_idx = torch.argmax(cosine_scores).item()
    best_score = cosine_scores[0][best_match_idx].item()
    raw_answer = qa_pairs[best_match_idx][1]
    return personality_wrap(raw_answer, mode), best_score

# ----------------------------------------
# Utilities
# ----------------------------------------

def print_animated_message(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def clean_prompt(prompt):
    cleaned = prompt.strip()
    print(f"[Cleaned Prompt] '{cleaned}'")
    return cleaned

# ----------------------------------------
# Wikipedia Search
# ----------------------------------------

def wiki_search(prompt):
    search_prompt = clean_prompt(prompt)
    try:
        results = wikipedia.search(search_prompt)
        if not results:
            print("No Wikipedia results. Going to Google.")
            google_search(prompt)
            return
        page = wikipedia.page(results[0])
        summary = wikipedia.summary(page.title, sentences=2)
        threading.Thread(target=speak, args=(summary,)).start()
        print_animated_message(summary)

        # Save & reload
        if not any(prompt.strip().lower() == q.lower() for q, _ in qa_pairs):
            qa_pairs.append((prompt.strip(), summary.strip()))
            save_qa_data(qa_file_path, qa_pairs)
            reload_embeddings()

    except wiki_exceptions.DisambiguationError:
        speak("That topic is too broad. Please be more specific.")
    except wiki_exceptions.PageError:
        google_search(prompt)

# ----------------------------------------
# Google Search
# ----------------------------------------

def google_search(query):
    query = clean_prompt(query)
    if query:
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open_new_tab(url)
        speak(f"Opening Google search results for {query}")
    else:
        speak("Sorry, I didn't catch that.")

# ----------------------------------------
# Main Brain Function (Personality-aware)
# ----------------------------------------

def brain(text, mode="default"):
    try:
        response, score = mind(text, mode=mode)

        # Fallback to Wikipedia for uncertain answers
        if score < 0.80 or len(text.split()) >= 7:
            wiki_search(text)
            return

        threading.Thread(target=speak, args=(response,)).start()
        print_animated_message(response)

        # Save & reload
        if not any(text.strip().lower() == q.lower() for q, _ in qa_pairs):
            qa_pairs.append((text.strip(), response.strip()))
            save_qa_data(qa_file_path, qa_pairs)
            reload_embeddings()

    except Exception as e:
        print(f"Error: {e}")
        wiki_search(text)

