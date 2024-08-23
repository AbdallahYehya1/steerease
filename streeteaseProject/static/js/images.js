document.getElementById('left-half').addEventListener('click', function() {
    console.log('Left half clicked');
    window.location.href = '/products/?gender=M';
});

document.getElementById('right-half').addEventListener('click', function() {
    console.log('Right half clicked');
    window.location.href = '/products/?gender=W';
});