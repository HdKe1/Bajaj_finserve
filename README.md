
# BFHL API - Full Stack Task

A REST API built with FastAPI that processes arrays and categorizes data into numbers, alphabets, and special characters with additional transformations.

## 🚀 Live Demo

**API Endpoint**: https://bajaj-finserve-27o3.onrender.com/bfhl


## 📋 Features

- **POST /bfhl**: Main endpoint that processes input arrays
- **GET /bfhl**: Returns operation code and API logic documentation
- **Automatic API documentation** with FastAPI Swagger UI
- **CORS enabled** for web requests
- **Error handling** with proper HTTP status codes
- **Input validation** and type checking

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Runtime**: Python 3.12
- **Server**: Uvicorn
- **Hosting**: Render.com
- **Documentation**: Auto-generated with Swagger/OpenAPI

## 📊 API Functionality

The API processes an input array and returns:

1. **Status** - Success/failure indicator
2. **User Details** - User ID, Email, Roll Number
3. **Number Arrays** - Separated odd and even numbers (as strings)
4. **Alphabets Array** - All alphabetic characters in uppercase
5. **Special Characters** - Non-alphanumeric characters
6. **Sum** - Total of all numbers (returned as string)
7. **Concatenated String** - Alphabets in reverse order with alternating case

### Request Format
```json
{
  "data": ["a", "1", "334", "4", "R", "$"]
}
```

### Response Format
```json
{
  "is_success": true,
  "user_id": "firstname_lastname_ddmmyyyy",
  "email": "user@example.com",
  "roll_number": "ABC123",
  "odd_numbers": ["1"],
  "even_numbers": ["334", "4"],
  "alphabets": ["A", "R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}
```

## 🔧 Local Development

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd bfhl-api
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API**
   - API: http://localhost:8000/bfhl
   - Documentation: http://localhost:8000/docs
   - Health Check: http://localhost:8000/health

## 🧪 Testing

### Using Swagger UI (Recommended)
1. Go to [API Documentation](https://bajaj-finserv-27o3.onrender.com/docs)
2. Click on "POST /bfhl"
3. Click "Try it out"
4. Enter test data and execute

### Using curl
```bash
curl -X POST "https://bajaj-finserv-27o3.onrender.com/bfhl" \
     -H "Content-Type: application/json" \
     -d '{"data": ["a","1","334","4","R", "$"]}'
```

### Using JavaScript (Browser Console)
```javascript
fetch('https://bajaj-finserv-27o3.onrender.com/bfhl', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({"data": ["a","1","334","4","R", "$"]})
})
.then(response => response.json())
.then(data => console.log(data));
```

## 📝 Test Cases

### Test Case 1: Mixed Data
**Input**: `["a","1","334","4","R", "$"]`
**Expected Output**:
- odd_numbers: `["1"]`
- even_numbers: `["334","4"]`
- alphabets: `["A","R"]`
- special_characters: `["$"]`
- sum: `"339"`
- concat_string: `"Ra"`

### Test Case 2: Complex Array
**Input**: `["2","a", "y", "4","&","-","*","5","92","b"]`
**Expected Output**:
- odd_numbers: `["5"]`
- even_numbers: `["2","4","92"]`
- alphabets: `["A","Y","B"]`
- special_characters: `["&","-","*"]`
- sum: `"103"`
- concat_string: `"ByA"`

### Test Case 3: Only Alphabets
**Input**: `["A","ABcD","DOE"]`
**Expected Output**:
- odd_numbers: `[]`
- even_numbers: `[]`
- alphabets: `["A","ABCD","DOE"]`
- special_characters: `[]`
- sum: `"0"`
- concat_string: `"EoDdCbAa"`

## 📂 Project Structure

```
bfhl-api/
├── main.py              # FastAPI application
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
└── .gitignore         # Git ignore rules
```

## 🔄 API Logic Breakdown

### String Concatenation Algorithm
1. Extract all alphabetic characters from input
2. Convert to uppercase: `["A", "Y", "B"]`
3. Join into single string: `"AYB"`
4. Reverse the string: `"BYA"`
5. Apply alternating case pattern:
   - Index 0 (even): Uppercase → `"B"`
   - Index 1 (odd): Lowercase → `"y"`
   - Index 2 (even): Uppercase → `"A"`
6. Result: `"ByA"`

### Number Processing
- Identifies numeric strings using `int()` conversion
- Separates into odd/even arrays
- Maintains original string format in response
- Calculates sum and returns as string

### Character Classification
- **Numbers**: Convertible to integers
- **Alphabets**: Contains only alphabetic characters
- **Special Characters**: Non-alphanumeric characters

## 📄 License

This project is licensed under the MIT License.
