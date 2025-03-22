# swift_Solution.py
SWIFT code solution for ensuring international wire transfers.

# Important
- The code assumes the spreadsheet is contained inside the data/ folder.
- The code assumes there is a "BIC" column in the spreadsheet.
- a "requirements.txt" file is added to ensure the needed dependencies are installed. Install dependencies by running "pip install -r requirements.txt"

# Features
- Retrieve SWIFT code details using an API.
- Handles missing or invalid SWIFT codes.
- Lightweight and runs from a single Python file ("swift_Solution.py").
- Built-in unit tests.

# Instructions
1. Install dependencies by running "requirements.txt"
2. Setup data in the following manner:
   
   swift-api/
   │── data/
   │   ├── swift_codes.xlsx
   │── app.py
   │── README.md

3. Run API server with "python swift_Solution.py"
4. Fetch details for a specific SWIFT code.
   Example: GET /swift/ABCDEFGHXXX

   Possible responses:
   - Response 200 - OK
     {
    "BIC": "ABCDEFGHXXX",
    "Bank Name": "Example Bank",
    "Country": "US",
    "City": "New York"
     }
     
   - Response 404 - Not Found or Invalid SWIFT Code
     {
    "detail": "SWIFT code not found"
     }

5. If all tests are passed the code prints:
   Running tests...
   All tests passed!

6. Optional: to run the server in live production run "uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4"
   This ensures the server is still running if the terminal is closed or the server restarted.
