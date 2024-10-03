# Socratic AI

SocraticAI is an innovative educational platform that leverages artificial intelligence and LLMs to teach concepts through the Socratic method. This intelligent teaching assistant guides students through conceptual understanding and practical implementation by asking probing questions rather than providing direct answers.

## Table of Contents

- [Key Features](#Key-Features)
- [Setup](#Setup)
  - [Installing Python](#Installing-Python)
    - [Windows Installation](#Windows-Installation)
    - [macOS Installation](#macOS-Installation)
    - [Linux Installation](#Linux-Installation)
      - [Ubuntu/Debian](#Ubuntu/Debian)
      - [Fedora](#Fedora)
  - [Installing Dependencies](#Installing-Dependencies)
  - [Obtain a Gemini API Key](#Obtain-a-Gemini-API-Key)
- [Running the Application](#Running-the-Application)   

## Key Features

- Interactive dialogue system that adapts to student understanding
- Large Language Models for natural dialogue and question generation
- Adaptive learning systems for personalized instruction

## Setup

### Installing Python

#### Windows Installation

##### Steps
1. Download Python
   - Visit [python.org/downloads](https://python.org/downloads)
   - Click "Download Python" (latest version)
   - The download will begin automatically

2. Run the Installer
   - Locate the downloaded file (usually in Downloads folder)
   - Right-click the installer and select "Run as administrator"
   - Important: Check "Add Python to PATH"
   - Click "Install Now" for standard installation

3. Verify Installation
   - Open Command Prompt (Win + R, type "cmd", press Enter)
   - Type: `python --version`
   - Type: `pip --version`
   
   Both commands should display version numbers.

4. Test Python
   ```bash
   python
   >>> print("Hello, World!")
   >>> exit()
   ```

#### macOS Installation

##### Steps
1. Using Homebrew (Recommended)
   ```bash
   # Install Homebrew if not installed
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   
   # Install Python
   brew install python
   ```

2. Alternative: Direct Download
   - Visit [python.org/downloads](https://python.org/downloads)
   - Download macOS installer
   - Open the downloaded .pkg file
   - Follow installation wizard

3. Verify Installation
   ```bash
   python3 --version
   pip3 --version
   ```

4. Test Python
   ```bash
   python3
   >>> print("Hello, World!")
   >>> exit()
   ```

#### Linux Installation

##### Ubuntu/Debian
1. Update Package List
   ```bash
   sudo apt update
   sudo apt upgrade
   ```

2. Install Python
   ```bash
   sudo apt install python3
   sudo apt install python3-pip
   ```

3. Verify Installation
   ```bash
   python3 --version
   pip3 --version
   ```

##### Fedora
1. Update System
   ```bash
   sudo dnf update
   ```

2. Install Python
   ```bash
   sudo dnf install python3
   sudo dnf install python3-pip
   ```

3. Verify Installation
   ```bash
   python3 --version
   pip3 --version
   ```

##### Test Python on Linux
```bash
python3
>>> print("Hello, World!")
>>> exit()
```

### Installing Dependencies

#### All OS (Windows/Mac/Linux)
```bash
# Install all at once
pip install python-dotenv google-generativeai Flask

# Or install individually
pip install python-dotenv
pip install google-generativeai
pip install Flask
```

#### Verify Installation
```python
from dotenv import load_dotenv
import google.generativeai as genai
from flask import Flask

print("All libraries installed successfully!")
```

Note: Use `pip3` instead of `pip` if needed. Add `sudo` for Linux/Mac if getting permission errors.

### Obtain a Gemini API Key

##### Getting a Gemini API Key

1. Visit Google AI Studio
   - Open [makersuite.google.com](https://makersuite.google.com)
   - Sign in with your Google account

2. Get API Key
   - Click on "Get API key" in the top right
   - Click "Create API key in new project" (or use existing project)
   - Copy and save your API key securely

3. Store API Key Safely
   - Create a `.env` file in your project
   - Add this line:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

## Running the Application

Simply run:
```bash
python app.py
```

Access app at: `http://127.0.0.1:5000`
