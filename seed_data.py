from models import get_db_connection, init_db

def seed_products():
    init_db()
    conn = get_db_connection()

    conn.execute('''INSERT INTO products (name, price, specifications, image, tag) VALUES
('Gaming Laptop High-End', 1800.00, 'Intel i9, 32GB RAM, 1TB SSD, NVIDIA RTX 3080', NULL, 'pc'),
('Gaming Laptop Mid-Range', 1200.00, 'Intel i7, 16GB RAM, 512GB SSD, NVIDIA GTX 1660Ti', NULL, 'pc'),
('Gaming Laptop Budget', 800.00, 'Intel i5, 8GB RAM, 256GB SSD, NVIDIA GTX 1650', NULL, 'pc'),
('Gaming Desktop', 1500.00, 'AMD Ryzen 7, 16GB RAM, 1TB SSD, Radeon RX 6700 XT', NULL, 'pc')
''')

    conn.execute('''INSERT INTO products (name, price, specifications, image, tag) VALUES
('Smart TV 55 inch 4K', 699.00, '55", HDR, Smart TV, 120Hz', NULL, 'tv'),
('Smart TV 65 inch 8K', 1499.00, '65", 8K, QLED, Smart TV', NULL, 'tv'),
('LED TV 43 inch Full HD', 349.00, '43", Full HD, LED', NULL, 'tv'),
('OLED TV 50 inch 4K', 999.00, '50", OLED, HDR, Smart TV', NULL, 'tv')
''')

    conn.execute('''INSERT INTO products (name, price, specifications, image, tag) VALUES
('Graphics Tablet Pro', 299.00, '13.3", 8192 Levels, Pen Display', NULL, 'graphics-tablets'),
('Graphics Tablet Medium', 149.99, '10"x6", 4096 Levels, USB', NULL, 'graphics-tablets'),
('Drawing Tablet Budget', 79.00, '8.5"x5.5", 2048 Levels, USB', NULL, 'graphics-tablets'),
('Graphics Monitor', 599.00, '27", QHD, IPS, Pen Support', NULL, 'graphics-tablets')
''')

    conn.execute('''INSERT INTO products (name, price, specifications, image, tag) VALUES
('PlayStation 5', 499.00, '4K Gaming, Blu-ray', NULL, 'gaming-consoles'),
('Xbox Series X', 499.00, '4K Gaming, High Performance', NULL, 'gaming-consoles'),
('Nintendo Switch OLED', 349.00, 'Portable, Hybrid Console', NULL, 'gaming-consoles'),
('Steam Deck', 399.00, 'Portable PC Gaming', NULL, 'gaming-consoles')
''')

    conn.execute('''INSERT INTO products (name, price, specifications, image, tag) VALUES
('Wireless Gaming Controller', 59.99, 'Bluetooth, Dual Vibration', NULL, 'gaming-controllers'),
('Wired Gaming Controller', 39.99, 'USB, Ergonomic Design', NULL, 'gaming-controllers'),
('Arcade Fight Stick', 129.00, 'High-Quality Components', NULL, 'gaming-controllers'),
('Racing Wheel and Pedals', 299.00, 'Force Feedback, Realistic Feel', NULL, 'gaming-controllers')
''')

    conn.execute('''INSERT INTO products (name, price, specifications, image, tag) VALUES
('Tablet 10 inch Android', 249.00, '10.1", 64GB, WiFi', NULL, 'tablets'),
('Tablet 12 inch iOS', 799.00, '12.9", 128GB, WiFi', NULL, 'tablets'),
('Tablet 8 inch Compact', 129.00, '8", 32GB, WiFi', NULL, 'tablets'),
('Tablet with Keyboard', 399.00, '11", 128GB, 2-in-1', NULL, 'tablets')
''')

    conn.execute('''INSERT INTO products (name, price, specifications, image, tag) VALUES
('Ultra HD Monitor 27 inch', 349.00, '27", 4K Resolution, IPS Panel', NULL, 'monitor'),
('Gaming Monitor 24 inch 144Hz', 279.00, '24", Full HD, 144Hz, 1ms', NULL, 'monitor'),
('Curved Ultrawide Monitor', 499.00, '34", UWQHD, 144Hz', NULL, 'monitor'),
('Portable Monitor USB-C', 199.00, '15.6", Full HD, Portable', NULL, 'monitor')
''')

    conn.execute('''INSERT INTO products (name, price, specifications, image, tag) VALUES
('Mechanical Keyboard RGB', 89.99, 'Cherry MX Red, RGB Lighting', NULL, 'keyboard'),
('Wireless Keyboard Slim', 59.00, 'Bluetooth, Low Profile Keys', NULL, 'keyboard'),
('Ergonomic Keyboard Split', 129.00, 'Wired, Ergonomic Design', NULL, 'keyboard'),
('Membrane Gaming Keyboard', 49.00, 'RGB Backlighting, Anti-Ghosting', NULL, 'keyboard')
''')

    conn.execute('''INSERT INTO products (name, price, specifications, image, tag) VALUES
('Wireless Mouse Ergonomic', 39.99, '2.4GHz, Optical, Vertical Design', NULL, 'mouse'),
('Gaming Mouse High DPI', 69.99, 'Wired, RGB, Adjustable DPI', NULL, 'mouse'),
('Bluetooth Mouse Compact', 29.00, 'Bluetooth 5.0, Portable', NULL, 'mouse'),
('Silent Click Mouse', 34.99, 'Wireless, Quiet Buttons', NULL, 'mouse')
''')

    conn.execute('''INSERT INTO products (name, price, specifications, image, tag) VALUES
('Noise Cancelling Headphones Wireless', 199.00, 'Bluetooth, 20h Battery, ANC', NULL, 'audio'),
('Bluetooth Soundbar 2.1', 199.00, '150W, Wireless Subwoofer', NULL, 'audio'),
('Portable Bluetooth Speaker Waterproof', 59.00, '10h Battery, IPX7', NULL, 'audio'),
('True Wireless Earbuds ANC', 149.00, 'Bluetooth 5.1, Active Noise Cancellation', NULL, 'audio')
''')

    conn.execute('''INSERT INTO products (name, price, specifications, image, tag) VALUES
('Smartwatch Fitness Tracker', 179.00, 'Heart Rate, GPS, Water Resistant', NULL, 'gadgets'),
('Smart Speaker Voice Assistant', 99.00, 'WiFi, Voice Control', NULL, 'gadgets'),
('Wireless Charging Pad', 29.99, 'Qi Certified, Fast Charging', NULL, 'gadgets'),
('Smart Home Hub', 79.00, 'Zigbee, Z-Wave, WiFi', NULL, 'gadgets')
''')

    conn.commit()
    conn.close()

'''
def delete_all_products():
    conn = get_db_connection()
    conn.execute("DELETE FROM products")
    conn.commit()
    conn.close()
'''

if __name__ == '__main__':
    seed_products()
    print("Тестові продукти додано до бази даних.")