document.addEventListener("DOMContentLoaded", function () {
    // 1. Typing Effect untuk Role
    const words = ["Web Developer", "PHP & Laravel Enthusiast", "Game Dev Learner"];
    let wordIndex = 0;

    function typingEffect() {
        let currentWord = words[wordIndex].split("");
        var loopTyping = function () {
            if (currentWord.length > 0) {
                document.getElementById('typing-text').innerHTML += currentWord.shift();
            } else {
                setTimeout(deletingEffect, 2200);
                return false;
            }
            setTimeout(loopTyping, 90);
        };
        loopTyping();
    }

    function deletingEffect() {
        let currentWord = words[wordIndex].split("");
        var loopDeleting = function () {
            if (currentWord.length > 0) {
                currentWord.pop();
                document.getElementById('typing-text').innerHTML = currentWord.join("");
            } else {
                wordIndex = (wordIndex + 1) % words.length;
                setTimeout(typingEffect, 400);
                return false;
            }
            setTimeout(loopDeleting, 45);
        };
        loopDeleting();
    }

    typingEffect();

    // 2. Filter Kategori Sertifikat
    const filterButtons = document.querySelectorAll('.cert-btn');
    const certCards = document.querySelectorAll('.cert-card');

    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            filterButtons.forEach(btn => btn.classList.remove('active'));
            button.classList.add('active');

            const filterValue = button.getAttribute('data-filter');

            certCards.forEach(card => {
                if (filterValue === 'all' || card.getAttribute('data-category') === filterValue) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });

    // 3. Scroll Reveal Effect (Efek Muncul Halus Saat Scroll)
    const revealElements = document.querySelectorAll('.reveal');

    function checkReveal() {
        const triggerBottom = window.innerHeight * 0.85;
        revealElements.forEach(el => {
            const elTop = el.getBoundingClientRect().top;
            if (elTop < triggerBottom) {
                el.classList.add('active');
            }
        });
    }

    window.addEventListener('scroll', checkReveal);
    checkReveal(); // Jalankan sekali di awal
});