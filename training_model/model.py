import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Head.mouth import speak
import random

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)


def load_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        qna_pairs = []
        for line in lines:
            if ':' in line:
                parts = line.strip().split(':', 1)
                if len(parts) == 2:
                    qna_pairs.append(parts)
        dataset = [{'question': q.strip(), 'answer': a.strip()} for q, a in qna_pairs]
    return dataset


def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    tokens = word_tokenize(text.lower())
    tokens = [ps.stem(token) for token in tokens if token.isalnum() and token not in stop_words]
    return ' '.join(tokens)


def train_tfidf_vectorizer(dataset):
    corpus = [preprocess_text(qa['question']) for qa in dataset]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    return vectorizer, X


def get_answer(question, vectorizer, X, dataset):
    question = preprocess_text(question)
    question_vec = vectorizer.transform([question])
    similarities = cosine_similarity(question_vec, X)
    best_match_index = similarities.argmax()
    return dataset[best_match_index]['answer']


# 🧠 Main intelligent response function
def mind(text):
    dataset_path = r'C:\Users\Dell\PycharmProjects\Jarvis 4.0\Data\brain_data\qna_data.txt'
    dataset = load_dataset(dataset_path)
    vectorizer, X = train_tfidf_vectorizer(dataset)
    user_question = " ".join(text)  # Convert token list to sentence
    answer = get_answer(user_question, vectorizer, X, dataset)
    return answer
