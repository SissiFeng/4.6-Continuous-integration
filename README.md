# NewsHarvester: CI/CD and Web Scraping Project

## Introduction

NewsHarvester is a web scraping project designed to demonstrate the principles of Continuous Integration and Continuous Deployment (CI/CD) in software development. While the project simulates web scraping functionality, its primary purpose is to showcase how CI/CD practices can be applied to any software project, including web scrapers.

## Project Significance

1. **CI/CD Experience**: This project introduces you to real-world CI/CD practices, essential in modern software development.
2. **Automated Testing**: Learn how to write and run automated tests, a crucial skill for ensuring code quality.
3. **Code Quality Tools**: Experience using linters, formatters, and type checkers to maintain high code standards.
4. **Version Control**: Practice using Git for version control, an indispensable tool in collaborative development.
5. **Python Programming**: Enhance your Python skills by implementing various functionalities.
6. **Software Design**: Understand how to structure a Python project with separate modules for different functionalities.

## Setup

You have two options to set up this project: using GitHub Codespaces or working locally.

### Option 1: GitHub Codespaces (Recommended)

1. Fork this repository to your GitHub account.
2. From your forked repository, click on the "Code" button.
3. Select the "Codespaces" tab.
4. Click on "Create codespace on main" to launch a new Codespace.
5. Wait for the Codespace to initialize. This may take a few minutes.
6. Once initialized, you'll have a fully configured development environment in your browser.

### Option 2: Local Setup

If you prefer to work on your local machine:

1. Fork this repository to your GitHub account.
2. Clone your forked repository:
   ```
   git clone https://github.com/your-username/NewsHarvester.git
   ```
3. Navigate to the project directory:
   ```
   cd NewsHarvester
   ```
