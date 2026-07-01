💎 AI Resume Analyzer System (Full Stack Web App)

This is an AI-powered resume-to-job matching system with explainable recommendations and skill gap analysis.

It has 3 main layers:

[ Angular Frontend ]
        ↓
[ FastAPI Backend ]
        ↓
[ AI Resume Processing Logic ]

========================
When you upload a resume:

1. User selects file (Angular)
2. File stored in component state
3. Click "Upload"
4. Angular sends file → FastAPI
5. FastAPI receives file
6. Backend extracts text from PDF
7. AI logic processes resume
8. Skills + experience + job match generated
9. Response sent back as JSON
10. Angular receives response
11. UI updates dashboard
