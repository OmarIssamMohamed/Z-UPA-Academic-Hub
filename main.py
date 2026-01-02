import customtkinter as ctk
from tkinter import messagebox
import os, json, webbrowser
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ctk.set_appearance_mode("Dark"); ctk.set_default_color_theme("dark-blue")
C = {"pri": "#1f6aa5", "sec": "#2b2b2b", "acc": "#10a37f", "bg": "#1a1a1a", "txt": "#fff", "dang": "#c0392b", "warn": "#e67e22", "succ": "#27ae60"}
FILES = {"cfg": "config.json", "stu": "students.txt", "crs": "courses.txt", "res": "results.txt", "svc": "services.txt", "cmp": "complaints.txt", "ntf": "notifications.txt", "tsk": "tasks.txt", "grd": "grades.txt", "cal": "calendar.txt", "att": "attendance.txt"}

def read_config(f): 
    if not os.path.exists(f): json.dump({"theme": "Dark"}, open(f, 'w'))
    return json.load(open(f))

def load_students_db(f):
    if not os.path.exists(f): 
        with open(f, 'w') as file: file.write("202508134,12345,Omar Issam,Year 1,CSAI\n202508008,12345,Ahmed Hussein,Year 1,CSAI")
    try: return [dict(zip(['id','pw','name','yr','maj'], l.strip().split(','))) for l in open(f) if l.strip()]
    except: return []

def validate_login(uid, pwd):
    return any(s['id'] == uid and s['pw'] == pwd for s in load_students_db(FILES['stu']))

def get_user_session(uid):
    return next((s for s in load_students_db(FILES['stu']) if s['id'] == uid), None)

def show_main_frame(app, name):
    views = {"Home": app.view_home, "Courses": app.view_courses, "Services": app.view_services, "Profile": app.view_profile, "Grades": app.view_grades, "Calendar": app.view_calendar, "Notifications": app.view_notifications, "Tasks": app.view_tasks}
    views.get(name, lambda: print(f"View {name} missing"))()

def toggle_theme(app, mode):
    ctk.set_appearance_mode(mode); app.cfg['theme'] = mode
    json.dump(app.cfg, open(FILES['cfg'], 'w'))

def logout(app): app.curr_user = None; app.view_login()

def load_courses(f):
    if not os.path.exists(f): 
        with open(f, 'w') as file: file.write("CSAI 101,Python,Dr. Ghada,Eng. Tasneem,Year 1\nMATH 103,Calculus,Dr. Ali,Eng. Sara,Year 1\nPHYS 102,Physics,Dr. Mohamed,Eng. Mona,Year 1")
    return [dict(zip(['code','name','prof','ta','yr'], l.strip().split(','))) for l in open(f) if l.strip()]

def filter_courses(yr, maj): return [c for c in load_courses(FILES['crs']) if c['yr'] == yr]

def get_lec_details(code):
    db = {"CSAI 101": {"lec": [{"t": "Intro to Python", "u": "http://google.com", "f": "Lec1.pdf"}, {"t": "Variables & Data Types", "u": "http://google.com", "f": "Lec2.pdf"}], "ass": ["Task 1", "Task 2"]},
          "MATH 103": {"lec": [{"t": "Limits", "u": "http://google.com", "f": "Math1.pdf"}, {"t": "Derivatives", "u": "http://google.com", "f": "Math2.pdf"}], "ass": ["Sheet 1", "Sheet 2"]},
          "PHYS 102": {"lec": [{"t": "Mechanics", "u": "http://google.com", "f": "Phys1.pdf"}], "ass": ["Problem Set 1"]}}
    return db.get(code, {"lec":[],"ass":[]})

def open_link(url): webbrowser.open(url)

def get_labs(code): 
    return {"CSAI 101": ["Lab1_Basics.pdf", "Lab2_Loops.pdf"], "CSAI 201": ["Lab_Arrays.pdf"], "PHYS 102": ["Lab_Exp1.pdf"]}.get(code, [])

def open_pdf(path): os.startfile(path) if os.path.exists(path) else messagebox.showinfo("Demo", f"Opening {path}")

def search_course(kw): 
    return [c for c in load_courses(FILES['crs']) if kw.lower() in c['code'].lower() or kw.lower() in c['name'].lower()]

