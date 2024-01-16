## Setup

1.**Clone the repository:**

    git clone https://github.com/meher-guesmi/pricinghub.git

2.**Create a virtual environment:**

    python -m venv venv

3.**Activate the virtual environment:**

    - On Windows:

    venv\Scripts\activate

    - On Unix or MacOS:

    source venv/bin/activate

4.**Install dependencies:**

    pip install -r requirements.txt

5.**Run the application:**

    python run.py

6.**Access the API:**

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
