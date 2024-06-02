from flask import Flask, render_template, jsonify
from database import init_db, get_clicks, update_clicks
from threading import Thread
import time

app = Flask(__name__)
init_db()

# Функция для восстановления энергии
def recover_energy():
    while True:
        time.sleep(10)  # Ждать 10 секунд
        clicks, energy, energy_limit, multiplier, energy_price, multiplier_price = get_clicks()
        energy = min(energy + 20, energy_limit)  # Прибавить энергию, но не превышать лимит
        update_clicks(clicks, energy, energy_limit, multiplier, energy_price, multiplier_price)

# Запуск потока для восстановления энергии
recovery_thread = Thread(target=recover_energy)
recovery_thread.daemon = True
recovery_thread.start()

@app.route('/')
def index():
    clicks, energy, energy_limit, multiplier, energy_price, multiplier_price = get_clicks()
    return render_template('index.html', salad_count=clicks, energy=energy, energy_limit=energy_limit, multiplier=multiplier, energy_price=energy_price, multiplier_price=multiplier_price)

@app.route('/start-mining', methods=['POST'])
def start_mining():
    clicks, energy, energy_limit, multiplier, energy_price, multiplier_price = get_clicks()
    if energy > 0:
        clicks += 1 * multiplier
        energy -= 15
    update_clicks(clicks, energy, energy_limit, multiplier, energy_price, multiplier_price)
    return jsonify({
        'salad_count': clicks,
        'energy': energy,
        'energy_limit': energy_limit,
        'multiplier': multiplier,
        'energy_price': energy_price,
        'multiplier_price': multiplier_price
    })

@app.route('/buy-energy', methods=['POST'])
def buy_energy():
    clicks, energy, energy_limit, multiplier, energy_price, multiplier_price = get_clicks()
    if clicks >= energy_price:
        clicks -= energy_price
        # energy += 1000
        energy_limit += 1000  # Увеличение максимального значения энергии после каждой покупки
        energy_price += 50  # Увеличение цены после каждой покупки
    update_clicks(clicks, energy, energy_limit, multiplier, energy_price, multiplier_price)
    return jsonify({
        'salad_count': clicks,
        'energy': energy,
        'energy_limit': energy_limit,
        'multiplier': multiplier,
        'energy_price': energy_price,
        'multiplier_price': multiplier_price
    })

@app.route('/buy-multiplier', methods=['POST'])
def buy_multiplier():
    clicks, energy, energy_limit, multiplier, energy_price, multiplier_price = get_clicks()
    if clicks >= multiplier_price:
        clicks -= multiplier_price
        multiplier += 1
        multiplier_price += 150  # Увеличение цены после каждой покупки
    update_clicks(clicks, energy, energy_limit, multiplier, energy_price, multiplier_price)
    return jsonify({
        'salad_count': clicks,
        'energy': energy,
        'energy_limit': energy_limit,
        'multiplier': multiplier,
        'energy_price': energy_price,
        'multiplier_price': multiplier_price
    })

@app.route('/get-status', methods=['GET'])
def get_status():
    clicks, energy, energy_limit, multiplier, energy_price, multiplier_price = get_clicks()
    return jsonify({
        'salad_count': clicks,
        'energy': energy,
        'energy_limit': energy_limit,
        'multiplier': multiplier,
        'energy_price': energy_price,
        'multiplier_price': multiplier_price
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
