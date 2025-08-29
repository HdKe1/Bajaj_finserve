from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI(title="BFHL API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def is_number(s: str) -> bool:
    """Check if string represents a number"""
    try:
        int(s)
        return True
    except ValueError:
        return False

def is_alphabet(s: str) -> bool:
    """Check if string contains only alphabets"""
    return s.isalpha()

def is_special_character(s: str) -> bool:
    """Check if string is a special character (not alphanumeric)"""
    return not s.isalnum()

def create_concat_string(alphabets: list) -> str:
    """Create concatenated string in reverse order with alternating caps"""
    # Join all alphabets and reverse
    all_chars = ''.join(alphabets)[::-1]
    
    result = ""
    for i, char in enumerate(all_chars):
        if i % 2 == 0:
            result += char.upper()  # First character (index 0) should be uppercase
        else:
            result += char.lower()  # Second character (index 1) should be lowercase
    
    return result

@app.post("/bfhl")
async def process_data(request: dict):
    try:
        data = request.get("data", [])
        
        if not data:
            raise HTTPException(status_code=400, detail="Data array is required")
        
        # Initialize arrays
        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        numbers_for_sum = []
        
        # Process each item in the data array
        for item in data:
            if is_number(item):
                num = int(item)
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
                numbers_for_sum.append(num)
            elif is_alphabet(item):
                alphabets.append(item.upper())
            elif is_special_character(item):
                special_characters.append(item)
        
        # Calculate sum
        total_sum = sum(numbers_for_sum)
        
        # Create concatenated string
        concat_string = create_concat_string(alphabets)
        
        # Create response
        response = {
            "is_success": True,
            "user_id": "adi_poduval_5",
            "email": "adityapoduval2022@vitbhopal.ac.in", 
            "roll_number": "22BCE11151",
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_string
        }
        
        return response
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.get("/bfhl")
async def get_operation_code():
    """GET endpoint showing the operation logic"""
    return {
        "operation_code": 1,
        "logic": {
            "description": "POST /bfhl processes an array and returns categorized data",
            "input": "JSON with 'data' array containing mixed alphanumeric and special characters",
            "processing": {
                "numbers": "Separated into odd and even arrays (returned as strings)",
                "alphabets": "Converted to uppercase and stored in alphabets array", 
                "special_characters": "Non-alphanumeric characters stored separately",
                "sum": "Sum of all numeric values (returned as string)",
                "concat_string": "All alphabets joined, reversed, with alternating lowercase/uppercase"
            },
            "output": {
                "is_success": "Boolean status",
                "user_id": "Format: firstname_lastname_ddmmyyyy", 
                "email": "User email address",
                "roll_number": "College roll number",
                "odd_numbers": "Array of odd numbers as strings",
                "even_numbers": "Array of even numbers as strings", 
                "alphabets": "Array of uppercase alphabetic characters",
                "special_characters": "Array of special characters",
                "sum": "Sum of all numbers as string",
                "concat_string": "Processed alphabetic string (reversed with alternating UPPER/lower case starting with uppercase)"
            },
            "example": {
                "input": {"data": ["a","1","334","4","R","$"]},
                "output": {
                    "odd_numbers": ["1"],
                    "even_numbers": ["334","4"], 
                    "alphabets": ["A","R"],
                    "special_characters": ["$"],
                    "sum": "339",
                    "concat_string": "Ra"
                }
            }
        }
    }

@app.get("/")
async def root():
    return {"message": "BFHL API is running", "endpoint": "/bfhl"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)