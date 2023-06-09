-- 코드를 입력하세요
SELECT B.HISTORY_ID, CASE WHEN B.DURATION BETWEEN 7 AND 29 THEN ROUND(A.DAILY_FEE * (1 - ((SELECT DISCOUNT_RATE FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN WHERE DURATION_TYPE = '7일 이상' AND CAR_TYPE = '트럭') / 100)) * B.DURATION) WHEN B.DURATION BETWEEN 30 AND 89 THEN ROUND(A.DAILY_FEE * (1 - ((SELECT DISCOUNT_RATE FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN WHERE DURATION_TYPE = '30일 이상' AND CAR_TYPE = '트럭')  / 100)) * B.DURATION) WHEN B.DURATION >= 90 THEN ROUND(A.DAILY_FEE * (1 - ((SELECT DISCOUNT_RATE FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN WHERE DURATION_TYPE = '90일 이상' AND CAR_TYPE = '트럭') / 100)) * B.DURATION) ELSE ROUND(A.DAILY_FEE * B.DURATION) END AS FEE
FROM CAR_RENTAL_COMPANY_CAR A
JOIN (
    SELECT HISTORY_ID, CAR_ID, DATEDIFF(END_DATE, START_DATE) + 1 AS DURATION
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
) AS B
ON A.CAR_ID = B.CAR_ID
WHERE A.CAR_TYPE = '트럭'
ORDER BY FEE DESC, B.HISTORY_ID DESC;