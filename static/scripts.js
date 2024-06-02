document.getElementById('start-mining').addEventListener('click', function() {
    fetch('/start-mining', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            updateUI(data);
        });
});

document.getElementById('buy-energy').addEventListener('click', function() {
    fetch('/buy-energy', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            updateUI(data);
        });
});

document.getElementById('buy-multiplier').addEventListener('click', function() {
    fetch('/buy-multiplier', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            updateUI(data);
        });
});

function updateUI(data) {
    document.getElementById('mining-status').innerText = `Салаты: ${data.salad_count} | Энергия: ${data.energy}/${data.energy_limit} | Множитель: ${data.multiplier}`;
    document.getElementById('energy-price').innerText = `Цена энергии: ${data.energy_price}`;
    document.getElementById('multiplier-price').innerText = `Цена множителя: ${data.multiplier_price}`;
    document.getElementById('energy-bar').style.width = `${(data.energy / data.energy_limit) * 100}%`;
}

// Запуск обновления UI каждые 10 секунд для отображения восстановленной энергии
setInterval(function() {
    fetch('/get-status', { method: 'GET' }) // Обновляем данные без уменьшения энергии
        .then(response => response.json())
        .then(data => {
            updateUI(data);
        });
}, 10000); // 10 секунд
