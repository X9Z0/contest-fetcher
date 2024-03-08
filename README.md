# Contest Fetcher

I created this small Python script to fetch and display information about upcoming coding contests from AtCoder and Codeforces. It's a simple tool designed to quickly provide me with the details of upcoming contests directly in the terminal.

## How it Works

1. **AtCoder:**

   - The script fetches the HTML content of the [AtCoder Contests](https://atcoder.jp/contests/) page.
   - It extracts data such as the start time, contest name, duration, and rated range of each upcoming contest.
   - The information is then displayed in a tabulated format in the terminal.

2. **Codeforces:**
   - Similarly, the script fetches the HTML content of the [Codeforces Contests](https://codeforces.com/contests) page.
   - It extracts contest titles, start times, and durations.
   - The extracted data is displayed in a tabulated format.

## How to Use

1. Clone the repository or download the script.

   ```bash
   git clone https://github.com/yourusername/contest-fetcher.git
   ```

2. Navigate to the script's directory.

   ```bash
   cd contest-fetcher
   ```

3. Create a virtual environment (recommended).

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment.

   - On Windows:

   ```bash
   .\venv\Scripts\activate
   ```

   - On Unix or MacOS:

   ```bash
   source venv/bin/activate
   ```

5. Install dependencies.

   ```bash
   pip install -r requirements.txt
   ```

6. Make the script executable.

   ```bash
   chmod +x contest_fetcher.py
   ```

7. Optionally, add the script's directory to your system's `PATH` to make it executable from anywhere.

   ```bash
   export PATH=$PATH:/path/to/contest-fetcher
   ```

8. Run the script.

   ```bash
   ./contest_fetcher.py
   ```

9. The script will fetch and display upcoming contest information from AtCoder and Codeforces.

## Dependencies

- [requests](https://docs.python-requests.org/en/latest/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [tabulate](https://pypi.org/project/tabulate/)

Install the dependencies using:

```bash
pip install requests beautifulsoup4 tabulate
```
