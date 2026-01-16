from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def match_resume_to_job(resume_text: str, job_text: str):
    embeddings = model.encode([resume_text, job_text])
    score = util.cos_sim(embeddings[0], embeddings[1]).item()

    return round(score * 100, 2)
