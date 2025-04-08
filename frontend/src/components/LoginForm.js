import React, { useState } from "react";
import "../styles/LoginForm.css";

const LoginForm = () => {
  const [role, setRole] = useState("student");
  const [id, setId] = useState("");
  const [secondField, setSecondField] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!id || !secondField) {
      alert("Please fill in all fields.");
      return;
    }

    if (role === "student") {
      console.log("Logging in as Student");
      console.log("Student ID:", id);
      console.log("Date of Birth:", secondField);
    } else {
      console.log("Logging in as Faculty");
      console.log("Faculty ID:", id);
      console.log("Faculty Name:", secondField);
    }

    // Add your login logic (API call or validation) here
  };

  return (
    <div className="login-container">
      <h2>{role === "student" ? "Student Login" : "Faculty Login"}</h2>
      <form onSubmit={handleSubmit}>
        <label>Role:</label>
        <select value={role} onChange={(e) => {
          setRole(e.target.value);
          setId("");
          setSecondField("");
        }}>
          <option value="student">Student</option>
          <option value="faculty">Faculty</option>
        </select>

        <label>{role === "student" ? "Student ID" : "Faculty ID"}:</label>
        <input
          type="text"
          placeholder={role === "student" ? "Enter Student ID" : "Enter Faculty ID"}
          value={id}
          onChange={(e) => setId(e.target.value)}
        />

        <label>
          {role === "student" ? "Date of Birth (YYYY-MM-DD)" : "Faculty Name"}:
        </label>
        <input
          type={role === "student" ? "date" : "text"}
          placeholder={role === "faculty" ? "Enter Faculty Name" : ""}
          value={secondField}
          onChange={(e) => setSecondField(e.target.value)}
        />

        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default LoginForm;