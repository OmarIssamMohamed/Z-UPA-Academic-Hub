


<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1F4E79,50:2E75B6,100:00B0F0&height=200&section=header&text=Z-UPA%20Academic%20Hub&fontSize=52&fontColor=ffffff&fontAlignY=38&desc=A%20Centralized%20Desktop%20Academic%20Management%20Platform&descAlignY=58&descSize=16" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.x-1F4E79?style=for-the-badge&logo=tkinter&logoColor=white)](https://github.com/TomSchimansky/CustomTkinter)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7+-11557C?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org)
[![OOP](https://img.shields.io/badge/Design-OOP%20Architecture-00B0F0?style=for-the-badge&logo=buffer&logoColor=white)]()
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen?style=for-the-badge)]()
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey?style=for-the-badge&logo=windows&logoColor=white)]()

<br/>

> **Z-UPA Academic Hub** is a production-quality desktop application engineered to eliminate academic fragmentation — consolidating course management, GPA tracking, attendance monitoring, performance analytics, and administrative services into one cohesive, beautifully designed platform.

<br/>

[🚀 Getting Started](#-installation) · [✨ Features](#-core-features) · [🏗️ Architecture](#️-system-architecture) · [📸 UI Preview](#-ui-preview) · [🤝 Contributors](#-contributors)

<br/>

</div>

---

## 📋 Table of Contents

- [💡 Why This Project?](#-why-this-project)
- [✨ Core Features](#-core-features)
- [🏗️ System Architecture](#️-system-architecture)
- [🛠️ Technology Stack](#️-technology-stack)
- [⚙️ Technical Highlights](#️-technical-highlights)
- [🔑 Key Engineering Concepts](#-key-engineering-concepts)
- [📸 UI Preview](#-ui-preview)
- [🚀 Installation](#-installation)
- [🗂️ Project Structure](#️-project-structure)
- [📖 Usage Guide](#-usage-guide)
- [🧪 Testing](#-testing)
- [🚧 Challenges Faced](#-challenges-faced)
- [📈 Future Improvements](#-future-improvements)
- [🎓 Learning Outcomes](#-learning-outcomes)
- [🤝 Contributors](#-contributors)
- [🙏 Acknowledgments](#-acknowledgments)
- [📄 License](#-license)

---

## 💡 Why This Project?

<div align="center">

> *"Students shouldn't spend more time navigating systems than actually learning."*

</div>

Modern university students face a structural problem: **academic fragmentation**. Grades live in one portal, tasks in another app, attendance sheets are manual, and course materials are scattered across platforms. The cognitive overhead of managing all of this is real — and it silently diminishes academic performance.

**Z-UPA Academic Hub was built to solve this.** As first-year Computer Science & AI students who lived this problem daily, we designed a platform that integrates every academic workflow into a single, intelligent interface.

| The Problem | Our Solution |
|-------------|--------------|
| 📊 GPA calculations done manually | ✅ Real-time automatic GPA engine |
| 📁 Course materials on separate platforms | ✅ Integrated content access per course |
| 📋 Tasks tracked in external apps | ✅ Built-in task manager with live dashboard sync |
| ⚠️ Attendance risks discovered too late | ✅ Threshold-based attendance alerts |
| 📝 No digital complaint channel | ✅ Complaint submission with timestamped logs |
| 🌑 Ugly, inconsistent legacy UIs | ✅ Modern dark/light CustomTkinter interface |

---

## ✨ Core Features

<details>
<summary><b>🔐 Authentication & Profile Management</b></summary>
<br/>

- Secure multi-user login with credential validation
- Password update with current-password verification
- Session isolation — zero data leakage between accounts
- Profile view displaying major, year, and student details

</details>

<details>
<summary><b>📊 Interactive Dashboard</b></summary>
<br/>

- Real-time statistical cards: **GPA**, **Pending Tasks**, **Enrolled Courses**
- Live pie chart showing task completion ratio (Matplotlib + CustomTkinter)
- Upcoming academic events panel
- Instant refresh on any data change — no manual reload required

</details>

<details>
<summary><b>🎓 GPA Tracking Engine</b></summary>
<br/>

- Automatic cumulative GPA calculation from all recorded grades
- 4.0-scale conversion using a standard grading rubric
- Per-course grade visualization via bar charts
- Historical grade trend tracking per assessment type

</details>

<details>
<summary><b>📅 Attendance Monitoring</b></summary>
<br/>

- Per-course attendance rate calculation
- **Visual red alert** for courses below the 75% threshold
- Attendance log history view
- Proactive warning system to prevent academic consequences

</details>

<details>
<summary><b>📚 Course & Content Management</b></summary>
<br/>

- Smart course filtering by **year** and **major**
- Direct access to PDF lecture materials and instructional videos
- Integrated quiz engine with instant score calculation and grade persistence
- Course-specific information hub per enrollment

</details>

<details>
<summary><b>✅ Task Manager</b></summary>
<br/>

- Add, view, and complete academic tasks
- Real-time dashboard synchronization on task state change
- Due date tracking with deadline awareness
- Pending count reflected instantly in dashboard analytics

</details>

<details>
<summary><b>🔔 Notifications & Calendar</b></summary>
<br/>

- Academic event calendar with upcoming deadline display
- Alerts module for attendance warnings and announcements
- University notice board with official institutional communications

</details>

<details>
<summary><b>🛠️ Administrative Services</b></summary>
<br/>

- Digital complaint submission with timestamped logging
- University announcement notice board
- Academic data export: generate a full personal academic report to text file

</details>

<details>
<summary><b>🎨 UI/UX Polish</b></summary>
<br/>

- **Dark Mode** (default) and **Light Mode** with one-click toggle
- Theme preference persisted to `config.json` across sessions
- Consistent Z-Blue color identity across all views
- Responsive layout with persistent sidebar navigation

</details>

---

## 🏗️ System Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                        Z-UPA ACADEMIC HUB                        │
├──────────────────────────────────────────────────────────────────┤
│                      PRESENTATION LAYER                          │
│         CustomTkinter Frames  ·  Matplotlib Canvas Embeds        │
├──────────────────────────────────────────────────────────────────┤
│                       CONTROLLER LAYER                           │
│            ZUPA_App Class  ·  Event Handlers  ·  Router          │
├──────────────────────────────────────────────────────────────────┤
│                     BUSINESS LOGIC LAYER                         │
│   calc_gpa()  ·  calc_attendance_rate()  ·  filter_courses()     │
│        calc_score()  ·  validate_login()  ·  change_password()   │
├──────────────────────────────────────────────────────────────────┤
│                      DATA ACCESS LAYER                           │
│            File I/O Functions  ·  JSON Config Parser             │
├──────────────────────────────────────────────────────────────────┤
│                      PERSISTENCE LAYER                           │
│  students.txt  ·  grades.txt  ·  courses.txt  ·  att.txt         │
│  tasks.txt  ·  complaints.txt  ·  notices.txt  ·  config.json    │
└──────────────────────────────────────────────────────────────────┘
```

### Design Pattern

The system follows a **GUI-adapted MVC architecture**:

| Layer | Role | Key Components |
|-------|------|----------------|
| **View** | Renders UI, captures events | CustomTkinter Frames per module |
| **Controller** | Manages state & navigation | `ZUPA_App` root class |
| **Model** | Data access & business logic | Pure functions + File I/O layer |

> **Navigation Pattern:** View transitions use a *destroy-and-rebuild* strategy — the content frame is cleared and rebuilt fresh on each navigation. This guarantees data freshness and eliminates stale state bugs entirely.

---

## 🛠️ Technology Stack

| Technology | Version | Role |
|------------|---------|------|
| **Python** | 3.10+ | Core runtime and application logic |
| **CustomTkinter** | 5.x | Modern, theme-aware GUI framework |
| **Matplotlib** | 3.7+ | Embedded analytics charts (pie & bar) |
| **JSON** | Native | User preference and config persistence |
| **File I/O** | stdlib | Lightweight file-based database layer |
| **os / datetime / webbrowser / re** | stdlib | Cross-platform utilities and validation |

---

## ⚙️ Technical Highlights

```python
# Real-time GPA computation engine
def calc_gpa(student_id: str, grades_file: str) -> float:
    """
    Reads all grade records for the authenticated student,
    maps percentage scores to 4.0-scale GPA points using
    a standard grading rubric, and returns the cumulative average.
    Handles empty grade sets gracefully (returns 0.00).
    """
```

```python
# Smart course filtering — predicate-based
def filter_courses(student_year: int, student_major: str) -> list:
    """
    Returns only courses matching BOTH the student's
    enrolled year AND declared major. Eliminates irrelevant
    course noise from the student's view.
    """
```

```python
# Theme-aware Matplotlib chart rendering
def build_chart(fig, ax, theme: str):
    """
    Reads active CustomTkinter appearance mode and applies
    matching Matplotlib style — dark background + white labels
    in dark mode, standard defaults in light mode.
    Eliminates visual discontinuity between UI and charts.
    """
```

### Embedded Analytics Architecture

```
CustomTkinter Window
└── CTkFrame (content area)
    └── FigureCanvasTkAgg  ◄── Matplotlib Figure
        └── Axes
            ├── Pie Chart  (Task Analytics)
            └── Bar Chart  (Grade Performance)
```

> Charts are explicitly closed via `plt.close(fig)` on view destroy to prevent Matplotlib's figure manager from accumulating memory across navigation cycles.

---

## 🔑 Key Engineering Concepts

### 1. Object-Oriented Architecture
The entire application is orchestrated by a single `ZUPA_App` controller class that inherits from `CTk`. This class owns all session state, manages view transitions, and coordinates communication between modules — eliminating global state and ensuring a single authoritative source of truth.

### 2. Separation of Concerns
Three strictly separated layers:
- **Presentation** — CustomTkinter widget construction only
- **Logic** — Pure functions with no GUI dependencies (independently testable)
- **Persistence** — Isolated file I/O functions (swappable to SQL without touching other layers)

### 3. Real-Time Data Synchronization
When a task is marked complete, the sequence is:
```
User action → Update tasks.txt → Invoke show_dashboard() → Fresh file read → Re-render stats + chart
```
No in-memory caching. Every dashboard render reads from authoritative file data.

### 4. Cross-Platform File Handling
All paths built with `os.path.join()` and anchored to `os.path.dirname(os.path.abspath(__file__))` — the application works identically on Windows and Linux with zero path configuration.

### 5. Modular Scalability
The data access layer is **intentionally replaceable**: all I/O is encapsulated in dedicated functions. Migrating from flat files to SQLite requires modifying only the data layer — the logic and GUI layers remain untouched.

---

## 📸 UI Preview

<div align="center">

### 🏠 Dashboard View
> *Real-time GPA card, task analytics pie chart, and upcoming events*

![Dashboard](screenshots/dashboard.png)

---

### 📊 Grades & Performance View
> *Per-course grade breakdown with Matplotlib bar chart visualization*

![Grades](screenshots/grades.png)

---

### 📚 Course Management View
> *Smart-filtered course catalog with material access and quiz launch*

![Courses](screenshots/courses.png)

---

### ✅ Task Manager View
> *Task list with live completion sync to dashboard*

![Tasks](screenshots/tasks.png)

---

### 🌙 Dark / ☀️ Light Theme
> *System-wide theme with persistent user preference*

| Dark Mode | Light Mode |
|-----------|------------|
| ![Dark](screenshots/dark_theme.png) | ![Light](screenshots/light_theme.png) |

</div>

> 📌 **Note:** Place your screenshots in a `/screenshots` folder at the repo root and update the paths above.

---

## 🚀 Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.10 or higher
- pip (Python package manager)

### Step 1 — Clone the Repository

```bash
git clone https://github.com/your-username/z-upa-academic-hub.git
cd z-upa-academic-hub
```

### Step 2 — Create a Virtual Environment *(recommended)*

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

**`requirements.txt`**
```
customtkinter>=5.0.0
matplotlib>=3.7.0
```

> All other dependencies (`os`, `json`, `datetime`, `re`, `webbrowser`) are part of Python's standard library — no additional installation required.

### Step 4 — Run the Application

```bash
python main.py
```

### Default Login Credentials *(for testing)*

| Student ID | Password |
|------------|----------|
| `2025081341` | `omar123` |
| `[ID-2]` | `[password-2]` |

> ⚠️ Replace with your actual test credentials from `data/students.txt`

---

## 🗂️ Project Structure

```
z-upa-academic-hub/
│
├── 📄 main.py                    # Application entry point
│
├── 📁 data/                      # File-based database
│   ├── students.txt              # Credentials & student profiles
│   ├── grades.txt                # Assessment records
│   ├── courses.txt               # Course catalog
│   ├── att.txt                   # Attendance logs
│   ├── tasks.txt                 # Student tasks
│   ├── complaints.txt            # Submitted complaints
│   ├── notices.txt               # University announcements
│   └── config.json               # User preferences (theme, etc.)
│
├── 📁 materials/                 # Course content
│   ├── pdfs/                     # Lecture PDF files
│   └── quizzes/                  # Quiz question files per course
│
├── 📁 screenshots/               # UI screenshots for README
│
├── 📄 requirements.txt           # Python dependencies
├── 📄 README.md                  # This file
└── 📄 LICENSE                    # MIT License
```

---

## 📖 Usage Guide

<details>
<summary><b>🔐 Logging In</b></summary>
<br/>

1. Launch the application with `python main.py`
2. Enter your **Student ID** and **Password**
3. Click **Login** — you'll be taken to your personalized dashboard

</details>

<details>
<summary><b>📊 Viewing Your Dashboard</b></summary>
<br/>

Your dashboard immediately displays:
- **Current GPA** — computed from all your recorded grades
- **Pending Tasks** — count of incomplete to-do items
- **Enrolled Courses** — count of courses in your academic year/major
- **Task Analytics Chart** — visual breakdown of completion status

</details>

<details>
<summary><b>📚 Accessing Courses & Taking Quizzes</b></summary>
<br/>

1. Click **Courses** in the sidebar
2. Your courses are auto-filtered by your year and major
3. Click any course to access:
   - 📄 PDF lecture materials
   - 🎥 Video lecture links
   - 📝 Quiz for the course
4. Complete the quiz — your score is saved and affects your GPA instantly

</details>

<details>
<summary><b>✅ Managing Tasks</b></summary>
<br/>

1. Click **Tasks** in the sidebar
2. Add a new task with a description and due date
3. Mark tasks as **Complete** — the dashboard pie chart updates immediately
4. Track your pending workload at a glance

</details>

<details>
<summary><b>⚠️ Monitoring Attendance</b></summary>
<br/>

1. Click **Grades** in the sidebar, then navigate to **Attendance**
2. Each course shows your attendance percentage
3. Courses below **75%** are highlighted in **red** — act quickly!

</details>

<details>
<summary><b>🎨 Switching Themes</b></summary>
<br/>

- Click the **theme toggle button** in the bottom-left corner of the sidebar
- The switch applies instantly across all views
- Your preference is saved automatically — it persists across restarts

</details>

<details>
<summary><b>📤 Exporting Your Academic Report</b></summary>
<br/>

1. Click **Profile** in the sidebar
2. Click **Export Report**
3. A structured `.txt` file with your full academic history is generated in the app directory

</details>

---

## 🧪 Testing

The core algorithmic functions were validated with unit tests covering standard cases, boundary conditions, and edge cases:

| Function | Test Scenario | Expected | Result |
|----------|--------------|----------|--------|
| `calc_gpa` | Standard grades (85, 78, 92) | 3.37 GPA | ✅ PASS |
| `calc_gpa` | No grades recorded | 0.00 GPA | ✅ PASS |
| `calc_attendance_rate` | 10/15 sessions attended | 66.7% 🔴 | ✅ PASS |
| `calc_attendance_rate` | Full attendance 15/15 | 100% | ✅ PASS |
| `calc_score` | 3 correct / 5 questions | 60% | ✅ PASS |
| `validate_login` | Valid credentials | Student record | ✅ PASS |
| `validate_login` | Wrong password | None returned | ✅ PASS |
| `filter_courses` | Year 1 + CSAI major | CSAI Year-1 only | ✅ PASS |

---

## 🚧 Challenges Faced

### 🎨 Matplotlib × CustomTkinter Theme Conflict
Charts rendered with Matplotlib's default white background in dark mode, creating a jarring visual break. **Solution:** A theme-aware chart renderer reads the active CustomTkinter appearance mode and applies matching Matplotlib style on every chart generation.

### 🔄 Stale Dashboard Data After Task Updates
Early builds cached student data in memory at login. Completing a task didn't update the dashboard statistics. **Solution:** Refactored all data reads to occur at the *point of display* from the authoritative file source — guaranteeing freshness with no synchronization complexity.

### 🖥️ Cross-Platform Path Failures
Windows-style paths caused `FileNotFoundError` on Linux. **Solution:** All path construction migrated to `os.path.join()` with an `os.path.abspath(__file__)` anchor point.

### 🧠 Memory Accumulation from Matplotlib Figures
Repeated navigation caused memory growth. Matplotlib's figure manager retained references to all historical figures. **Solution:** Explicit `plt.close(fig)` and `canvas.get_tk_widget().destroy()` calls added to every view teardown.

### 👥 Team Coding Inconsistency
Three developers writing in parallel produced style drift: naming mismatches, duplicated logic, inconsistent widget sizing. **Solution:** A shared coding standard document + mandatory code review before every integration session.

---

## 📈 Future Improvements

| Priority | Feature | Description |
|----------|---------|-------------|
| 🔴 High | **SQLite Migration** | Replace flat-file storage with SQLite for transactions, foreign keys, and query performance |
| 🔴 High | **Cryptographic Password Hashing** | Migrate to `bcrypt` / `Argon2` for proper credential security |
| 🟡 Medium | **REST API Backend** | FastAPI backend enabling multi-device sync and instructor dashboards |
| 🟡 Medium | **Automated Test Suite** | `pytest` unit + integration test coverage for all modules |
| 🟡 Medium | **Mobile Companion App** | Kivy or Flutter mobile app with push notifications |
| 🟢 Low | **AI Academic Advisor** | LLM-powered study recommendations based on grade trends and attendance patterns |
| 🟢 Low | **Calendar Export** | iCal-format academic calendar export for Google Calendar / Outlook sync |

---

## 🎓 Learning Outcomes

Building Z-UPA Academic Hub produced deep, practical competence across multiple engineering dimensions:

- **Python Mastery** — OOP architecture, file I/O, standard library depth, modular design
- **GUI Engineering** — CustomTkinter widget lifecycle, theme systems, embedded Matplotlib canvases
- **Software Architecture** — MVC pattern, separation of concerns, scalable module design
- **Data Engineering** — Schema design for flat-file databases, data validation, atomic write patterns
- **Collaborative Development** — Git workflows, code review practices, team coding standards
- **UX Thinking** — Real-time synchronization, visual feedback design, accessibility considerations
- **Problem-Driven Development** — Building from lived user pain, not speculative requirements
- **Debugging & Optimization** — Memory profiling, cross-platform testing, performance debugging

---

## 🤝 Contributors

<div align="center">

| <img src="https://github.com/identicons/omar.png" width="80" height="80" style="border-radius:50%"/> | <img src="https://github.com/identicons/teammate2.png" width="80" height="80" style="border-radius:50%"/> | <img src="https://github.com/identicons/teammate3.png" width="80" height="80" style="border-radius:50%"/> |
|---|---|---|
| **Omar Issam Mohamed** | **[Teammate 2 Name]** | **[Teammate 3 Name]** |
| Lead Developer & Architect | GUI Engineer & UX Designer | Data Engineer & QA Lead |
| System architecture, GPA engine, auth | CustomTkinter interface, theme system | File I/O layer, data export, testing |
| [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github)](https://github.com/your-profile) | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github)](https://github.com/teammate2) | [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github)](https://github.com/teammate3) |

</div>

---

## 🙏 Acknowledgments

- **Our course instructor and supervisor** — for guidance, constructive feedback, and raising the bar throughout the project lifecycle
- **The School of CSAI** — for an academic environment that challenges students to build real things
- **[Tom Schimansky](https://github.com/TomSchimansky/CustomTkinter)** — for the exceptional CustomTkinter library that made our UI vision achievable
- **The Matplotlib team** — for a data visualization library that integrates seamlessly into desktop Python applications
- **The Python Foundation** — for the language, standard library, and ecosystem that made all of this possible

---

## 📄 License

```
MIT License

Copyright (c) 2026 Omar Issam Mohamed, [Teammate 2], [Teammate 3]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

See [LICENSE](LICENSE) for full terms.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00B0F0,50:2E75B6,100:1F4E79&height=120&section=footer" width="100%"/>

**Built with 💙 by the Z-UPA Team · School of Computational Sciences and Artificial Intelligence · 2026**

*"Engineered to simplify. Designed to inspire."*

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Built with CustomTkinter](https://img.shields.io/badge/Built%20with-CustomTkinter-1F4E79?style=flat-square)](https://github.com/TomSchimansky/CustomTkinter)

</div>

