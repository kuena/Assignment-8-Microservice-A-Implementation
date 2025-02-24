### **README.md**  

```markdown
# 📊 Rating Average Microservice

## 📝 Overview  
This microservice calculates the **average rating** from a given list of numerical values (1-10 scale).  
It communicates using **ZeroMQ (ZMQ) Messaging Queue**.

---

## 🚀 How to Request Data  
To send a request to the microservice, use a **JSON-formatted message** containing a list of ratings.  
The client program must use **ZeroMQ** to send this request.

### **Example Request:**
```json
{
  "ratings": [8, 9, 7, 10, 6, 8, 7, 9]
}
```

### **Example Python Code to Send Request:**
```python
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")  # Connect to microservice

ratings_data = {"ratings": [8, 9, 7, 10, 6, 8, 7, 9]}
socket.send_json(ratings_data)  # Send request

response = socket.recv_json()  # Receive response
print("Average Rating:", response.get("average", "Error"))
```

---

## 📥 How to Receive Data  
The microservice responds with a JSON object containing either:  
✅ **The calculated average rating (integer)** OR  
❌ **An error message if the request is invalid**.

### **Example Response (Success):**
```json
{
  "average": 8
}
```

### **Example Response (Invalid Input):**
```json
{
  "error": "Invalid input: ratings must be a list of numbers"
}
```

---

## 🔧 Error Handling  
The microservice ensures **robust error handling** for common issues:  

| **Issue**             | **Error Message**                            |
|-----------------------|---------------------------------------------|
| Non-numeric values   | `"Invalid input: ratings must be a list of numbers"` |
| Empty list           | `"Invalid input: ratings must be a list of numbers"` |
| Missing `ratings` key | `"Invalid input: ratings must be a list of numbers"` |

---

## 📡 Communication Method  
- **Protocol:** ZeroMQ (ZMQ)  
- **Port:** `5555`  
- **Data Format:** JSON  
- **Type:** Request-Response (Synchronous)  

---

## 📊 UML Sequence Diagram  
This diagram shows how the client interacts with the microservice:

![UML Sequence Diagram](./uml_sequence_diagram.png)

### **Process Flow:**
1️⃣ **Client sends a request** with a list of ratings.  
2️⃣ **Microservice validates** the data.  
3️⃣ **Microservice computes** the average.  
4️⃣ **Microservice sends back** the calculated average or an error message.  

---

## 📂 Installation & Setup  
### **1️⃣ Install Dependencies**
Ensure you have Python and ZeroMQ installed:
```bash
pip install pyzmq
```

### **2️⃣ Start the Microservice**
Run the following command:
```bash
python rating_microservice.py
```
Expected output:
```
Rating Microservice is running...
```

### **3️⃣ Run the Test Client**
In a new terminal window, run:
```bash
python test_client.py
```
Expected output:
```
Average Rating: 8
```

---

## ⚠️ Troubleshooting & Common Issues  

### ❌ **Problem:** `ModuleNotFoundError: No module named 'zmq'`  
✅ **Solution:** Install ZeroMQ using:  
```bash
pip install pyzmq
```

### ❌ **Problem:** No response from the microservice  
✅ **Solution:** Ensure `rating_microservice.py` is **running before** executing the test client.

### ❌ **Problem:** Port already in use  
✅ **Solution:** Modify the **port number** in both files:
- In `rating_microservice.py`:  
  ```python
  socket.bind("tcp://*:5556")
  ```
- In `test_client.py`:  
  ```python
  socket.connect("tcp://localhost:5556")
  ```

---

## 🔄 Mitigation Plan (If Issues Occur)  
If my teammate **Anthony** experiences issues:  
- **Step 1:** Verify Python & ZeroMQ installation (`pip install pyzmq`).  
- **Step 2:** Confirm `rating_microservice.py` is running.  
- **Step 3:** Reach out via **Slack or Email** for assistance.  
- **Step 4:** Notify me **at least 2 days before the deadline** if major issues persist.  

👨‍💻 **My Availability:**  
- **Monday - Friday:** 3 PM - 6 PM (Teams or Email)  
- **Weekends:** Available upon request (response within 24 hours)  

---

## 🔗 GitHub Repository  
📌 **Clone this project from GitHub:**  
➡ **https://github.com/kuena/Assignment-8-Microservice-A-Implementation.git


---

## ✅ Summary  
- This microservice **calculates average ratings** on a **1-10 scale**.  
- It uses **ZeroMQ (ZMQ)** for communication.  
- **Clients must send valid JSON requests.**  
- **Handles errors gracefully** (invalid input, missing data).  
- **Teammates can integrate using the communication contract provided.**  
