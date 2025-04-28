# Shelf Helper SRS (MVP Submission)

## Feature Checklist

| Feature                        | Status         | Notes                                      |
|--------------------------------|---------------|--------------------------------------------|
| User registration/login        | Complete      | auth.py, Flask-Login                       |
| Add/edit/delete shelf items    | Complete      | admin routes in app.py                     |
| View all items                 | Complete      | dashboard/index routes                     |
| Search/filter items            | In Progress   | Logic in index, basic UI present           |
| Export shelf data (CSV/PDF)    | Placeholder   | Export route present, not fully implemented |
| User authentication/roles      | Complete      | is_admin flag, login required              |
| UI enhancements                | In Progress   | Basic, improvements planned                |
| Documentation                  | In Progress   | SRS draft, checklist/changelog added       |

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
