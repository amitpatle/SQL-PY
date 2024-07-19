<img src="https://github.com/amitpatle/SQL-PY/blob/main/standard.gif" align="center" />
</div>
# SQL Query Generator

Welcome to the SQL Query Generator! This project utilizes a Large Language Model (LLM) to generate SQL queries based on user input prompts and database schemas. The tool also allows for the execution of these queries with user-provided database credentials.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- Generate SQL queries from natural language prompts.
- Customize the temperature of the model to control creativity.
- Provide database schema to guide query generation.
- Edit generated SQL queries before execution.
- Submit human feedback score for generated queries.
- Execute SQL queries directly from the interface.

## Installation

To get started, clone the repository and set up the environment:

```bash
git clone https://github.com/amitpatle/SQL-PY.git
cd SQL-PY
```

Create a virtual environment and activate it:

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py
```

Navigate to `http://127.0.0.1:5000` in your web browser to access the LLM SQL Query Generator interface.

### Form Fields

- **Enter Your Prompt**: Provide a natural language prompt describing the desired query.
- **Enter Your Database Schema**: Input the schema of the database to assist in generating accurate queries.
- **Model Temperature**: Adjust the temperature of the model to control the randomness and creativity of the generated queries.

### Executing Queries

After generating a query, you can:

1. Edit the generated query if needed.
2. Provide a human feedback score using the slider.
3. Enter database credentials (User Name, Password, Host, Database) to execute the query directly.

## Configuration

Configure environment variables in a `.env` file for sensitive information such as database credentials and API keys.

```env
DATABASE_USER=your_db_user 
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=your_db_host
DATABASE_NAME=your_db_name
```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
