SELECT
  DATE(history.timestamp) AS day,
  ROUND(history.close, 2) AS close_price,
  ROUND(buy.price, 2) AS buy_price,
  ROUND(IFNULL(sell.price, buy.price), 2) AS sell_price,
FROM `martinview7`.`trader`.`history` AS history
LEFT OUTER JOIN `martinview7`.`trader`.`buy` AS buy ON history.symbol = buy.symbol
LEFT OUTER JOIN `martinview7`.`trader`.`sell` AS sell ON history.symbol = sell.symbol
WHERE history.symbol = 'LAZR'
ORDER BY timestamp;
