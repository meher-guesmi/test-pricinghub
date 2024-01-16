6.**Access the API:**

1.**Clone the repository:**

    ``bash     git clone https://github.com/yourusername/pricinghub.git     ``

2.**Create a virtual environment:**

    ``bash     python -m venv venv     ``

3.**Activate the virtual environment:**

    - On Windows:

    ``bash       venv\Scripts\activate       ``

    - On Unix or MacOS:

    ``bash       source venv/bin/activate       ``

4.**Install dependencies:**

    ``bash     pip install -r requirements.txt     ``

5.**Run the application:**

    ``bash     python run.py     ``

Open your web browser or API testing tool and navigate to [http://localhost:5000/api/calculate_price_difference](http://localhost:5000/api/calculate_price_difference) with a POST request.

## API Usage

### Calculate Price Difference

**Endpoint:**`/api/calculate_price_difference`

**Method:**`POST`

**Input:**

- `calculation_type`: Type of calculation, either "last_two_dates" or "first_last_dates".
- `percent_threshold`: Percentage threshold for price difference (float).
- `euro_threshold`: Euro threshold for price difference (float).

**Example Input:**

```json
{
    "calculation_type": "last_two_dates",
    "percent_threshold": 25,
    "euro_threshold": 5
}
```
