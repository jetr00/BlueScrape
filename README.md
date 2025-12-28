BlueScrape is a Python-based tool designed to scrape and aggregate data efficiently. This project uses external APIs to fetch the latest information and process it locally.

## 📋 Prerequisites

Before running the program, ensure you have the following installed on your system:
* Python 3.13.5
* Git
* Pip (Python package manager)

---

## ⚙️ Setup & Installation

Follow these steps exactly to get the environment ready:

### 1. Clone the repository
bash:
git clone git@github.com:jetr00/BlueScrape.git
cd BlueScrape

### 2. Configure API Keys

The application requires a News API key to function. For security reasons, this key is kept in a separate folder.

    Create the apis folder:
    Bash

    mkdir apis

    Create the key file: Inside the apis folder, create a file named apis.env.

    Add your API key: Open the file and add your key in the following format:
    
    NEWS_API_KEY="your_api_key_here"

### 3. Install Dependencies

There is a requirements.txt file, install the necessary libraries:
Bash

pip install -r requirements.txt

Usage

To start the scraping process, run:
Bash

python3 main.py

### Built With

    Python - The core programming language.

    NewsAPI - Used for fetching data.

### Author

    jetr00 - John Choriatellis
