# 🎉 Fake API Maker

![GitHub](https://img.shields.io/github/license/With-555/Fake-API-Maker)
![Version](https://img.shields.io/github/v/release/With-555/Fake-API-Maker)
![Docker](https://img.shields.io/badge/docker-enabled-blue)

## Overview

Welcome to the **Fake API Maker** project! This tool, created by Felix-ITS, serves as a simple, fast, and easy-to-use generator for fake APIs. It's designed to assist frontend developers, testers, or any programmers in need of demo data. You can create RESTful endpoints based on JSON files effortlessly.

If you're looking to get started quickly, check out the [Releases section](https://github.com/With-555/Fake-API-Maker/releases) for downloadable files.

## Features

- **Fast Setup**: Get your fake API running in minutes.
- **Customizable**: Tailor your endpoints to fit your needs.
- **Easy to Use**: Simple commands to generate data.
- **Open Source**: Contribute to the project or use it freely.

## Topics

This project utilizes various technologies and libraries, including:

- **Celery**: For asynchronous task management.
- **Django**: The web framework that powers the API.
- **Django REST Framework**: To create RESTful APIs.
- **Docker**: For containerization.
- **Docker Compose**: To manage multi-container Docker applications.
- **Faker**: For generating fake data.
- **Faker Generator**: A library to create various types of fake data.
- **Redis**: For caching and data storage.
- **Python**: The programming language used.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.x**
- **Docker**
- **Docker Compose**

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/With-555/Fake-API-Maker.git
   cd Fake-API-Maker
   ```

2. Build the Docker container:

   ```bash
   docker-compose build
   ```

3. Start the application:

   ```bash
   docker-compose up
   ```

4. Access the API at `http://localhost:8000`.

For additional files and updates, please visit the [Releases section](https://github.com/With-555/Fake-API-Maker/releases).

## Usage

### Creating Endpoints

You can create custom endpoints by modifying the JSON configuration files in the `config` directory. Each file can define different types of data structures, such as:

- User profiles
- Product listings
- Blog posts

### Example

To create a simple user endpoint, you might define a JSON file like this:

```json
{
  "users": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    },
    {
      "id": 2,
      "name": "Jane Smith",
      "email": "jane.smith@example.com"
    }
  ]
}
```

Once your JSON is set up, you can access the endpoint via:

```
GET http://localhost:8000/api/users/
```

### Generating Fake Data

You can also generate fake data using the Faker library. To do this, simply call the relevant functions in your Python code:

```python
from faker import Faker

fake = Faker()
print(fake.name())
print(fake.email())
```

## Contributing

We welcome contributions! If you want to help improve this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, feel free to reach out to the maintainers:

- Felix-ITS Team: [felix-its@example.com](mailto:felix-its@example.com)

## Acknowledgments

- Thanks to the contributors and community for their support.
- Special thanks to the maintainers of the libraries used in this project.

## Conclusion

Thank you for checking out the **Fake API Maker**! We hope this tool simplifies your development process. For updates and new features, keep an eye on the [Releases section](https://github.com/With-555/Fake-API-Maker/releases).

Happy coding! 🚀