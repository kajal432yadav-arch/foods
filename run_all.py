"""
Master Runner Script
Runs everything automatically:
1. Generates data
2. Runs analysis
3. Creates Excel report
4. Launches Streamlit dashboard
"""
import subprocess
import sys

def run(cmd):
    print(f"\n▶ Running: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"❌ Error running: {cmd}")
        sys.exit(1)
    print(f"✅ Done!")

if __name__ == "__main__":
    print("=" * 50)
    print("  SWIGGY ANALYTICS - AUTO SETUP & LAUNCH")
    print("=" * 50)

    run("python scripts/generate_data.py")
    run("python scripts/analysis.py")
    run("python scripts/create_excel_report.py")

    print("\n" + "=" * 50)
    print("  🚀 Launching Live Dashboard...")
    print("  Open http://localhost:8501 in your browser")
    print("=" * 50 + "\n")

    subprocess.run("python -m streamlit run scripts/dashboard_app.py", shell=True)
