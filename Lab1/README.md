# Lab 1 - CI/CD Workflow

## Workflow Description
This repository contains a simple Python project with a GitHub Actions CI pipeline.  
The workflow is configured to run only **after a Pull Request is merged into my personal branch (`jay-9062044`)**.  

The pipeline performs the following steps:
1. Install dependencies from `requirements.txt`.
2. Run all tests using `pytest`.
3. Execute the `show_info.py` script to display project information in the CI logs.

## Reviewer
Reviewer: Varun Kakkar