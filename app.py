from flask import Flask, jsonify, render_template_string
from machine_info import get_machine_info
from time_synchronization import get_time_string
import os
import socket

app = Flask(__name__)

# html template include bootstrap and vanilla js
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial_scale=1.0">
    <title>Network Diagnostic Dashboard></title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container py-5">
        <h1 class="mb-4 text-center">Network Diagnostic Dashboard</h1>

        <div class="row g-4">
        <!-- machine info -->
        <div class="col-md-6">
            <div class="card h-100 shadow-sm">
                    <div class="card-header bg-primary text-white">System & Time Info</div>
                    <div class="card-body">
                        <h5 class="card-title" id="hostname">Loading...</h5>
                        <p class="card-text text-muted" id="sntp-time">Fetching SNTP Time...</p>
                        <button class="btn btn-outline-primary btn-sm" onclick="fetchSystemInfo()">Refresh Info</button>
                    </div>
                </div>
            </div>

            <!-- chat logs -->
            <div class="col-md-6">
                <div class="card h-100 shadow-sm">
                    <div class="card-header bg-success text-white">Chat Logs (chat_file.txt)</div>
                    <div class="card-body">
                        <pre id="chat-logs" class="bg-dark text-light p-3 rounded" style="max-height: 200px; overflow-y: auto;">Loading logs...</pre>
                        <button class="btn btn-outline-success btn-sm" onclick="fetchLogs()">Refresh Logs</button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
    // fetch data
        function fetchSystemInfo() {
        fetch('/api/system')
            .then(response => response.json())
            .then(data => {
                document.getElementById('hostname').innerText = `Host: ${data.hostname} | IP: ${data.ip}`;
                document.getElementById('sntp-time').innerText = `SNTP Time: ${data.time}`;
            });
        }

    function fetchLogs() {
        fetch('/api/logs')
            .then(response => response.json())
            .then(data => {
                document.getElementById('chat-logs').innerText = data.logs || "No logs found.";
            });
        }
        // retrieve data when the page loads
        window.onload = () => { fetchSystemInfo(); fetchLogs(); };
    </script>
</body>
</html>
"""

@app.route('/')
def dashboard():
    # render the main dahsboard interface
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/system')
def api_system():
    # api endpoint to provide machine and time data
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return jsonify({
        "hostname": hostname,
        "ip": ip_address,
        "time": get_time_string()
    })

@app.route('/api/logs')
def api_logs():
    # api endpoint to read and provide chat logs from text file
    try:
        with open("chat_file.txt", "r", encoding="utf-8") as f:
            content = f.read()
            if not content.strip():
                return jsonify({"logs": "File exist but empty."})
            return jsonify({"logs": content})
    except Exception as e:
        return jsonify({"logs": f"Python read error: {str(e)}"})

if __name__ == '__main__':
    print("Web Dashboard Started")
    print("Open http://127.0.0.1:5000 in your browser.")
    app.run(debug=True, port=5000)