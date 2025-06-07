🖥️ Desktop Intuitive Commercial Kernel

A modular, production-ready desktop application framework built with PyQt5, designed for internal ERP/CRM tooling. It is a fully-functional, cleanly architected, signal-based interface framework that follows separation of concerns, scalable routing, and event-driven rendering — written with real-world use in mind.

Originally created as a gesture of gratitude to a local vendor offering honest prices, this project now serves as a clean template for newcomers and professionals alike.

⸻

⚙️ Core Architecture

1. Controllers as Pages

Each page is a subclassed QMainWindow with:
	•	Independent UI logic.
	•	Connected signal/slot system.
	•	Support for data reloading (render_data).

2. Router System
	•	routes.py holds a simple, extensible list of route definitions.
	•	Pages (controllers) are dynamically imported and injected into a QStackedWidget.
	•	Navigation is signal-based (gotoSignal) allowing clean page transitions.

3. Provider Layer

CoreProvider.boot(widget) acts as a lifecycle hook:
	•	Automatically re-renders UI data when the page is opened.
	•	Can be disabled for performance tuning.

4. Data Layer
	•	SQLAlchemy ORM models (User, etc.)
	•	Authentication, password hashing (sha512 + salt)
	•	Session storage with relationship binding

5. Modularity and Extensibility
	•	Structure supports rapid creation of new modules (CRUD pages).
	•	Designed with junior onboarding and enterprise extensibility in mind.
	•	Localization hook via get_translate().

⸻

📁 Project Layout

```
app/
├── controllers/         # Page logic (MVC controllers)
├── models/              # SQLAlchemy models (User, Auth, etc.)
core/
├── window.py            # Router, page stack, signals
├── routes.py            # Page route declarations
├── providers/           # Lifecycle & global hooks
```

⸻

✨ Features
	•	🔐 JWT-based authentication with 2FA (via SMS)
	•	🧾 Token refresh logic with secure storage
	•	🛒 Cart system supporting both guests and authenticated users
	•	📦 Modular product & order management
	•	🧩 Middleware-based authorization (staff, guest, superuser)
	•	📬 SMS adapter interface (adapter pattern for notificators)
	•	⚙️ Async PostgreSQL with SQLAlchemy 2.0 style
	•	🔄 Pragmatic error handling and validation
	•	🧠 Clear separation of concerns (serializers, services, adapters)
	•	🐳 Dockerized with ready-to-use Makefile

⸻

🚀 Getting Started

🔧 Local Setup
	1.	Install dependencies

pip install -r requirements.txt

	2.	Set environment variables
Create a .env file:

DATABASE_URL=postgresql+asyncpg://user:pass@localhost/dbname
SECRET_KEY=your-super-secret
ALGORITHM=HS256
ENVIRONMENT=local

	3.	Run locally

make build
make start
make migrate

You will need Docker being installed.

⸻

✅ Auth Flow (Summary)
	1.	Login Attempt (no token):
	•	Password is verified.
	•	SMS 2FA code is sent.
	•	In local mode, the code is returned in the response for testing.
	2.	Login Attempt (with 2FA token):
	•	If valid and not expired, JWT tokens are returned.
	3.	Token Usage:
	•	JWTs are validated via custom middleware (BaseAuthMiddleware, StaffMiddleware, etc.)
	•	Behavior changes based on token source: cookie vs. header vs. guest.

⸻

💡 Use Cases
	•	Internal dashboards
	•	CRM/ERP modules
	•	Lightweight POS systems
	•	Embedded tooling for offline environments

⸻

🤝 Author

Emil Erofeevskiy
