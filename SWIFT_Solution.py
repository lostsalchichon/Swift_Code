from fastapi import FastAPI, HTTPException
import pandas as pd

# Start FastAPI
app = FastAPI()

# Load SWIFT codes from a spreadsheet into a Pandas DataFrame
df = pd.read_excel("data/swift_codes.xlsx")

@app.get("/swift/{bic}")
def get_swift_code(bic: str):
    """Fetch SWIFT code by BIC"""
    result = df[df['BIC'] == bic].to_dict(orient="records")
    if not result:
        raise HTTPException(status_code=404, detail="SWIFT code not found")
    return result[0]

# Unit test using FastAPI's TestClient
if __name__ == "__main__":
    import uvicorn
    from fastapi.testclient import TestClient

    client = TestClient(app)

    def test_valid_swift_code():
        response = client.get("/swift/ABCDEFGHXXX")
        assert response.status_code == 200

    def test_invalid_swift_code():
        response = client.get("/swift/INVALID123")
        assert response.status_code == 404

    print("Running tests")
    test_valid_swift_code()
    test_invalid_swift_code()
    print("All tests passed")

    # Start FastAPI server
    uvicorn.run(app, host="127.0.0.1", port=8000)
