# Django Project with Daphne and Django Channels

This Django project harnesses the power of Django Channels with Daphne to enable real-time communication features in your web application.

[Detailed Blog](https://leo-stacks.com/blogs/how-to-use-websockets-django/ "Visit Blog")

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Leo-Stacks/django-websockets
    cd django-websockets
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run migrations:

    ```bash
    python manage.py migrate
    ```

2. Start the Daphne server:

    ```bash
    python manage.py runserver
    ```

3. Access your Django application at `http://localhost:8000`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
