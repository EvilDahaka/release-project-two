from models import get_db_connection, init_db

def seed_products():
    init_db()  # Спочатку ініціалізуємо базу даних
    conn = get_db_connection()

    conn.execute('''INSERT INTO products (name, price, specifications, image, tag) VALUES
('Gaming Laptop', 1200.00, 'Intel i7, 16GB RAM, 512GB SSD, NVIDIA GTX 1660Ti', NULL, 'pc'),
('Wireless Mouse', 25.99, '2.4GHz, Optical, 1600 DPI', NULL, 'accessoires'),
('Smartphone X', 799.00, '128GB, OLED Display, Dual Camera', NULL, 'phone'),
('Mechanical Keyboard', 89.99, 'Cherry MX Red switches, RGB Lighting', NULL, 'accessoires'),
('Noise Cancelling Headphones', 199.00, 'Bluetooth, 20h battery life, ANC', NULL, 'accessoires'),
('Ultra HD Monitor', 349.00, '27", 4K Resolution, IPS Panel', NULL, 'pc'),
('Smartphone Charger', 15.00, 'Fast Charging, USB-C', NULL, 'accessoires'),
('Graphics Tablet', 129.99, '10"x6", 8192 Pressure Levels, USB', NULL, 'pc'),
('Smartwatch', 179.00, 'Heart Rate Monitor, GPS, 5ATM Water Resistance', NULL, 'phone'),
('External Hard Drive', 89.00, '1TB, USB 3.0', NULL, 'accessoires'),
('4K Ultra HD TV', 699.00, '55", HDR, Smart TV, 120Hz', NULL, 'tv'),
('Bluetooth Soundbar', 199.00, '2.1 Channel, 150W, Wireless', NULL, 'audio'),
('Gaming Headset', 119.00, '7.1 Surround Sound, Noise Cancelling', NULL, 'accessoires'),
('LED TV Stand', 149.00, 'Modern Design, Adjustable Height', NULL, 'tv'),
('Portable Bluetooth Speaker', 59.00, '10h battery life, Waterproof', NULL, 'audio'),
('Touchscreen Monitor', 249.00, '24", Full HD, Touchscreen', NULL, 'pc'),
('Smart LED Light Bulb', 29.99, 'RGB, WiFi enabled, Voice Control', NULL, 'accessoires'),
('Game Console', 399.00, '4K HDR, Blu-ray player', NULL, 'gaming'),
('Gaming Mouse', 69.99, 'RGB Lighting, Adjustable DPI', NULL, 'accessoires'),
('Portable Power Bank', 39.99, '10000mAh, Fast Charging', NULL, 'accessoires'),
('Wireless Earbuds', 129.99, 'True Wireless, 6h battery life, Noise Cancelling', NULL, 'audio'),
('Fitness Tracker', 69.00, 'Heart Rate Monitoring, Sleep Tracker', NULL, 'phone'),
('Home Security Camera', 129.00, '1080p, Night Vision, Motion Detection', NULL, 'accessoires'),
('Noise Cancelling Bluetooth Headphones', 219.00, '50h battery, Over-ear, ANC', NULL, 'audio');
''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    seed_products()
    print("Тестові продукти додано до бази даних.")
