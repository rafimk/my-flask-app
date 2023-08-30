from flask import Flask, Response, request, jsonify
import matplotlib.pyplot as plt
import io
import os  # Import the os module

app = Flask(__name__)

api_port = int(os.environ.get('API_PORT', 80))

@app.route('/chart', methods=['POST'])
def generate_chart():
    try:
        # Get data from the request JSON
        data = request.json

        # Ensure that the request contains 'labels', 'sizes', and 'colors' keys
        if 'labels' not in data or 'sizes' not in data or 'colors' not in data:
            return jsonify({"error": "Invalid data format"}), 400

        labels = data['labels']
        sizes = data['sizes']
        colors = data['colors']

        # Create a pie chart
        plt.figure()  # Create a new figure explicitly.
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('Dynamic Pie Chart')

        # Save the chart as bytes in memory
        img_data = io.BytesIO()
        plt.savefig(img_data, format='png')
        img_data.seek(0)
        plt.close()

        # Return the image binary data as a Flask response
        return Response(img_data.getvalue(), content_type='image/png')
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=api_port, debug=False,  threaded=False)
