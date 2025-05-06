let selectedProductId = null;

function selectProduct(productId, productName) {
    selectedProductId = productId;
    document.getElementById('selectedProduct').textContent = `Selected: ${productName}`;
    document.getElementById('orderModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('orderModal').style.display = 'none';
    document.getElementById('customerName').value = '';
}

function submitOrder() {
    const customerName = document.getElementById('customerName').value;
    if (!customerName) {
        alert('Please enter your name');
        return;
    }

    fetch('/create_order', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            product_id: selectedProductId,
            customer_name: customerName
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Order created successfully! Please collect your item at the counter.');
            closeModal();
            location.reload();
        } else {
            alert('Failed to create order: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while creating your order');
    });
}

// AJAX Search & Filter
const searchForm = document.getElementById('searchForm');
if (searchForm) {
    searchForm.addEventListener('submit', function(e) {
        e.preventDefault();
        showSpinner();
        const formData = new FormData(searchForm);
        const params = new URLSearchParams(formData).toString();
        fetch('/?' + params, { headers: { 'X-Requested-With': 'XMLHttpRequest' } })
            .then(response => response.text())
            .then(html => {
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, 'text/html');
                const newGrid = doc.querySelector('.products-grid');
                const oldGrid = document.querySelector('.products-grid');
                if (newGrid && oldGrid) {
                    oldGrid.innerHTML = newGrid.innerHTML;
                }
                hideSpinner();
                showEmptyStateIfNeeded();
            });
    });
}

// Spinner
function showSpinner() {
    let spinner = document.getElementById('loadingSpinner');
    if (!spinner) {
        spinner = document.createElement('div');
        spinner.id = 'loadingSpinner';
        spinner.innerHTML = '<div class="spinner"></div>';
        spinner.className = 'loading-overlay';
        document.body.appendChild(spinner);
    }
    spinner.style.display = 'flex';
}
function hideSpinner() {
    const spinner = document.getElementById('loadingSpinner');
    if (spinner) spinner.style.display = 'none';
}

// Empty State
function showEmptyStateIfNeeded() {
    const grid = document.querySelector('.products-grid');
    if (grid && grid.children.length === 0) {
        if (!document.getElementById('emptyState')) {
            const empty = document.createElement('div');
            empty.id = 'emptyState';
            empty.className = 'empty-state';
            empty.innerHTML = '<img src="/static/images/empty.svg" alt="No results" style="width:120px;opacity:0.6;"><div>No products found. Try changing your search or filters!</div>';
            grid.appendChild(empty);
        }
    } else {
        const empty = document.getElementById('emptyState');
        if (empty) empty.remove();
    }
}

// Lightbox for product images
function openLightbox(src, alt) {
    let overlay = document.getElementById('lightboxOverlay');
    if (!overlay) {
        overlay = document.createElement('div');
        overlay.id = 'lightboxOverlay';
        overlay.className = 'lightbox-overlay';
        overlay.innerHTML = '<img id="lightboxImg" src="" alt=""><span class="lightbox-close" tabindex="0" aria-label="Close">&times;</span>';
        document.body.appendChild(overlay);
        overlay.querySelector('.lightbox-close').onclick = closeLightbox;
        overlay.onclick = function(e) { if (e.target === overlay) closeLightbox(); };
        overlay.querySelector('.lightbox-close').onkeydown = function(e) { if (e.key === 'Enter' || e.key === ' ') closeLightbox(); };
    }
    document.getElementById('lightboxImg').src = src;
    document.getElementById('lightboxImg').alt = alt;
    overlay.style.display = 'flex';
    document.body.style.overflow = 'hidden';
    document.getElementById('lightboxImg').focus();
}
function closeLightbox() {
    const overlay = document.getElementById('lightboxOverlay');
    if (overlay) overlay.style.display = 'none';
    document.body.style.overflow = '';
}
document.addEventListener('DOMContentLoaded', function() {
    document.body.addEventListener('click', function(e) {
        if (e.target.matches('.product-card img')) {
            openLightbox(e.target.src, e.target.alt);
        }
    });
});

// Accessibility: focus trap for modal/lightbox
// (Could be further enhanced)
