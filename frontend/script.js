const API_BASE = "http://127.0.0.1:8000";

async function send() {
  const feature = document.getElementById("feature").value;
  const message = document.getElementById("message").value.trim();
  const output = document.getElementById("output");

  if (!message) {
    output.textContent = "Please enter a message.";
    return;
  }

  let body = { message };
  if (feature === "assignment") {
    body = { topic: message, mode: "assignment_help" };
  }
  if (feature === "question-paper") {
    body = { subject: message, total_questions: 10 };
  }

  output.textContent = "Thinking...";

  try {
    const response = await fetch(`${API_BASE}/${feature}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });

    const data = await response.json();
    output.textContent = JSON.stringify(data, null, 2);
  } catch (error) {
    output.textContent = `Request failed: ${error.message}`;
  }
}

document.getElementById("sendBtn").addEventListener("click", send);
