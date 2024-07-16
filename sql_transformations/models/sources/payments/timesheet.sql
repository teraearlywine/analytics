{{
    config(
        materialized='table'
    )
}}

SELECT  timesheet_id
      , employee_id
      , work_date
      , hours_worked
      , overtime_hours
      , vacation_hours
      , sick_hours
FROM    {{ source('source', 'timesheet_schema_50_fintech_employees_3_months_pai') }}