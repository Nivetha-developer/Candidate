# Candidate Directory Management System

This is a Django-based application for managing candidate information, providing CRUD operations for the CandidateDirectory model.


### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Installation

1. Clone the repository:

    ```
    git clone https://github.com/Nivetha-developer/Candidate.git
    cd candidate
    ```
2. Create virtual environment
    python -m venv venv

3. Activate  virtual environment
    source venv/bin/activate      # Unix or MacOS
    ( OR )
    .\venv\Scripts\activate      # Windows

4. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

5. Apply migrations to set up the database:

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Update data in database

### Usage

1. Run the development server:

    ```
    python manage.py runserver
    ```



## Endpoints

    1. Without Template
        1.candidate list
        http://127.0.0.1:8000/candidates

        2.create candidate
        http://127.0.0.1:8000/candidates

        3.candidate detail view
        http://127.0.0.1:8000/candidates/<int:pk>/

        4.update candidate
        http://127.0.0.1:8000/candidates/<int:pk>/

        5.delete candidate
        http://127.0.0.1:8000/candidates/<int:pk>/

    

    2. Using Templates
        1.candidate list
        http://127.0.0.1:8000/

        2.candidate detail view
        http://127.0.0.1:8000/candidate/<int:pk>/

        3.create new candidate
        http://127.0.0.1:8000/candidate/new/

        4.update candidate
        http://127.0.0.1:8000/candidate/<int:pk>/edit/

        5.delete candidate
        http://127.0.0.1:8000/candidate/<int:pk>/delete/


