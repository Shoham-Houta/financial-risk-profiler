# Project Plan: AI-Powered Financial Risk Profiler

## 🎯 Project Objectives
Develop a matchine learning tool that profiles a user's financial risk tolerance based on key personal and financial attributes, and output a risk level (Low, Medium, High) with suggested investment guidelines.

## 🗂️ Features (Planned)
- Survey-style input form (age, income, expenses, goals, knowledge)
- Risk classification using ML model
- Visual risk profile output
- Optional: Investment portfolio suggestions based on risk class

## 🧱 Tech Stack
- **Frontend/UI**: Streamlit
- **Backend/Model**: Python, scikit-learn
- **Data**: Simulated dataset (CSV), optionally extended with public datasets
- **Environment**: Conda + environment.yml
- **Deployment**: Streamlit Cloud or similar

## 📆 Development Phases

| Phase | Description | Status |
|-------|-------------|--------|
| 1     | Project setup, repo, environment       | ✅ Completed |
| 2     | Data simulation/collection + preprocessing | ⏳ In Progress |
| 3     | Model training + evaluation            | ⬜ Not Started |
| 4     | Streamlit UI + model integration       | ⬜ Not Started |
| 5     | Visualization + UX improvements        | ⬜ Not Started |
| 6     | Testing + cleanup                      | ⬜ Not Started |
| 7     | Deployment + full documentation        | ⬜ Not Started |

## 🧪 Dataset Design (Overview)
| Feature              | Type        | Description |
|----------------------|-------------|-------------|
| Age                  | int         | User age    |
| Income               | float       | Annual income |
| Expenses             | float       | Monthly expenses |
| Investment Knowledge | categorical | None/Basic/Advanced |
| Financial Goal       | categorical | Short-/Long-term |
| Risk Tolerance       | label       | Target variable (Low/Medium/High) |

## 🔮 Risk Assignment Heuristic (For Synthetic Data)
TBD: Initial logic may include high income + high knowledge → High risk.

## 📌 Notes
- All code will be modular (scripts under `/utils`, `/model`)
- Clean and reproducible environment via Conda
- Unit tests to be written for preprocessing/model components