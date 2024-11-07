// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    
    // Structure to store student details
    struct Student {
        uint id;
        string name;
        uint age;
        string course;
    }
    
    // Array to store student data
    Student[] public students;
    
    // Fallback function to handle unexpected calls
    fallback() external payable {
        // Accept ether if sent to this contract with data.
    }

    // Receive function to handle direct Ether transfers (without data)
    receive() external payable {
        // Accept ether if sent to this contract without data.
    }
    
    // Function to add a student
    function addStudent(uint _id, string memory _name, uint _age, string memory _course) public {
        Student memory newStudent = Student({
            id: _id,
            name: _name,
            age: _age,
            course: _course
        });
        
        students.push(newStudent);
    }
    
    // Function to get the details of a student by ID
    function getStudent(uint _id) public view returns (uint, string memory, uint, string memory) {
        require(_id < students.length, "Student does not exist!");
        Student memory student = students[_id];
        return (student.id, student.name, student.age, student.course);
    }
    
    // Function to get the total number of students
    function getTotalStudents() public view returns (uint) {
        return students.length;
    }
}
