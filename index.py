from flask import Flask, request, render_template
import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded file from the request
    file = request.files['file']

    # Create a VideoCapture object to read from the uploaded file
    cap = cv2.VideoCapture(file)

    while True:
        # Read a frame from the video capture
        ret, frame = cap.read()

        # Perform additional processing on the frame as needed

        # Exit the loop if the video capture is finished
        if not ret:
            break

    # Release the video capture and return a response to the user
    cap.release()
    return 'Video processing complete'

if __name__ == '__main__':
    app.run()
