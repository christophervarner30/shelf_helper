# Shelf Helper Application

A web-based application to help customers order items from high shelves in stores. This application provides an accessible interface for users to browse products, request assistance with hard-to-reach items, and receive notifications when their orders are ready for pickup.

## Setup Instructions

1. Install Python requirements:
```
pip install -r requirements.txt
```

2. Set up environment variables (optional but recommended for production):
```
# On Windows
set SECRET_KEY=your_secure_secret_key

# On Linux/Mac
export SECRET_KEY=your_secure_secret_key
```

3. Run the application:
```
python app.py
```

3. Access the application:
- Customer interface: http://localhost:5000
- Staff interface: http://localhost:5000/staff

## Features

### Customer Interface
- Browse available products with filtering and search capabilities
- Voice search functionality for hands-free operation
- Select items for pickup from various store locations
- Provide name for order identification
- Receive confirmation when order is placed

### Staff Interface
- View pending orders in real-time
- See product shelf locations and availability
- Mark orders as complete when items are retrieved
- Manage inventory efficiently

### Accessibility Features
- High contrast mode for visually impaired users
- Large text mode for better readability
- Voice search capabilities
- Keyboard navigation support
- Screen reader friendly with proper ARIA attributes
- Responsive design for all device sizes

### Security Features
- CSRF protection for all forms
- Secure authentication system
- Environment variable configuration for sensitive data
- Input validation and sanitization

## Initial Setup

The database will be automatically created when you first run the application. To add sample products quickly, you can use the provided script:

```
python add_sample_products.py
```

Or manually add products using the Python shell:

```python
from app import app, db, Product
with app.app_context():
    # Add sample products
    product = Product(
        name="Sample Product",
        description="Description",
        price=9.99,
        shelf_location="A1",
        stock=10,
        category="Electronics",
        high_shelf=True,
        image_url="https://example.com/image.jpg"
    )
    db.session.add(product)
    db.session.commit()
```

## Week 8 - Bug Fixing and Optimizations (May 21, 2025)

The following improvements were completed during Week 8:

### Security Enhancements
- Added CSRF protection to all form submissions
- Implemented environment variable for SECRET_KEY
- Added comprehensive error handling with try/catch blocks
- Improved form validation and data sanitization

### Accessibility Improvements
- Enhanced high contrast mode for visually impaired users
- Improved large text mode with better UI element sizing
- Fixed voice search with multi-language support (English and Spanish)
- Added visual feedback during voice recognition
- Improved keyboard navigation and focus management
- Enhanced screen reader compatibility with ARIA attributes

### Responsive Design Fixes
- Fixed layout issues on mobile devices
- Improved search filter positioning on small screens
- Enhanced modal dialogs for better mobile interaction
- Optimized touch targets for better usability

### General Bug Fixes
- Fixed missing image references
- Added better error messaging for users
- Fixed transaction handling in database operations
- Improved form validation with better user feedback
- Enhanced JavaScript error handling

### Documentation
- Updated README with comprehensive feature descriptions
- Added detailed setup instructions
- Included browser compatibility information

## Browser Compatibility

The application has been tested and works on the following browsers:
- Google Chrome (latest)
- Mozilla Firefox (latest)
- Microsoft Edge (latest)
- Safari (latest)

## Week 10 - Final Fixes and Optimizations (May 21, 2025)

This week focused on making the project feature complete and optimized, with an emphasis on bug fixes. The goal was to create working, bug-free code rather than adding new but potentially buggy features.

### Key Deliverables Completed:

1. **Bug Fixes**:
   - Fixed all remaining UI/UX issues across different browsers and devices
   - Resolved edge cases in form validation and data processing
   - Addressed accessibility issues for screen readers and keyboard navigation
   - Fixed voice recognition issues in different environments

2. **Feature Completion**:
   - Ensured all planned features are fully implemented and working correctly
   - Completed any partial implementations from previous weeks
   - Verified all user flows work from start to finish

3. **Optimizations**:
   - Improved page load times and application performance
   - Optimized database queries for faster response
   - Enhanced mobile responsiveness for all screen sizes
   - Reduced unnecessary code and improved maintainability

4. **User Testing**:
   - Conducted final user testing sessions to validate user experience
   - Collected and addressed feedback from real users
   - Verified application works correctly in different scenarios

5. **Documentation Updates**:
   - Updated SRS document with a changelog of all implemented features
   - Created comprehensive feature list in the documentation
   - Ensured all code is properly commented for future maintenance

### SRS Document Updates

The SRS document has been updated to reflect all the changes made during the development process. A detailed changelog has been added to track the evolution of features, and a comprehensive feature list has been included for reference.

### Final Delivery

The Shelf Helper application is now feature-complete, optimized, and ready for deployment. All planned requirements have been implemented, and the code is as bug-free as possible, focusing on quality over quantity of features.
