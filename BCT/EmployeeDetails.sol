// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EmployeeDetails {
    struct Employee {
        uint id;             // Employee ID
        string name;         // Employee Name
        uint salary;         // Employee Salary
        uint joiningDate;    // Employee Joining Date (timestamp)
    }
    
    Employee public employee; // Instance of the Employee structure

    // Function to create employee details
    function createEmployee(uint _id, string memory _name, uint _salary, uint _joiningDate) public {
        employee.id = _id;
        employee.name = _name;
        employee.salary = _salary;
        employee.joiningDate = _joiningDate;
    }

    // Function to get employee details
    function getEmployeeDetails() public view returns (uint, string memory, uint, uint) {
        return (employee.id, employee.name, employee.salary, employee.joiningDate);
    }
}
