# Shelf Helper Project Presentation

---

## Slide 1: Title Slide

**Shelf Helper**  
Christopher Varner  

---

## Slide 2: Project Overview

- Shelf Helper is a web application for managing store shelves, products, and orders.
- Designed for both customers and staff/admins.
- Focus: Simplicity, usability, and maintainability.

---

## Slide 3: Project Goals & Philosophy

- **Keep it Basic:** Only essential features.
- **User-Friendly:** Clean, modern UI.
- **Maintainable:** Simple code, clear docs, minimal dependencies.
- **Extensible:** Easy to add features in the future.

---

## Slide 4: Technology Stack

- **Backend:** Python 3, Flask
- **Frontend:** HTML, Bootstrap CSS, Jinja2 Templates
- **Database:** SQLite (easy setup, file-based)
- **Forms & Validation:** WTForms
- **Session Management:** Flask-Login

---

## Slide 5: Major Milestones

1. **Project Setup:** Flask app, SQLite DB, Bootstrap integration.
2. **User Auth:** Registration, login, logout (WTForms validation).
3. **Product Management:** Admin add/edit/delete.
4. **Order System:** Place/view/complete orders.
5. **Staff/Admin Dashboards:** Separate admin and staff panels.
6. **UI Consistency:** Bootstrap navbar and styling everywhere.
7. **Error Handling:** Form validation, error messages.
8. **Documentation:** README, code comments, user guidance.

---

## Slide 6: Application Structure

- **app.py:** Main Flask app, routes, logic.
- **templates/:** HTML templates for all pages.
- **static/:** Bootstrap CSS and other static files.
- **models.py:** Database models for User, Product, Order.
- **README.md:** Setup, usage, and feature documentation.

---

## Slide 7: User Roles & Permissions

- **Customer:**  
  - Register, login, browse products, place orders, view order history.
- **Staff:**  
  - View and complete pending orders.
- **Admin:**  
  - Login, manage products, view all orders.

---

## Slide 8: Customer Features

- **Registration/Login:**  
  - Secure account creation with validation.
- **Product Browsing:**  
  - See all available products, filter/search.
- **Order Placement:**  
  - Simple form, instant validation, error feedback.
- **Order History & Recommendations:**  
  - Dashboard shows past orders and suggested products.

---

## Slide 9: Staff/Admin Features

- **Admin Login:**  
  - Secure, separate login.
- **Product Management:**  
  - Add, edit, delete products (with validation).
- **Order Management:**  
  - View all orders, mark as completed.
- **Staff Dashboard:**  
  - See pending orders, complete them.

---

## Slide 10: Form Validation & Error Handling

- **WTForms:**  
  - All forms use WTForms for input validation.
- **Error Display:**  
  - Validation errors shown at the top of each form.
- **Flash Messages:**  
  - Feedback for login failures, invalid actions.
- **User Guidance:**  
  - Clear instructions and helpful error messages.

---

## Slide 11: Navigation & User Interface

- **Bootstrap Navbar:**  
  - Consistent navigation on all pages.
- **Responsive Design:**  
  - Works on desktop and mobile.
- **Visual Feedback:**  
  - Alerts for errors, confirmations, and actions.

---

## Slide 12: Database Models

- **User:**  
  - id, username, email, password_hash, is_admin
- **Product:**  
  - id, name, description, price, shelf_location, stock, category, high_shelf, image_url
- **Order:**  
  - id, product_id, customer_name, user_id, store, timestamp, status

---

## Slide 13: Key Functions & Routes

- `/register` — User registration
- `/login` — User login
- `/dashboard` — User dashboard (orders, recommendations)
- `/order` — Place an order
- `/admin/login` — Admin login
- `/admin` — Admin dashboard
- `/admin/add_product` — Add new product
- `/admin/edit_product/<id>` — Edit product
- `/admin/delete_product/<id>` — Delete product
- `/staff` — Staff dashboard (pending orders)
- `/complete_order/<id>` — Complete an order

---

## Slide 14: Example: Registration Flow

1. User fills registration form.
2. WTForms validates username, email, password.
3. If errors, they’re displayed at the top of the form.
4. On success, user is added to the database and redirected to login.

---

## Slide 15: Example: Admin Product Management

1. Admin logs in via `/admin/login`.
2. Can add, edit, or delete products.
3. All actions validated (e.g., name required, price must be a number).
4. Success/failure feedback shown to admin.

---

## Slide 16: Example: Order Placement & Completion

1. User selects product, fills order form.
2. System checks product stock and form validity.
3. Order is recorded and marked as pending.
4. Staff/admin views pending orders and marks as completed.

---

## Slide 17: Error Handling & User Feedback

- **Form Errors:**  
  - Shown in red alert boxes above forms.
- **Flash Messages:**  
  - For invalid logins, failed actions.
- **404/500 Pages:**  
  - (Optional) Can be added for friendlier error handling.

---

## Slide 18: Documentation & Support

- **README.md:**  
  - Setup, usage, feature list, troubleshooting.
- **Code Comments:**  
  - All major functions and routes are documented.
- **User Guidance:**  
  - Clear instructions on every page.

---

## Slide 19: Project Milestones (Timeline)

1. Project setup & planning
2. User authentication system
3. Product database & admin features
4. Order system & staff dashboard
5. UI/UX improvements (Bootstrap, navbar)
6. Validation, error handling, and documentation

---

## Slide 20: Future Improvements

- More flash messages for all actions
- Custom 404/500 error pages
- Automated tests for all flows
- Deployment to cloud (Heroku, etc.)
- More advanced reporting or analytics

---

## Slide 21: Conclusion

- **Shelf Helper** is a complete, basic shelf management and order app.
- All core features are implemented and tested.
- The codebase is simple, well-documented, and ready for use or extension.

---

## Slide 22: Thank You

**Questions?**  
Christopher Varner