def load_quiz(f):
    if not os.path.exists(f): return []
    try: return [dict(zip(['q','opts','ans'], [l.split('|')[0], l.split('|')[1:5], l.split('|')[5]])) for l in open(f) if l.strip()]
    except: return []

def calc_score(user, correct): return int((sum(u==c for u,c in zip(user, correct))/len(correct))*100) if correct else 0

def save_result(sid, crs, sc): open(FILES['res'], 'a').write(f"{sid},{crs},{sc},{datetime.now()}\n")

def load_services(typ):
    if not os.path.exists(FILES['svc']): open(FILES['svc'], 'w').write("SERVICES:\n- Library (8AM-8PM)\n- IT Support\n- Student Affairs\nCONFERENCES:\n- Tech Fair 2025\n- AI Workshop")
    c = open(FILES['svc']).read(); return c.split("CONFERENCES:")[0 if typ=="services" else 1]

def save_complaint(sid, msg): open(FILES['cmp'], 'a').write(f"[{datetime.now()}] {sid}: {msg}\n")

def reset_form(frm): [w.deselect() for w in frm.winfo_children() if isinstance(w, ctk.CTkRadioButton)]

def export_report(sid):
    if not os.path.exists(FILES['res']): return None
    data = [l for l in open(FILES['res']) if l.startswith(sid)]
    if data: open(f"Report_{sid}.txt", 'w').write("".join(data)); return f"Report_{sid}.txt"

def load_notifications(sid):
    if not os.path.exists(FILES['ntf']): 
        open(FILES['ntf'], 'w').write("all,New semester started!,2025-01-01\nall,Exam schedule released,2025-01-05")
    return [dict(zip(['sid','msg','date'], l.strip().split(','))) for l in open(FILES['ntf']) if l.strip() and (l.startswith('all') or l.startswith(sid))]

def add_notification(sid, msg): open(FILES['ntf'], 'a').write(f"{sid},{msg},{datetime.now().strftime('%Y-%m-%d')}\n")

def load_tasks(sid, crs=None):
    if not os.path.exists(FILES['tsk']): 
        open(FILES['tsk'], 'w').write("all,CSAI 101,Submit Lab 1,2025-02-01,pending\nall,MATH 103,Complete Sheet 2,2025-02-05,pending")
    tasks = [dict(zip(['sid','crs','task','due','status'], l.strip().split(','))) for l in open(FILES['tsk']) if l.strip()]
    return [t for t in tasks if (t['sid'] == 'all' or t['sid'] == sid) and (not crs or t['crs'] == crs)]

def update_task_status(sid, task, status):
    if not os.path.exists(FILES['tsk']): return
    lines = open(FILES['tsk']).readlines()
    with open(FILES['tsk'], 'w') as f:
        for l in lines:
            if task in l and (sid in l or 'all' in l): f.write(l.replace(l.split(',')[4], f"{status}\n"))
            else: f.write(l)

def load_grades(sid):
    if not os.path.exists(FILES['grd']): 
        open(FILES['grd'], 'w').write("202508134,CSAI 101,Quiz1,85,2025-01-15\n202508134,MATH 103,Midterm,78,2025-01-20")
    return [dict(zip(['sid','crs','type','grade','date'], l.strip().split(','))) for l in open(FILES['grd']) if l.strip() and l.startswith(sid)]

def calc_gpa(grades):
    if not grades: return 0.0
    total = sum(int(g['grade']) for g in grades)
    return round(total / len(grades) / 25, 2)

def load_calendar():
    if not os.path.exists(FILES['cal']): 
        open(FILES['cal'], 'w').write("2025-02-01,Midterm Exams Start\n2025-02-15,Registration Deadline\n2025-03-01,Spring Break")
    return [dict(zip(['date','event'], l.strip().split(','))) for l in open(FILES['cal']) if l.strip()]

def get_upcoming_events():
    events = load_calendar()
    today = datetime.now()
    upcoming = [e for e in events if datetime.strptime(e['date'], '%Y-%m-%d') >= today]
    return sorted(upcoming, key=lambda x: x['date'])[:5]

def change_password(sid, old_pw, new_pw):
    students = load_students_db(FILES['stu'])
    for s in students:
        if s['id'] == sid and s['pw'] == old_pw:
            lines = open(FILES['stu']).readlines()
            with open(FILES['stu'], 'w') as f:
                for l in lines:
                    if l.startswith(sid): f.write(l.replace(old_pw, new_pw))
                    else: f.write(l)
            return True
    return False

