CREATE DATABASE crypto_data;
CREATE Table Prices(
	id INT AUTO_INCREMENT PRIMARY KEY,
    coin_name VARCHAR(50),
    price DECIMAL(15,2),
    timestamp DATETIME
);
select * from Prices;