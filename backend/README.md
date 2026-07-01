I built an AI-powered resume-to-job matching system with explainable recommendations and skill gap analysis

steps to run:
1)python -m venv venv
2)\venv\Scripts\activate   
3)cd gotobackend dir
4)pip install -r requirements.txt  
5)uvicorn app.main:app --reload --port 800   
6)cd gotofrontendresumeui dir
7)npm install
8)ng serve # this will give port that port needs to add in main.py to avoid CORS error

==================================================
To avoid CORS error add code in main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
        "http://127.0.0.1:4200",
        "http://localhost:51959" //here add port no on which frontend is running.
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
====================================================

continue this project further, roadmap for future update:

🔐 1. Authentication System (VERY IMPORTANT)
Login / Signup
JWT auth
user sessions

👉 This makes it a real SaaS

📁 2. Resume History Dashboard
store all uploads
view past results
compare resumes
📄 3. Download AI Report (PDF)
export analysis
recruiter-friendly report
🧠 4. Better AI Layer
GPT-based feedback
resume improvement suggestions
skill gap recommendations
☁️ 5. Deployment (CRITICAL FOR RESUME)
Frontend → Vercel / Netlify
Backend → Render / Railway
DB → Postgres / MongoDB Atlas
🔗 6. Shareable Link Feature
each analysis has a URL
like: /report/123
