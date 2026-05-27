import { useEffect, useState } from "react";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
} from "recharts";

function App() {

  const [records, setRecords] = useState([]);

  const fetchRecords = () => {

    fetch("https://breathe-esg-dashboardd.onrender.com/api/records/")

      .then((response) => response.json())

      .then((data) => {

        setRecords(data);

      });

  };

  useEffect(() => {

    fetchRecords();

  }, []);

  const handleUpload = async (event) => {

    const file = event.target.files[0];

    const formData = new FormData();

    formData.append("file", file);

    await fetch(
      "https://breathe-esg-dashboardd.onrender.com/api/upload/",
      {
        method: "POST",
        body: formData,
      }
    );

    fetchRecords();

  };

  const updateStatus = async (id, status) => {

    await fetch(
      `https://breathe-esg-dashboardd.onrender.com/api/records/${id}/update/`,
      {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify({ status }),
      }
    );

    fetchRecords();

  };

  return (

    <div style={{ padding: "40px", fontFamily: "Arial" }}>

      <h1>Breathe ESG Dashboard</h1>

      <hr />

      <h2>Upload CSV</h2>

      <input type="file" onChange={handleUpload} />

      <hr />

      <h2>Review Dashboard</h2>

      <table border="1" cellPadding="10">

        <thead>

          <tr>

            <th>Source Name</th>

            <th>Value</th>

            <th>Unit</th>

            <th>Status</th>

            <th>Actions</th>

          </tr>

        </thead>

        <tbody>

          {records.map((record) => (

            <tr key={record.id}>

              <td>{record.source_name}</td>

              <td>{record.value}</td>

              <td>{record.unit}</td>

              <td
                style={{
                  color:
                    record.status === "APPROVED"
                      ? "limegreen"
                      : record.status === "FLAGGED"
                      ? "red"
                      : "gold",

                  fontWeight: "bold",
                }}
              >

                {record.status}

              </td>

              <td>

                <button
                  onClick={() =>
                    updateStatus(record.id, "APPROVED")
                  }
                >
                  Approve
                </button>

                <button
                  onClick={() =>
                    updateStatus(record.id, "FLAGGED")
                  }
                  style={{ marginLeft: "10px" }}
                >
                  Flag
                </button>

              </td>

            </tr>

          ))}

        </tbody>

      </table>

      <h2 style={{ marginTop: "50px" }}>
        Emission Overview
      </h2>

      <BarChart
        width={700}
        height={300}
        data={records}
      >

        <CartesianGrid strokeDasharray="3 3" />

        <XAxis dataKey="source_name" />

        <YAxis />

        <Tooltip />

        <Bar
          dataKey="value"
          fill="#00bfff"
        />

      </BarChart>

    </div>

  );
}

export default App;