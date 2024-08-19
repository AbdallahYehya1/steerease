document.addEventListener('DOMContentLoaded', function() {
    // Retrieve the cart data from the script tag
   
    console.log(cartData);
    generateTable(cartData);
});

function generateTable(cart) {
    const container = document.getElementById('cart-container');
    let table = document.getElementById('cart-table');

    let header = table.createTHead();
    let headerRow = header.insertRow(0);

    let headers = ['Item', 'Quantity', 'Price', 'Actions'];
    headers.forEach((headerText, index) => {
        let th = document.createElement('th');
        th.appendChild(document.createTextNode(headerText));
        headerRow.appendChild(th);
    });

    let tbody = table.createTBody();
    let totalPrice = 0;

    cart.forEach(product => {
        let row = tbody.insertRow();

        // Product Details
        let ItemCell = row.insertCell();
        ItemCell.classList.add("item-name");

        // Image element
        let image = document.createElement("img");
        image.setAttribute("src", "/static/images/" + product.imagepath);
        image.setAttribute("width", "100px");
        image.setAttribute("height", "100px");
        ItemCell.appendChild(image);

        // Span element
        let spanName = document.createElement("span");
        spanName.innerHTML = product.name +"<br/>"+product.size_name;
        ItemCell.appendChild(spanName);

        let quantityCell = row.insertCell();
        quantityCell.classList.add("quantityButtons");
        let minus = document.createElement('button');
        minus.classList.add('Quantity');
        minus.appendChild(document.createTextNode('-'));
        let plus = document.createElement('button');
        plus.appendChild(document.createTextNode('+'));
        plus.classList.add('Quantity');

        let spanQuantity = document.createElement("span");
        spanQuantity.innerHTML = product.quantity;
        quantityCell.appendChild(minus);
        quantityCell.appendChild(spanQuantity);
        quantityCell.appendChild(plus);

        minus.onclick = function(event) {
            const target = event.target;
            const parentRow = target.closest('tr');
            const secondCell = parentRow.cells[1];
            if (product.quantity == 1) {
                parentRow.remove();
                totalPrice -= product.price * product.quantity;
                cart = cart.filter(p => p.id !== product.id);

                total.innerHTML = totalPrice;
                checkIfTableIsEmpty();
            } else {
                product.quantity -= 1;
                secondCell.children[1].innerHTML = product.quantity;
                totalPrice -= product.price;
                total.innerHTML = totalPrice;
                checkIfTableIsEmpty();
            }
        };

        plus.onclick = function(event) {
            const target = event.target;
            const parentRow = target.closest('tr');
            const secondCell = parentRow.cells[1];
            product.quantity += 1;
            secondCell.children[1].innerHTML = product.quantity;
            totalPrice += product.price;
            total.innerHTML = totalPrice;
        };

        let cell = row.insertCell();
        cell.appendChild(document.createTextNode(product.price));
        totalPrice += product.price * product.quantity;

        cell = row.insertCell();
        let button = document.createElement('button');
        button.appendChild(document.createTextNode('Remove'));
        button.classList.add('danger');
        button.setAttribute("id", `${product.id}`);
        button.onclick = function(event) {
            const target = event.target;
            const parentRow = target.closest('tr');
            parentRow.remove();
            totalPrice -= product.price * product.quantity;
            cart = cart.filter(p => p.id !== product.id);

            total.innerHTML = totalPrice;
            checkIfTableIsEmpty();
        };

        cell.appendChild(button);
    });

    let total = document.getElementById("total");
    total.innerHTML = totalPrice;

    checkIfTableIsEmpty();
}

function checkIfTableIsEmpty() {
    const table = document.querySelector('#cart-container table');
    const tbody = table.querySelector('tbody');
    const checkoutButton = document.getElementById('checkout-button');

    if (tbody.rows.length === 0) {
        checkoutButton.onclick = function() {
            alert('The cart is empty! Cannot proceed to checkout.');
        };
    }
}
