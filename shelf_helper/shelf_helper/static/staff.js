function completeOrder(orderId) {
    fetch(`/complete_order/${orderId}`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById(`order-${orderId}`).remove();
        } else {
            alert('Failed to complete order');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while completing the order');
    });
}
