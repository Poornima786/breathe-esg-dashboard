import { useEffect, useState } from "react";

function App() {
  const [records, setRecords] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/records/")
      .then((response) => response.json())
      .then((data) => {
        setRecords(data);
      });
  }, []);

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>Breathe ESG Dashboard</h1>

      <hr />

      <h2>Upload Data</h2>

      <div style={{ marginBottom: "20px" }}>
        <p>SAP Upload</p>
        <input type="file" />
      </div>

      <div style={{ marginBottom: "20px" }}>
        <p>Utility Upload</p>
        <input type="file" />
      </div>

      <div style={{ marginBottom: "20px" }}>
        <p>Travel Upload</p>
        <input type="file" />
      </div>

      <hr />

      <h2>Review Dashboard</h2>

      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>Source</th>
            <th>Value</th>
            <th>Unit</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>
          {records.map((record) => (
            <tr key={record.id}>
              <td>{record.source}</td>
              <td>{record.value}</td>
              <td>{record.unit}</td>
              <td>{record.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;