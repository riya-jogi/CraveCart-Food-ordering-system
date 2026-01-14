# CraveCart - Food Delivery System

CraveCart is a comprehensive food delivery web application built with Django. It allows users to browse food items, add them to a cart, place orders, and track their status.

## Features

-   **User Authentication**: Secure user registration and login system.
-   **Browse Food**: Users can browse a variety of food items categorized for easy access.
-   **Shopping Cart**: Add items to the cart, update quantities, and view total costs.
-   **Order Management**: Place orders with options for payment methods (COD, Card, UPI) and shipping addresses.
-   **Order Tracking**: Track the status of orders (Pending, Processing, Delivered, Cancelled).
-   **Admin Panel**: Manage categories, food items, orders, and users via the Django Admin interface.

## Tech Stack

-   **Backend**: Django (Python)
-   **Database**: SQLite (Default)
-   **Frontend**: HTML, CSS, JavaScript
-   **Templating**: Django Template Language (DTL)

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

-   [Python](https://www.python.org/downloads/) (v3.8 or higher)
-   `pip` (Python package manager)

## Installation

Follow these steps to set up the project locally:

1.  **Clone the Repository** (or extract the downloaded zip file):
    ```bash
    git clone <repository-url>
    cd Food-Delivery-main
    ```

2.  **Create a Virtual Environment** (Recommended):
    ```bash
    # On Windows
    python -m venv venv
    venv\Scripts\activate

    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**:
    Since there is no `requirements.txt` provided, install Django manually:
    ```bash
    pip install django
    ```

4.  **Apply Database Migrations**:
    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser** (to access the admin panel):
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to set a username, email, and password.

6.  **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

## Usage

1.  Open your web browser and navigate to `http://127.0.0.1:8000/`.
2.  Register for a new account or log in.
3.  Browse the food catalog and add items to your cart.
4.  Proceed to checkout to place an order.
5.  Access the **Admin Panel** at `http://127.0.0.1:8000/admin/` to manage the system (requires superuser credentials).

## Authors

-   Riya Jogi & Diya Vaghasiya
