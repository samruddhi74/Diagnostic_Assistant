async function getDiagnosis() {
    let symptoms = document.getElementById("symptoms").value;
    let resultDiv = document.getElementById("result");

    if (!symptoms.trim()) {
        resultDiv.innerHTML = "Please enter symptoms.";
        return;
    }

    resultDiv.innerHTML = "Checking...";

    try {
        let response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ symptoms: symptoms })
        });

        if (!response.ok) {
            let errorData = await response.json();
            throw new Error(errorData.detail || "Server error");
        }

        let data = await response.json();
        resultDiv.innerHTML = `<strong>Possible Conditions:</strong> <br> ${data.diagnosis}`;
    } catch (error) {
        resultDiv.innerHTML = `Error: ${error.message}`;
    }
}
