#!/usr/bin/env python3
"""
Generate resume.pdf using fpdf2
"""
from fpdf import FPDF

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Helvetica", "B", 20)
pdf.set_text_color(15, 25, 141)
pdf.cell(0, 10, "Aakash", ln=True, align="C")

pdf.set_font("Helvetica", "B", 14)
pdf.set_text_color(40, 208, 255)
pdf.cell(0, 8, "Full Stack Developer", ln=True, align="C")

pdf.set_font("Helvetica", "", 10)
pdf.set_text_color(80, 80, 80)
pdf.cell(0, 6, "aakash76k747@gmail.com | Faridabad, Haryana, India | 1+ Years Experience", ln=True, align="C")
pdf.ln(5)

# Professional Summary
pdf.set_font("Helvetica", "B", 12)
pdf.set_text_color(15, 25, 141)
pdf.cell(0, 8, "PROFESSIONAL SUMMARY", ln=True)
pdf.set_draw_color(40, 208, 255)
pdf.line(15, pdf.get_y(), 195, pdf.get_y())
pdf.ln(2)

pdf.set_font("Helvetica", "", 10)
pdf.set_text_color(50, 50, 50)
summary = "Dedicated Full Stack Developer with 1+ year of hands-on experience in creating responsive, efficient, and visually appealing web applications. Proficient in MERN Stack and emerging AI technologies. Passionate about solving real-world problems through technology."
pdf.multi_cell(0, 5, summary)
pdf.ln(3)

# Technical Skills
pdf.set_font("Helvetica", "B", 12)
pdf.set_text_color(15, 25, 141)
pdf.cell(0, 8, "TECHNICAL SKILLS", ln=True)
pdf.line(15, pdf.get_y(), 195, pdf.get_y())
pdf.ln(2)

pdf.set_font("Helvetica", "", 10)
pdf.set_text_color(50, 50, 50)
skills = [
    "Frontend: React, JavaScript, HTML5, CSS3, Responsive Design",
    "Backend: Node.js, Express.js, RESTful APIs, MongoDB",
    "MERN Stack: MongoDB, Express, React, Node.js",
    "Emerging Tech: Generative AI, AI Integration",
    "Tools: Git, GitHub, VS Code, Figma, npm, Postman"
]
for skill in skills:
    pdf.cell(5, 5, "•", ln=False)
    pdf.multi_cell(0, 5, skill)
pdf.ln(2)

# Professional Experience
pdf.set_font("Helvetica", "B", 12)
pdf.set_text_color(15, 25, 141)
pdf.cell(0, 8, "PROFESSIONAL EXPERIENCE", ln=True)
pdf.line(15, pdf.get_y(), 195, pdf.get_y())
pdf.ln(2)

experiences = [
    {
        "title": "Full Stack Developer (Training)",
        "company": "DUCAT, India | 2026 - Present",
        "bullets": [
            "Advanced training in MERN Stack",
            "Generative AI and AI integration courses",
            "Building portfolio projects with industry best practices"
        ]
    },
    {
        "title": "Full Stack Developer",
        "company": "MEW INDUSTRIES | July 2025 - December 2025",
        "bullets": [
            "Designed and developed Attendance System",
            "Built responsive React frontend with real-time updates",
            "Created robust Node.js and Express backend APIs",
            "Implemented MongoDB database design"
        ]
    },
    {
        "title": "Web Developer / Intern",
        "company": "Web Development Projects | Jan - Jun 2025",
        "bullets": [
            "Created Employee Database Portal with CRUD",
            "Developed Company Website with modern design",
            "Implemented responsive design for all devices"
        ]
    }
]

for exp in experiences:
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(15, 25, 141)
    pdf.cell(0, 6, exp["title"], ln=True)
    
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(40, 208, 255)
    pdf.cell(0, 5, exp["company"], ln=True)
    
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(50, 50, 50)
    for bullet in exp["bullets"]:
        pdf.cell(5, 4, "•", ln=False)
        pdf.multi_cell(0, 4, bullet)
    pdf.ln(2)

# Key Projects
pdf.set_font("Helvetica", "B", 12)
pdf.set_text_color(15, 25, 141)
pdf.cell(0, 8, "KEY PROJECTS", ln=True)
pdf.line(15, pdf.get_y(), 195, pdf.get_y())
pdf.ln(2)

projects = [
    ("Attendance System Portal", "React | Node.js | MongoDB", "Complete employee management system successfully deployed at MEW INDUSTRIES"),
    ("Employee Database Portal", "React | MongoDB | REST APIs", "Comprehensive employee management with search and filtering"),
    ("Company Website", "React | HTML5 | CSS3", "Modern, responsive website with portfolio section"),
    ("Portfolio Website", "HTML5 | CSS3 | JavaScript", "Professional portfolio with animations and filtering")
]

for proj_name, tech, desc in projects:
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(15, 25, 141)
    pdf.cell(0, 5, proj_name, ln=True)
    
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(40, 208, 255)
    pdf.cell(0, 4, tech, ln=True)
    
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(50, 50, 50)
    pdf.multi_cell(0, 4, desc)
    pdf.ln(2)

# Education
pdf.set_font("Helvetica", "B", 12)
pdf.set_text_color(15, 25, 141)
pdf.cell(0, 8, "EDUCATION & TRAINING", ln=True)
pdf.line(15, pdf.get_y(), 195, pdf.get_y())
pdf.ln(2)

education = [
    ("MERN Stack + Generative AI", "DUCAT, India | 2026", "Advanced training in Full Stack Development"),
    ("Full Stack Web Development", "Self-Learning | 2024-2025", "React, Node.js, MongoDB, REST APIs")
]

for edu_name, org, desc in education:
    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(15, 25, 141)
    pdf.cell(0, 5, edu_name, ln=True)
    
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(40, 208, 255)
    pdf.cell(0, 4, org, ln=True)
    
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 4, desc, ln=True)
    pdf.ln(1)

# Achievements
pdf.set_font("Helvetica", "B", 12)
pdf.set_text_color(15, 25, 141)
pdf.cell(0, 8, "ACHIEVEMENTS", ln=True)
pdf.line(15, pdf.get_y(), 195, pdf.get_y())
pdf.ln(2)

achievements = [
    "Successfully deployed production-ready attendance system",
    "15+ projects completed with satisfied clients",
    "5+ active clients with repeat work opportunities",
    "Strong MERN Stack expertise with AI integration knowledge"
]

pdf.set_font("Helvetica", "", 10)
pdf.set_text_color(50, 50, 50)
for ach in achievements:
    pdf.cell(5, 4, "•", ln=False)
    pdf.multi_cell(0, 4, ach)

# Save PDF
pdf.output("resume.pdf")
print("✅ Resume PDF created successfully!")
