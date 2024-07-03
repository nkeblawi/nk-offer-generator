async function generateOffer() {
    const occupation = document.getElementById('occupation').value;
    if (occupation.length > 1000) {
        alert("Input is too long. Please limit to 1000 characters.");
        return;
    }

    document.getElementById('loading').style.display = 'block';
    document.getElementById('output').innerText = '';

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ occupation: occupation })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: $${response.status}`);
        }

        const result = await response.json();
        const result_text = JSON.stringify(result, null, 2);

        document.getElementById('output').innerText = result_text;
    } catch (error) {
        document.getElementById('output').innerText = `An error occurred: $${error.message}`;
        console.error('Error:', error);
    } finally {
        document.getElementById('loading').style.display = 'none';
    }
}

// Not being used yet - being tested in a separate environment
function formatJSON(jsonData) {
    const dwySolutions = [];
    const dfySolutions = [];
    const diySolutions = [];
  
    // Process each set of solutions in the JSON data
    jsonData.solutions.forEach(solutionSet => {
      dwySolutions.push(...(solutionSet.done_with_you_solutions || []));
      dfySolutions.push(...(solutionSet.done_for_you_solutions || []));
      diySolutions.push(...(solutionSet.do_it_yourself_solutions || []));
    });
  
    // Format the collected solutions
    function formatSolutions(solutions, title) {
      let formattedOutput = `${title}:\n`;
      solutions.forEach((solution, idx) => {
        formattedOutput += `  ${idx + 1}. ${solution}\n`;
      });
      return formattedOutput;
    }
  
    // Generate the final formatted output
    let finalOutput = formatSolutions(dwySolutions, "done with you solutions");
    finalOutput += formatSolutions(dfySolutions, "done for you solutions");
    finalOutput += formatSolutions(diySolutions, "do it yourself solutions");
  
    return finalOutput;
  }