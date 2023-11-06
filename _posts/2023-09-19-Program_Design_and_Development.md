---
toc: true
comments: false
layout: post
title: Program Design and Development
description: Team Test Section 3
type: hacks
courses: { compsci: {week: 5} }
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Factorial Calculator</title>
    <style>
        /* Basic CSS for styling the UI */
        body {
            font-family: Arial, sans-serif;
            background-color: #F4F4F4;
        }
        #calculator {
            max-width: 400px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
        }
        h1 {
            color: #333;
        }
        input[type="number"] {
            width: 95% ;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 10px;
        }
        button {
            background-color: #007BFF;
            color: #fff;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div id="calculator">
        <h1>Factorial Calculator</h1>
        <label for="number">Enter a non-negative integer:</label>
        <input type="number" id="number" min="0" step="1" required>
        <button id="calculate">Calculate Factorial</button>
        <p id="result"></p>
    </div>
<script>
    // Add an event listener to the 'calculate' button
    document.getElementById('calculate').addEventListener('click', function () {
        // Get the input value as a number
        const inputNumber = parseInt(document.getElementById('number').value);
        try {
            // Calculate the factorial using the calculateFactorial function
            const factorialResult = calculateFactorial(inputNumber);
            // Display the factorial result in the 'result' element
            document.getElementById('result').textContent = `The factorial of ${inputNumber} is ${factorialResult}`;
        } catch (error) {
            // Handle errors by displaying an error message in the 'result' element
            document.getElementById('result').textContent = error.message;
        }
    });
    // Function to calculate the factorial
    function calculateFactorial(num) {
        // Check if the input is a non-negative integer
        if (typeof num !== 'number' || num < 0 || Math.floor(num) !== num) {
            throw new Error('Input must be a non-negative integer.');
        }
        // Calculate the factorial using a loop
        let result = 1;
        for (let i = 1; i <= num; i++) {
            result *= i;
        }
        // Return the calculated factorial
        return result;
    }
</script>
<br>
<h1>Visual illustration of algorithm</h1>
<img src="https://cdn.discordapp.com/attachments/728322409387786250/1154100776877174826/0.png">
</body>
</html>
10:45
HTML:
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Factorial Calculator</title>
    <style>
        /* Basic CSS for styling the UI */
        body {
            font-family: Arial, sans-serif;
            background-color: #F4F4F4;
        }
        #calculator {
            max-width: 400px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
        }
        h1 {
            color: #333;
        }
        input[type="number"] {
            width: 95% ;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 10px;
        }
        button {
            background-color: #007BFF;
            color: #fff;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
        }
    </style>
</head>
<body>
<br>
    <div id="calculator">
        <h1>Factorial Calculator</h1>
        <label for="number">Enter a non-negative integer:</label>
        <input type="number" id="number" min="0" step="1" required>
        <button id="calculate">Calculate Factorial</button>
        <p id="result"></p>
    </div>
<script>
    // Add an event listener to the 'calculate' button
    document.getElementById('calculate').addEventListener('click', function () {
        // Get the input value as a number
        const inputNumber = parseInt(document.getElementById('number').value);
        try {
            // Calculate the factorial using the calculateFactorial function
            const factorialResult = calculateFactorial(inputNumber);
            // Display the factorial result in the 'result' element
            document.getElementById('result').textContent = `The factorial of ${inputNumber} is ${factorialResult}`;
        } catch (error) {
            // Handle errors by displaying an error message in the 'result' element
            document.getElementById('result').textContent = error.message;
        }
    });
    // Function to calculate the factorial
    function calculateFactorial(num) {
        // Check if the input is a non-negative integer
        if (typeof num !== 'number' || num < 0 || Math.floor(num) !== num) {
            throw new Error('Input must be a non-negative integer.');
        }
        // Calculate the factorial using a loop
        let result = 1;
        for (let i = 1; i <= num; i++) {
            result *= i;
        }
        // Return the calculated factorial
        return result;
    }
</script>
<br>
<h1>Visual illustration of algorithm</h1>
<img src="https://cdn.discordapp.com/attachments/728322409387786250/1154100776877174826/0.png">
</body>
</html>