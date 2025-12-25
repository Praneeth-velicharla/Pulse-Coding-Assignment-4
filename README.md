📘 Pulse Coding Assignment 4 – SaaS Reviews Scraper
📌 Objective

Develop a Python script to collect SaaS product reviews for a given company
within a specified time period from multiple review platforms.

The script accepts user input and outputs the reviews in a structured JSON
format.

🛠️ Approach

Direct scraping of platforms like G2 and Capterra is restricted due to
anti-bot and security mechanisms.

To ensure reliability, legality, and consistent results, this project uses
SerpAPI (Google Search API) to fetch publicly indexed review data related
to the selected platforms.

This approach avoids scraping restrictions while still retrieving
relevant and real-world review information.

🌐 Supported Review Sources

G2

Capterra

Trustpilot (Bonus Source)

The script can be easily extended to support additional SaaS review platforms.

📥 Input Parameters

When running the script, the following inputs are required:

Company Name – Name of the SaaS product (e.g., slack)

Source – Review platform (g2, capterra, or trustpilot)

Start Date – Beginning of review period (YYYY-MM-DD)

End Date – End of review period (YYYY-MM-DD)

📤 Output Format

The script generates an output.json file containing an array of reviews.

Each review includes:

title – Review title or page title

review – Review content or snippet

date – Review publication date

reviewer – Reviewer identifier (platform-based)

rating – Rating (estimated or unavailable)

platform_link – Source page URL

source – Review platform name

📄 Sample Output
[
  {
    "title": "G2 for Slack | Slack Marketplace",
    "review": "G2 Reviews are published on a G2 Profile...",
    "date": "2025-02-02",
    "reviewer": "G2 User",
    "rating": "4/5",
    "platform_link": "https://slack.com/marketplace/AUKLFH44A-g2-for-slack",
    "source": "g2"
  }
]

▶️ How to Run the Project
1️⃣ Install Dependencies
pip install requests python-dateutil

2️⃣ Configure API Key

Set your SerpAPI key in the script:

SERP_API_KEY = "YOUR_SERPAPI_KEY"

3️⃣ Run the Script
python scraper.py

4️⃣ Provide Input When Prompted
Company name: slack
Source (g2/capterra/trustpilot): g2
Start date (YYYY-MM-DD): 2024-07-06
End date (YYYY-MM-DD): 2025-06-01

5️⃣ View Output

The extracted reviews will be saved in:

output.json

⭐ Bonus Feature

A third review source (Trustpilot) has been integrated using the same
workflow and input format, satisfying the bonus requirement of the assignment.