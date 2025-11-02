CREATE DATABASE cripto_db;

USE cripto_db;

CREATE OR REPLACE VIEW cripto_db.crypto_prices AS
SELECT fecha, 'BTC-USD' AS simbolo, `BTC-USD` AS precio_cierre FROM cripto_db.market_prices
UNION ALL
SELECT fecha, 'ETH-USD', `ETH-USD` FROM cripto_db.market_prices
UNION ALL
SELECT fecha, 'CL=F', `CL=F` FROM cripto_db.market_prices
UNION ALL
SELECT fecha, 'GC=F', `GC=F` FROM cripto_db.market_prices
UNION ALL
SELECT fecha, '^GSPC', `^GSPC` FROM cripto_db.market_prices;


SELECT simbolo, DATE_FORMAT(fecha, '%Y-%m') AS mes, 
       AVG(precio_cierre) AS precio_promedio
FROM cripto_db.crypto_prices
GROUP BY simbolo, mes
ORDER BY simbolo, mes
LIMIT 1000;
