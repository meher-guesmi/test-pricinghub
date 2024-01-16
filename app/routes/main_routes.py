from flask import jsonify, request
from app import app
from data_processing.pipeline import main_pipeline

@app.route('/api/calculate_price_difference', methods=['POST'])
def api_calculate_price_difference():
    try:
        request_data = request.get_json()

        calculation_type = request_data.get('calculation_type')
        percent_threshold = request_data.get('percent_threshold')
        euro_threshold = request_data.get('euro_threshold')

        results = main_pipeline(calculation_type, percent_threshold, euro_threshold)

        return jsonify(results)

    except Exception as e:
        return jsonify({'error': str(e)}), 500