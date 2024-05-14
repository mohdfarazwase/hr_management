import os
from .doc2text import extract_text_from_docx
from .pdf2text import extract_text_from_pdf
from .extractor import extract_skills, extract_names, extract_emails
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from hrapp.models import JobMatches, Job, Resume
def match_resume_with_job(job_id=1, resumes = Resume.objects.all()): 
    job = Job.objects.get(id=job_id)
    job_desc = job.description
    for resume in resumes:
        # try:
        path = resume.file.path
        if path.endswith('.pdf'):
            resume_text = extract_text_from_pdf(path)
        else:
            resume_text = extract_text_from_docx(path)

        name = extract_names(resume_text)
        email = extract_emails(resume_text)
        skills = extract_skills(resume_text, job.skills)
        print(name, email, skills)
        job_data = [f'{job_desc} {" ".join(skills)} {job.location} {job.title}']
        resume_data = [f'{resume_text} {" ".join(skills)}'] 
        data = job_data + resume_data
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(data)
        vectors = X.toarray()
        similarity = cosine_similarity([vectors[0]], [vectors[1]])[0][0]
        threshold = 0.5 # 50% match
        score  = round(similarity * 100)
        job_match = JobMatches(job=job, resume=resume, score=score)
        job_match.save()
        print(f"Matched with {job.title} with a score of {similarity}")
        # except Exception as e:
        #     print(f"Error processing resume {path.name}: {e}")
            
    
