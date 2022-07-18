var updateBtns = document.getElementsByClassName('update-cart')

//looping through the button
for(i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'action:', action)

        // checking if the user is authenticated or not
        console.log('USER:', user)
        if (user == 'AnonymousUser'){
            addCookieItem(productId, action)
        }
        else{
            updateUserOrder(productId, action)
        
        }
    })
}


//adding cookie
function addCookieItem(productId, action){
    console.log('User is not authenticated')

    //increasing the cart
    if (action == 'add'){
        if (cart[productId] == undefined){
            cart[productId] = {'quantity':1}
        }
        else{
            cart[productId]['quantity'] +=1
        }
    }
    //removing the item
    if(action == 'remove'){
        cart[productId]['quantity'] -=1

        if (cart[productId]['quantity'] <= 0){
            console.log('Product should be deleted')
            delete cart[productId]
        }
    }
    console.log('Cart:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart + ";domain=;path=/")
    location.reload()
}



//sending data
function updateUserOrder(productId, action){
    console.log('User is authenticated')

    var url = '/update_item/' //setting the data to 

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action}), 
    })
    //returning response as a promise
    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data:', data)

        location.reload() //helps the data to be added when the user adds
    });
}