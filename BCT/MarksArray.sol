// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract MarksArray {

    // Declare an array to hold the marks
    uint256[] public marks;

    // Function to accept an array of marks
    function setMarks(uint256[] memory _marks) public {
        // Clear existing marks before updating
        delete marks;

        // Store the provided marks in the marks array
        for (uint i = 0; i < _marks.length; i++) {
            marks.push(_marks[i]);
        }
    }

    // Function to display all the marks
    function getMarks() public view returns (uint256[] memory) {
        return marks;
    }

    // Function to find the addition of marks in the array
    function sumMarks() public view returns (uint256) {
        uint256 sum = 0;

        // Loop through the array and add each mark to sum
        for (uint i = 0; i < marks.length; i++) {
            sum += marks[i];
        }

        return sum;
    }
}