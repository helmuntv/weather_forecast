# Project name
Weather forecast

Application to obtain the weather forecast in a city or country

## Project installation

Follow the steps below to set up and run the project in your local environment.

### Previous requirements

- Python (versión 3.10.6)
- Pip (versión 23.1.2)
- Git (versión 2.34.1)

### Installation steps

1. Clone the repository to your local machine:

git clone https://github.com/helmuntv/weather_forecast.git

2. Navigate to the project directory:

cd weather_forecast

3. Create a virtual environment:

python -m venv venv

4. Activate the virtual environment:

- Windows:

venv\Scripts\activate

- Linux/Mac:

source venv/bin/activate

5. Install the project dependencies:

pip install -r requirements.txt

6. Configuration of the .env file:

- Rename the .env.example file to .env.

- Open the .env file and fill in the necessary environment variables.

7. Run the project:

python manage.py runserver

8. Access the application in your web browser:

http://localhost:8000/