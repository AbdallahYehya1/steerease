document.addEventListener('DOMContentLoaded', function() {
    // Retrieve the cart data from the script tag
   
    console.log(cartData);
    generateTable(cartData);
});


/**
 * @param {*} type - | + | remove
 */
function wrapButtonWithFrom( type,id,sName) {
    // Create the form element
    
    let form = document.createElement('form');
    form.method = 'post';
    form.action = data_url;  // Specify the action URL
    let csrfToken = document.createElement('input');
    csrfToken.type = 'hidden';
    csrfToken.name = 'csrfmiddlewaretoken';
    csrfToken.value = csrftokenht;  // Use the embedded CSRF token
    form.appendChild(csrfToken);

    // Add hidden input for specify the type of operation
    let hiddenInput = document.createElement('input');
    hiddenInput.type = 'hidden';
    hiddenInput.name = "operation";
    hiddenInput.value = type.toLowerCase();
    form.appendChild(hiddenInput);
    let item = document.createElement('input');
    item.type = 'hidden';
    item.name = "id";
    item.value = id;
    form.appendChild(item);
    let sizename = document.createElement('input');
    sizename.type = 'hidden';
    sizename.name = "sName";
    sizename.value = sName.toUpperCase();
    form.appendChild(sizename);
    // Create the submit button
    let button = document.createElement('button');
    button.type = 'submit';  // Set type to 'submit' to trigger form submission
    button.innerText = type;
    form.appendChild(button);

    return form;

}

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
        let minusForm = wrapButtonWithFrom( '-',product.id,product.size_name);
        minusForm.style.display = "inline-flex";
        minusForm.style.margin = "0";
        minusForm.childNodes[minusForm.childNodes.length - 1].classList.add('Quantity');
        let plusForm = wrapButtonWithFrom( '+',product.id,product.size_name);
        plusForm.style.display = "inline-flex";
        plusForm.style.margin = "0";
        plusForm.childNodes[plusForm.childNodes.length - 1].classList.add('Quantity');

        let spanQuantity = document.createElement("span");
        spanQuantity.innerHTML = product.quantity;
        quantityCell.appendChild(minusForm);
        quantityCell.appendChild(spanQuantity);
        quantityCell.appendChild(plusForm);

        // minus.onclick = function(event) {
        //     const target = event.target;
        //     const parentRow = target.closest('tr');
        //     const secondCell = parentRow.cells[1];
        //     if (product.quantity == 1) {
        //         parentRow.remove();
        //         totalPrice -= product.price * product.quantity;
        //         cart = cart.filter(p => p.id !== product.id);

        //         total.innerHTML = totalPrice;
        //         checkIfTableIsEmpty();
        //     } else {
        //         product.quantity -= 1;
        //         secondCell.children[1].innerHTML = product.quantity;
        //         totalPrice -= product.price;
        //         total.innerHTML = totalPrice;
        //         checkIfTableIsEmpty();
        //     }
        // };

        // plus.onclick = function(event) {
        //     const target = event.target;
        //     const parentRow = target.closest('tr');
        //     const secondCell = parentRow.cells[1];
        //     product.quantity += 1;
        //     secondCell.children[1].innerHTML = product.quantity;
        //     totalPrice += product.price;
        //     total.innerHTML = totalPrice;
        // };

        let cell = row.insertCell();
        cell.appendChild(document.createTextNode(product.price));
        totalPrice += product.price * product.quantity;

        cell = row.insertCell();
        let buttonForm = wrapButtonWithFrom( 'Remove',product.id,product.size_name);
        buttonForm.childNodes[buttonForm.childNodes.length - 1].classList.add('danger');
        // buttonForm.setAttribute("id", `${product.id}`);
        // buttonForm.onclick = function(event) {
            // const target = event.target;
            // const parentRow = target.closest('tr');
            // parentRow.remove();
        //     totalPrice -= product.price * product.quantity;
        //     cart = cart.filter(p => p.id !== product.id);

        //     total.innerHTML = totalPrice;
        //     checkIfTableIsEmpty();
        // };

        cell.appendChild(buttonForm);
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
