AI Attendance System 🎓🤖

An AI-based attendance management system that automatically marks attendance using real-time face recognition through a webcam.
The system identifies known individuals and records their attendance with date and time in a CSV file.
🚀 Features
Real-time face detection & recognition

Automatic attendance logging

Stores records in CSV format

Simple and easy-to-use setup

Scalable for classrooms and offices

🛠 Technologies Used

Python

OpenCV

NumPy

face_recognition

📁 Project Structure
AI-Attendance-System/
├── known_faces/            # Images of known people
├── attendance.csv          # Attendance records
├── attendance_system.py    # Main Python script
├── requirements.txt        # Dependencies (optional)
└── README.md               # Project documentation

📸 Creating Known Faces

Create a folder named known_faces in the project directory.

Add clear, front-facing images of each person.

Image naming format:

Name.jpg


Example:

Ali.jpg
Sara.png
Ahmed.jpeg


Each image should contain only one face for best accuracy.

⚙️ Installation

Make sure Python 3.8+ is installed.

Install required libraries:
pip install opencv-python numpy face-recognition


⚠️ Note (Windows users):
If face_recognition fails to install, first install dlib:

pip install dlib
pip install face-recognition

▶️ How to Run

Navigate to the project folder:

cd AI-Attendance-System


Run the program:

python attendance_system.py


The webcam will open and:

Recognize faces in real-time

Mark attendance automatically

Save records in attendance.csv

📄 Attendance Output

The CSV file format:

Name, Date, Time
Ali, 2025-12-26, 10:32:45
Sara, 2025-12-26, 10:33:10

🎯 Use Cases

Classroom attendance

Office employee attendance

Secure access monitoring

Smart surveillance systems

🔒 Future Improvements

Database integration

Multiple camera support

Face mask detection

Web-based dashboard

👨‍💻 Author
Abdul Moeed
AI Student | Python Developer
📍 PAF-IAST
Abdul Moeed
AI Student | Python Developer
📍 PAF-IAST