4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```


## Tasks

1. Implement the following method in `src/scraper.py`:
   - `get_news_by_id(self, news_id: int) -> Dict[str, str]`
     💡 Hint: Use a loop or list comprehension to find the news item with the matching id. Remember to handle the case where the id doesn't exist.

2. Implement the following methods in `src/parser.py`:
   - `extract_keywords(article: Dict[str, str], num_keywords: int = 5) -> List[str]`
     💡 Hint: Split the article content into words, count their frequencies (consider using `collections.Counter`), and return the most common words. You might want to exclude very common words (stop words) for better results.
   
   - `categorize_article(article: Dict[str, str]) -> str`
     💡 Hint: Look for specific words in the article title or content that might indicate its category. You could use a simple if-else structure or a more sophisticated approach like a dictionary of category keywords.

3. Implement the following methods in `src/database.py`:
   - `update_article(self, article_id: int, updated_data: Dict[str, str])`
     💡 Hint: Use an SQL UPDATE statement. Be sure to handle the case where the article_id doesn't exist.
   
   - `delete_article(self, article_id: int)`
     💡 Hint: Use an SQL DELETE statement. Again, consider what should happen if the article_id doesn't exist.
   
   - `get_articles_by_category(self, category: str) -> List[Dict[str, str]]`
     💡 Hint: Use an SQL SELECT statement with a WHERE clause to filter by category. Remember to return the results in the same format as the `get_articles()` method.

For each implemented method:
- Ensure it passes the corresponding unit tests in the `tests/` directory.
- Add appropriate error handling and edge case management. Consider what should happen if inputs are invalid or if no results are found.
- Follow PEP 8 style guidelines. You can use the `flake8` tool to check your code style.
- Add type hints to your function parameters and return values to improve code readability and catch potential type-related errors early.

💡 Remember, the goal is not just to make the tests pass, but to write clean, efficient, and robust code. Think about how your implementation would handle real-world scenarios and edge cases.

## Running Tests

Run the test suite using pytest


## Code Quality Checks

Maintaining high code quality is crucial in professional software development. Here are the checks you should run and what they mean:

1. Run the linter:
   ```
   flake8 src tests
   ```
   💡 Flake8 checks your code for style and potential errors. It will output:
   - Line numbers where issues are found
   - Error codes (e.g., E501 for line too long)
   - Brief descriptions of the issues

   Aim for zero warnings. If you see output, it means there are style issues to fix.

2. Check code formatting:
   ```
   black --check src tests
   ```
   💡 Black is an opinionated code formatter. This command checks if your code meets Black's style without changing it.
   - If you see "All done!" it means your code is properly formatted.
   - If you see "would reformat file.py", it means that file needs formatting. Run `black src tests` to automatically format your code.

3. Run type checking:
   ```
   mypy src
   ```
   💡 Mypy checks for type consistency in your Python code. It will show:
   - File names and line numbers with type issues
   - Descriptions of type mismatches or other type-related problems

   Aim for "Success: no issues found". Any output means there are type inconsistencies to address.

4. Run tests with coverage:
   ```
   pytest --cov=src
   ```
   💡 This runs your tests and reports on code coverage. You'll see:
   - Test results (passes and failures)
   - A coverage report showing the percentage of code covered by tests
   - Aim for 100% coverage, but anything above 80% is generally considered good.

Understanding the output:
- For flake8: Each line of output represents a style issue. The number at the start is the line number in your code.
- For Black: "would reformat" means your code doesn't meet the style guide and needs formatting.
- For mypy: Each line of output represents a type issue. It will show the file, line number, and description of the problem.
- For pytest with coverage: Look at the percentage next to each file name. This represents how much of that file is covered by tests.

Remember, the goal is to have all these checks pass without any warnings or errors. This ensures your code is clean, well-formatted, type-safe, and well-tested.

## Continuous Integration

This project uses GitHub Actions for CI. On each push:
- All tests are run
- Code coverage is checked
- Linting and formatting are verified
- Type checking is performed

Check the Actions tab in your GitHub repository to see the results of these checks.

## Why Web Scraping for CI?

While this project simulates web scraping, the focus is on CI/CD practices. Web scraping projects often involve:
1. Frequent updates to handle changes in target websites
2. Need for robust error handling
3. Data processing and storage
4. Potential for breaking changes

These characteristics make web scraping projects excellent candidates for demonstrating CI/CD principles. The skills you learn here (automated testing, code quality checks, CI pipelines) are transferable to any software project.

## Submission

1. Complete all the tasks in the project.

2. Ensure all your changes are committed and pushed to your GitHub repository:
   ```
   git add .
   git commit -m "Complete NewsHarvester project"
   git push origin main
   ```

3. Wait for the GitHub Actions CI workflow to complete. You can check the status in the "Actions" tab of your GitHub repository.

4. Verify that all CI checks pass. If any checks fail, make necessary corrections and push your changes again.

5. Once all CI checks pass, create a new release:
   - Go to the "Releases" section in your GitHub repository
   - Click "Create a new release"
   - Set the tag version to "v1.0.0"
   - Set the release title to "NewsHarvester Project Submission"
   - In the description, briefly summarize your implementation and any challenges you faced
   - Click "Publish release"

6. After publishing the release, a new GitHub Action will automatically generate a submission report. You can find this report in the "Actions" tab of your repository:
   - Go to the "Actions" tab
   - Click on the most recent "Submission Report" workflow run
   - In the "Artifacts" section, you will see a "submission-report" file. This contains your submission details and test results.

7. Your submission is complete once the "Submission Report" workflow has finished successfully.

💡 Note: Make sure all your tests are passing and you have achieved satisfactory code coverage before creating your release. The submission report will include this information for grading purposes.

## Grading Criteria

- Correct implementation of required methods (40%)
- Passing all unit tests (20%)
- Code quality (adherence to PEP 8, proper error handling) (20%)
- Successful CI pipeline execution (20%)

Good luck, and remember: the goal is not just to make a web scraper, but to understand and apply CI/CD principles!
