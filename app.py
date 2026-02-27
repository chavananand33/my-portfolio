# ============================================================
#  app.py  –  Anand Chavan Portfolio  +  AI Tools
# ============================================================
#
#  HOW TO RUN:
#
#  1. Install dependencies:
#       pip install flask anthropic
#
#  2. Set your Anthropic API key (one-time, in your terminal):
#       Windows :  set ANTHROPIC_API_KEY=sk-ant-...
#       Mac/Linux: export ANTHROPIC_API_KEY=sk-ant-...
#
#  3. Run the app:
#       python app.py
#
#  4. Open browser → http://127.0.0.1:5000
#
#  Get a free API key at: https://console.anthropic.com
# ============================================================

import os
import urllib.parse
from flask import Flask, render_template, request, jsonify
from anthropic import Anthropic

app = Flask(__name__)
anthropic_client = Anthropic()   # reads ANTHROPIC_API_KEY env var automatically

# ── Portfolio Data ────────────────────────────────────────────

PROFILE = {
    "name": "Anand Chavan",
    "title": "Support Engineer · AI Enthusiast",
    "tagline": "Open to Technical Operations, AI & Automation Roles",
    "summary": (
        "Technical Operations & Application Support professional with 7.6+ years "
        "in Telecom IT, SAP CRM, and mission-critical production systems — "
        "transitioning into AI-driven Operations & Intelligent Automation."
    ),
    "location": "Pune, Maharashtra, India",
    "email": "chavananand33@gmail.com",
    "phone": "+91 97303 43050",
    "linkedin": "https://linkedin.com/in/anand-chavan-7615b9118",
    "github": "https://github.com/chavananand33",
    "twitter": "https://x.com/chavananand33",
    "whatsapp": "https://wa.me/919730343050",
    "photo": "images/ac.jpeg",
    "tags": [
        "Production Support L2", "SAP CRM", "Oracle DB", 
        "Unix / Linux", "Incident Management", "AI Upskilling.. ",
    ],
    "stats": [
        {"num": "7.6+",  "label": "Years Exp"},
        {"num": "99.9%", "label": "SLA Uptime"},
        {"num": "25%",   "label": "MTTR Cut"},
    ],
}

EXPERIENCE = [
    {
        "title": "Support Engineer",
        "company": "IBM India Pvt. Ltd. · Pune",
        "period": "Aug 2024 – Nov 2024",
        "desc": (
            "DXL (Digital Experience Layer) — Backend middleware connecting VI App, "
            "Web Portal & Retail POS to billing, CRM and product systems via REST APIs. "
            "MongoDB primary database."
        ),
        "bullets": [
            "L2 Production Support for CRM-based telecom activation workflows",
            "Monitored system health and API performance proactively",
            "Reduced incident resolution time by 25% via structured RCA",
            "Collaborated with dev & infrastructure teams for permanent fixes",
            "Managed critical incidents within agreed SLA timelines",
        ],
        "badge": None,
    },
    {
        "title": "Deputy Manager",
        "company": "JIO Platforms Limited · Mumbai RCP",
        "period": "May 2022 – Jul 2024",
        "desc": (
            "Enterprise SAP CRM — JIO postpaid number activations with GST validation, "
            "customer KYC (POA/POI), Termination/Suspension for IOT, Mobility, "
            "Jio_Link, and ODCPE CAFs."
        ),
        "bullets": [
            "L2 Production Support for CRM-based telecom activation workflows",
            "Monitored queues and logs ensuring 99.9% uptime",
            "Executed Linux-based system backups and validations",
            "Implemented configuration and security changes",
            "Ensured SLA adherence and minimized downtime across all platforms",
        ],
        "badge": "⭐ Improved system stability via proactive monitoring practices",
    },
    {
        "title": "Application Support Engineer",
        "company": "IBM India Pvt. Ltd. · Pune",
        "period": "Mar 2017 – May 2022",
        "desc": (
            "VI Second Consent Gateway (TRAI-mandated VAS activation compliance) "
            "& OFFNET — PAN India centralized PPU event-based charging API with "
            "refund and subscriber blacklisting support."
        ),
        "bullets": [
            "Drove VAS and IT system consolidation for the Vodafone-Idea merger",
            "Supported event-based charging APIs (PPU) and refund workflows",
            "Managed production escalations across IT, Marketing & Business teams",
            "Launched new brand VI across VAS and Digital platforms",
            "Configured new services, short codes, and verbiage for VIL vendors",
        ],
        "badge": "⭐ Supported high-volume platforms serving millions of subscribers",
    },
]

SKILLS = [
    {"icon": "⚙️", "title": "Operations & Support",
     "pills": ["App Support L1/L2","Incident Management","Problem Management","SLA / KPI Governance","Root Cause Analysis","Change Management"], "ai": False},
    {"icon": "💾", "title": "Databases & OS",
     "pills": ["Oracle 11g","Oracle 19c","SQL","SQL Developer","Unix / Linux","MongoDB"], "ai": False},
    {"icon": "🛠️", "title": "Enterprise Tools",
     "pills": ["SAP CRM","BMC Remedy","HPSM","Citrix","WinSCP","Putty","RDP Server"], "ai": False},
    {"icon": "🤖", "title": "AI & Emerging Tech",
     "pills": ["Python (AI/Automation)","Machine Learning","Generative AI","Prompt Engineering","ChatGPT","Claude AI","Google Gemini","Perplexity"], "ai": True},
    {"icon": "📊", "title": "Analytics & BI",
     "pills": ["Power BI (PL-300)","Excel Expert","Data Analytics","Advanced Reporting"], "ai": False},
    {"icon": "🤝", "title": "Soft Skills",
     "pills": ["Stakeholder Coordination","Vendor Management","Cross-team Collaboration","Crisis Management","ITIL Framework"], "ai": False},
]