def load_attendance(sid):
    if not os.path.exists(FILES['att']): 
        open(FILES['att'], 'w').write("202508134,CSAI 101,2025-01-10,present\n202508134,CSAI 101,2025-01-12,present\n202508134,MATH 103,2025-01-11,absent")
    att = [dict(zip(['sid','crs','date','status'], l.strip().split(','))) for l in open(FILES['att']) if l.strip() and l.startswith(sid)]
    return att

def calc_attendance_rate(sid, crs):
    att = [a for a in load_attendance(sid) if a['crs'] == crs]
    if not att: return 100
    present = sum(1 for a in att if a['status'] == 'present')
    return int((present / len(att)) * 100)

def get_course_stats(sid, yr):
    courses = filter_courses(yr, "")
    grades = load_grades(sid)
    return {"total": len(courses), "completed": len(set(g['crs'] for g in grades)), "pending": len(courses) - len(set(g['crs'] for g in grades))}

class ZUPA_App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.cfg = read_config(FILES['cfg']); self.curr_user = None
        self.title("Z-UPA Academic Hub"); self.geometry("1100x750")
        self.main = ctk.CTkFrame(self, fg_color="transparent"); self.main.pack(fill="both", expand=True)
        self.view_login()

    def clear(self): [w.destroy() for w in self.main.winfo_children()]

    def sidebar(self):
        sb = ctk.CTkFrame(self.main, width=220, corner_radius=0, fg_color=C['bg']); sb.pack(side="left", fill="y"); sb.pack_propagate(0)
        ctk.CTkLabel(sb, text="Z-UPA", font=("Impact", 28), text_color=C['pri']).pack(pady=(40, 5))
        ctk.CTkLabel(sb, text=f"👤 {self.curr_user['name'].split()[0]}", font=("Arial", 14, "bold")).pack(pady=10)
        
        btns = [("🏠 Home","Home"), ("📚 Courses","Courses"), ("📊 Grades","Grades"), ("✅ Tasks","Tasks"), 
                ("📅 Calendar","Calendar"), ("🔔 Alerts","Notifications"), ("🛠 Services","Services"), ("🎓 Profile","Profile")]
        for t, cmd in btns:
            ctk.CTkButton(sb, text=t, fg_color="transparent", anchor="w", command=lambda c=cmd: show_main_frame(self, c)).pack(fill="x", padx=10, pady=3)
        
        theme_frame = ctk.CTkFrame(sb, fg_color="transparent"); theme_frame.pack(side="bottom", pady=10)
        ctk.CTkButton(theme_frame, text="🌙", width=40, command=lambda: toggle_theme(self, "Dark")).pack(side="left", padx=2)
        ctk.CTkButton(theme_frame, text="☀️", width=40, command=lambda: toggle_theme(self, "Light")).pack(side="left", padx=2)
        
        ctk.CTkButton(sb, text="Logout", fg_color=C['dang'], command=lambda: logout(self)).pack(side="bottom", padx=20, pady=10)
        return ctk.CTkFrame(self.main, fg_color="transparent")

    def view_login(self):
        self.clear(); box = ctk.CTkFrame(self.main, width=380, height=480, fg_color=C['sec']); box.place(relx=0.5, rely=0.5, anchor="c")
        ctk.CTkLabel(box, text="🎓 Z-UPA Login", font=("Arial", 26, "bold"), text_color=C['pri']).pack(pady=40)
        e1, e2 = ctk.CTkEntry(box, placeholder_text="Student ID", width=300), ctk.CTkEntry(box, placeholder_text="Password", width=300, show="*")
        e1.pack(pady=10); e2.pack(pady=10)
        
        def log():
            if validate_login(e1.get(), e2.get()): self.curr_user = get_user_session(e1.get()); self.view_home()
            else: messagebox.showerror("Error", "Invalid Credentials")
            
        ctk.CTkButton(box, text="Login", fg_color=C['pri'], width=300, height=40, command=log).pack(pady=30)
        ctk.CTkLabel(box, text="Demo: 202508134 / 12345", text_color="gray", font=("Arial", 11)).pack()

    def view_home(self):
        self.clear(); content = self.sidebar(); content.pack(side="right", fill="both", expand=True)
        scroll = ctk.CTkScrollableFrame(content, fg_color="transparent"); scroll.pack(fill="both", expand=True, padx=30, pady=30)
        
        ctk.CTkLabel(scroll, text=f"Welcome back, {self.curr_user['name']}", font=("Arial", 28, "bold")).pack(anchor="w")
        ctk.CTkLabel(scroll, text=f"{self.curr_user['yr']} | {self.curr_user['maj']}", text_color="gray", font=("Arial", 13)).pack(anchor="w", pady=(0, 25))
        
        stats = ctk.CTkFrame(scroll, fg_color="transparent"); stats.pack(fill="x")
        crs = filter_courses(self.curr_user['yr'], self.curr_user['maj'])
        tasks = load_tasks(self.curr_user['id'])
        pending = sum(1 for t in tasks if t['status'] == 'pending')
        completed = sum(1 for t in tasks if t['status'] == 'completed')
        grades = load_grades(self.curr_user['id'])
        gpa = calc_gpa(grades)
        
        for lbl, val, col in [("Courses", len(crs), C['pri']), ("Pending Tasks", pending, C['warn']), ("GPA", gpa, C['succ'])]:
            c = ctk.CTkFrame(stats, fg_color=C['sec']); c.pack(side="left", fill="x", expand=True, padx=5)
            ctk.CTkLabel(c, text=str(val), font=("Arial", 32, "bold"), text_color=col).pack(pady=12)
            ctk.CTkLabel(c, text=lbl, font=("Arial", 12)).pack(pady=(0,12))

        chart_frame = ctk.CTkFrame(scroll, fg_color=C['sec'], height=250); chart_frame.pack(fill="x", pady=20)
        ctk.CTkLabel(chart_frame, text="Task Analytics", font=("Arial", 14, "bold")).pack(anchor="w", padx=20, pady=10)
        
        if pending + completed > 0:
            fig, ax = plt.subplots(figsize=(6, 2), dpi=100)
            fig.patch.set_facecolor(C['sec'])
            ax.set_facecolor(C['sec'])
            
            wedges, texts, autotexts = ax.pie([pending, completed], labels=['Pending', 'Done'], 
                                              colors=[C['warn'], C['succ']], autopct='%1.1f%%', 
                                              startangle=90, textprops={'color':"white"})
            for t in texts: t.set_color("white")
            
            canvas = FigureCanvasTkAgg(fig, master=chart_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=True)
            plt.close(fig) 
        else:
            ctk.CTkLabel(chart_frame, text="No task data available for chart.", text_color="gray").pack(pady=30)
        
        ctk.CTkLabel(scroll, text="Upcoming Events", font=("Arial", 18, "bold")).pack(anchor="w", pady=(20, 10))
        events = get_upcoming_events()[:3]
        for e in events:
            ef = ctk.CTkFrame(scroll, fg_color=C['sec'], height=50); ef.pack(fill="x", pady=5)
            ctk.CTkLabel(ef, text=e['date'], font=("Arial", 11, "bold"), text_color=C['acc']).pack(side="left", padx=15)
            ctk.CTkLabel(ef, text=e['event']).pack(side="left")

    def view_courses(self):
        self.clear(); content = self.sidebar(); content.pack(side="right", fill="both", expand=True)
        
        head = ctk.CTkFrame(content, fg_color="transparent"); head.pack(fill="x", padx=30, pady=20)
        ctk.CTkLabel(head, text="My Courses", font=("Arial", 24, "bold")).pack(side="left")
        srch = ctk.CTkEntry(head, placeholder_text="Search courses..."); srch.pack(side="right")
        
        scroll = ctk.CTkScrollableFrame(content, fg_color="transparent"); scroll.pack(fill="both", expand=True, padx=30)
        
        def render(lst):
            [w.destroy() for w in scroll.winfo_children()]
            if not lst: ctk.CTkLabel(scroll, text="No courses found.").pack(pady=20)
            for c in lst:
                fr = ctk.CTkFrame(scroll, fg_color=C['sec']); fr.pack(fill="x", pady=6)
                info = ctk.CTkFrame(fr, fg_color="transparent"); info.pack(side="left", fill="both", expand=True, padx=15, pady=12)
                ctk.CTkLabel(info, text=f"{c['code']} - {c['name']}", font=("Arial", 13, "bold"), anchor="w").pack(anchor="w")
                ctk.CTkLabel(info, text=f"👨‍🏫 {c['prof']} | 👨‍💻 {c['ta']}", text_color="gray", font=("Arial", 10), anchor="w").pack(anchor="w")
                
                att_rate = calc_attendance_rate(self.curr_user['id'], c['code'])
                ctk.CTkLabel(fr, text=f"{att_rate}%", text_color=C['succ'] if att_rate >= 75 else C['dang'], font=("Arial", 11, "bold")).pack(side="right", padx=10)
                ctk.CTkButton(fr, text="Quiz", width=70, fg_color=C['acc'], command=lambda x=c: self.view_quiz(x)).pack(side="right", padx=5)
                ctk.CTkButton(fr, text="View", width=70, command=lambda x=c: self.view_content(x)).pack(side="right")
        
        srch.bind("<KeyRelease>", lambda e: render(search_course(srch.get()) if srch.get() else filter_courses(self.curr_user['yr'], self.curr_user['maj'])))
        render(filter_courses(self.curr_user['yr'], self.curr_user['maj']))

    def view_content(self, c):
        self.clear(); content = self.sidebar(); content.pack(side="right", fill="both", expand=True)
        ctk.CTkButton(content, text="← Back", width=80, fg_color="transparent", command=self.view_courses).pack(anchor="w", padx=20, pady=10)
        
        scroll = ctk.CTkScrollableFrame(content, fg_color="transparent"); scroll.pack(fill="both", expand=True, padx=30)
        ctk.CTkLabel(scroll, text=f"{c['code']}: {c['name']}", font=("Arial", 22, "bold"), text_color=C['pri']).pack(anchor="w", pady=10)
        ctk.CTkLabel(scroll, text=f"Instructor: {c['prof']} | TA: {c['ta']}", text_color="gray").pack(anchor="w", pady=(0,20))
        
        data = get_lec_details(c['code'])
        ctk.CTkLabel(scroll, text="📖 Lectures", font=("Arial", 17, "bold")).pack(anchor="w", pady=10)
        for l in data['lec']:
            row = ctk.CTkFrame(scroll, fg_color=C['sec']); row.pack(fill="x", pady=5)
            ctk.CTkLabel(row, text=l['t'], font=("Arial", 12)).pack(side="left", padx=15, pady=10)
            ctk.CTkButton(row, text="🎥 Video", width=80, command=lambda u=l['u']: open_link(u)).pack(side="right", padx=5)
            ctk.CTkButton(row, text="📄 PDF", width=80, fg_color="gray", command=lambda f=l['f']: open_pdf(f)).pack(side="right", padx=5)

        ctk.CTkLabel(scroll, text="🧪 Labs", font=("Arial", 17, "bold")).pack(anchor="w", pady=(20,10))
        labs = get_labs(c['code'])
        if labs:
            for lab in labs:
                r = ctk.CTkFrame(scroll, fg_color=C['sec']); r.pack(fill="x", pady=4)
                ctk.CTkLabel(r, text=lab, font=("Arial", 12)).pack(side="left", padx=15, pady=8)
                ctk.CTkButton(r, text="Open", width=70, command=lambda f=lab: open_pdf(f)).pack(side="right", padx=10)
        else:
            ctk.CTkLabel(scroll, text="No labs available", text_color="gray").pack(anchor="w", padx=15)

    def view_quiz(self, c):
        self.clear(); content = self.sidebar(); content.pack(side="right", fill="both", expand=True)
        qf = f"{c['code'].replace(' ','')}_quiz1.txt"
        if not os.path.exists(qf): open(qf, 'w').write(f"Sample Question for {c['name']}?|Option A|Option B|Option C|Option D|A")
        
        qs = load_quiz(qf); vars = []
        scroll = ctk.CTkScrollableFrame(content, fg_color="transparent"); scroll.pack(fill="both", expand=True, padx=40, pady=20)
        ctk.CTkLabel(scroll, text=f"📝 Quiz: {c['code']}", font=("Arial", 24, "bold")).pack(pady=20)
        
        for i, q in enumerate(qs):
            fr = ctk.CTkFrame(scroll, fg_color=C['sec']); fr.pack(fill="x", pady=12)
            ctk.CTkLabel(fr, text=f"Question {i+1}: {q['q']}", font=("Arial", 14, "bold")).pack(anchor="w", padx=20, pady=15)
            v = ctk.StringVar(); vars.append(v)
            for j, opt in enumerate(q['opts']):
                ctk.CTkRadioButton(fr, text=opt, variable=v, value=['A','B','C','D'][j], font=("Arial", 12)).pack(anchor="w", padx=40, pady=4)
        
        def sub():
            ans = [v.get() for v in vars]
            if not all(ans): return messagebox.showwarning("Incomplete", "Please answer all questions!")
            sc = calc_score(ans, [q['ans'] for q in qs])
            save_result(self.curr_user['id'], c['code'], sc)
            messagebox.showinfo("Quiz Submitted", f"Your Score: {sc}%\n{'Excellent!' if sc >= 80 else 'Good job!' if sc >= 60 else 'Keep practicing!'}"); 
            self.view_courses()
        ctk.CTkButton(scroll, text="Submit Quiz", fg_color=C['acc'], width=200, height=40, command=sub).pack(pady=30)

    def view_grades(self):
        self.clear(); content = self.sidebar(); content.pack(side="right", fill="both", expand=True)
        scroll = ctk.CTkScrollableFrame(content, fg_color="transparent"); scroll.pack(fill="both", expand=True, padx=30, pady=30)
        
        ctk.CTkLabel(scroll, text="📊 My Grades", font=("Arial", 26, "bold")).pack(anchor="w", pady=(0,10))
        grades = load_grades(self.curr_user['id'])
        gpa = calc_gpa(grades)
        
        gpa_card = ctk.CTkFrame(scroll, fg_color=C['pri'], height=80); gpa_card.pack(fill="x", pady=(10,20))
        ctk.CTkLabel(gpa_card, text=f"Current GPA: {gpa}", font=("Arial", 22, "bold")).pack(pady=20)

        if grades:
            crs_names = [g['crs'] for g in grades]
            scores = [int(g['grade']) for g in grades]
            
            graph_frame = ctk.CTkFrame(scroll, fg_color=C['sec']); graph_frame.pack(fill="x", pady=10)
            ctk.CTkLabel(graph_frame, text="Performance Overview", font=("Arial", 14, "bold")).pack(pady=5)
            
            fig, ax = plt.subplots(figsize=(6, 3), dpi=100)
            fig.patch.set_facecolor(C['sec']) 
            ax.set_facecolor(C['sec'])
            
            bars = ax.bar(crs_names, scores, color=C['acc'], width=0.4)
            ax.set_ylabel("Score", color="white")
            ax.set_ylim(0, 100)
            ax.tick_params(axis='x', colors='white')
            ax.tick_params(axis='y', colors='white')
            ax.spines['bottom'].set_color('white')
            ax.spines['left'].set_color('white')
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)

            canvas = FigureCanvasTkAgg(fig, master=graph_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)
            plt.close(fig)

        
        if grades:
            for g in grades:
                gf = ctk.CTkFrame(scroll, fg_color=C['sec']); gf.pack(fill="x", pady=6)
                ctk.CTkLabel(gf, text=g['crs'], font=("Arial", 13, "bold"), width=120, anchor="w").pack(side="left", padx=15, pady=12)
                ctk.CTkLabel(gf, text=g['type'], width=100, anchor="w").pack(side="left")
                ctk.CTkLabel(gf, text=f"{g['grade']}%", font=("Arial", 16, "bold"), text_color=C['succ'] if int(g['grade']) >= 60 else C['dang']).pack(side="right", padx=20)
                ctk.CTkLabel(gf, text=g['date'], text_color="gray", font=("Arial", 10)).pack(side="right", padx=10)
        else:
            ctk.CTkLabel(scroll, text="No grades available yet.", text_color="gray").pack(pady=30)

    def view_tasks(self):
        self.clear(); content = self.sidebar(); content.pack(side="right", fill="both", expand=True)
        scroll = ctk.CTkScrollableFrame(content, fg_color="transparent"); scroll.pack(fill="both", expand=True, padx=30, pady=30)
        
        ctk.CTkLabel(scroll, text="✅ My Tasks", font=("Arial", 26, "bold")).pack(anchor="w", pady=(0,20))
        tasks = load_tasks(self.curr_user['id'])
        
        pending = [t for t in tasks if t['status'] == 'pending']
        completed = [t for t in tasks if t['status'] == 'completed']
        
        ctk.CTkLabel(scroll, text=f"Pending ({len(pending)})", font=("Arial", 18, "bold"), text_color=C['warn']).pack(anchor="w", pady=(10,10))
        for t in pending:
            tf = ctk.CTkFrame(scroll, fg_color=C['sec']); tf.pack(fill="x", pady=5)
            ctk.CTkLabel(tf, text=t['crs'], font=("Arial", 12, "bold"), width=100, anchor="w").pack(side="left", padx=15, pady=10)
            ctk.CTkLabel(tf, text=t['task'], anchor="w").pack(side="left", fill="x", expand=True)
            ctk.CTkLabel(tf, text=f"Due: {t['due']}", text_color=C['dang'], font=("Arial", 10)).pack(side="right", padx=10)
            ctk.CTkButton(tf, text="✓", width=40, fg_color=C['succ'], command=lambda x=t: (update_task_status(self.curr_user['id'], x['task'], 'completed'), self.view_tasks())).pack(side="right", padx=5)
        
        if not pending: ctk.CTkLabel(scroll, text="No pending tasks!", text_color="gray").pack(anchor="w", padx=15, pady=10)
        
        ctk.CTkLabel(scroll, text=f"Completed ({len(completed)})", font=("Arial", 18, "bold"), text_color=C['succ']).pack(anchor="w", pady=(30,10))
        for t in completed[:5]:
            tf = ctk.CTkFrame(scroll, fg_color=C['sec']); tf.pack(fill="x", pady=3)
            ctk.CTkLabel(tf, text=f"✓ {t['crs']}: {t['task']}", text_color="gray", font=("Arial", 11)).pack(side="left", padx=15, pady=8)

    def view_calendar(self):
        self.clear(); content = self.sidebar(); content.pack(side="right", fill="both", expand=True)
        scroll = ctk.CTkScrollableFrame(content, fg_color="transparent"); scroll.pack(fill="both", expand=True, padx=30, pady=30)
        
        ctk.CTkLabel(scroll, text="📅 Academic Calendar", font=("Arial", 26, "bold")).pack(anchor="w", pady=(0,20))
        events = load_calendar()
        
        for e in events:
            ef = ctk.CTkFrame(scroll, fg_color=C['sec']); ef.pack(fill="x", pady=6)
            ctk.CTkLabel(ef, text=e['date'], font=("Arial", 13, "bold"), text_color=C['pri'], width=120, anchor="w").pack(side="left", padx=20, pady=15)
            ctk.CTkLabel(ef, text=e['event'], font=("Arial", 12)).pack(side="left")

    def view_notifications(self):
        self.clear(); content = self.sidebar(); content.pack(side="right", fill="both", expand=True)
        scroll = ctk.CTkScrollableFrame(content, fg_color="transparent"); scroll.pack(fill="both", expand=True, padx=30, pady=30)
        
        ctk.CTkLabel(scroll, text="🔔 Notifications", font=("Arial", 26, "bold")).pack(anchor="w", pady=(0,20))
        notifs = load_notifications(self.curr_user['id'])
        
        if notifs:
            for n in notifs:
                nf = ctk.CTkFrame(scroll, fg_color=C['sec']); nf.pack(fill="x", pady=6)
                ctk.CTkLabel(nf, text="🔔", font=("Arial", 20)).pack(side="left", padx=15)
                info = ctk.CTkFrame(nf, fg_color="transparent"); info.pack(side="left", fill="both", expand=True, pady=12)
                ctk.CTkLabel(info, text=n['msg'], font=("Arial", 13), anchor="w").pack(anchor="w")
                ctk.CTkLabel(info, text=n['date'], text_color="gray", font=("Arial", 10), anchor="w").pack(anchor="w")
        else:
            ctk.CTkLabel(scroll, text="No new notifications.", text_color="gray").pack(pady=30)

    def view_services(self):
        self.clear(); content = self.sidebar(); content.pack(side="right", fill="both", expand=True)
        scroll = ctk.CTkScrollableFrame(content, fg_color="transparent"); scroll.pack(fill="both", expand=True, padx=30, pady=30)
        
        ctk.CTkLabel(scroll, text="🛠 Services & Support", font=("Arial", 26, "bold")).pack(anchor="w", pady=(0,20))
        
        ctk.CTkLabel(scroll, text="Available Services", font=("Arial", 18, "bold")).pack(anchor="w", pady=(10,10))
        info = ctk.CTkTextbox(scroll, height=150, font=("Arial", 12)); info.pack(fill="x")
        info.insert("1.0", load_services("services")); info.configure(state="disabled")
        
        ctk.CTkLabel(scroll, text="Upcoming Conferences", font=("Arial", 18, "bold")).pack(anchor="w", pady=(20,10))
        conf = ctk.CTkTextbox(scroll, height=100, font=("Arial", 12)); conf.pack(fill="x")
        conf.insert("1.0", load_services("conferences")); conf.configure(state="disabled")
        
        ctk.CTkLabel(scroll, text="Submit Complaint", font=("Arial", 18, "bold")).pack(anchor="w", pady=(20,10))
        box = ctk.CTkTextbox(scroll, height=120); box.pack(fill="x")
        ctk.CTkButton(scroll, text="Send Complaint", fg_color=C['pri'], command=lambda: (save_complaint(self.curr_user['id'], box.get("1.0","end")), box.delete("1.0","end"), messagebox.showinfo("Sent","Complaint submitted successfully!"))).pack(pady=15, anchor="e")

    def view_profile(self):
        self.clear(); content = self.sidebar(); content.pack(side="right", fill="both", expand=True)
        scroll = ctk.CTkScrollableFrame(content, fg_color="transparent"); scroll.pack(fill="both", expand=True, padx=50, pady=40)
        
        card = ctk.CTkFrame(scroll, fg_color=C['sec']); card.pack(fill="both", pady=10)
        ctk.CTkLabel(card, text="🎓 Student Profile", font=("Arial", 26, "bold")).pack(pady=30)
        
        for k, v in [("Full Name", self.curr_user['name']), ("Student ID", self.curr_user['id']), ("Year", self.curr_user['yr']), ("Major", self.curr_user['maj'])]:
            r = ctk.CTkFrame(card, fg_color="transparent"); r.pack(fill="x", padx=80, pady=8)
            ctk.CTkLabel(r, text=f"{k}:", width=120, anchor="w", font=("Arial",13,"bold")).pack(side="left")
            ctk.CTkLabel(r, text=v, font=("Arial", 12)).pack(side="left")
        
        ctk.CTkButton(card, text="📊 Export Academic Report", width=250, command=lambda: messagebox.showinfo("Report Saved", f"Report saved as: {export_report(self.curr_user['id'])}")).pack(pady=25)
        
        pw_card = ctk.CTkFrame(scroll, fg_color=C['sec']); pw_card.pack(fill="x", pady=20)
        ctk.CTkLabel(pw_card, text="🔒 Change Password", font=("Arial", 18, "bold")).pack(pady=20)
        
        old_pw = ctk.CTkEntry(pw_card, placeholder_text="Current Password", show="*", width=300); old_pw.pack(pady=5)
        new_pw = ctk.CTkEntry(pw_card, placeholder_text="New Password", show="*", width=300); new_pw.pack(pady=5)
        confirm_pw = ctk.CTkEntry(pw_card, placeholder_text="Confirm Password", show="*", width=300); confirm_pw.pack(pady=5)
        
        def change_pw():
            if new_pw.get() != confirm_pw.get(): return messagebox.showerror("Error", "Passwords don't match!")
            if len(new_pw.get()) < 5: return messagebox.showerror("Error", "Password too short!")
            if change_password(self.curr_user['id'], old_pw.get(), new_pw.get()):
                messagebox.showinfo("Success", "Password changed successfully!")
                old_pw.delete(0, 'end'); new_pw.delete(0, 'end'); confirm_pw.delete(0, 'end')
            else: messagebox.showerror("Error", "Current password incorrect!")
        
        ctk.CTkButton(pw_card, text="Change Password", fg_color=C['acc'], width=250, command=change_pw).pack(pady=20)

if __name__ == "__main__":
    app = ZUPA_App()
    app.mainloop()


















