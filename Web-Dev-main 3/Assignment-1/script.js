let currentimg = 0;

const images = [
    {
        title: "New to Minecraft?",
        text: "Explore our Tips for Beginners: from how you craft or use a controller, to how you play with friends.",
        image: "Images/img1.avif",
        link: "#get-started",
        linkText: "Get Started"
    },
    {
        title: "Daring adventures!",
        text: "Team up or go solo and discover new blocks, mobs, weapons, and the trial chambers – a sprawling structure stuffed with traps and treasures for every player!",
        image: "Images/img2.jpg",
        link: "https://www.minecraft.net/en-us/updates/tricky-trials",
        linkText: "Explore Now"
    },
    {
        title: "Your Friends, Your Server",
        text: "Embark on a shared adventure with Realms Plus on your very own, always-online server!",
        image: "Images/img3.jpg",
        link: "https://www.minecraft.net/en-us/realms/bedrock",
        linkText: "Learn More"
    },
    {
        title: "Customize Any World",
        text: "MODS let you safely customize your gameplay by adding new elements like blocks, items, mobs, recipes, and other content to your Minecraft worlds.",
        image: "Images/img4.jpg",
        link: "https://www.curseforge.com/Minecraft/search?page=1&pageSize=20&sortBy=relevancy&class=mc-mods",
        linkText: "Try Now"
    }
];

const correctAnswers = {
    1: 'Leather',
    2: 'Cave Game',
    3: 'Pig'
};

function updateImage() {
    const highlight = images[currentimg];
    document.getElementById('highlight-img').src = highlight.image;
    document.getElementById('box-title').innerText = highlight.title;
    document.getElementById('box-text').innerText = highlight.text;
    document.getElementById('ext-link').href = highlight.link;
    document.getElementById('ext-link').innerText = `${highlight.linkText} ➡`;
}

document.getElementById('next-img').addEventListener('click', () => {
    currentimg = (currentimg + 1) % images.length;
    updateImage();
});

document.getElementById('prev-img').addEventListener('click', () => {
    currentimg = (currentimg - 1 + images.length) % images.length;
    updateImage();
});

function checkAnswer(questionNumber) {
    const questionName = questionNumber === 1 ? 'armor' : questionNumber === 2 ? 'original-name' : 'ridden-animal';
    const selectedOption = document.querySelector(`input[name="${questionName}"]:checked`);
    const button = document.querySelector(`#question${questionNumber} .check-answer`);

    if (!selectedOption) {
        button.disabled = true;
        return;
    } else {
        button.disabled = false;
    }

    const answer = selectedOption.value;
    const isCorrect = answer === correctAnswers[questionNumber];
    const resultText = isCorrect ? 'Correct!' : `Wrong! The correct answer is ${correctAnswers[questionNumber]}.`;
    const resultElement = document.querySelector(`#question${questionNumber} .result`);
    
    resultElement.textContent = resultText;
    resultElement.style.color = isCorrect ? 'green' : 'red';

    const dots = document.querySelectorAll('.dot');
    dots.forEach(dot => dot.remove());

    const dot = document.createElement('div');
    dot.className = `dot ${isCorrect ? 'green' : 'red'}`;
    document.body.appendChild(dot);
    dot.style.position = 'fixed';
    dot.style.bottom = '10px';
    dot.style[isCorrect ? 'left' : 'right'] = '10px';
    dot.style.zIndex = '1000';

    button.disabled = true;
}

function enableCheckButtons() {
    document.querySelectorAll('.check-answer').forEach(button => {
        const questionNumber = button.dataset.question;
        const selectedOption = document.querySelector(`input[name="${questionNumber}"]:checked`);
        button.disabled = !selectedOption;
    });
}

document.querySelectorAll('input[type="radio"]').forEach(input => {
    input.addEventListener('change', () => {
        enableCheckButtons();
    });
});

updateImage();

document.querySelector('#question1 .check-answer').addEventListener('click', () => checkAnswer(1));
document.querySelector('#question2 .check-answer').addEventListener('click', () => checkAnswer(2));
document.querySelector('#question3 .check-answer').addEventListener('click', () => checkAnswer(3));

enableCheckButtons();
