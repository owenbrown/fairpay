Eventually, the application will be an iOS and Android app.
Initially, the application will only be an web application.

# Structure
The application is a Django application.
- The reason for using Django is that it's ORM is top notch.
- Using SQLAlchemy slows down development.

It is structured as a single app.
When possible, the project strives to be as idiomatic as possible.
The application uses a tierd architecture. Management commands and views may extract from services. Services never extract from views or management commands. Anything can extract from models. Models never extract from services or views.

# Other
- All code is hosted in git
- The services will be deployed using render.com
- The datbase is PostgreSQL 
- Anything slow is handled by a queue. Initally, we use huey and PostgreSQL. 
- Machine learning is handled by Verfy

# User experience
Users create an account.
They service is free, but e must track usage to preent abuse.
When a user gos to the grocery store, the user scans tags of items.
After the user pays for their grocerys, they scan their receipt.
The application then tells the whether they were overcharged for any items.

# Frontend standards
- See docs/adr/frontend_standards.md


