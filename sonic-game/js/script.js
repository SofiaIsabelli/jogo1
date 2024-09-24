const sonic = document.querySelector('.sonic');
const obstaculo1 = document.querySelector('.obstaculo1');

const jump = () => {
    sonic.classList.add('jump');

    setTimeout(() => {

        sonic.classList.remove('jump');

    }, 500)
}

const loop = setInterval(() => {

    const obstaculo1Position = obstaculo1.offsetLeft;
    const sonicPosition = +window.getComputedStyle(sonic).bottom.replace('px', '');

    console.log(sonicPosition);

    if (obstaculo1Position <= 50  && sonicPosition > 0 && sonicPosition < 80) {

        obstaculo1.style.animation = 'none';
        obstaculo1.style.left = `${obstaculo1Position}px`

        sonic.style.animation = 'none';
        sonic.style.bottom = `${sonicPosition}px`

        sonic.src = './images/game-over.webp';
        sonic.style.width = '120px'

        clearInterval(loop);
    }

},10);

document.addEventListener('keydown', jump)