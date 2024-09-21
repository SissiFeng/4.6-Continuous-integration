# NewsHarvester: CI/CD Assignment

## Introduction

NewsHarvester is a web scraping project designed to demonstrate Continuous Integration and Continuous Deployment (CI/CD) practices. This project includes a web scraper, HTML parser, and a database interface for storing and retrieving news articles.

## Objectives

By completing this assignment, you will:

1. Implement a web scraper with error handling and rate limiting
2. Create an HTML parser using BeautifulSoup
3. Develop a SQLite database interface
4. Write comprehensive unit tests
5. Set up a CI/CD pipeline using GitHub Actions
6. Implement code quality checks (linting, formatting)
7. Create and maintain project documentation
8. Perform security scanning on your code
9. Automate the deployment process

## Setup

1. Fork this repository to your GitHub account.
2. Clone your forked repository locally or open it in GitHub Codespaces.
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Tasks

1. Complete the TODOs in `src/scraper.py`, `src/parser.py`, and `src/database.py`.
2. Implement the missing unit tests in the `tests/` directory.
3. Update the usage documentation in `docs/usage.md`.
4. Modify the GitHub Actions workflow in `.github/workflows/ci.yml` if necessary.
5. Ensure your code passes all linting and formatting checks.
6. Address any security issues identified by Bandit.
7. Set up PyPI deployment credentials in your GitHub repository secrets.

## Submission

1. Ensure all your changes are committed and pushed to your GitHub repository.
2. Submit the URL of your GitHub repository to your instructor.

## Grading Criteria

- Correct implementation of scraper, parser, and database (30%)
- Comprehensive unit tests (20%)
- Proper error handling and edge case management (10%)
- Successful CI/CD pipeline execution (20%)
- Code quality (linting, formatting, security) (10%)
- Documentation quality (10%)

## Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Pytest Documentation](https://docs.pytest.org/)
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Bandit Documentation](https://bandit.readthedocs.io/)

Good luck!
