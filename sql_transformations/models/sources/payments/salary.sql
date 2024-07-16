{{
    config(
        materialized='table'
    )
}}

SELECT  salary_id 
      , employee_id
      , base_salary
      , bonus
      , overtime_pay
      , deductions
      , net_pay
      , pay_date
FROM    {{ source('source', 'employee_salaries') }}