EDUCATION = [
    {"degree": "BE — Computer Engineering", "institute": "Pune University",        "result": "✦ Distinction"},
    {"degree": "Diploma in Engineering",    "institute": "MSBTE",                  "result": "✦ Distinction"},
    {"degree": "SSC — 10th Standard",       "institute": "Maharashtra State Board", "result": "✦ Distinction"},
]

CERTIFICATIONS = [
    {"icon": "📊", "name": "MOS: PowerPoint Associate (MO-310)",       "provider": "Microsoft · AI for Techies"},
    {"icon": "📈", "name": "MOS: Excel Expert (MO-211)",               "provider": "Microsoft · AI for Techies"},
    {"icon": "📉", "name": "Power BI Data Analyst Associate (PL-300)", "provider": "Microsoft · AI for Techies"},
    {"icon": "🐍", "name": "Python for AI & Automation",              "provider": "AI for Techies"},
    {"icon": "🧠", "name": "AI & Machine Learning Mastery",           "provider": "AI for Techies"},
    {"icon": "✨", "name": "Generative AI & Prompt Engineering",      "provider": "AI for Techies"},
    {"icon": "⚡", "name": "AI Tools & Automation",                   "provider": "Be10x"},
    {"icon": "📐", "name": "Advanced Data Analytics & AI",            "provider": "Be10x"},
    {"icon": "🎯", "name": "IT Service Management (ITIL)",            "provider": "Officemaster"},
    {"icon": "🔄", "name": "Automation & Digital Transformation",     "provider": "Officemaster"},
]

# ── Routes ────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html",
        profile=PROFILE, experience=EXPERIENCE, skills=SKILLS,
        education=EDUCATION, certifications=CERTIFICATIONS)

@app.route("/contact", methods=["POST"])
def contact():
    data = request.get_json()
    name    = data.get("name","").strip()
    email   = data.get("email","").strip()
    message = data.get("message","").strip()
    if not name or not email or not message:
        return jsonify({"ok": False, "error": "All fields are required."}), 400
    print(f"\n📬 New Message from {name} <{email}>:\n   {message}\n")
    return jsonify({"ok": True, "message": f"Thanks {name}! I'll get back to you soon."})

# ── AI: Chatbot ───────────────────────────────────────────────

@app.route("/api/chat", methods=["POST"])
def chat():
    """
    Multi-turn chatbot using Claude.
    Receives full conversation history each call so Claude remembers context.
    Body: { "messages": [{"role":"user","content":"..."},{"role":"assistant","content":"..."},...] }
    """
    data     = request.get_json()
    messages = data.get("messages", [])
    if not messages:
        return jsonify({"ok": False, "error": "No messages provided."}), 400
    try:
        resp = anthropic_client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            system=(
                "You are a friendly AI assistant on Anand Chavan's portfolio website. "
                "Anand is an IT professional with 7.6+ years in Telecom IT, SAP CRM, "
                "Oracle DB, Unix/Linux, now transitioning into AI & Automation. "
                "Answer questions about his skills, experience, or general tech topics. "
                "Keep answers concise and professional."
            ),
            messages=messages,
        )
        return jsonify({"ok": True, "reply": resp.content[0].text})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

# ── AI: Summarizer ────────────────────────────────────────────

@app.route("/api/summarize", methods=["POST"])
def summarize():
    """
    Summarizes pasted text in three styles.
    Body: { "text": "...", "style": "bullet|paragraph|short" }
    """
    data  = request.get_json()
    text  = data.get("text","").strip()
    style = data.get("style","bullet")
    if not text:
        return jsonify({"ok": False, "error": "Please paste some text first."}), 400
    if len(text) > 15000:
        return jsonify({"ok": False, "error": "Text too long. Max 15,000 characters."}), 400

    style_map = {
        "bullet":    "Summarize as 5-7 clear bullet points. Start each bullet with •.",
        "paragraph": "Summarize in 2-3 well-written paragraphs.",
        "short":     "Summarize in 2-3 sentences only — be as brief as possible.",
    }
    instruction = style_map.get(style, style_map["bullet"])

    try:
        resp = anthropic_client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            messages=[{"role":"user","content":
                f"Summarize the following text.\nStyle: {instruction}\n\nTEXT:\n{text}"
            }],
        )
        return jsonify({"ok": True, "summary": resp.content[0].text})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

# ── AI: Image Generator ───────────────────────────────────────

@app.route("/api/generate-image", methods=["POST"])
def generate_image():
    """
    1. Uses Claude to enhance the user's prompt.
    2. Returns a Pollinations.ai URL (100% free, no API key needed).
    Body: { "prompt": "..." }
    """
    data   = request.get_json()
    prompt = data.get("prompt","").strip()
    if not prompt:
        return jsonify({"ok": False, "error": "Please enter a prompt."}), 400

    # Enhance prompt with Claude
    try:
        enhance = anthropic_client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=150,
            messages=[{"role":"user","content":
                f"Rewrite this as a vivid, detailed image generation prompt (max 80 words, no explanations):\n{prompt}"
            }],
        )
        enhanced = enhance.content[0].text.strip()
    except Exception:
        enhanced = prompt   # fall back to original

    seed     = abs(hash(prompt)) % 99999
    encoded  = urllib.parse.quote(enhanced)
    image_url = (
        f"https://image.pollinations.ai/prompt/{encoded}"
        f"?width=768&height=768&nologo=true&enhance=true&seed={seed}"
    )
    return jsonify({"ok": True, "image_url": image_url, "enhanced_prompt": enhanced})

# ── Run ───────────────────────────────────────────────────────

if __name__ == "__main__":
    app.run(debug=True)
