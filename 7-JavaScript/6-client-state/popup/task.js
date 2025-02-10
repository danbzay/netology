if (!document.cookie.includes('modal: closed')) {
  const subscriber = document.querySelector('#subscribe-modal');
  subscriber.classList.add('modal_active');
  document.querySelector('.modal__close').addEventListener('click', () => {
    document.cookie = 'modal: closed';
    subscriber.classList.remove('modal_active');
  });
}
