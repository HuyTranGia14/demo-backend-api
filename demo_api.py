from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/login")
def login(username: str, password: str):
    if password == "123456":
        return {
            "success": True,
            "message": "Login successful",
            "profile_url": f"http://localhost:8000/profile/{username}"
        }
    else:
        return {
            "success": False,
            "message": "Invalid username or password"
        }

@app.get("/profile/{username}")
def get_profile(username: str):
    return {
        "username": username,
        "email": f"{username}@example.com",
        "role": "intern"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)