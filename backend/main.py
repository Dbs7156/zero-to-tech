from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

profile = {
    "heroTitle": "关于我",
    "heroSubtitle": "项目，创意，灵感，心得，我的作品",
}

class AnalyzeRequest(BaseModel):
    text: str


@app.get("/api/profile")
def get_profile():
    return profile
#uvicorn main:app --reload手动跑起来
#fastapi dev快捷指令


@app.post("/api/analyze")
def analyze(req: AnalyzeRequest):
    return {
        "text": req.text,
        "score": 0.5,
        "label": "偏平静",
        "pinyin": "（模块 6 再说）",
    }
#post方式
#curl http://localhost:8000/api/analyze \
#-H "Content-Type: application/json" \
#-d '{"text": "今天的风很轻，适合把想法写下来"}'

