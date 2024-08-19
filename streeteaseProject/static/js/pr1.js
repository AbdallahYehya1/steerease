document.addEventListener('DOMContentLoaded', function() {
    const thumbnails = document.querySelectorAll('.thumbnail');


    const mainImage = document.querySelector('.product-image img');


    thumbnails.forEach(thumbnail => {
        thumbnail.addEventListener('click', function() {

            mainImage.src = this.src;

            
            thumbnails.forEach(thumb => thumb.classList.remove('selected'));
            
            this.classList.add('selected');
        });
    });
});
