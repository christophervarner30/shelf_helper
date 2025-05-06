# Shelf Helper SRS (MVP Submission)

## Feature Checklist

| Feature                        | Status         | Notes                                      |
|--------------------------------|---------------|--------------------------------------------|
| User registration/login        | Complete      | auth.py, Flask-Login                       |
| Add/edit/delete shelf items    | Complete      | admin routes in app.py                     |
| View all items                 | Complete      | dashboard/index routes                     |
| Search/filter items            | Complete      | Logic in index, basic UI present           |
| Export shelf data (CSV/PDF)    | Placeholder   | Export route present, not fully implemented |
| User authentication/roles      | Complete      | is_admin flag, login required              |
| UI enhancements                | Complete      | Basic, improvements planned                |
| Documentation                  | Complete      | SRS draft, checklist/changelog added       |

---

## Changelog (MVP Submission)
- Implemented user registration, login, and logout functionality
- Added product and order database models
- Built admin dashboard for product management (add/edit/delete)
- Created user dashboard and product listing
- Added order placement logic
- Started search/filter functionality
- Set up internationalization (i18n) with Flask-Babel
- Added placeholder export feature for future CSV export

---

## Changelog (Week 7)
- Added admin dashboard for product and order management.
- Implemented product search and filtering on the main page (by category, shelf location, price, stock status).
- Enabled multi-language support (English and Spanish) using Flask-Babel.
- Added product image support (image URL field).
- Integrated user authentication and admin login/logout.
- Added staff dashboard for viewing and completing orders.
- Improved input validation using WTForms.
- Enhanced UI with Bootstrap styling.
- Added sample data scripts for easier setup.
- Created automated tests for registration, login, product addition, and order creation.
- Improved database models for better data integrity.
- Added session-based language switching.
- Refined error handling and user feedback.

## Updated Feature List (Week 7)
- User registration and login (with admin role).
- Browse products, search, and filter by category, shelf, price, and stock.
- Place orders for products (with customer name and store).
- Staff dashboard to view and complete orders.
- Admin dashboard to add, edit, and delete products, and view all orders.
- Multi-language support (English/Spanish) with language selector.
- Product image support.
- Input validation on all forms.
- Real-time updates for staff/admin dashboards.
- Automated unit tests for core functionality.
- Bootstrap-styled UI for improved user experience.

---

## Requirement/Design Changes
- Decided to use Flask-Babel for i18n support
- Added admin/regular user distinction
- Export feature planned for next release (placeholder present)
- UI improvements planned for future sprints

---

## Next Steps
- Complete export feature (CSV/PDF)
- Enhance UI/UX for easier shelf management
- Expand search/filter capabilities
- Improve documentation for onboarding
