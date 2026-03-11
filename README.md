# AI-Smart-Attendance-System
An AI-powered smart attendance system that automatically marks attendance using facial recognition.

## Features

* Face recognition using **DeepFace (FaceNet embeddings)**
* Real-time camera detection
* Face mask detection
* Attendance stored in **SQLite database**
* Automatic **Excel report generation**
* Interactive **Streamlit dashboard**

## Tech Stack

* Python
* OpenCV
* DeepFace
* TensorFlow
* Streamlit
* SQLite
* Pandas

## Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/ai-smart-attendance-system.git
```

Navigate to the project folder:

```
cd ai-smart-attendance-system
```

Create a virtual environment:

```
python -m venv myenv
```

Activate environment:

Windows:

```
myenv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
streamlit run app.py
```

## Project Structure

```
├── app.py
├── face_recognition.py
├── mask_detector.py
├── database.py
├── attendance.py
├── export_excel.py

## Future Improvements

* ArcFace based recognition
* Multi-face detection
* Cloud database
* Mobile interface
* FAISS based face search

## Author

Kushal Kadyan

