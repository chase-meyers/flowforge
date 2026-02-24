import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";

import { apiGet } from "../lib/api";

function Workflows() {
  const [workflows, setWorkflows] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    async function fetchWorkflows() {
      const data = await apiGet("/workflows");
      setWorkflows(Array.isArray(data) ? data : []);
    }

    fetchWorkflows();
  }, []);

  return (
    <div>
      <button type="button" onClick={() => navigate("/workflows/new")}>
        Create Workflow
      </button>

      {workflows.length === 0 ? (
        <div>No workflows yet</div>
      ) : (
        <ul>
          {workflows.map((workflow) => (
            <li key={workflow.id}>
              <Link to={`/workflows/${workflow.id}`}>{workflow.name}</Link>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default Workflows;
