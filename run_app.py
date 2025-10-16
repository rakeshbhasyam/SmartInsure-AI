#!/usr/bin/env python3
"""
Startup script to run both FastAPI backend and Streamlit frontend
"""
import subprocess
import sys
import time
import threading
import os
from pathlib import Path

def run_fastapi():
    """Run the FastAPI backend server"""
    print("🚀 Starting FastAPI backend server...")
    try:
        subprocess.run([
            sys.executable, "-m", "uvicorn", 
            "app:app", 
            "--host", "127.0.0.1", 
            "--port", "8000", 
            "--reload"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ FastAPI server failed to start: {e}")
    except KeyboardInterrupt:
        print("🛑 FastAPI server stopped")

def run_streamlit():
    """Run the Streamlit frontend"""
    print("🎨 Starting Streamlit frontend...")
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", 
            "run", "frontend.py",
            "--server.port", "8501",
            "--server.address", "127.0.0.1"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Streamlit frontend failed to start: {e}")
    except KeyboardInterrupt:
        print("🛑 Streamlit frontend stopped")

def main():
    """Main function to start both servers"""
    print("=" * 60)
    print("🏥 SmartInsure AI - Insurance Premium Predictor")
    print("=" * 60)
    print("Starting both FastAPI backend and Streamlit frontend...")
    print()
    
    # Check if required files exist
    if not Path("app.py").exists():
        print("❌ Error: app.py not found!")
        return
    
    if not Path("frontend.py").exists():
        print("❌ Error: frontend.py not found!")
        return
    
    # Start FastAPI in a separate thread
    fastapi_thread = threading.Thread(target=run_fastapi, daemon=True)
    fastapi_thread.start()
    
    # Wait a moment for FastAPI to start
    print("⏳ Waiting for FastAPI to initialize...")
    time.sleep(3)
    
    print()
    print("🌐 Services will be available at:")
    print("   • FastAPI Backend: http://127.0.0.1:8000")
    print("   • Streamlit Frontend: http://127.0.0.1:8501")
    print("   • API Documentation: http://127.0.0.1:8000/docs")
    print()
    print("Press Ctrl+C to stop both servers")
    print("=" * 60)
    
    try:
        # Start Streamlit in the main thread
        run_streamlit()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down both servers...")
        print("✅ All services stopped successfully!")

if __name__ == "__main__":
    main()
