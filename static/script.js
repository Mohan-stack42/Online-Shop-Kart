// Change main image when click thumbnail
function changeImg(src) {
  document.getElementById('mainImg').src = src;
}

// Search live - highlight
document.addEventListener('DOMContentLoaded', function() {
  console.log('ShopKart Loaded!');
  // Confirm before remove from cart
  document.querySelectorAll('a[href*="remove"]').forEach(function(link) {
    link.addEventListener('click', function(e) {
      if (!confirm('Remove this item from cart?')) e.preventDefault();
    });
  });
});