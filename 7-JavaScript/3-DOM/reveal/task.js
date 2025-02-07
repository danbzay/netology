const blocks = document.querySelectorAll('.reveal');
document.addEventListener('scroll', (e) => {
  setTimeout(() => {
    blocks.forEach((block) => {
      if (block.getBoundingClientRect().top < window.innerHeight) {
        block.classList.add('reveal_active');
      }
    });
  }, 1000);
});
    
