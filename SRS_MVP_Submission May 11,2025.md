# Shelf Helper – Software Requirements Specification (SRS)

## 1. Introduction
Shelf Helper is a web-based application designed to help customers request assistance with products located on high shelves in retail stores. The application streamlines the process for both customers and staff, providing an efficient workflow from order placement to fulfillment.

---

## 2. Feature Checklist
| Feature                              | Status     | Notes                                    |
|--------------------------------------|------------|------------------------------------------|
| User registration/login              | Complete   | auth.py, Flask-Login                     |
| Add/edit/delete shelf items          | Complete   | admin routes in app.py                   |
| View all items                       | Complete   | dashboard/index routes                   |
| Search/filter items                  | Complete   | Logic in index, basic UI present         |
| Export shelf data (CSV/PDF)          | Placeholder| Export route present, not fully implemented |
| User authentication/roles            | Complete   | is_admin flag, login required            |
| UI enhancements planned              | Complete   | Basic, improvements planned              |
| Documentation, checklist/changelog   | Complete   | SRS, testing notes, changelog added      |

---

## 3. User Testing & Feedback (2025-05-10)
**Test Date:** 2025-05-10  
**Tester:** Family Member  
**Facilitator:** Chris

### Observations & Issues
- User could browse products and place an order without guidance.
- Some confusion at the login screen (customer vs. admin).
- “Order” button was easy to find, but confirmation could be clearer.
- Admin dashboard was intuitive, but user wanted a search/filter for orders.

### User Feedback
- **How well did this solve your problem?**  
  “It’s really helpful for getting help with high shelves—easy to pick what I need.”
- **What was difficult to understand?**  
  “I wasn’t sure if I needed to log in as a customer, or just the staff/admin. Also, after placing an order, I wasn’t sure if it worked.”
- **What worked well for you?**  
  “Browsing products and picking them was very straightforward.”
- **What features would you like to see?**  
  “A way to track my order status, and maybe a notification when it’s ready.”
- **If you could change anything about the app, what would it be?**  
  “Make the confirmation message after ordering more obvious. Maybe add a guest checkout.”

### Bugs Found
- None critical; minor confusion on login and order confirmation.

---

## 4. Changelog
- 2025-05-11: Created SRS for MVP submission with real user feedback and requirements checklist.
- 2025-05-10: Added user testing notes and updated feature list.
- Implemented user registration, login, and logout functionality.
- Built admin dashboard and product management (add/edit/delete).
- Created user dashboard and product listing.
- Added order placement logic.
- Started search/filter functionality.
- Set up internationalization (i18n) with Flask-Babel.
- Added placeholder export feature for future CSV export.

---

## 5. Updated Feature List
- User registration and login (with admin role).
- Browse products, search, and filter by category, shelf, price, and stock.
- Place orders for products (with customer name and store).
- Orders dashboard to view and complete orders.
- Admin dashboard to add, edit, and delete products, and view all orders.
- Multi-language support (English/Spanish) with language selector.
- Product image support.
- Input validation on all forms.
- Real-time updates for staff/admin dashboards.
- Bootstrap-styled UI for improved user experience.
- (Planned) Export feature for next release.
- (Planned) Order status tracking for customers.
- (Planned) Improved order confirmation and guest checkout.

---

## 6. Requirements/Design Changes
- Decided to use Flask-Babel for i18n support.
- Added admin/regular user distinction.
- Export feature planned for next release (placeholder present).
- UI improvements planned for future sprints.

---

## 7. Next Steps
- Complete export feature (CSV/PDF).
- Enhance UI/UX for easier shelf management.
- Expand search/filter capabilities.
- Improve documentation for onboarding.

---

## 8. Requirements Completion Checklist
- [x] Application tested by a real user (non-developer)
- [x] Observations and feedback recorded
- [x] Bugs and usability issues documented
- [x] SRS document updated with changelog and feature list
- [x] Testing notes included in repository

---

## 9. References
- User testing notes (see repository)
- Application code and documentation

---

*End of SRS Document*
