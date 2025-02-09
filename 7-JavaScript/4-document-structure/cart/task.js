const cart = document.querySelector('.cart');

if (localStorage.length > 0) {
  for (const id in {...localStorage}) {
    addProductToCart(id, localStorage.getItem(id));
  }
} else {
  cart.style.display = 'none';
}

const products = document.querySelectorAll('.product');

products.forEach((product) => {
  const quantity = product.querySelector('.product__quantity-value');
  product.querySelector('.product__quantity-control_dec')
    .addEventListener('click', () => {
      if (quantity.textContent > 0) {
        quantity.textContent--;
      }
    });
  product.querySelector('.product__quantity-control_inc')
    .addEventListener('click', () => quantity.textContent++);
  product.querySelector('.product__add').addEventListener('click', (e) => {
    e.preventDefault();
    addProductToCart(product.dataset.id, quantity.textContent, 
      product.querySelector('.product__image'));
  });
});

function addProductToCart(id, quantity, image = null) {
  let count, img;
  if (cart.style.display == 'none') cart.style.display = null;
  const product = document.querySelector(`.products [data-id="${id}"]`);
  if (cart.querySelector(`[data-id="${id}"]`) == null) {
    const cartProduct = document.createElement('div');
    cartProduct.classList.add('cart__product');
    cartProduct.dataset.id = id;
    const img = document.createElement('img');
    img.src = product.querySelector('.product__image').src
    img.classList.add('cart__product-image');
    count = document.createElement('div');
    count.classList.add('cart__product-count');
    count.textContent = quantity;
    const remover = document.createElement('div');
    remover.innerHTML = '&times;';
    remover.style.cursor = 'pointer';
    remover.addEventListener('click', () => {
      cartProduct.remove();
      localStorage.removeItem(id);
      if (localStorage.length == 0) cart.style.display ='none';
    });
    cartProduct.append(img, count, remover);
    cart.querySelector('.cart__products').append(cartProduct);
  } else {
    count = cart.querySelector(`[data-id="${id}"] .cart__product-count`);
    count.textContent = Number(count.textContent) + Number(quantity);
  }
  localStorage.setItem(id, count.textContent);
  if (image != null) {
    if (typeof img =='undefined') {
      img = cart.querySelector(`[data-id="${id}"] img`);
     } 
    flyImage(image, img);
  }
}

const timer = ms => new Promise(res => setTimeout(res, ms));

async function flyImage(img0, img1) {
  const pos0 = img0.getBoundingClientRect();
  const pos1 = img1.getBoundingClientRect();
  const flyingImg = document.createElement('img');
  flyingImg.style.position = 'absolute';
  flyingImg.style.width = '100px';
  flyingImg.style.objectFit = 'contain';
  flyingImg.src = img0.src;
  img0.after(flyingImg);
  for (let i = 1; i <= 10; i++) {
    flyingImg.style.top = 
      (scrollY + pos0.top + (pos1.top - pos0.top)*i/10) + 'px';
    flyingImg.style.left = 
      (scrollX + pos0.left + (pos1.left - pos0.left)*i/10) + 'px';
    await timer(100);
  }
  flyingImg.remove();
}

