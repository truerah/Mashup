from flask import Flask, request, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')  # Ensure this matches your form's file name

@app.route('/submit', methods=['POST'])
def submit():
    singer_name = request.form['singerName']
    num_videos = request.form['numVideos']
    video_duration = request.form['videoDuration']
    email = request.form['email']
    output_file_name = request.form['outputFileName']

    try:
        # Call the main.py script with the provided inputs
        subprocess.run(['python', 'main.py', singer_name, str(num_videos), str(video_duration), output_file_name, email])
    except Exception as e:
        print(f"Error: {e}")

    return redirect(url_for('form'))  # Redirect back to the form after submission

if __name__ == '__main__':
    app.run(debug=True)
