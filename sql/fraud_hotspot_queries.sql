-- Top cities by fraud count
SELECT City, COUNT(*) AS FraudCount
FROM transactions
WHERE IsFraud = 1
GROUP BY City
ORDER BY FraudCount DESC
LIMIT 5;

-- Fraud rate by city
SELECT
  City,
  COUNT(*) AS TotalTransactions,
  SUM(CASE WHEN IsFraud = 1 THEN 1 ELSE 0 END) AS FraudTransactions,
  (SUM(CASE WHEN IsFraud = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*)) AS FraudRatePercent
FROM transactions
GROUP BY City
ORDER BY FraudRatePercent DESC
LIMIT 5;

-- Contribution to total fraud
SELECT
  City,
  COUNT(*) AS FraudCount,
  COUNT(*) * 100.0 / (SELECT COUNT(*) FROM transactions WHERE IsFraud = 1)
    AS PercentOfAllFrauds
FROM transactions
WHERE IsFraud = 1
GROUP BY City
ORDER BY FraudCount DESC;
