from transformers import pipeline

generator = pipeline(
    model="distilgpt2",
    task="text-generation",
    max_new_tokens=150,
    do_sample=True,
    temperature=0.7
)

def get_resume_suggestions(jd_text, resume_text):
    jd_text = jd_text[:500]
    resume_text = resume_text[:500]

    prompt = (
        f"You are a resume expert.\n"
        f"Job Description:\n{jd_text}\n\n"
        f"Resume:\n{resume_text}\n\n"
        f"Give 3 specific suggestions to improve the resume for this job."
    )

    result = generator(prompt, num_return_sequences=1)
    return result[0]['generated_text']






