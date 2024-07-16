{{
    config(
        materialized='table'
    )
}}

SELECT  payroll_id
      , payroll_period_start
      , payroll_period_end
      , pay_date
      , total_gross_pay
      , total_net_pay
FROM    {{ source('source', 'payroll') }}